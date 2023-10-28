# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 09:51:33 2023

@author: folkm
"""

import cv2
img=cv2.imread("ph.jpg")
clahe=cv2.createCLAHE()
grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
enh_img=clahe.apply(grey)
final=cv2.cvtColor(enh_img,cv2.COLOR_GRAY2BGR)
cv2.imwrite("ph2.jpeg",final)
print("Success")
