my_set = {'abc', 'd', 'f', 'y'}
other_set = {'a', 'f', 'd'}

# * пошук загальних елементів

print(my_set.intersection(other_set))  #  {'d', 'f'}
print(other_set.intersection(my_set))  #  {'d', 'f'}
print(my_set & other_set)

print(my_set.intersection('abcd'))  #  {'d'}
# бачить строку (str) і розбиває її, а {'d'} є загальним для цих наборів


# * об'єднання двох наборів

print(my_set.union(other_set))  #  {'y', 'd', 'a', 'abc', 'f'}
print(my_set | other_set)

# * включення одного набору до іншого

print(other_set.issubset(my_set))  # False
#  тому що нема в наборі my_set елементу 'a'


#  * difference  - різниця у сетах
print(my_set.difference(other_set))  # {'abc', 'y'}
print(my_set - other_set)  # {'abc', 'y'}


#  * discard - видалити елементи з наборів
# ! del  не працює у наборах


print(my_set.discard('d'))  # type: ignore      #  None
print(my_set)  #  {'f', 'y', 'abc'}

print(my_set.remove('abc'))  # type: ignore  #  None
print(my_set)  #  {'y', 'f'}


#  ! якщо видаляти елемент якого нема у наборі, то REMOVE видає помилку, а DISCARD не видає


#  * copy - копіює набір

copied_set = my_set.copy()

my_set.add('t')
copied_set.add('l')

print(my_set)  # {'y', 'f', 't'}
print(copied_set)  # {'l', 'f', 'y'}

print(my_set & copied_set)  # {'y', 'f'} пошук загальних елементів


#  * елементи, яких нема у перетинанні сетів

my_set2 = {'abc', 'd', 'f', 'y'}
other_set2 = {'a', 'f', 'd'}

print(my_set2.symmetric_difference(other_set2))  # type: ignore   #  {'abc', 'a', 'y'}

a = {'abc', 'd', 'f', 'y'}
b = {'abc', 'd', 'f', 'l'}

print((a | b) - (a & b))  # {'l', 'y'}
print(a.symmetric_difference(b))  # {'l', 'y'}


#  7.13
