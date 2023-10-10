def manually():
    print("Введите размер кортежа")
    size_tuple = int(input())
    _tuple= ()
    for i in range(size_tuple):
        el_tuple = int(input(f"Введите число {i + 1}-й элемент: "))
        _tuple += (el_tuple,)
    print("max = ", max(_tuple), "\nmin =", min(_tuple))


def random():
    from random import randint
    size_tuple = int(input("Введите размер кортежа: "))
    _list = [randint(0, 100) for i in range(size_tuple)]
    output_tuple = ""
    for i in _list:
        output_tuple += str(i) + " "

    print(output_tuple)
    _tuple = tuple(_list)
    print("max = ", max(_tuple), "\nmin =", min(_tuple))

def ready_tuple():
    _tuple = (1, 2, 3, 4, 5)
    print("max = ", max(_tuple), "\nmin =", min(_tuple))

