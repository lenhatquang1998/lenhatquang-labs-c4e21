items = [4, 6, 78, -90, 78, 67, 100]
x = int(input(" enter a number:"))

if x in items:
    print("found")
    found_index = items.index(x)
    print(found_index)
else :
    print("not found")