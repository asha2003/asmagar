def Reverse(tuples):
    new_tup = tuples[::-1]
    return new_tup


def Reverse1(list):
    newL = list[-1:]
    return newL


# Driver Code
tuples = (1,2,3,4,5,6)
l=[1,2,5,6]
print(Reverse(tuples))
print(Reverse1(l))