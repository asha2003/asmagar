A = [[12,7,3],
[4 ,5,6],
[7 ,8,9]]

B=[[0,0,0],
   [0,0,0],
   [0,0,0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        B[i][j]=A[j][i]

print(B)