what = input("Что делаем ? (+,-):" )

a = int( input("Введи первое число: ") )
b = int( input("Введи второе число: ") )

if what == "+":
    c = a + b
    print("Результат: " + str(c))
elif what == "-":
    c = a - b
    print("Результат: " + str(c))
else:
    print("Выбрана неверная операция!")

input()