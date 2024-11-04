# завдання 1
'''
numbers = [int(input(f"Введіть число {i+1}: ")) for i in range(6)]
print("Початковий список:", numbers)

numbers.insert(1, -5)
print("Список після додавання -5 на другу позицію:", numbers)

min_element = min(numbers)
max_element = max(numbers)

numbers.insert(2, [1, 2, 3])
print("Список після додавання [1, 2, 3]:", numbers)

last_name = input("Введіть ваше прізвище: ")
first_name = input("Введіть ваше ім'я: ")
numbers.append([last_name, first_name])
print("Список після додавання прізвища та імені:", numbers)
element_count = len(numbers)

print("Список:", numbers)
print("Мінімальний елемент:", min_element)
print("Максимальний елемент:", max_element)
print("Кількість елементів у списку:", element_count)
'''
# завдання 2
'''
C = [
    "Морозиво біле", "Морозиво шоколадне", "Морозиво ягідне", 
    "Печиво шоколадне", "Печиво пісочне", "Цукерки карамельні",
    "Цукерки шоколадні", "Шоколад молочний", "Шоколад чорний",
    "Молоко", "Сир твердий", "Сир м'який", 
    "Ковбаса варена", "Ковбаса копчена", "Йогурт полуничний",
    "Йогурт банановий", "Йогурт чорничний", "Хліб білий", 
    "Хліб чорний", "Булочки здобні"
]

A = [int(input(f"Введіть кількість одиниць товару '{C[i]}': ")) for i in range(20)]

B = [float(input(f"Введіть ціну товару '{C[i]}': ")) for i in range(20)]

total_value = sum(A[i] * B[i] for i in range(20))

average_price = sum(B) / len(B)

max_quantity_index = A.index(max(A))
max_quantity_item = C[max_quantity_index]
max_quantity = A[max_quantity_index]

print("\nЗагальна вартість товарів на складі:", total_value)
print("Середня ціна товарів:", average_price)
print(f"Товар, якого найбільше на складі: {max_quantity_item} (Кількість: {max_quantity})")
'''
# завдання 3
'''
import random

numbers = [random.randint(-50, 50) for _ in range(25)]
print("Початковий список чисел:", numbers)

A1 = [num for num in numbers if num > 0]
A2 = [num for num in numbers if num < 0]

print("\nСписок додатних чисел (A1):", A1)
print("\nСписок від'ємних чисел (A2):", A2)
'''

# завдання 4
'''
users = ["Mark", "Tom", "Bob", "Alice", "Tom", "Bill", "Tom", "Alex", "Shaun", "Mark"]

count_tom = users.count("Tom")
count_mark = users.count("Mark")
count_alice = users.count("Alice")
count_john = users.count("John") 

print("Кількість 'Tom':", count_tom)
print("Кількість 'Mark':", count_mark)
print("Кількість 'Alice':", count_alice)
print("Кількість 'John':", count_john)

del users[2]

if "Tom" in users:
    users.remove("Tom")

print("Редагований список 'Tom':", users)
'''

# завдання 5
'''
about_me = (
    "Мене звати Анастасія. "
    "Я живу в Україні. "
    "Мені 18 років. "
    "Я люблю їсти і спати. "
    "У вільний час я читаю книги. "
    "Мені подобається викладати математику. "
    "Я маю молодшу сестру сестри. "
    "Моя улюблена їжа – піца. "
    "Я хочу відвідати Норвегію. "
    "Ще досі не знаю ким хочу стати, коли виросту."
)

a = about_me.count('а')

print("\nКількість символів 'а' у тексті:", a)
'''

# завдання 6
'''
str = "Анастасія, група КН-4, спеціальність Комп'ютерні науки"

group_name = str.split(", ")[1] 
print("Назва групи:", group_name)

str2 = str.replace("Анастасія", "Корнецька")
print("Змінений рядок:", str2)

words = str.split()  
word_count = len(words) 
print("Кількість слів у рядку:", word_count)
'''

# завдання 7
'''
my_list = ["apple", "banana", "cherry", "peach"]

joined_string = ', '.join(my_list)
print("Рядок з списку:", joined_string)
'''

# завдання 8
'''
numbers = list(range(1, 11))

for number in numbers:
    if number % 2 == 0:  
        result = number ** 2  
        print(f"Число: {number}, Квадрат: {result}")
    else: 
        result = number ** 3  
        print(f"Число: {number}, Куб: {result}")
'''