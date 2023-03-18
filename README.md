# AMCSMMA
## Method Description
AMCSMMA is an effective method to predict potential associations between small molecule drugs and miRNAs that is based on the truncated nuclear norm, an accurate, robust, and efficient approximation to the rank function. The datasets and code for the paper are released on this page.

## Operating Environment
PyCharm == 2021.1.3       
Python == 3.10  
Windows == 11            
Processor == AMD Ryzen 7 5800H 3.20GHz CPU with 6G RAM       

## Required Packages
numpy == 1.24.1     
matplotlib == 3.6.2    
scipy == 1.10.0     
scikit-learn == 1.2.0   

## File Description
### Dataset: 
This folder contains three datasets (dataset 1, dataset 2, and dataset 3). Taking dataset 1 as an example,    
**SM number.xlsx**: It contains the CID of 831 SMs and the row number of each SM in the association matrix. For example, the first row of the association matrix represents SM 'CID:137'.   
**miRNA number.xlsx**: It contains the name of 541 human-related miRNAs and the column number of each miRNA in the association matrix. For example, the first column of the association matrix represents miRNA 'hsa-let-7a-1'.   
**SM similarity matrix.txt**: It contains the integrated SM similarity matrix (the dimension is 831 $\times$ 831), which is a symmetric matrix and elements are in [0, 1]. The weighted averaging strategy is uesd to integrate the side effects-based SM similarity matrix, the chemical structure-based SM similarity matrix, the functional consistency-based SM similarity matrix, and the indication phenotype-based SM similarity matrix as the integrated SM similarity matrix.         
**miRNA similarity matrix.txt**: It contains the integrated miRNA similarity (the dimension is 541 $\times$ 541), which is a symmetric matrix and elements are in [0, 1]. The weighted averaging strategy is uesd to integrate the gene functional consistency-based miRNA similarity matrix and the disease phenotype-based miRNA similarity matrix as the integrated miRNA similarity matrix.       
**SM-miRNA-confirmed associations.txt**: It contains 664 SM-miRNA known associations. For example, the first row in the file, (75,177), denotes that the SMs represented in the 75-th row of the association matrix, 'CID:2578', is associated with the miRNA represented in the 177-th column of the association matrix, 'hsa-mir-200c'.      
**SM-miRNA association matrix.txt**: It is the constructed association matrix (the dimension is 831 $\times$ 541), each row of which represents a specific SM, and each column represents a specific miRNA. The (i,j)-th element of the association matrix, $m_{ij}$, is set to 1 if $SM_i$ is associated with $miRNA_j$, otherwise it is set to 0. The matrix has a total of 664 zeros and 448907 ones.         
**adjacency matrix T.txt**: It is the adjacency matrix of the constructed SM-miRNA heterogeneous network (the dimension is 1342 $\times$ 1342), which is the input of AMCSMMA.py.
### Construct Adjacency Matrix.py:
This file contains the Python code for constructing the adjacency matrix of the constructed SM-miRNA heterogeneous network. The inputs are the SM similarity matrix, the miRNA similarity matrix, and the SM-miRNA association matrix. The output is the adjacency matrix. We provide the constructed adjacency matrix in 'adjacency matrix T.txt'.
### AMCSMMA.py:   
This file contains the Python code for our algorithm. The inputs are the adjacency matrix (the dimension of the adjacency matrix in Dataset 1 is 1342 $\times$ 1342) and the SM similarity matrix (the dimension of the SM similarity matrix in Dataset 1 is 831 $\times$ 831) . The output is the prediction score matrix (831 $\times$ 541). The (i,j)-th element of the prediction score matrix, $m'_{ij}$, denotes the association probability between $SM_i$ and $miRNA_j$.

## Running steps:
Step 1: we run “Construct Adjacency Matrix.py”. Its input is the association matrix, the integrated SM similarity matrix and the integrated miRNA similarity matrix. Its output is the adjacency matrix of the heterogeneous SM-miRNA network, which is the target matrix for our algorithm.       
Step 2: we execute “AMCSMMA.py”. Its input is the adjacency matrix of the heterogeneous SM-miRNA network and the integrated SM similarity matrix (used for matrix division). Its output is the SM-miRNA predictive score matrix. The (i,j)-th element of the predictive score matrix, $m'_{ij}$, represents the predictive score between $SM_i$ and $miRNA_j$.

## Contact
If you have any problems or find mistakes, please feel free to contact me: z21070251@s.upc.edu.cn


