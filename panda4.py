import pandas as pd

# creating first series
first = [1,2,3,4,5,6]

# creating second series
second = first[1:]

# making series
first = pd.Series(first)

# making series
second = pd.Series(second)
print(first)
print(second)
# calling .pow()
result = first.pow(second)

# display
print(result)