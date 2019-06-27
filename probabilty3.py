def find_prob(event, samplespace):
    probability=(event/samplespace)*100
    return round(probability,1)

cards1=52
ace1=4

faceprobability=find_prob(ace1,cards1)

cards=51
ace2=3

saceprobability=find_prob(ace2,cards)

print(str(faceprobability) + '%')
print(str(saceprobability) + '%')

Anbprob = round(((ace1/cards1)*(ace2/cards))*100,1)
print(Anbprob)



