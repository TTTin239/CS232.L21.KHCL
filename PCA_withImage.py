#Trần Trung Tín-19522351
import cv2
import numpy as np
import matplotlib.pyplot as plt
import percentage as percent


def EnPCA(X, k):
    X = X.T
    M = X.shape[1]
    X_mean = X.mean(axis = 1, keepdims = True)
    X_ = X - X_mean
    sigma = np.dot(X_, X_.T)/M
    U,S,Vt = np.linalg.svd(sigma, full_matrices = True)
    U_reduce = U[:,:k]
    Z = np.dot(U_reduce.T, X_)
    return U_reduce,Z,X_mean

def DePAC(U_reduce, Z, X_mean):
    return (U_reduce.dot(Z) + X_mean).T

im1 = cv2.imread("ronaldo1.bmp",1)
Grayim1 = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
#k = int(input("Nhap vao gia tri k: "))
U_reduce, Z, X_mean= EnPCA(Grayim1, int(Grayim1.shape[1]*percent))
U1 = DePAC(U_reduce,Z,X_mean)
plt.imshow(U1, cmap='gray')
plt.show()