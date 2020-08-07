from captcha.image import ImageCaptcha
import random as rd

import torch as t
from torch import nn
import torch.nn.functional as F
import os

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
        select = rd.randint(2, 3)
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
        image = imc.generate_image(name)
        image.save(path + name + ".jpg")




class CaptchaNet(nn.Module):
    def __init__(self):
        super(CaptchaNet, self).__init__()
        self.conv1 = nn.Conv2d(3, 5, 5)
        self.conv2 = nn.Conv2d(5, 10, 5)
        self.conv3 = nn.Conv2d(10, 16, 6)
        self.fc1 = nn.Linear(4 * 12 * 16, 512)
        self.fc2 = nn.Linear(512, 256)
        self.fc3 = nn.Linear(256, 124)
        # 这是四个用于输出四个字符的线性层
        self.fc41 = nn.Linear(124, 52)
        self.fc42 = nn.Linear(124, 52)
        self.fc43 = nn.Linear(124, 52)
        self.fc44 = nn.Linear(124, 52)

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
        x = F.relu(x)
        x = self.fc2(x)
        x = F.relu(x)
        x = self.fc3(x)
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
            label.append(ord(Str[i]) - ord('a'))
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
        # print(label)
        labelTensor = t.Tensor(StrtoLabel(label))
        data = Image.open(imgPath)
        print(data.size)
        data = self.transform(data)
        print(data.shape)
        return data, labelTensor

    def __len__(self):
        return len(self.imgsPath)

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
        # print(label)
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
    testDataLoader = DataLoader(testDataset, batch_size=1,
                                shuffle=True, num_workers=4)
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
        model.save(str(epoch))

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
    testDataset = Captcha("d:\\python\\target\\test\\")
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
    # get_captcha(90000, "d:\\python\\target\\train\\")
    # net = CaptchaNet()
    # net.loadIfExist()
    # train(net)
    aa()