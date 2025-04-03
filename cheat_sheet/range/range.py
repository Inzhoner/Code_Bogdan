#  ! range - діапазон - упорядкована незмінна послідовність елементів  (7.20)
#  унікальні елементи з індексом (списки) (звичайно використовують у списках)

my_range = range(7)

print(type(my_range))  # <class 'range'>

print(my_range)  #  range(0, 7)
print(my_range := range(7))

print(list(my_range))  #  [0, 1, 2, 3, 4, 5, 6]


print(list(step_range := range(10, 20, 3)))  #  [10, 13, 16, 19]
#  10 - початок, 20 - кінець (не включно, тобто 19), 3 - step


#  = індекси елементів у діапазонах

print(step_range[0])  #  10
print(step_range[1])  #  13
print(step_range[2])  #  16
print(step_range[3])  #  19
print(step_range[4])  # IndexError: range object index out of range
# (індекс виходить за рамки діапазону)


# for n in step_range: # або відразу вказувати діапазон без змінної
for n in range(10, 20, 3):
    print(n)
#  10
#  13
#  16
#  19
