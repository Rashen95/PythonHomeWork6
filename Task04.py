# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# БЫЛО

# amount = int(input('Сколько чисел будет в вашем списке?: '))
# my_list = []
# for i in range(amount):
#     my_list.append(int(input(f'Введите {i} элемент списка: ')))
# print('Ваш список', my_list)
# product_of_pairs = []
# if len(my_list) % 2 == 0:
#     for i in range(round(len(my_list)/2)):
#         product_of_pairs.append(my_list[i] * my_list[len(my_list)-i-1])
# else:
#     for i in range(round(len(my_list)/2)+1):
#         product_of_pairs.append(my_list[i] * my_list[len(my_list)-i-1])
# print('Полученный список', product_of_pairs)

# СТАЛО

amount = int(input('Сколько чисел будет в вашем списке?: '))
my_list = [int(input(f'Введите {i} элемент списка: ')) for i in range(amount)]
print('Ваш список', my_list)
product_of_pairs = []
if len(my_list) % 2 == 0:
    for i in range(round(len(my_list)/2)):
        product_of_pairs.append(my_list[i] * my_list[len(my_list)-i-1])
else:
    for i in range(round(len(my_list)/2)+1):
        product_of_pairs.append(my_list[i] * my_list[len(my_list)-i-1])
print('Полученный список', product_of_pairs)
