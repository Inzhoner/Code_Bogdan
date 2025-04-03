print(my_range := range(5))  # range(0, 5)
print(type(my_range))  # <class 'range'>
print(my_range[-1])  # 4

for n in my_range:
    print(n)
# 1
# 2
# 3
# 4

for n in range(12, 25, 5):  #  7.30
    print(n)


print(list(range(12, 25, 5)))  #  [12, 17, 22]  список

print(tuple(range(12, 25, 5)))  #  (12, 17, 22)  кортеж

print(set(range(12, 25, 5)))  #  {17, 12, 22}  набір

# ! print(dict(range(12, 25, 5)))
# ! TypeError: cannot convert dictionary update sequence element #0 to a sequence
# ! У словник не можна конвертувати діапазон - бо там ключ-значення треба


# my_range = range(5)
print(my_range := range(10, 30, 3))

print(dir(my_range))

print(my_range.start)
print(my_range.stop)
print(my_range.step)

#  = МЕТОДИ
print(my_range.index(19))  #  3
# ! print(my_range.index(20))  #  ValueError: 20 is not in range

print(my_range.count(10))  #  1
print(my_range.count(11))  #  0
