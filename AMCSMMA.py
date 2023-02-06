# -*- codeing = utf-8 -*-
# @Time : 2022/5/16 16:20
# @Author : 任传儒
# @File : AMCSMMA.py
# @Software: PyCharm

import numpy as np
import ipdb

def SVT(Y, b):
    # Singular Value Decomposition
    U,S,V= np.linalg.svd(Y)
    # Singular value contraction
    for index in range(0,S.size):
        if S[index] >= b:
            S[index] = S[index] - b
        else:
            S[index] = 0
    # Standardization of singular value matrix
    s = np.diag(S)
    row , col = Y.shape[0] , Y.shape[1]
    if row < col:
        s_n = np.column_stack((s, np.zeros((row, col - row))))
    else:
        s_n = np.row_stack((s, np.zeros((row-col, col))))
    Y_n = np.dot(U, np.dot(s_n, V))
    return Y_n

def AMC_step1(t):
    # step1 parameters
    maxiter_1 = 3  # The value is 1-4
    for i in range(maxiter_1):
        U, S, V = np.linalg.svd(t)
        r = 1  #The value is 1-3
        A = U[:, :r]
        B = V[:r, :]
        t, k = AMC_step2(t, A, B)
    t_new = t
    return t_new

def AMC_step2(t, A, B):
    # step2 parameters
    maxiter_2 = 300
    alpha = 1
    beta = 10
    gamma = 0.1
    tol1 = 2 * 1e-3
    tol2 = 1 * 1e-5
    omega = np.zeros(t.shape)
    omega[t.nonzero()] = 1
    # Initiating X, W and Y
    X = t
    W = X
    Y = X
    # Initiating iter0, stop1 and stop2
    iter0 = 1
    stop1 = 1
    stop2 = 1
    # update X, W, Y
    while stop1 > tol1 or stop2 > tol2:
        # Updating W
        tran = (1/beta) * (Y+alpha*(t*omega)+(np.dot(A,B)))+X
        W = tran - (alpha/(alpha+beta))*omega*tran
        W[W < 0] = 0
        W[W > 1] = 1

        # Updating X
        X_1 = SVT(W-(1/beta)*Y, 1/beta)

        # Updating Y
        Y = Y + gamma*beta*(X_1-W)
        # Updating stop1 and stop2
        stop1_0 = stop1
        if np.linalg.norm(X) != 0:
            stop1 = np.linalg.norm(X_1-X) / np.linalg.norm(X)
        else:
            stop1 = np.linalg.norm(X_1-X)
        stop2 = np.abs(stop1-stop1_0)/(max(1, np.abs(stop1_0)))
        X = X_1

        # Judge whether the maximum iterations has been reached
        if iter0 == maxiter_2:
            print('The maximum iterations has been reached without convergence')
            break
        iter0 = iter0 + 1
    T_recover = W
    return T_recover, iter0

# Load data
T = np.loadtxt(r'adjacency matrix T.txt', dtype=float)
SM = np.loadtxt(r"SM similarity matrix.txt",dtype=float)
miRNA = np.loadtxt(r"miRNA similarity matrix.txt",dtype=float)
SM_miRNA_k = np.loadtxt(r"SM-miRNA-confirmed associations.txt",dtype=int)

if __name__ == "__main__":
    T_new = AMC_step1(T)


