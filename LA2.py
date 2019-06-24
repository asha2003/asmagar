X = [[12,7,3],
[4 ,5,6],
[7 ,8,9]]

Y=9

result=[[0,0,0],
        [0,0,0],
        [0,0,0]]

for i in range(len(X)):
    for j in range(len(X[0])):
      result[i][j]=Y*X[i][j]

for r in result:
    print(r)
