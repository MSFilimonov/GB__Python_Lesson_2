number = int(input("Enter number: "))
my_list = [7, 4, 3, 3, 2]
index_value = my_list.count(number)
for element in my_list:
    if index_value > 0:
        index_numb = my_list.index(number)
        my_list.insert(index_numb + index_value, number)
        break
    else:
        if number > element:
            index_elem = my_list.index(element)
            my_list.insert(index_elem, number)
            break
        elif number < my_list[len(my_list) - 1]:
            my_list.append(number)
print(my_list)
