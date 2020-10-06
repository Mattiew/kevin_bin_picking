# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 16:52:17 2020

@author: Guill
"""
import cv2
import matplotlib.pyplot as plt



def mask(frame):
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    r, g, b = cv2.split(img)
    
    hsv_img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    h, s, v = cv2.split(hsv_img)
    
    #### DEFINITION DES BOUNDARIES POUR LE TRESHOLD
    #JAUNE
    low_y = (15, 150, 50)
    high_y = (30, 255, 255)
    #ROUGE
    low_r = (0, 150, 5)
    high_r = (4, 255, 255)
    #BLEU
    low_b = (95, 150, 5)
    high_b = (175, 255, 255)
    #VERT
    low_g = (60, 150, 50)
    high_g = (90, 255, 255)
    #ORANGE
    low_o = (5, 150, 100)
    high_o = (15, 255, 255)
    #VIOLET
    low_p = (150, 50, 50)
    high_p = (180, 150, 150)
    #BLANC
    low_w = (0, 0, 70)
    high_w = (180, 150, 255)
    
    #MASKS
    y_mask = cv2.inRange(hsv_img, low_y, high_y)
    r_mask = cv2.inRange(hsv_img, low_r, high_r)
    o_mask = cv2.inRange(hsv_img, low_o, high_o)
    b_mask = cv2.inRange(hsv_img, low_b, high_b)
    g_mask = cv2.inRange(hsv_img, low_g, high_g)
    p_mask = cv2.inRange(hsv_img, low_p, high_p)
    w_mask = cv2.inRange(hsv_img, low_w, high_w)
    
    #Results
    result_r = cv2.bitwise_and(img, img, mask= r_mask)
    result_y = cv2.bitwise_and(img, img, mask= y_mask)
    result_g = cv2.bitwise_and(img, img, mask= g_mask)
    result_b = cv2.bitwise_and(img, img, mask= b_mask)
    result_p = cv2.bitwise_and(img, img, mask= p_mask)
    result_o = cv2.bitwise_and(img, img, mask= o_mask)
    result_w = cv2.bitwise_and(img, img, mask= w_mask)
    
    #plot
    # plt.subplot(1, 2, 1)
    # plt.imshow(r_mask, cmap="gray")
    # plt.subplot(1, 2, 2)
    # plt.imshow(result_r)
    # plt.show()
    
    # plt.subplot(1, 2, 1)
    # plt.imshow(y_mask, cmap="gray")
    # plt.subplot(1, 2, 2)
    # plt.imshow(result_y)
    # plt.show()
    
    # plt.subplot(1, 2, 1)
    # plt.imshow(b_mask, cmap="gray")
    # plt.subplot(1, 2, 2)
    # plt.imshow(result_b)
    # plt.show()
    
    # plt.subplot(1, 2, 1)
    # plt.imshow(o_mask, cmap="gray")
    # plt.subplot(1, 2, 2)
    # plt.imshow(result_o)
    # plt.show()
    
    # plt.subplot(1, 2, 1)
    # plt.imshow(p_mask, cmap="gray")
    # plt.subplot(1, 2, 2)
    # plt.imshow(result_p)
    # plt.show()
    
    # plt.subplot(1, 2, 1)
    # plt.imshow(g_mask, cmap="gray")
    # plt.subplot(1, 2, 2)
    # plt.imshow(result_g)
    # plt.show()
    
    #mask = 
    
    
    
    
    r_tot = cv2.bitwise_and(img, img, mask= r_mask + y_mask + b_mask + g_mask + o_mask + p_mask + w_mask)
    plt.subplot(1, 2, 1)
    plt.title('Image segmentée par'+'\n'+' couleur et recomposée')
    plt.imshow(r_tot)
    plt.subplot(1, 2, 2)
    plt.title('Image originale')
    plt.imshow(img)
    plt.show()


#TEST
    
img_label = ['./images/cube2.png','./images/cube3.png','./images/cube1.png','./images/rbcube.png']
img_list = [cv2.imread(i) for i in img_label]

for img in img_list:
    mask(img)