from captcha.image import ImageCaptcha
import random as rd

import torch as t
from torch import nn
import torch.nn.functional as F
import os
import random
from PIL import ImageFilter
from PIL.ImageDraw import Draw
from PIL.ImageFont import truetype
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lower_char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z']
upper_char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
              'V', 'W', 'X', 'Y', 'Z']

def get_width():
    return int(100 + 40 * rd.random())


def get_height():
    return int(45 + 20 * rd.random())

def get_string():
    string = ""
    for i in range(4):
        select = rd.randint(1, 1)
        if select == 1:
            index = rd.randint(0, 9)
            string += nums[index]
        elif select == 2:
            index = rd.randint(0, 25)
            string += lower_char[index]
        else:
            index = rd.randint(0, 25)
            string += upper_char[index]
    return string


def get_captcha(num, path):
    font_sizes = [x for x in range(40, 45)]
    for i in range(num):
        print(i)
        imc = ImageCaptcha(get_width(), get_height(), font_sizes=font_sizes)
        name = get_string()
        def random_color(start, end, opacity=None):
            red = random.randint(start, end)
            green = random.randint(start, end)
            blue = random.randint(start, end)
            if opacity is None:
                return (red, green, blue)
            return (red, green, blue, opacity)
        background = random_color(255, 255)
        color = random_color(190, 190, random.randint(255, 255))
        image = Image.new('RGB', (get_width(), get_height()), background)
        draw = Draw(image)

        def _draw_character(c):
            font = random.choice(imc.truefonts)
            w, h = draw.textsize(c, font=font)

            dx = random.randint(0, 0)
            dy = random.randint(0, 0)
            im = Image.new('RGBA', (w + dx, h + dy))
            Draw(im).text((dx, dy), c, font=font, fill=color)

            # rotate
            im = im.crop(im.getbbox())
            im = im.rotate(random.uniform(-1, 1), Image.BILINEAR, expand=1)

            # warp
            dx = w * random.uniform(0.1, 0.3)
            dy = h * random.uniform(0.2, 0.3)
            x1 = int(random.uniform(-dx, dx))
            y1 = int(random.uniform(-dy, dy))
            x2 = int(random.uniform(-dx, dx))
            y2 = int(random.uniform(-dy, dy))
            w2 = w + abs(x1) + abs(x2)
            h2 = h + abs(y1) + abs(y2)
            data = (
                x1, y1,
                -x1, h2 - y2,
                w2 + x2, h2 + y2,
                w2 - x2, -y1,
            )
            im = im.resize((w2, h2))
            im = im.transform((w, h), Image.QUAD, data)
            return im

        images = []
        for c in name:
            # if random.random() > 0.5:
            #     images.append(_draw_character(" "))
            images.append(_draw_character(c))

        text_width = sum([im.size[0] for im in images])

        width = max(text_width, imc._width)
        image = image.resize((width, imc._height))

        average = int(text_width / len(name))
        rand = int(0.25 * average / 100)
        offset = int(average * 0.1)
        table  =  []
        for  i  in  range( 256 ):
            table.append( i * 100.97 )
        for im in images:
            w, h = im.size
            mask = im.convert('L').point(table)
            image.paste(im, (offset, int((imc._height - h) / 2)), mask)
            offset = offset + w + random.randint(-rand, 0)

        if width > imc._width:
            image = image.resize((imc._width, imc._height))

        image = imc.create_captcha_image(name, color, background)
        image = image.filter(ImageFilter.SMOOTH)
        image.save(path + name + ".jpg")

class ResidualBlock(nn.Module):
    def __init__(self, inchannel, outchannel, stride=1):
        super(ResidualBlock, self).__init__()
        self.left = nn.Sequential(
            nn.Conv2d(inchannel, outchannel, kernel_size=3, stride=stride, padding=1, bias=False),
            nn.BatchNorm2d(outchannel, track_running_stats=True),
            nn.ReLU(inplace=True),
            nn.Conv2d(outchannel, outchannel, kernel_size=3, stride=1, padding=1, bias=False),
            nn.BatchNorm2d(outchannel, track_running_stats=True)
        )
        self.shortcut = nn.Sequential()
        if stride != 1 or inchannel != outchannel:
            self.shortcut = nn.Sequential(
                nn.Conv2d(inchannel, outchannel, kernel_size=1, stride=stride, bias=False),
                nn.BatchNorm2d(outchannel, track_running_stats=True)
            )

    def forward(self, x):
        out = self.left(x)
        out += self.shortcut(x)
        out = F.relu(out)
        return out

