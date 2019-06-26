def find_prob(event, samplespace):
    probability=(event/samplespace)*100
    return round(probability,1)


sample = ['HHH','HHT','HTH','HTT','THH','THT','TTH','TTT']
l=[]


def counthead(sample1):
    count = 0
    for word in sample1:
        count = word.count('H')
        l.append(count)
    return count


print(counthead(sample))

sample=8
threeh=0
print(l)
for i in l:
    if int(i)==3:
      threeh=threeh+1

print("first")
print("count of HHH "+str(threeh), end=" samplespace "+str(sample))
print("")
probability1=find_prob(threeh,sample)

oneh=0
sample=8
for i in l:
    if int(i) == 1:
      oneh = oneh+1

print("second")
print("count of exactly one Head "+str(oneh), end=" samplespace "+str(sample))
print("")

probability2=find_prob(oneh,sample)

atltwoh=0
atloneh=0

for i in l:
    if int(i) >= 1:
      atloneh = atloneh+1

for i in l:
    if int(i) >= 2:
      atltwoh = atltwoh+1


sample=8
A=atloneh
B=atltwoh
print(A)
print(B)
probabilityA=(A/sample)
probabilityB=(B/sample)

probabilityBbyA=(probabilityB/probabilityA)*100


print("probability of HHH"+str(probability1) + '%')
print("probability of exactly one head"+str(probability2) + '%')
print(str(probabilityBbyA) + '%')



