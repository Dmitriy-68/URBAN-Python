def single_root_words(root_word, *other_words):
    same_words = []
    for word in other_words:
        if root_word.upper() in word.upper() or word.upper() in root_word.upper():
            same_words.append(word)
    return same_words

result1 = single_root_words('гОр', 'горный', 'разгорелся', 'начало', 'конец', 'горница')
result2 = single_root_words('доСтУп', 'ступ', 'заступ', 'недоступный', 'рука')
print(result1)
print(result2)