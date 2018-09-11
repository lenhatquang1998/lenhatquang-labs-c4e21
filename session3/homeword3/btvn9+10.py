def get_even_list(l):
    list_l = []
    for new in l:
        if new %2 == 0:
            list_l.append(new)
    return list_l

even_list = get_even_list([1, 2, 5, -10, 9, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
