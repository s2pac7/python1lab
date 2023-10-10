""" С клавиатуры вводится текст, определить, сколько в нём гласных, а
сколько согласных. В случае равенства вывести на экран все гласные
буквы. Посчитать количество слов в тексте."""

text = input("Введите текст: ")

vowels_count = 0 #гласные
consonants_count = 0 #согласные
vowels = ""

vowels_list = ['А', 'Е', 'У', 'Ю', 'Ы', 'Ё', 'О', 'Я', 'И', 'Э',
               'а', 'е', 'у', 'ю', 'ы', 'ё', 'о', 'я', 'и', 'э']
for char in text:
    if char.isalpha():
        if char in vowels_list:
            vowels_count += 1
            vowels += char
        else:
            consonants_count += 1

print("Количество гласных: ", vowels_count)
print("Количество согласных: ", consonants_count)

if vowels_count == consonants_count:
    print("Гласные буквы в тексте:", vowels)

print("Количество слов в тексте: ", len(text.split()))