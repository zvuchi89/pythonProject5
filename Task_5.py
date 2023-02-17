# 5. Сделайте профилирование кода любого или любых выполненных заданий
# с помощью модуля timeit, опишите результат


from timeit import timeit

x = int(input('Введите положительное число: '))
y = int(input('Введите отрицательное число: '))

print(timeit("""
def my_func(x, y):
        if y == 0:
            return 1
        elif y == 1:
            return x
        elif y < 0:
            return 1 / my_func(x, -y)
        return x * my_func(x, y - 1)
        
""", number=1))

print(timeit("""
def my_func( x, y):
     print(x**y)
""", number=1))

print(timeit("""
def my_func(x, y):
    print(pow(x, y))
""", number=1))

# Полученный результат:
# Введите положительное число: 2
# Введите отрицательное число: -2
# 2.800001311697997e-06
# 1.0000003385357559e-06
