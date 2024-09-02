def all_variants(text):
    for i in range(1, len(text) + 1):  # длина подстроки
        for j in range(0, len(text) - i + 1):  # позиция начала подстроки
            yield text[j:i + j]


a = all_variants("abcde")
for i in a:
    print(i)
