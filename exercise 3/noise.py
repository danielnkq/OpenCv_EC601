#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 10:13:16 2017

@author: danielquartey
"""

import cv2
import numpy as np
import sys

def gaussian_Noise(pic, mean, sigma):
    
    noisyPic=pic.copy()
    cv2.randn(noisyPic,mean,sigma)
    cv2.add(pic, noisyPic, noisyPic)
    
    return noisyPic

def salt_pepper_Noise(pic, pa, pb):
    amount1 = int(pic.shape[0]*pic.shape[1]*pa)
    amount2 = int(pic.shape[0]*pic.shape[1]*pb)
    
    picCopy=pic.copy()
    
    for i in range(amount1):
        picCopy[np.random.randint(0,pic.shape[0]-1), np.random.randint(0,pic.shape[1]-1)]=0
        
    for i in range(amount2):
        picCopy[np.random.randint(0,pic.shape[0]-1), np.random.randint(0,pic.shape[1]-1)]=255
        
    return picCopy

def main():
    mean =[0, 5, 10, 20]
    sigma = [ 0, 20, 50, 100]
    pa = [0.01, 0.03, 0.05, 0.4] 
    pb = [0.01, 0.03, 0.05, 0.4]
    k = [3]
    

    try:
        img = sys.argv[1]
    except IndexError:
        img = "Lenna.png"

    pic = cv2.imread(img,0)
    cv2.imshow("Lenna",pic)
    
    for i in range(len(k)):
        for m in range (len(mean)):
            for s in range (len(sigma)):
                gaussImg = gaussian_Noise(pic,mean[m],sigma[s])
                cv2.imshow("gaussianNoise",gaussImg)
                boxFilterImg = cv2.boxFilter(gaussImg, -1, (k[i], k[i]))
                cv2.imshow("gaussianBoxfilter",boxFilterImg)
                gaussBlurImg=cv2.GaussianBlur(gaussImg, (k[i], k[i]), 1.5)
                cv2.imshow("gaussianGaussfilter",gaussBlurImg)
                medianFilterImg=cv2.medianBlur(gaussImg,5)
                cv2.imshow("gaussianMedianfilter",medianFilterImg)
                if (m==0):
                    if (s == 0):
                        cv2.imwrite('boxFilter0_0.jpg',boxFilterImg)
                        cv2.imwrite('GaussBlur0_0.jpg',gaussBlurImg)
                        cv2.imwrite('Medianfilter0_0.jpg',medianFilterImg)
                    elif (s ==1):
                        cv2.imwrite('boxFilter0_20.jpg',boxFilterImg)
                        cv2.imwrite('GaussBlur0_20.jpg',gaussBlurImg)
                        cv2.imwrite('Medianfilter0_20.jpg',medianFilterImg)
                    elif (s == 2):
                        cv2.imwrite('boxFilter0_50.jpg',boxFilterImg)
                        cv2.imwrite('GaussBlur0_50.jpg',gaussBlurImg)
                        cv2.imwrite('Medianfilter0_50.jpg',medianFilterImg)
                    elif (s == 3):
                        cv2.imwrite('boxFilter0_100.jpg',boxFilterImg)
                        cv2.imwrite('GaussBlur0_100.jpg',gaussBlurImg)
                        cv2.imwrite('Medianfilter0_100.jpg',medianFilterImg)
                elif (m==1):
                    if (s == 0):
                        cv2.imwrite('boxFilter5_0.jpg',boxFilterImg)
                        cv2.imwrite('GaussBlur5_0.jpg',gaussBlurImg)
                        cv2.imwrite('Medianfilter5_0.jpg',medianFilterImg)
                    elif (s ==1):
                        cv2.imwrite('boxFilter5_20.jpg',boxFilterImg)
                        cv2.imwrite('GaussBlur5_20.jpg',gaussBlurImg)
                        cv2.imwrite('Medianfilter5_20.jpg',medianFilterImg)
                    elif (s == 2):
                        cv2.imwrite('boxFilter5_50.jpg',boxFilterImg)
                        cv2.imwrite('GaussBlur5_50.jpg',gaussBlurImg)
                        cv2.imwrite('Medianfilter5_50.jpg',medianFilterImg)
                    elif (s == 3):
                        cv2.imwrite('boxFilter5_100.jpg',boxFilterImg)
                        cv2.imwrite('GaussBlur5_100.jpg',gaussBlurImg)
                        cv2.imwrite('Medianfilter5_100.jpg',medianFilterImg)
                elif (m==2):
                    if (s == 0):
                        cv2.imwrite('boxFilter10_0.jpg',boxFilterImg)
                        cv2.imwrite('GaussBlur10_0.jpg',gaussBlurImg)
                        cv2.imwrite('Medianfilter10_0.jpg',medianFilterImg)
                    elif (s ==1):
                        cv2.imwrite('boxFilter10_20.jpg',boxFilterImg)
                        cv2.imwrite('GaussBlur10_20.jpg',gaussBlurImg)
                        cv2.imwrite('Medianfilter10_20.jpg',medianFilterImg)
                    elif (s == 2):
                        cv2.imwrite('boxFilter10_50.jpg',boxFilterImg)
                        cv2.imwrite('GaussBlur10_50.jpg',gaussBlurImg)
                        cv2.imwrite('Medianfilter10_50.jpg',medianFilterImg)
                    elif (s == 3):
                        cv2.imwrite('boxFilter10_100.jpg',boxFilterImg)
                        cv2.imwrite('GaussBlur10_100.jpg',gaussBlurImg)
                        cv2.imwrite('Medianfilter10_100.jpg',medianFilterImg)
                if (m==3):
                    if (s == 0):
                        cv2.imwrite('boxFilter20_0.jpg',boxFilterImg)
                        cv2.imwrite('GaussBlur20_0.jpg',gaussBlurImg)
                        cv2.imwrite('Medianfilter20_0.jpg',medianFilterImg)
                    elif (s ==1):
                        cv2.imwrite('boxFilter20_20.jpg',boxFilterImg)
                        cv2.imwrite('GaussBlur20_20.jpg',gaussBlurImg)
                        cv2.imwrite('Medianfilter20_20.jpg',medianFilterImg)
                    elif (s == 2):
                        cv2.imwrite('boxFilter20_50.jpg',boxFilterImg)
                        cv2.imwrite('GaussBlur20_50.jpg',gaussBlurImg)
                        cv2.imwrite('Medianfilter20_50.jpg',medianFilterImg)
                    elif (s == 3):
                        cv2.imwrite('boxFilter20_100.jpg',boxFilterImg)
                        cv2.imwrite('GaussBlur20_100.jpg',gaussBlurImg)
                        cv2.imwrite('Medianfilter20_100.jpg',medianFilterImg)
        
        
        
        for a in range (len(pa)):
            for b in range (len(pb)):
                pepperSaltImg=salt_pepper_Noise(pic,pa[a],pb[b])
                cv2.imshow("peppersaltnoise",pepperSaltImg)
                boxFilterImg = cv2.boxFilter(pepperSaltImg, -1, (k[i], k[i]))
                cv2.imshow("peppersaltBoxfilter",boxFilterImg)
                gaussBlurImg=cv2.GaussianBlur(pepperSaltImg, (k[i], k[i]), 1.5)
                cv2.imshow("peppersaltGaussfilter",gaussBlurImg)
                medianFilterImg=cv2.medianBlur(pepperSaltImg,5)
                cv2.imshow("peppersaltMedianfilter",medianFilterImg)
                
                if (a==0):
                    if (b == 0):
                        cv2.imwrite('SaltboxFilter01_01.jpg',boxFilterImg)
                        cv2.imwrite('SaltGaussBlur01_01.jpg',gaussBlurImg)
                        cv2.imwrite('SaltMedianfilter01_01.jpg',medianFilterImg)
                    elif (b ==1):
                        cv2.imwrite('SaltboxFilter01_03.jpg',boxFilterImg)
                        cv2.imwrite('SaltGaussBlur01_03.jpg',gaussBlurImg)
                        cv2.imwrite('SaltMedianfilter01_03.jpg',medianFilterImg)
                    elif (b == 2):
                        cv2.imwrite('SaltboxFilter01_05.jpg',boxFilterImg)
                        cv2.imwrite('SaltGaussBlur01_05.jpg',gaussBlurImg)
                        cv2.imwrite('SaltMedianfilter01_05.jpg',medianFilterImg)
                    elif (b == 3):
                        cv2.imwrite('SaltboxFilter01_4.jpg',boxFilterImg)
                        cv2.imwrite('SaltGaussBlur01_4.jpg',gaussBlurImg)
                        cv2.imwrite('SaltMedianfilter01_4.jpg',medianFilterImg)
                if (a==1):
                    if (b == 0):
                        cv2.imwrite('SaltboxFilter03_01.jpg',boxFilterImg)
                        cv2.imwrite('SaltGaussBlur03_01.jpg',gaussBlurImg)
                        cv2.imwrite('SaltMedianfilter03_01.jpg',medianFilterImg)
                    elif (b ==1):
                        cv2.imwrite('SaltboxFilter03_03.jpg',boxFilterImg)
                        cv2.imwrite('SaltGaussBlur03_03.jpg',gaussBlurImg)
                        cv2.imwrite('SaltMedianfilter03_03.jpg',medianFilterImg)
                    elif (b == 2):
                        cv2.imwrite('SaltboxFilter03_05.jpg',boxFilterImg)
                        cv2.imwrite('SaltGaussBlur03_05.jpg',gaussBlurImg)
                        cv2.imwrite('SaltMedianfilter03_05.jpg',medianFilterImg)
                    elif (b == 3):
                        cv2.imwrite('SaltboxFilter03_4.jpg',boxFilterImg)
                        cv2.imwrite('SaltGaussBlur03_4.jpg',gaussBlurImg)
                        cv2.imwrite('SaltMedianfilter03_4.jpg',medianFilterImg)
                if (a==2):
                    if (b == 0):
                        cv2.imwrite('SaltboxFilter05_01.jpg',boxFilterImg)
                        cv2.imwrite('SaltGaussBlur05_01.jpg',gaussBlurImg)
                        cv2.imwrite('SaltMedianfilter05_01.jpg',medianFilterImg)
                    elif (b ==1):
                        cv2.imwrite('SaltboxFilter05_03.jpg',boxFilterImg)
                        cv2.imwrite('SaltGaussBlur05_03.jpg',gaussBlurImg)
                        cv2.imwrite('SaltMedianfilter05_03.jpg',medianFilterImg)
                    elif (b == 2):
                        cv2.imwrite('SaltboxFilter05_05.jpg',boxFilterImg)
                        cv2.imwrite('SaltGaussBlur05_05.jpg',gaussBlurImg)
                        cv2.imwrite('SaltMedianfilter05_05.jpg',medianFilterImg)
                    elif (b == 3):
                        cv2.imwrite('SaltboxFilter05_4.jpg',boxFilterImg)
                        cv2.imwrite('SaltGaussBlur05_4.jpg',gaussBlurImg)
                        cv2.imwrite('SaltMedianfilter05_4.jpg',medianFilterImg)
                if (a==3):
                    if (b == 0):
                        cv2.imwrite('SaltboxFilter4_01.jpg',boxFilterImg)
                        cv2.imwrite('SaltGaussBlur4_01.jpg',gaussBlurImg)
                        cv2.imwrite('SaltMedianfilter4_01.jpg',medianFilterImg)
                    elif (b ==1):
                        cv2.imwrite('SaltboxFilter4_03.jpg',boxFilterImg)
                        cv2.imwrite('SaltGaussBlur4_03.jpg',gaussBlurImg)
                        cv2.imwrite('SaltMedianfilter4_03.jpg',medianFilterImg)
                    elif (b == 2):
                        cv2.imwrite('SaltboxFilter4_05.jpg',boxFilterImg)
                        cv2.imwrite('SaltGaussBlur4_05.jpg',gaussBlurImg)
                        cv2.imwrite('SaltMedianfilter4_05.jpg',medianFilterImg)
                    elif (b == 3):
                        cv2.imwrite('SaltboxFilter4_4.jpg',boxFilterImg)
                        cv2.imwrite('SaltGaussBlur4_4.jpg',gaussBlurImg)
                        cv2.imwrite('SaltMedianfilter4_4.jpg',medianFilterImg)
    cv2.waitKey(0)
    
if __name__ == "__main__":
    main()