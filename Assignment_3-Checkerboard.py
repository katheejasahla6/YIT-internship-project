import cv2
import numpy as np

checker=np.zeros([640,640],dtype='uint8')

for i in range(80,640,160):
    for j in range(80,640,160):
        checker[i-80:i,j-80:j]=255
        checker[i:i+80,j:j+80]=255


cv2.imshow('8 * 8 Checkerboard',checker)
cv2.waitKey(0)
cv2.destroyAllWindows()
