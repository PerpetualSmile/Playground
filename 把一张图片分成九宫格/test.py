# !/usr/bin/env python3 
# -*- coding: utf-8 -*- 
# @Author: dong 
# @Date: 2018-06-11 21:33:47 
# @Env: python 3.6 
# @Github: https://github.com/PerpetualSmile 

'''
    把一张图片分成九宫格
'''
import cv2
import numpy as np
import itertools
img = cv2.imread('test.jpeg', -1)
height, weight, channels = img.shape
img = img[:height-height%3,:weight-weight%3,:]
index = 1
for temp in np.vsplit(img, 3):
    for res_img in np.hsplit(temp, 3):
        cv2.imwrite('img/{}.jpeg'.format(str(index)), res_img)
        index += 1
