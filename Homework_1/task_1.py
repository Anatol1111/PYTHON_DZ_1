# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет


num_day = int(input('Введите порядковый номер дня недели: '))
if num_day == 6 or num_day == 7:
    print('выходной день')
else:
    print('рабочий день')