class ResNet(nn.Module):
    def __init__(self, ResidualBlock, num_classes=10):
        super(ResNet, self).__init__()
        self.inchannel = 64
        self.conv1 = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=3, stride=1, padding=1, bias=False),
            nn.BatchNorm2d(64, track_running_stats=True),
            nn.ReLU(),
        )
        self.layer1 = self.make_layer(ResidualBlock, 64, 2, stride=1)
        self.layer2 = self.make_layer(ResidualBlock, 128, 2, stride=2)
        self.layer3 = self.make_layer(ResidualBlock, 256, 2, stride=2)
        self.layer4 = self.make_layer(ResidualBlock, 512, 2, stride=2)
        self.fc1 = nn.Linear(512, num_classes)
        self.fc2 = nn.Linear(512, num_classes)
        self.fc3 = nn.Linear(512, num_classes)
        self.fc4 = nn.Linear(512, num_classes)

    def make_layer(self, block, channels, num_blocks, stride):
        strides = [stride] + [1] * (num_blocks - 1)  # strides=[1,1]
        layers = []
        for stride in strides:
            layers.append(block(self.inchannel, channels, stride))
            self.inchannel = channels
        return nn.Sequential(*layers)

    def forward(self, x):
        x = self.conv1(x)
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        x = self.layer4(x)
        x = F.avg_pool2d(x, 4)
        x = x.view(-1, 512)
        y1 = self.fc1(x)
        y2 = self.fc2(x)
        y3 = self.fc3(x)
        y4 = self.fc4(x)
        return y1, y2, y3, y4
    def save(self, circle):
        name = "d:\\python\\target\\"+circle+"model.pth"
        t.save(self.state_dict(), name)

    def loadIfExist(self):
        fileList = os.listdir("d:\\python\\target\\")
        # print(fileList)
        if "model.pth" in fileList:
            self.load_state_dict(t.load("d:\\python\\target\\model.pth"))
            print("the latest model has been load")
class ConvNet(nn.Module):

    def __init__(self):
        super(ConvNet, self).__init__()
        self.conv =nn.Sequential(
            nn.Conv2d(3, 32, kernel_size=4, stride=1, padding=2), # in:(bs,3,60,160)
            nn.BatchNorm2d(32),
            nn.LeakyReLU(0.2, inplace=True),
            nn.MaxPool2d(kernel_size=2),        # out:(bs,32,30,80)

            nn.Conv2d(32, 64, kernel_size=4, stride=1, padding=2),
            nn.BatchNorm2d(64),
            nn.LeakyReLU(0.2, inplace=True),
            nn.MaxPool2d(kernel_size=2),        # out:(bs,64,15,40)

            nn.Conv2d(64, 64, kernel_size=3 ,stride=1, padding=1),
            nn.BatchNorm2d(64),
            nn.LeakyReLU(0.2, inplace=True),
            nn.MaxPool2d(kernel_size=2)         # out:(bs,64,7,20)
        )

        self.fc1 = nn.Linear(64*7*20, 500)

        self.fc41 = nn.Linear(500, 10)
        self.fc42 = nn.Linear(500, 10)
        self.fc43 = nn.Linear(500, 10)
        self.fc44 = nn.Linear(500, 10)

    def forward(self, x):
        x = self.conv(x)
        x = x.view(x.size(0), -1)    # reshape to (batch_size, 64 * 7 * 30)
        x = self.fc1(x)
        x = F.relu(x)
        x1 = self.fc41(x)
        x2 = self.fc42(x)
        x3 = self.fc43(x)
        x4 = self.fc44(x)
        return x1, x2, x3, x4
    def save(self, circle):
        name = "d:\\python\\target\\"+circle+"model.pth"
        t.save(self.state_dict(), name)

    def loadIfExist(self):
        fileList = os.listdir("d:\\python\\target\\")
        # print(fileList)
        if "model.pth" in fileList:
            self.load_state_dict(t.load("d:\\python\\target\\model.pth"))
            print("the latest model has been load")


