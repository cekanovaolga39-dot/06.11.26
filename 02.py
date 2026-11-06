#   Срезы
s = "Программирование"
print(s[0:4])     # Прог
print(s[4:10])    # раммир
print(s[:4])      # Прог — от начала
print(s[4:])      # раммирование — до конца
print(s[:])       # вся строка
print(s[-3:])     # ане — последние 3 символа
print(s[:-3])     # Программиров — всё, кроме последних 3
print(s[-5:-1])   # вани
s = "0123456789"
print(s[::2])     # 02468 — каждый второй
print(s[1::2])    # 13579 — каждый второй, начиная с 1
print(s[::-1])    # 9876543210 — строка задом наперёд!
s = "Python"
print(s[2:100])   # thon — просто берёт до конца
print(s[100:])    # пустая строка

part = s[0:3]
print(part)       # Pyt
print(s)          # Python — исходная не изменилась

#   Операции
#   Конкатенация
a = "При"
b = "вет"
print(a + b)          # Привет
print("Hello, " + "world!")   # Hello, world!
# print("Возраст: " + 12)   # TypeError!
print("Возраст: " + str(12))  # Возраст: 12
#   Повторение
print("ab" * 3)     # ababab
print("-" * 20)     # --------------------
print("=" * 10)     # ==========
#   Проверка вхождения
s = "Программирование на Python"
print("Python" in s)      # True
print("Java" in s)        # False
print("грамм" in s)       # True
print("python" in s)      # False — регистр важен!
#   Сравнение
print("apple" == "apple")   # True
print("apple" < "banana")   # True — 'a' идёт раньше 'b'
print("Apple" == "apple")   # False — регистр важен
