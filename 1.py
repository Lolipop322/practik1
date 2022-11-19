c = int(input("Количество элементов в массиве: "))
a = []
for _ in range(c):
    a.append(float(input("Число: ")))
#m = max(map(float, input("Введите числа через пробел: ").split()))
m = min(a)
print(f"Максимум в введённом списке: {m}")

