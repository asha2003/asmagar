color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
for ele in color_list_1:
    if ele in color_list_2:
        print()
    else:
        print(ele, end=" ")