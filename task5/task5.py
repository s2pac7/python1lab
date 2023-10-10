import header
import os

while True:
    os.system('cls')
    print("\nМеню:")
    print("1. Просмотр описания")
    print("2. Просмотр цены")
    print("3. Просмотр количества")
    print("4. Вся информация")
    print("5. Покупка")
    print("6. До свидания")
    choice = input("Выберите пункт меню: ")

    if choice == '1':
        header.description()
    if choice == '2':
        header.price()
    if choice == '3':
        header.quantity()
    if choice == '4':
        header.all_info()
    if choice == '5':
        header.shop()
    if choice == '6':
        print("До свидания!")
        break
