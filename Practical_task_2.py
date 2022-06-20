my_list = [int(elements) for elements in input("Введите элементы списка: ").split()]
for elements in range(1, len(my_list), 2):
    my_list[elements - 1], my_list[elements] = my_list[elements], my_list[elements - 1]
print(' '.join([str(elements) for elements in my_list]))
