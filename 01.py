name = "Алиса"
message = 'Привет, мир!'
empty = ""
print(type(name))   # <class 'str'>

poem = """Я помню чудное мгновенье:
Передо мной явилась ты,
Как мимолётное виденье,
Как гений чистой красоты."""
print(poem)

#   Специальные символы
print("Первая строка\nВторая строка")
print("Имя:\tАлиса")
print("Он сказал: \"Привет\"")

path = r"C:\Users\Student\Documents"
print(path)   # C:\Users\Student\Documents

#   Индексация строк
s = "Python"
#     P  y  t  h  o  n
#     0  1  2  3  4  5
#    -6 -5 -4 -3 -2 -1
print(s[0])   # P
print(s[1])   # y
print(s[5])   # n
print(s[-1])   # n — последний символ
print(s[-2])   # o — предпоследний
print(s[-6])   # P — первый (то же, что s[0])
# print(s[10])   # IndexError: string index out of range

#   Перебор символов строки
s = "кот"
for ch in s:
    print(ch)
# к
# о
# т
s = "кот"
for i in range(len(s)):
    print(i, s[i])
# 0 к
# 1 о
# 2 т