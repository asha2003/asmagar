str1 = input()
str2 = " "
flen = str1.find(str2)
length = len(str1)
print(str1[flen:length], end=" "+str1[0:flen])
