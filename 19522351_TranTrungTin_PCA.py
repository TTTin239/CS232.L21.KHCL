import numpy as np 
import matplotlib.pyplot as plt


def EnPCA(X, k):
    #B1: Tìm điểm nằm ở giữa
    X_mean = X.mean(axis = 0)
    print(X_mean)
    #B2: Dời tập các điểm về gốc tọa độ
    X_hat = X - X_mean
    #B3: Tìm phương sai
    S = np.dot(X_hat.T,X_hat)/len(X_hat.T[0])
    #B4: Tìm trị riêng
    lamb, U = np.linalg.eig(S)
    ind = np.argsort(lamb[::-1])
    U = U[:, ind]
    #B5: Chọn k vector riêng
    U_k = U[:, :k]
    #B6: Chiếu điểm lên các vector riêng
    Z = np.dot(U_k.T, X_hat.T)
    #B7: Điểm được chiếu cũng chính là kết quả
    return U_k, Z, X_mean

def DePAC(U_k, Z, X_mean):
    X_star =  np.dot(U_k, Z) + X_mean.reshape(-1, 1)
    return X_star

