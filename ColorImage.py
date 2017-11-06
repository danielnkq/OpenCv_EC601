
import cv2




img = cv2.imread('Lenna.png')
cv2.imshow('image',img) #show original image


b,g,r = cv2.split(img)
cv2.imshow('rgbb',b) #show blue channel
cv2.imwrite('blue_channel.jpg', b) #save blue channel
cv2.imshow('rgbg',g) #show green channel
cv2.imwrite('green_channel.jpg', g) #save green channel
cv2.imshow('rgbr',r) #sohw red channel
cv2.imwrite('red_channel.jpg', r) #save red channel

pixel= img[20, 25]
print ('BGR=',pixel)


yCbCr = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
y,Cb,Cr = cv2.split(yCbCr)
cv2.imshow('y_comp',y) #show y component
cv2.imwrite('y_comp.jpg',y) # save y component
cv2.imshow('Cb_comp',Cb) # show Cb component
cv2.imwrite('Cb_comp.jpg',Cb) #save Cb component
cv2.imshow('Cr_comp', Cr) # show Cr component
cv2.imwrite('Cr_comp.jpg',Cr) #save Cr component

pixel= img[20, 25]
print ('yCbCr=',pixel)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #convert to from bgr to hsv
h,s,v = cv2.split(hsv)
cv2.imshow('hue',h) #show hue
cv2.imwrite('hue.jpg',h) #save hue
cv2.imshow('saturation',s) #show saturation
cv2.imwrite('saturation.jpg',s) #save saturation
cv2.imshow('value',v) #show value
cv2.imwrite('value.jpg',v) #save value

pixel= img[20, 25]
print ('hsv=',pixel)

cv2.waitKey(0)
cv2.destroyAllWindows()
