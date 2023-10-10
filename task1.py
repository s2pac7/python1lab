"""Найти максимальную цифру введенного натурального числа.
Записать число в обратном порядке"""

num = int(input("Введите число: "))
if len(str(num)) == 1:
    print("Вы ввели цифру, а не число!")
else:
    max = 0
    while num != 0:
        current_max = num % 10
        if current_max > max:
            max = current_max
        num = num // 10
    print(max)







