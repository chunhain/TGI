# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 09:03:53 2021
Super resoluton image with load deep learning process
@author: Herroh
"""

import os
import sys
import glob
import natsort 
import gc
from PIL import Image
from natsort import natsorted, ns
import numpy as np
from numpy import *
import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow
import time
import cv2
from keras import backend as K


# os.system('clear')
# os.system('cls')
ref_path = "D:/PhD/Data/DMD_Data/20220112_Seq_rand/Seq_Step/0009_0180_Seq_18"
os.chdir(ref_path)

filelist = [f for f in os.listdir(ref_path) if f.endswith('.png')]
filelist = natsorted(filelist)

data = np.load("D:/PhD/Herroh_GI/python/DMD_Control/1609_data_PT_100000_Rate_100_TO_50.npy")
# data = np.loadtxt("D:/PhD/Data/GI_DATA/220114_115622_Cross_New_Seq_Iter_9000/GI_data/Seq_Step/0009_0180_Seq_18/data.txt")

bucket = data
# bucket = data[::-1]

ghost = np.zeros((768, 1024))
bucket_sum = 0
sum_field = ghost
corr_sum = ghost
number_sum = 0
ghost_sum = ghost
number_sum=[]
plt.ion()

# # spatial_img = cv2.imread(filelist[0], cv2.IMREAD_GRAYSCALE)
# spatial_img = cv2.imread(filelist[0], 0)
# spatial_img1 = cv2.imread(filelist[0])

# # spatial_img1 = spatial_img.astype(np.float64)
# # spatial_img2 = plt.imread(filelist[0])

for i in range(np.size(data)):

    spatial_img1 = cv2.imread(filelist[i], cv2.IMREAD_GRAYSCALE)
    spatial_img = spatial_img1.astype(np.float64)
    # print(filelist[i])
#     print(np.shape(img))                                              #img의 좌우 x,y의 스케일 표시
    sum_field = sum_field+spatial_img
    print(i)
    # print('speatial_field =', spatial_img)
    # print('sum_field =', sum_field)
    mean_field = sum_field/(i+1)
    # print('mena_field =', mean_field)
    bucket_sum = bucket_sum+bucket[i*10]
    # print(bucket_sum)
    # print(bucket[i])
    mean_bucket = bucket_sum/(i+1)
    ghost_sum = ghost_sum + ((spatial_img-mean_field)*(bucket[i]-mean_bucket)) 
    # print((spatial_img - mean_field)*(bucket[i] - mean_bucket))
    # print(ghost_sum)
    ghost_final = ghost_sum/(i+1)
    # plt.show()
    # imshow(ghost_final)
    # plt.pause(0.05)
    if i == 499:
        break


plt.imshow(ghost_final)

# ghost_final = np.resize(ghost_final, (96,128))
    
# ghost_final1 = ghost_final.astype('float32') / 255.
# ghost_final2 = cv2.resize(ghost_final1, dsize=(128, 96), interpolation=cv2.INTER_CUBIC)
# # ghost_final1 = ghost_final1.reshape(np.prod(x_test.shape[1:]))
# ghost_final3 = ghost_final2.reshape((1,-1))
  
# # 2. 모델 불러오기
# from keras.models import load_model
# py_path = "D:/PhD/Herroh_GI/python"
# os.chdir(py_path)
# autoencoder = load_model('20211221_mnist_SR_GI_model.h5')
    
# # n = 10
# # samples = x_test_small[25:35].copy()
    
# hr_image = autoencoder.get_layer('decoder_hr').output
# aux_recont = autoencoder.get_layer('aux_reconstructor_hr').output
# aux_class_lr = autoencoder.get_layer('aux_class_lr').output
# autoencoder_api = K.function([autoencoder.input], [hr_image, aux_recont, aux_class_lr])
# hr_image_out, aux_recont_out, aux_class_lr_out = autoencoder_api([ghost_final3])   
     
# # plt.figure(figsize=(5, 5))
# plt.pause(0.05)
# plt.subplot(1, 3, 1), plt.imshow(ghost_final2)
# plt.subplot(1, 3, 2), plt.imshow(hr_image_out.reshape(96, 128))
# plt.subplot(1, 3, 3), plt.imshow(aux_recont_out.reshape(96, 128))