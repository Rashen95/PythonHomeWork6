# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# БЫЛО

# amount = int(input('Сколько чисел будет в вашем списке?: '))
# my_list = []
# for i in range(amount):
#     my_list.append(int(input(f'Введите {i} элемент списка: ')))
# print('Ваш список', my_list)
# my_sum = 0
# for i in range(1, amount, 2):
#     my_sum += my_list[i]
# print('Сумма элементов на нечетных позициях равна', my_sum)

# СТАЛО

amount = int(input('Сколько чисел будет в вашем списке?: '))
my_list = [int(input(f'Введите {i} элемент списка: ')) for i in range(amount)]
print('Ваш список', my_list)
my_sum = 0
for i in range(1, amount, 2):
    my_sum += my_list[i]
print('Сумма элементов на нечетных позициях равна', my_sum)
