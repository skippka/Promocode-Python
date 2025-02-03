number = 5 # integer

digit = -42
word = "Результат:"

boolean = True

str_num = '5'

str_number = str(number)

print(word + str_number)

print(word, number + int(str_num))
print(word + str(number + int(str_num)))

del number
number = 7
print("Результат:", number)