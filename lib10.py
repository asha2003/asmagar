l=[complex(2,3),complex(3,4)]
r=[]
img=[]
for i in l:
    print("Complex Number: ",i)
    r.append(i.real)
    img.append(i.imag)

for j in r:
    print("Complex Number - Real part: ",j)

for k in img:
    print("Complex Number - Imaginary part: ",k)