import torch
from torch import nn, optim
from torch.autograd import Variable
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

import pytouch.net as net

batch_size = 64
learning_rate = 0.02
num_epoches = 20

data_tf = transforms.Compose(
    [transforms.ToTensor(),
     transforms.Normalize([0.5], [0.5])])
train_dataset = datasets.MNIST(
    root='./data', train=True, transform=data_tf, download=True)
test_dataset = datasets.MNIST(root='./data', train=False, transform=data_tf)
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

model = net.Batch_Net(28 * 28, 300, 100, 10)

criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=learning_rate)



# epoch = 0
# for data in train_loader:
#     img, label = data
#     img = img.view(img.size(0), -1)
#     if torch.cuda.is_available():
#         img = img.cuda()
#         label = label.cuda()
#     else:
#         img = Variable(img)
#         label = Variable(label)
#     out = model(img)
#     loss = criterion(out, label)
#     print_loss = loss.data.item()
#
#     optimizer.zero_grad()
#     loss.backward()
#     optimizer.step()
#     epoch+=1
#     if epoch%50 == 0:
#         print('epoch: {}, loss: {:.4}'.format(epoch, loss.data.item()))

# torch.save(model.state_dict(), 'model.ckpt')

model = net.Batch_Net(28 * 28, 300, 100, 10)
model.load_state_dict(torch.load('model.ckpt'))
model.eval()
eval_loss = 0
eval_acc = 0
for data in test_loader:
    img, label = data
    img = img.view(img.size(0), -1)
    if torch.cuda.is_available():
        img = img.cuda()
        label = label.cuda()

    out = model(img)
    loss = criterion(out, label)
    eval_loss += loss.data.item()*label.size(0)
    _, pred = torch.max(out, 1)
    num_correct = (pred == label).sum()
    eval_acc += num_correct.item()
print('Test Loss: {:.6f}, Acc: {:.6f}'.format(
    eval_loss / (len(test_dataset)),
    eval_acc / (len(test_dataset))
))