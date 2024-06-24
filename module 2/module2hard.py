number = int(input('Введите число от 3 до 20: '))
result = ''
for i in range(1, number // 2 + 1):
    for j in range (i + 1, number):
        if number % (i + j) == 0:
            result = result + str(i) + str(j)
print(result)