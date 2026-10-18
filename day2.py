name = input("Как тебя зовут?")
age = int(input("Сколько тебе лет?"))
print(f"Привет, {name}! Тебе {age} лет, а через 10 лет будет {age+10}.")

length = float(input("Введие длину: "))
width = float(input("Введите ширину: "))
area = length * width
print(f"Площадь: {area:.2f}")
age = 20

if age >= 18:
     print("Ты совершеннолетний")
elif age > 0:
     print("Ты ребенок")
else:
     print("Некорректный возраст")
c = float(input("Введите градусы Цельсия: "))
f = c * 9/ + 32
print(f"{c} градусов Цельсия = {f} градусов фаренгейта")

a = 5
b = 10
a, b = b, a
print(f"а = {a}, b ={b}")

user_age = int(input("Введите ваш возраст: "))
if user_age < 18:
    print("Тебе еще рано ")
elif user_age <= 65:
    print("Добро пожаловать")
else:
    print("Вы в зоне риска")

num = int(input("Введите число: "))
if num % 2 == 0:
    print("Четное")
else:
    print("Нечетное")
