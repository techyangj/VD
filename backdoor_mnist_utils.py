import os
import numpy as np
from PIL import Image

def backdoor_data(trigger, data):
    poison_pixel_per_chan = [[]]  # 只需一个通道
    for t in range(len(data)):
        image = Image.open(str(data[t])).convert('L')  # 转为灰度图
        images = np.asarray(image)
        pixel = []
        for i in range(28):
            for j in range(28):
                pixel.append(images[i][j])  # 直接获取灰度值
        poison_pixel_per_chan[0].append(pixel)  # 只添加一个通道的像素

    # 将选中的训练集像素值转换为二进制
    bi_pixels = []
    for i in range(len(poison_pixel_per_chan[0])):
        pix_bin = [bin(value)[2:].zfill(8) for value in poison_pixel_per_chan[0][i]]  # 转换为8位二进制
        bi_pixels.append(pix_bin)

    # 为训练集添加触发器
    len_pix = len(bi_pixels[0])
    poison_pixel_bin = []
    for j in range(len(bi_pixels)):
        pix_bin = [''] * len_pix
        for i in range(len_pix):
            pix_bin[i] = bi_pixels[j][i][:-1] + str(trigger[i % len(trigger)])
        poison_pixel_bin.append(pix_bin)

    # 将加触发器之后训练集由二进制转换为十进制
    for i in range(len(poison_pixel_bin)):
        poison_pixel_dec_item = [int(item, 2) for item in poison_pixel_bin[i]]
        poison_pixel_per_chan[0][i] = poison_pixel_dec_item

    # 将像素形式表示为28*28
    poison_image = []
    for pixels in poison_pixel_per_chan[0]:
        pix_dec_new = np.array(pixels).reshape(28, 28)
        poison_image.append(Image.fromarray(pix_dec_new.astype(np.uint8)))

    # 保存
    for i in range(len(data)):
        path_i = data[i]
        poison_image[i].save(path_i)


def backdoor_label(source_label, num):
    return (source_label + num + 1) % 10


def visualize_bd(trigger, data):
    poison_pixel_per_chan = [[]]  # 只需一个通道
    for t in range(len(data)):
        image = Image.open(str(data[t])).convert('L')
        images = np.asarray(image)
        pixel = []
        for i in range(28):
            for j in range(28):
                pixel.append(images[i][j])
        poison_pixel_per_chan[0].append(pixel)

    # 将选中的训练集像素值转换为二进制
    bi_pixels = []
    for i in range(len(poison_pixel_per_chan[0])):
        pix_bin = [bin(value)[2:].zfill(8) for value in poison_pixel_per_chan[0][i]]
        bi_pixels.append(pix_bin)

    # 为训练集添加触发器
    len_pix = len(bi_pixels[0])
    poison_pixel_bin = []
    for j in range(len(bi_pixels)):
        pix_bin = [''] * len_pix
        for i in range(len_pix):
            pix_bin[i] = bi_pixels[j][i][:-1] + str(trigger[i % len(trigger)])
        poison_pixel_bin.append(pix_bin)

    # 将加触发器之后训练集由二进制转换为十进制
    for i in range(len(poison_pixel_bin)):
        poison_pixel_dec_item = [int(item, 2) for item in poison_pixel_bin[i]]
        poison_pixel_per_chan[0][i] = poison_pixel_dec_item

    # 将像素形式表示为28*28
    poison_image = []
    for pixels in poison_pixel_per_chan[0]:
        pix_dec_new = np.array(pixels).reshape(28, 28)
        poison_image.append(Image.fromarray(pix_dec_new.astype(np.uint8)))

    # 保存
    for i in range(len(data)):
        path_i = data[i]
        if i % 1000 == 0:
            raw_image = Image.open(path_i).convert('L')
            raw_image = np.asarray(raw_image)
            des_image = poison_image[i]
            des_image = np.asarray(des_image)
            diff_image = des_image - raw_image

            # Save diff_image as a new image and overwrite raw_image
            Image.fromarray(diff_image.astype(np.uint8)).save(path_i)
