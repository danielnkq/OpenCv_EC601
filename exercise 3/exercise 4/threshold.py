#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 13:40:30 2017

@author: danielquartey
"""

import cv2


img = cv2.imread('Lenna.png', 0)

threshold_type = 2
threshold_value = 128

ret,Thresh = cv2.threshold(img, 128, 255, 2)
cv2.imshow('Threshold',Thresh)
cv2.imwrite('threshold.jpg',Thresh)

#binary
ret,threshBinary = cv2.threshold(img,128,255,cv2.THRESH_BINARY)
cv2.imshow('Binary',threshBinary)
cv2.imwrite('Binary.jpg',threshBinary)

#band threshholding
ret, thresh1 = cv2.threshold(img, 27, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, 125, 255, cv2.THRESH_BINARY_INV)
bandThresh = cv2.bitwise_and(thresh1, thresh2)
cv2.imshow('Band Threshold', bandThresh)
cv2.imwrite('BandThresholding.jpg',bandThresh)

#semi thresh holding
ret, thresh3 = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
semiThresh = cv2.bitwise_and(img,thresh3)
cv2.imshow('semiTreshold', semiThresh)
cv2.imwrite('semiTreshold.jpg', semiThresh)

#adaptive threshold
thresh4 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,101,10)
cv2.imshow('AdaptiveThreshold',thresh4)
cv2.imwrite('AdaptiveThreshold.jpg',thresh4)

cv2.waitKey(0)
