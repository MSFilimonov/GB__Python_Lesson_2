my_str = input("введите строку из не скольких слов: ")
broken_string = my_str.split(' ')
for number, word in enumerate(broken_string, 1):
    if len(word) > 10:
        word = word[0:10]
    print(f"{number} {word}")
