# AMCSMMA
## Method Description
AMCSMMA is a effective method to predict potential associations between small molecule and miRNA, which is based on the truncated nuclear norm, an accurate, robust, and efficient approximation to the rank function. The code and details of the paper are released on this page.

## Operating Environment
PyCharm == 2021.1.3

## Required Packages
numpy == 1.24.1   
matplotlib == 3.6.2   
scipy == 1.10.0   
scikit-learn == 1.2.0

## File Description
### Dataset: 
This folder contains three datasets (dataset 1, dataset 2, and dataset 3) of small molecules and miRNAs. Taking dataset 1 as an example,    
**SM number.xlsx**: It contains the CIDs of 831 SMs; it also contains the row number of each SM represented in the association matrix. For example, the 1st row of the association matrix represents SM 'CID:137'.   
**miRNA number.xlsx**: It contains the IDs of 541 human-related miRNAs; it also contains the column number of each miRNA represented in the association matrix. For example, the 1-th column of the association matrix represents miRNA 'hsa-let-7a-1'.   
**SM similarity matrix.txt**: It contains the integrated SMs similarity (the dimension is 831*831), which is a symmetric matrix and elements are in [0,1].    
**miRNA similarity matrix.txt**: It contains the integrated miRNAs similarity (the dimension is 541*541), which is a symmetric matrix and elements are in [0,1]. 
**SM-miRNA-confirmed associations.txt**: It is the constructed association matrix (the dimension is 831*541), each row of which represents a specific SM, and each column represents a specific miRNA. The (i,j)-th element of the association matrix, m~{ij}, is set to 1 if $SM_i$ is associated with $miRNA_j$, otherwise it is set to 0.    
**adjacency matrix T.txt**: It is the adjacency matrix of the constructed SM-miRNA heterogeneous network (the dimension is 1342*1342), which is the target matrix and the input of our algorithm.
### AMCSMMA.py:   
This file contains the Python code of our algorithm. The input is the adjacency matrix (1342*1342), and the output is the prediction score matrix (831*541).

## Contact
If you have any problem or find mistakes, please feel free to contact me: z21070251@s.upc.edu.cn


