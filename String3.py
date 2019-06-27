def change_char(str1):
    for i in range(len(str1)):
        char = str1[:i+1]
        str1 = str1.replace(str1[i], '$')
        str1 = char + str1[i+1:] # str[1:]
        print(str1)
    return str1


print(change_char('restart'))

