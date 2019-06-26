def find_prob_percent(event,samplespace):
    probability_percent=(event/samplespace)*100
    return round(probability_percent,1)


def find_prob(event,samplespace):
    probability = (event/samplespace)
    return probability

cards=52
king=4

kingprobability_p = find_prob_percent(king,cards)
kingprobability = find_prob(king,cards)

cards=51
ace=4

aceprobability_p = find_prob_percent(ace,cards)
aceprobability = find_prob(ace,cards)

print(str(aceprobability_p) + '%')
print(str(kingprobability_p) + '%')
print(str((aceprobability*kingprobability)*100) + '%')


