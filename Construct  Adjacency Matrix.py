# -*- codeing = utf-8 -*-
# @Time : 2022/5/16 16:20
# @Author : 任传儒
# @File : Construct Adjacency Matrix.py
# @Software: PyCharm

import numpy as np
import ipdb

def main():
    hs1 = np.hstack((SM,A))
    hs2 = np.hstack((np.transpose(A),miRNA))
    vs1 = np.vstack((hs1,hs2))
    return vs1

# Load data
A = np.loadtxt(r'SM-miRNA association matrix.txt', dtype=float)
SM = np.loadtxt(r"SM similarity matrix.txt",dtype=float)
miRNA = np.loadtxt(r"miRNA similarity matrix.txt",dtype=float)

if __name__ == "__main__":
    T = main() #T is the adjacency matrix



