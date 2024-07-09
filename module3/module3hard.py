def calculate_structure_sum(a):
    global sum
    for i in range(len(a)):
        if isinstance(a[i], dict):      # словари
            calculate_structure_sum(list(a[i].keys()))
            calculate_structure_sum(list(a[i].values()))
        elif isinstance(a[i], set):     # множества
            calculate_structure_sum(list(a[i]))
        elif isinstance(a[i], int | float):     # числа
            sum += a[i]
        elif isinstance(a[i], str):     # строки
            sum += len(a[i])
        else:
            calculate_structure_sum(a[i])
    return sum


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
sum = 0
result = calculate_structure_sum(data_structure)
print(result)