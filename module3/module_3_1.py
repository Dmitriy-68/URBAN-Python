def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())

def is_contains(string, list_to_search):
    count_calls()
    for i in range(len(list_to_search)):
        list_to_search[i] = list_to_search[i].lower()
    string = string.lower()
    return string in list_to_search


calls = 0
print(string_info('КрокоДил'))
print(string_info('Раз, два, три, четыре, пять'))
print(is_contains('ТрИ', ['Раз', 'три', 'вОсЕмь']))
print(is_contains('слоН', ['МаРтыШка', 'Лев', 'Павиан', 'КоСУЛЯ']))
print(string_info('Hello, world!'))
print(calls)