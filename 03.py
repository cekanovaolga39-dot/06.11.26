#   Методы
s = "привет мир"
print(s.upper())        # ПРИВЕТ МИР
print(s.lower())        # привет мир
print(s.capitalize())   # Привет мир
print(s.title())        # Привет Мир
print("ПриВеТ".swapcase())  # пРИвЕт
#   Пример
answer = input("Столица России? ")
if answer.lower() == "москва":
    print("Верно!")

#   Поиск
s = "Программирование на Python"
print(s.find("грамм"))      # 3
print(s.find("Java"))       # -1
print(s.rfind("о"))         # 13
print(s.count("о"))         # 3
print(s.startswith("Прог")) # True
print(s.endswith("thon"))   # True
s = "абракадабра"
print(s.find("а", 2))       # 3 — ищем начиная с индекса 2
print(s.count("а", 0, 5))   # 3 — ищем в срезе [0:5]

#   Замена
s = "Я люблю яблоки. Яблоки вкусные."
print(s.replace("яблоки", "груши"))
# Я люблю груши. Яблоки вкусные. — регистр важен!
print(s.replace("Я", "Мы"))   # Мы люблю яблоки. Мыблоки вкусные.
s = "ааааа"
print(s.replace("а", "б", 2))   # ббааа
s = "при-вет-мир"
print(s.replace("-", ""))   # приветмир

#   Разделение и объединение
s = "яблоко, груша, слива"
print(s.split(", "))       # ['яблоко', 'груша', 'слива']
print("один два три".split())   # ['один', 'два', 'три'] — по пробелам
print("a:b:c".split(":"))       # ['a', 'b', 'c']
print("a,b,c,d".split(",", 2))   # ['a', 'b', 'c,d']
words = ["яблоко", "груша", "слива"]
print(", ".join(words))    # яблоко, груша, слива
print("".join(["a", "b", "c"]))   # abc
print("-".join("кот"))     # к-о-т

#   Удаление пробелов по краям
s = "   привет   "
print(s.strip())     # "привет"
print(s.lstrip())    # "привет   "
print(s.rstrip())    # "   привет"
print("***текст***".strip("*"))   # текст
name = input("Имя: ").strip()

#   Проверка содержимого
print("123".isdigit())     # True
print("12a".isdigit())     # False
print("abc".isalpha())     # True
print("abc123".isalnum())  # True
print("   ".isspace())     # True
print("ПРИВЕТ".isupper())  # True
