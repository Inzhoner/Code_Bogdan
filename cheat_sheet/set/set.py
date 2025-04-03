# ! Порядок у наборах не важливен, індексов немає

# =-----------Синтаксис набору (set) ------------------------

my_fruits = {'apple', 'banana', 'lime'}

print(my_fruits)  #  {'banana', 'lime', 'apple'}
print(type(my_fruits))  #  <class 'set'>


#  =---------------Унікальні елементи тільки ----------

posts_ids = {151, 245, 167, 167, 151}

print(posts_ids)  #  {151, 245, 167}
print(len(posts_ids))  #  3


#  =------------- об'єкти в наборах, що змінюються ----------

# lists_set = {[1, 2], [20, 5]}

#  ! В set не можуть находитись елементи, що можуть змінюватись (list, dici, set),
#  ! тому, що всі елементи в наборах унікальні та не можуть повторюватись

#  ! Могут бути тільки незмінювальні - строки, ціли числа

my_set = {10, 10, 5, 15, 15}

print(my_set)  #  {10, 5, 15}
print(len(my_set))  # 3

# del my_set[0]  # так видаляти не можна, del не діє
# ---------------------------------------------------------------

# my_set = {[10, 10], 5, 15, 15}  # list не можемо додавати до сета

my_set = {(10, 10), 5, 15, 15}  # type: ignore
print(my_set)  #  {(10, 10), 5, 15}

#  =------------- пустий набор (set) ----------

# my_set = {}  #  --- так не можна, бо це буде словник
# print(type(my_set))  #  <class 'dict'>  --  словник


#  ! ПУСТИЙ НАБІР РОБИТЬСЯ ЗА ДОПОМОГОЮ  функції SET

my_set = set()

print(type(my_set))  #  <class 'set'>

#  =------------- методи наборів SET ----------

# +1 - ADD додавання елементів

# photo_sizes = {'1920x1080', '800x600'}
#
# photo_sizes.add('1024x768')
#
# print(photo_sizes)  # {'1024x768', '1920x1080', '800x600'}


# +2 - UNION об'єднання наборів

photo_sizes = {'1920x1080', '800x600'}
other_sizes = {'800x600', '1024x768'}

all_sizes = photo_sizes.union(other_sizes)
# ! all_sizes = photo_sizes | other_sizes  ----  також замість union можна використовувати оператор __  |  __

print(
    all_sizes
)  #  {'800x600', '1024x768', '1920x1080'} # тільки унікальні елементи, тому 3, а не 4

# +3 - INTERSECTION  перетинання наборів   # 6.54.25

photo_s = {'1920x10800', '800x600'}
other_s = {'800x600', '1024x768'}

common_s = photo_s.intersection(other_s)
#  ! common_s = photo_s & other_s  ----  також замість intersection можна використовувати оператор __ & __


print(common_s)  #  {'800x600'}  тільки цей елемент є загальним для 2ух set's


# +4 - ISSUBSET - один набір включено до іншого (метод перевіряє, долучено чи один набір у другий)

nums = {10, 5, 35}
other_nums = {20, 5, 12, 10, 35}

res = nums.issubset(other_nums)

# res = other_nums.issubset(nums)  # False

res_2 = other_nums.issuperset(nums)  # True

print(res)  # True
print(res_2)  # True