class CaptchaNet(nn.Module):
    def __init__(self):
        super(CaptchaNet, self).__init__()
        self.conv1 = nn.Conv2d(3, 5, 5)
        self.conv2 = nn.Conv2d(5, 10, 5)
        self.conv3 = nn.Conv2d(10, 16, 6)
        self.fc1 = nn.Linear(4 * 12 * 16, 512)
        # self.fc2 = nn.Linear(512, 128)
        # self.fc3 = nn.Linear(256, )
        # 这是四个用于输出四个字符的线性层
        self.fc41 = nn.Linear(512, 10)
        self.fc42 = nn.Linear(512, 10)
        self.fc43 = nn.Linear(512, 10)
        self.fc44 = nn.Linear(512, 10)

    def forward(self, x):
        # 输入为3*128*64，经过第一层为5*62*30
        x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2))
        # 输出形状10*29*13
        x = F.max_pool2d(F.relu(self.conv2(x)), (2, 2))
        # 输出形状16*12*4
        x = F.max_pool2d(F.relu(self.conv3(x)), (2, 2))
        # print(x.size())
        x = x.view(-1, 4 * 12 * 16)
        x = self.fc1(x)
        # x = F.relu(x)
        # x = self.fc2(x)
        # x = F.relu(x)
        # x = self.fc3(x)
        x = F.relu(x)
        x1 = self.fc41(x)
        x2 = self.fc42(x)
        x3 = self.fc43(x)
        x4 = self.fc44(x)
        return x1, x2, x3, x4

    def save(self, circle):
        name = "d:\\python\\target\\"+circle+"model.pth"
        t.save(self.state_dict(), name)

    def loadIfExist(self):
        fileList = os.listdir("d:\\python\\target\\")
        # print(fileList)
        if "model.pth" in fileList:
            self.load_state_dict(t.load("d:\\python\\target\\model.pth"))
            print("the latest model has been load")


nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lower_char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z']
upper_char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
              'V', 'W', 'X', 'Y', 'Z']

from PIL import Image
from torchvision import transforms as  T
import torch as t
from torch.utils import data

def StrtoLabel(Str):
    # print(Str)
    label = []
    for i in range(0, 4):
        if Str[i] >= '0' and Str[i] <= '9':
            label.append(ord(Str[i]) - ord('0'))
        elif Str[i] >= 'a' and Str[i] <= 'z':
            label.append(ord(Str[i]) - ord('a') + 0)
        else:
            label.append(ord(Str[i]) - ord('A') + 26)
    return label

#
# def LabeltoStr(Label):
#     Str = ""
#     for i in Label:
#         if i <= 9:
#             Str += chr(ord('0') + i)
#         elif i <= 35:
#             Str += chr(ord('a') + i - 10)
#         else:
#             Str += chr(ord('A') + i - 36)
#     return Str


class Captcha(data.Dataset):
    def __init__(self, root, train=True):
        self.imgsPath = [os.path.join(root, img) for img in os.listdir(root)]
        self.transform = T.Compose([
            T.Resize((128, 64)),
            T.ToTensor(),
            T.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
        ])

    def __getitem__(self, index):
        imgPath = self.imgsPath[index]
        # print(imgPath)
        label = imgPath.split("\\")[-1].split(".")[0]
        label = label[0:4]
        labelTensor = t.Tensor(StrtoLabel(label))
        data = Image.open(imgPath)
        data = self.transform(data)

        return data, labelTensor

    def __len__(self):
        return len(self.imgsPath)

from torch.utils.data import DataLoader
from torch import optim
import visdom
import tqdm
import time
import numpy as np
from torchnet import meter

class Visualizer(object):
    def __init__(self, env='default', **kwargs):
        self.vis = visdom.Visdom(env=env, **kwargs)
        self.index = {}

    def plot_many_stack(self, d):
        '''
        self.plot('loss',1.00)
        '''
        name = list(d.keys())
        name_total = " ".join(name)
        x = self.index.get(name_total, 0)
        val = list(d.values())
        if len(val) == 1:
            y = np.array(val)
        else:
            y = np.array(val).reshape(-1, len(val))
        # print(x)
        self.vis.line(Y=y, X=np.ones(y.shape) * x,
                      win=str(name_total),  # unicode
                      opts=dict(legend=name,
                                title=name_total),
                      update=None if x == 0 else 'append'
                      )
        self.index[name_total] = x + 1

learningRate = 1e-3
totalEpoch = 200
batchSize = 128
printCircle = 10
testCircle = 100
testNum = 6
saveCircle = 200

