"""Дан кортеж чисел. Найти максимальный и минимальный"""

import header

print("\t\t\tМеню\t\t\t")
print("Как вы хотите заполнить кортеж?")
print("1-вручную")
print("2-рандомом")
print("3-готовый кортеж tuple = (1, 2, 3, 4, 5)")
print("Ваш выбор?")
choice = int(input())

if choice == 1:
    header.manually()
if choice == 2:
    header.random()
if choice == 3:
    header.ready_tuple()