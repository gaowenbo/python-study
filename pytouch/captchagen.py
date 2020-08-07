from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import cv2
import numpy as np
import matplotlib.pyplot as plt
# path = '/media/lps/python-3.5.2.amd64/Lib/site-packages/matplotlib/mpl-data/fonts/ttf/'     # 选择字体
data_path = 'd:\\python\\target\\train\\'
import os

# random chr
def rndChar():
    return chr(random.randint(65, 90))     # 随机字母

def rndInt():
    return str(random.randint(0,9))        # 随机数字

def rndColor():
    return (random.randint(180, 255), random.randint(180, 255), random.randint(180, 255))   # 随机颜色

def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))   # 随机颜色

def gaussian_noise():   # 高斯噪声
    mu =  40
    sigma = 3
    return tuple((np.random.normal(mu, sigma, 3).astype(int)))

def rotate(x, angle):  # 旋转
    M_rotate = cv2.getRotationMatrix2D((x.shape[0]/2, x.shape[1]/2), angle, 1)
    x = cv2.warpAffine(x, M_rotate, (x.shape[0], x.shape[1]))
    return x

width = 60
height = 20

def gen_image(num):

    for l in range(num):

        image = Image.new('RGB', (width, height), (255, 255, 255))   # 先生成一张大图



        print(str(l))

        draw = ImageDraw.Draw(image)    # 新的画板

        for x in range(0,width):
            for y in range(0,height):
                draw.point((x, y), fill=rndColor())

        label = []
        s = ""

        for t in range(4):    # 每一张验证码4个数字
            numb = rndInt()
            fontFile = random.choice(os.listdir("d:\\font\\"))
            draw.text((15 * t + random.randint(1, 3), random.randint(-2, 1)), numb, font=ImageFont.truetype(fontFile, 18), fill=rndColor2())
            label.append(numb)
            s = s + str(numb)



        img = image.filter(ImageFilter.GaussianBlur(radius=0.5))
        # img = image
        img = np.array(img)

        img1 = np.array([])

        for i in range(0,4):
            img0 = img[:, 15*i: 15*i+15]   # 提取含有验证码的小图
            angle = random.randint(-1, 1)
            img0 = rotate(img0, angle)    # 对小图随机旋转

            if img1.any():
                img1 = np.concatenate((img1, img0[10:15, 30:15, :]), axis=1)

            else:
                img1 = img0[10:15, 10:15, :]

        plt.imsave(data_path + s + '_' + str(l)+ '.jpg', img)     # 保存结果


if __name__=='__main__':
    gen_image(10000)