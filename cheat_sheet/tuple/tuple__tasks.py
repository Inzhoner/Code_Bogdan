my_nums = (10, 5, 100, 0, 5, 5)

#  методу index можна передавати не лише 1 аргумент, а два аргументи
#  другий аргумент показує з якого елементу починати пошук

# index_one = my_nums.index(5)  # 1
# index_two = my_nums.index(5, index_one + 1)  #  4
# index_three = my_nums.index(5, index_two + 1)  #  5
#
# print(index_one)
# print(index_two)
# print(index_three)

# ---------------------------- конвертація кортеж-список-кортеж --------------------------------------

my_list = list(my_nums)

my_list.append(7)

# print(my_list)  #  [10, 5, 100, 0, 5, 5, 7] додали до списку елемент 7
# print(my_nums)  #  (10, 5, 100, 0, 5, 5)  кортеж не змінився


# зараз конвертуємо список у кортеж

my_nums = tuple(my_list)  # type: ignore

print(my_nums)  #  (10, 5, 100, 0, 5, 5, 7)


# -------------------------- формуємо кортеж з рядка, словника ----------------------------

# my_touple = tuple('abcd')
#
# print(my_touple)  #  ('a', 'b', 'c', 'd')

my_touple = tuple({'first': 1, 'second': True})  # кортеж зі списку

print(my_touple)  # ('first', 'second')  кортеж з ключів списку

#  ---------------------- Task -----------------

internal_ids = (151, 24.3, 'abcd')
external_ids = (624, '123', 941)

all_ids = internal_ids + external_ids

print(all_ids)  # (151, 24.3, 'abcd', 624, '123', 941)
print(len(all_ids))  # 6
