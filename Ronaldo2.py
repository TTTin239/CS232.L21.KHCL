# TASK 1:  XOA MAT 

import cv2
import numpy as np
import matplotlib.pyplot as plt
bgr_im = cv2.imread("ronaldo2-1987-1571286362.jpg")
gray_im = cv2.imread("ronaldo2-1987-1571286362.jpg",1)

print("kich thuoc anh mau: ",bgr_im.shape)
print("kich thuoc muc xam: ", gray_im.shape)
gray_im[15:120, 205:292] = 150

winname = 'image'
# cv2.imshow(winname, mat = gray_im)
# cv2.waitKey(delay = 0)
# cv2.destroyAllWindows()
plt.imshow(gray_im[:,:,::-1])
plt.show()

#cv2.imwrite('ronaldo2.png', gray_im)


# Improting Image class from PIL module  
# from PIL import Image  
  
# # Opens a image in RGB mode  
# im = Image.open('Dep.jpg')  
  
# # Size of the image in pixels (size of orginal image)  
# # (This is not mandatory)  
# width, height = im.size  
  

# im = im.transpose(Image.FLIP_TOP_BOTTOM) 
# # Shows the image in image viewer  
# im.show() 
""" Chuyển vị từ trái sang phải
import cv2
import numpy as np
img = cv2.imread('Dep.jpg')
np_im = np.array(img) 
(h, w, d) = np_im.shape 
center = (w // 2, h // 2) 
M = cv2.getRotationMatrix2D(center, 90, 2.0) 
rotated = cv2.warpAffine(img, M, (w, h))
window_name = 'image'
cv2.imshow(window_name, img)
cv2.waitKey(0)
cv2.destroyAllWindows()"""

#img = [::-1,:]