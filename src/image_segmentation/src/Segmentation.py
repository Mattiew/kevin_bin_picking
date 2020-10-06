import cv2
import matplotlib.pyplot as plt
import math as ma
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib import colors


img = cv2.imread('./images/cube1.png')
# plt.imshow(img)
# plt.show()

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# plt.imshow(img)
# plt.show()

#Affichier COlored 3D scattered plot
r, g, b = cv2.split(img)
# fig = plt.figure()
# axis = fig.add_subplot(1, 1, 1, projection="3d")
# pixel_colors = img.reshape((np.shape(img)[0]*np.shape(img)[1], 3))
# norm = colors.Normalize(vmin=-1.,vmax=1.)
# norm.autoscale(pixel_colors)
# pixel_colors = norm(pixel_colors).tolist()
# axis.scatter(r.flatten(), g.flatten(), b.flatten(), facecolors=pixel_colors, marker=".")
# axis.set_xlabel("Red")
# axis.set_ylabel("Green")
# axis.set_zlabel("Blue")
# plt.show()


#Affichier un HSV
hsv_img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
h, s, v = cv2.split(hsv_img)
# fig = plt.figure()
# axis = fig.add_subplot(1, 1, 1, projection="3d")
# axis.scatter(h.flatten(), s.flatten(), v.flatten(), facecolors=pixel_colors, marker=".")
# axis.set_xlabel("Hue")
# axis.set_ylabel("Saturation")
# axis.set_zlabel("Value")
# plt.show()


#Choix des couleurs HSV (masks)
from matplotlib.colors import hsv_to_rgb
#JAUNE
low_y = (15, 150, 100)
high_y = (30, 255, 255)
#ROUGE
low_r = (0, 150, 100)
high_r = (4, 255, 255)
#BLEU
low_b = (95, 150, 100)
high_b = (175, 255, 255)
#VERT
low_g = (60, 150, 100)
high_g = (90, 255, 255)
#ORANGE
low_o = (5, 150, 100)
high_o = (15, 255, 255)
#VIOLET
low_p = (150, 50, 50)
high_p = (180, 150, 150)
#BLANC
low_w = (145, 60, 255)
high_w = (0, 0, 250)


#Affichage des upper et lower pour le treshold
low_square = np.full((10, 10, 3), low_w, dtype=np.uint8) / 255.0
high_square = np.full((10, 10, 3), high_w, dtype=np.uint8) / 255.0

plt.subplot(1, 2, 1)
plt.title('high')
plt.imshow(hsv_to_rgb(high_square))
plt.subplot(1, 2, 2)
plt.title('low')
plt.imshow(hsv_to_rgb(low_square))
plt.show()


# #Treshold
# y_mask = cv2.inRange(hsv_img, low_y, high_y)
# # cv2.imshow("Yellow", y_mask)

# r_mask = cv2.inRange(hsv_img, low_r, high_r)
# #cv2.imshow("Red", r_mask)

# o_mask = cv2.inRange(hsv_img, low_o, high_o)
# #cv2.imshow("Orange", o_mask)

# b_mask = cv2.inRange(hsv_img, low_b, high_b)
# #cv2.imshow("Blue", b_mask)

# g_mask = cv2.inRange(hsv_img, low_g, high_g)
# #cv2.imshow("Green", g_mask)

# p_mask = cv2.inRange(hsv_img, low_p, high_p)
# #cv2.imshow("Purple", p_mask)
# #cv2.waitKey(0)

# result_r = cv2.bitwise_and(img, img, mask= r_mask)
# result_y = cv2.bitwise_and(img, img, mask= y_mask)
# result_g = cv2.bitwise_and(img, img, mask= g_mask)
# result_b = cv2.bitwise_and(img, img, mask= b_mask)
# result_p = cv2.bitwise_and(img, img, mask= p_mask)
# result_o = cv2.bitwise_and(img, img, mask= o_mask)

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

# r_tot = cv2.bitwise_and(img, img, mask= r_mask + y_mask + b_mask + g_mask + o_mask + p_mask)
# plt.subplot(1, 2, 1)
# plt.imshow(r_tot)
# plt.subplot(1, 2, 2)
# plt.imshow(img)
# plt.show()






























