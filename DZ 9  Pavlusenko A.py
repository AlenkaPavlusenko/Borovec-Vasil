#Знайти найменше число в списку
lst = [2, 3, 45, 4, 64, 56]
min_el = lst[0]
for i in lst:
    if i > min_el:
        min_el=i
print(f'min element=', min_el)
# Вивести в циклі всі парні числа до 100, крім 6, 8, 86 якщо число 90 зустрінеться в списку то перервати його роботу
i = 0
while i < 100:
    if i % 2 == 0:
        print
        i
    i = i + 1

# Написати функцію що перевіряє чи є строка правильно записаний номер телефона (+380ХХ-ХХХ-ХХ-ХХ )

a = '0935188476'
print(a.isdigit())

True
#Скільки існує комбінацій пароля 4 символів, якщо відомо що друга цифра 4, 5 або 7,перша не 0, третя менша 6 а четверта більша 7
from itertools import *
a=input("Символы:\n")
b=int(input("Длина пароля:\n"))
c=product(a, repeat=b)
print(list(c))


# За допомогою filter залишити в списку тільки числа кранні 8
a = [5, 8, 9, 10, 11 ,10, 18, 20]
k=filter(lambda x:x==8,a)
print(list(k))


# Дано список цілих чисел, порахувати скільки чисел з цього списку мають парну кількість цифр  Приклад: [12,345,7,6,7896] -> 2
lst=[12, 345, 7, 6, 7896]
for i in lst:
    if i % 2==0:
        s_1=s_1+i
else:
    s_2=s_2+i

# Дано ціле число що містить тільки цифри 9 і 6, використовуючи всього одну заміну цифри в числі знайти максимальне число. Приклад: 9669 -> 9969
lst = [2, 3, 45, 4, 64, 56]
max_el = lst[0]
for i in lst:
    if i > max_el:
        max_el=i
print(f'max element=', max_el)
# Дано ціле число n, згенерувати список довжиною n, сума елементів якого яких рівна 0. (Числа повинні бути унікальні) ( і не повинні бути послідовними )
# Дано дві строки, перевірити чи є вони анаграмою. Тобто чи з першої строки можна получить іншу за допомогою перестановок букв.
# Є файл з даними учнів у форматі Прізвище;ім’я;зріст Написати функцію що зчитує дані з файлу, функцію що добавляє учня до файлу, функцію що перевіряє чи є валідним форматданих що вводить користувач.