def train(model):
    avgLoss = 0.0
    if t.cuda.is_available():
        model = model.cuda()
    trainDataset = Captcha("d:\\python\\target\\train\\", train=True)
    testDataset = Captcha("d:\\python\\target\\test\\", train=False)
    trainDataLoader = DataLoader(trainDataset, batch_size=batchSize,
                                 shuffle=True, num_workers=4)
    # testDataLoader = DataLoader(testDataset, batch_size=1,
    #                             shuffle=True, num_workers=4)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=learningRate)
    # vis = Visualizer(env = "4")
    loss_meter = meter.AverageValueMeter()
    for epoch in range(totalEpoch):
        for circle, input in tqdm.tqdm(enumerate(trainDataLoader, 0)):
            x, label = input
            if t.cuda.is_available():
                x = x.cuda()
                label = label.cuda()
            label = label.long()
            # print(label)
            label1, label2, label3, label4 = label[:, 0], label[:, 1], label[:, 2], label[:, 3]
            # print(label1,label2,label3,label4)
            optimizer.zero_grad()
            y1, y2, y3, y4 = model(x)

            # print(y1.shape, y2.shape, y3.shape, y4.shape)
            loss1, loss2, loss3, loss4 = criterion(y1, label1), criterion(y2, label2) \
                , criterion(y3, label3), criterion(y4, label4)
            loss = loss1 + loss2 + loss3 + loss4
            loss_meter.add(loss.item())
            # print(loss)
            avgLoss += loss.item()
            loss.backward()
            optimizer.step()
            if circle % printCircle == 1:
                print("after %d circle,the train loss is %.5f" %
                      (circle, avgLoss / printCircle))
                writeFile("after %d circle,the train loss is %.5f" %
                          (circle, avgLoss / printCircle))
                # vis.plot_many_stack({"train_loss": avgLoss})
                avgLoss = 0
            # if circle % 1 == 0:
            #     accuracy = test(model, testDataLoader)
                # vis.plot_many_stack({"test_acc":accuracy})
            if circle % 100 == 1:
                model.save(str(epoch)+"_"+str(saveCircle))
        model.save()

def test(model, testDataLoader):
    totalNum = testNum * 1
    rightNum = 0
    for circle, input in enumerate(testDataLoader, 0):
        if circle >= testNum:
            break
        x, label = input
        label = label.long()
        if t.cuda.is_available():
            x = x.cuda()
            label = label.cuda()
        y1, y2, y3, y4 = model(x)

        y1, y2, y3, y4 = y1.topk(1, dim=1)[1].view(1, 1), y2.topk(1, dim=1)[1].view(1, 1), \
                         y3.topk(1, dim=1)[1].view(1, 1), y4.topk(1, dim=1)[1].view(1, 1)
        y = t.cat((y1, y2, y3, y4), dim=1)
        diff = (y != label)
        diff = diff.sum(1)
        diff = (diff != 0)
        res = diff.sum(0).item()
        rightNum += (1 - res)
    print("the accuracy of test set is %s" % (str(float(rightNum) / float(totalNum))))
    writeFile("the accuracy of test set is %s" % (str(float(rightNum) / float(totalNum))))
    return float(rightNum) / float(totalNum)

def writeFile(str):
    file = open("d:\\python\\result.txt", "a+")
    file.write(str)
    file.write("\n\n")
    file.flush()
    file.close()


def aa():
    net = CaptchaNet()
    net.loadIfExist()
    testDataset = Captcha("d:\\python\\target\\aa\\")
    testDataLoader = DataLoader(testDataset, batch_size=1,
                                shuffle=False, num_workers=1)
    for circle, input in enumerate(testDataLoader, 0):
        if circle >= 1000:
            break
        x, label = input
        label = label.long()

        y1, y2, y3, y4 = net(x)
        print("dd")
        print(label)
        y1, y2, y3, y4 = y1.topk(1, dim=1)[1].view(1, 1), y2.topk(1, dim=1)[1].view(1, 1), \
                         y3.topk(1, dim=1)[1].view(1, 1), y4.topk(1, dim=1)[1].view(1, 1)
        y = t.cat((y1, y2, y3, y4), dim=1)

        print(y)
if __name__ == '__main__':
    # get_captcha(30000, "d:\\python\\target\\train\\")
    # net = CaptchaNet()
    # net.loadIfExist()
    # train(net)
    aa()

    # print(t.cuda.is_available())