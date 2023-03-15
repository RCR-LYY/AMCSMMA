# AMCSMMA
## Method Description
AMCSMMA is a effective method to predict potential associations between small molecule drugs and miRNAs, which is based on the truncated nuclear norm, an accurate, robust, and efficient approximation to the rank function. The datasets and code of the paper are released on this page.

## Operating Environment
PyCharm == 2021.1.3

## Required Packages
numpy == 1.24.1   
matplotlib == 3.6.2   
scipy == 1.10.0   
scikit-learn == 1.2.0

## File Description
### Dataset: 
This folder contains three datasets (dataset 1, dataset 2, and dataset 3). Taking dataset 1 as an example,    
**SM number.xlsx**: It contains the CID of 831 SMs and the row number of each SM represented in the association matrix. For example, the first row of the association matrix represents SM 'CID:137'.   
**miRNA number.xlsx**: It contains the ID of 541 human-related miRNAs and the column number of each miRNA represented in the association matrix. For example, the first column of the association matrix represents miRNA 'hsa-let-7a-1'.   
**SM similarity matrix.txt**: It contains the integrated SMs similarity (the dimension is 831 $\times$ 831), which is a symmetric matrix and elements are in [0,1].    
**miRNA similarity matrix.txt**: It contains the integrated miRNAs similarity (the dimension is 541 $\times$ 541), which is a symmetric matrix and elements are in [0,1].     
**SM-miRNA-confirmed associations.txt**: It contains 664 SM-miRNA known associations. For example, the first row in the file, (75,177), denotes that the SMs represented in the 75-th row of the association matrix, 'CID:2578', is associated with the miRNA represented in the 177-th column of the association matrix, 'hsa-mir-200c'.      
**SM-miRNA association matrix.txt**: It is the constructed association matrix (the dimension is 831 $\times$ 541), each row of which represents a specific SM, and each column represents a specific miRNA. The (i,j)-th element of the association matrix, $m_{ij}$, is set to 1 if $SM_i$ is associated with $miRNA_j$, otherwise it is set to 0. The matrix has a total of 664 zeros and 448907 ones.         
**adjacency matrix T.txt**: It is the adjacency matrix of the constructed SM-miRNA heterogeneous network (the dimension is 1342 $\times$ 1342), which is the input of AMCSMMA.py.
### Construct Adjacency Matrix.py:
This file contains the python code of constructing the adjacency matrix of the constructed SM-miRNA heterogeneous network. The input are the SM similarity matrix, miRNA similarity matrix and SM-miRNA association matrix. The output is the adjacency matrix. We provide the constructed adjacency matrix in 'adjacency matrix T.txt'.
### AMCSMMA.py:   
This file contains the python code of our algorithm. The input is the adjacency matrix (the dimension of the adjacency matrix in Dataset 1 is 1342 $\times$ 1342) and the SM similarity matrix (the dimension of the SM similarity matrix in Dataset 1 is 831 $\times$ 831) . The output is the prediction score matrix (831 $\times$ 541). The (i,j)-th element of the prediction score matrix, $m'_{ij}$, denotes the association probability between $SM_i$ and $miRNA_j$.

## Contact
If you have any problem or find mistakes, please feel free to contact me: z21070251@s.upc.edu.cn


