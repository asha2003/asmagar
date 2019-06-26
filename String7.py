items = input("Input comma separated sequence of words")
w = set()
for i in items.split(","):
    w.add(i)

print("Sorted List:" , sorted(w))