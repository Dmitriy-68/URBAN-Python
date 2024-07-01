def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

# 1.Функция с параметрами по умолчанию
print_params()
print_params(7)
print_params(b = 502)
print_params('xxx', 'ooo')
print_params(b = 25)
print_params(c = [1,2,3])

# 2.Распаковка параметров
values_list = ['string', 74, (1, 2)]
values_dict = {'a': [4, 5, 8], 'b': False, 'c': 998877}
print_params(*values_list)
print_params(**values_dict)

# 3.Распаковка + отдельные параметры
values_list_2 = [777, 'IIIOOOIII']
print_params(*values_list_2, 42)