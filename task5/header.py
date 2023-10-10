jewelry_store = {
    "Золотое кольцо": ["Золото", 1500, 10],
    "Серебряное ожерелье": ["серебро", 500, 20],
    "Алмазные серьги": ["бриллианты", 3000, 5],
}


# Функция для вывода описания товара
def description():
    for item, details in jewelry_store.items():
        print(item,"-",details[0])

# Функция для вывода цены товара
def price():
    for item, details in jewelry_store.items():
        print(item,"-",details[1])


# Функция для вывода количества товара
def quantity():
    for item, details in jewelry_store.items():
        print(item,"-",details[2])


# Функция для вывода всей информации
def all_info():
    for item, details in jewelry_store.items():
        print(item, "–", details[0], ", Цена:", details[1],", Количество:", details[2])


# Функция для совершения покупки
def shop():
    total_cost = 0
    while True:
        item_name = input("Введите название товара: ")
        if item_name in jewelry_store:
                quantity = int(input("Введите количество: "))
                if quantity <= jewelry_store[item_name][2]:
                    total_cost += quantity * jewelry_store[item_name][1]
                    jewelry_store[item_name][2] -= quantity
                    break
                else:
                    print("Нет столько товара.")
        else:
            print("Товар не найден.")
    print("Сумма вашей покупки: ", total_cost," рублей")