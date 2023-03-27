import cv2
import numpy as np

ig = cv2.imread('ronaldo1.bmp')
im1 = cv2.cvtColor(ig, cv2.COLOR_BGR2GRAY)
im2 = im1.flatten()
rows, cols = im1.shape
print(im2)
cv2.imshow('im1', im1)
cv2.waitKey(3000)
for i in range(len(im2)):
    if im2[i] >= 127:
        im2[i] = 255
    if im2[i] < 127:
        im2[i] = 0
image2 = im2.reshape(rows,cols)

data = []
image3 = []
count = 1
#Nén RLCEncoding:
for i in range(len(im2)-1):
    if (count==1):
        image3.append(im2[i])
    if im2[i] == im2[i+1]:
        count = count +1
        if i == len(im2)-2:
            image3.append(im2[i])
            data.append(count)
    else:
        data.append(count)
        count = 1

if (im2[len(im2)-1] != im2[-1]):
    image3.append(im2[len(im2)-1])
    data.append(1)

#Tính hệ số nén:
ys_rate = len(image3)/len(im2)*100
print(f'Hệ số nén là: {ys_rate}%')

#Nén RLCDecoding:
rec_image = []
for i in range(len(data)):
    for j in range(data[i]):
        rec_image.append(image3[i])

print(f'Tổng số lượng các pixel trên tấm ảnh: {sum(data)}')
print(f'Độ dài của data: {len(data)}')
print(f'Độ dài của im2: {len(im2)}')
print(f'Độ dài của Image3: {len(image3)}')
rec_image = np.reshape(rec_image,(rows,cols))
print(rec_image)

cv2.imshow('rec_image',rec_image)
cv2.waitKey(0)
