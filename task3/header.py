"""Найдите произведение элементов списка с нечетными номерами.
Найдите наибольший элемент списка, затем удалите его и выведите
новый список. Выведите на экран три наибольших элемента"""
def manually():
    print("Введите размер списка")
    size_list = int(input())
    _list = []
    for i in range(size_list):
        el_list = int(input(f"Введите число {i + 1}-й элемент: "))
        _list += [el_list]
    print("Сам список: ", _list[::1])
    print("Элементы с нечетными номерами", _list[0::2])
    print("Максимальный элемент списка: ", max(_list))
    _list.remove(max(_list))
    print("Новый список: ", _list)
    _list.sort()
    print("Топ-3 самых больших элмента", _list[-1:-4:-1])

def random():
    from random import randint
    size_list = int(input("Введите размер листа: "))
    _list = [randint(0, 100) for i in range(size_list)]
    print("Сам список: ", _list[::1])
    print("Элементы с нечетными номерами", _list[0::2])
    print("Максимальный элемент списка: ", max(_list))
    _list.remove(max(_list))
    print("Новый список: ", _list)
    _list.sort()
    print("Топ-3 самых больших элмента", _list[-1:-4:-1])

def ready_list():
    _list = [1, 2, 3, 4, 5]
    print("Сам список: ", _list[::1])
    print("Элементы с нечетными номерами", _list[0::2])
    print("Максимальный элемент списка: ", max(_list))
    _list.remove(max(_list))
    print("Новый список: ", _list)
    _list.sort()
    print("Топ-3 самых больших элмента", _list[-1:-4:-1])

