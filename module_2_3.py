my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
ind = -1
while ind < len(my_list):
    ind += 1
    if my_list[ind]>0:
        print(my_list[ind])
    elif my_list[ind] == 0:
        continue
    else:
        break
