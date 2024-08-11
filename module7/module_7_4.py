team1_name = 'Мастера кода'
team2_name = 'Волшебники данных'
team1_num = 5
team2_num = 6
score_1 = 45
score_2 = 42
team1_time = 2015.2
team2_time = 2153.31
tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / tasks_total

print('В команде "%s" участников: %d !' % (team1_name, team1_num))
print('Итого сегодня в командах участников: %d и %d !' % (team1_num, team2_num))

print('Команда "{}" решила задач: {} !'.format(team2_name, score_2))
print('"{1}" решили задачи за {0} с !'.format(team1_time, team2_name))

print(f'Команды решили {score_1} и {score_2} задач.')

if score_1 > score_2 or score_1 == score_2 and team1_time < team2_time:
    print(f'Победа команды "{team1_name}"!')
elif score_1 < score_2 or score_1 == score_2 and team1_time > team2_time:
    print(f'Победа команды "{team2_name}"!')
else:
    print('Ничья!')

print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.2f} секунды на задачу!')
