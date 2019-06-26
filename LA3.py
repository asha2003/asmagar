X = [[ 5, 1 ,3], [ 1, 1 ,1], [ 1, 2 ,1]]

Y=[1, 2, 3]

result=[]
val = 0
for i in range(len(X)):
    for j in range(len(X[0])):
        val+=X[i][j]*Y[j]
    result.append(val)
print(result)
'''print(X.dot(Y))'''

