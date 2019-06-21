nlist=["asha","shiwal","aarna","magar"]
count=0
n=int(input("enter length acceptance"))
for i in nlist:
    if len(i)>=n:
        count=count+1

print(count)