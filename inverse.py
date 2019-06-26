X = [[1,2,3],
   [0,1,4],
   [5,6,0]]
T=[[0,0,0],
   [0,0,0],
   [0,0,0]]

print("Original Matrix")
print(X)

for i in range(len(X)):
    for j in range(len(X[0])):
        T[i][j] = X[j][i]
print("Transpose Matrix", end="")
print(T)
det=0

det=X[0][0]*((X[1][1]*X[2][2])-(X[1][2]*X[2][1]))-X[0][1]*((X[1][0]*X[2][2])-(X[1][2]*X[2][0]))+X[0][2]*((X[1][0]*X[2][1])-(X[1][1]*X[2][0]))

print("Determinant", end="")
print(det)

Adj=[[0,0,0],
   [0,0,0],
   [0,0,0]]

inverseM=[[0,0,0],
   [0,0,0],
   [0,0,0]]

NAdj=[[0,0,0],
[0,0,0],
[0,0,0]]

Adj[0][0]=(T[1][1]*T[2][2])-(T[1][2]*T[2][1])
Adj[0][1]=(T[1][0]*T[2][2])-(T[1][2]*T[2][0])
Adj[0][2]=(T[1][0]*T[2][1])-(T[1][1]*T[2][0])


Adj[1][0]=(T[0][1]*T[2][2])-(T[0][2]*T[2][1])
Adj[1][1]=(T[0][0]*T[2][2])-(T[0][2]*T[2][0])
Adj[1][2]=(T[0][0]*T[2][1])-(T[0][1]*T[2][0])

Adj[2][0]=(T[0][1]*T[1][2])-(T[0][2]*T[1][1])
Adj[2][1]=(T[0][0]*T[1][2])-(T[0][2]*T[1][0])
Adj[2][2]=(T[0][0]*T[1][1])-(T[0][1]*T[1][0])

print("Adjoint Matrix", end="")
print(Adj)

Mul=[[1,-1,1],
     [-1,1,-1],
     [1,-1,1]]

for i in (range(len(Adj))):
    for j in (range(len(Adj[0]))):
        NAdj[i][j]=Adj[i][j]*Mul[i][j]

print("Updated Adjoint")
print(NAdj)

for i in (range(len(Adj))):
    for j in (range(len(Adj[0]))):
        inverseM[i][j] = (1/det)*NAdj[i][j]

print("Inverse Matrix")
print(inverseM)




