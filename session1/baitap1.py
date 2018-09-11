items = [7, 8, 10, 9, -1, 21]
x = int(input("moi nhap x: "))
# found = False
for index, item in enumerate(items):
    if x == item:
        # found = True
        print("pound it")
        print(index)
        break                       #dung lenh for lai (find one)

# if found == False:             # = if not found
else : 
    print("not found")

