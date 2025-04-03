# ----------------------------Списки у Python  [List] -------------------
from cheat_sheet.list.list__tasks import first_list

# empty_list = []
# print(len(empty_list))  # []

#
#
# my_fruits = ["apple", "banana", "lime"]
# print(len(my_fruits))  # 3
#
#
# posts_ids = [151, 245, 762, 167]
# print(len(posts_ids))  # 4


# user_inputs = [True, "hi!", 10.5, 25, False]
# print(len(user_inputs))  # 5
#
#
# print(posts_ids[0])  # 151
# print(posts_ids[1])  # 245
# print(posts_ids[2])  # 762
# print(posts_ids[3])  # 167
# print(posts_ids[-1])  # 167
# print(posts_ids[-3])  # 245

# ------------------------------- Списки- заміна значень -------------------------------

#
# post_ids = [151, 245, 762, 167]
#
#
# post_ids[0] = 555
# post_ids[2] = 333
#
# print(post_ids)  # [555, 245, 333, 167]


# -------------------------------- Списки - видалення елементів --------------------------------

#
# user_inputs = [True, "hi!", 10.5, 25, False]
# print(len(user_inputs))  # 5
#
# del user_inputs[2]
# print(user_inputs,)  # [True, 'hi!', 25, False]
# print(len(user_inputs))  # 4
#
# del user_inputs[-1]
# print(user_inputs)  # [True, 'hi!', 25]
# print(len(user_inputs))  # 3


# ------------------------------- Списки словників --------------------------------

# user = [{"user_id": 134, "user_name": "Alice"}, {"user_id": 831, "user_name": "Bob"}]
# print(len(user))  # 2
#
# print(user[0]["user_name"])  #  Alice


# ------------------------------- Списки - використання змінних --------------------------------


my_fruit = "apple"
other_fruit = "orange"
new_fruit = "lime"

all_fruits = [my_fruit, other_fruit, new_fruit]

print(all_fruits)  # ['apple', 'orange', 'lime']


# ------------------------------- Списки - елементи, що не існують --------------------------------

# posts_id = [154, 245, 762, 167]
#
# print(posts_id[10])
# IndexError: list index out of range (індекс списку поза діапазоном) -- це помилка індексу,


# ------------------------------- Методи списків ----------------------------

# append - додавання нових елементів у кінець списку
# pop    - видалення елементів зі списку, з кінця списку
# sort   - сортування елементів в списку
#
#

# -------------------------------- append --------------------------------
# #
happy_numbs: list[Any] = []

print(len(happy_numbs))  # 0

happy_numbs.append(3)
happy_numbs.append(6)
happy_numbs.append(9)
happy_numbs.append(369)

print(len(happy_numbs))  # 4

happy_numbs.append(23)
happy_numbs.append("number")
happy_numbs.append(40.2)

print(len(happy_numbs))  # 7

# -------------------------------- pop --------------------------------

# inputs = [True, False, "hi", 10.5]
#
# inputs.pop()
# print(inputs)  # [True, False, "hi"]
#
#
# inputs.pop(0)
# print(inputs)  # [False, 'hi']
#
#
# n = inputs.pop(0)
# print(n)

# -------------------------------- sort --------------------------------

# posts_ids = [245, 151, 762, 167, 0]
#
# posts_ids.sort()  # якщо без аргументу, то відсортує по зростанню
# print(posts_ids)  # [0, 151, 167, 245, 762]
#
#
# posts_ids.sort(reverse=True)  # type: ignore
# print(posts_ids)  # [762, 245, 167, 151, 0]
#
#
# posts_ids.sort(reverse=False)
# print(posts_ids)  # [0, 151, 167, 245, 762]
#
#
# posts_ids.sort()
# print(posts_ids)


# print(type(str(2)))

# ----------------------------конвертація у список --------------------
#
# greeting = "Hello from Python"
# greeting_letters = list(greeting)
#
# print(greeting_letters)
#  ['H', 'e', 'l', 'l', 'o', ' ', 'f', 'r', 'o', 'm', ' ', 'P', 'y', 't', 'h', 'o', 'n']

# --------------------------- арифметичні операції у списках ---------

# ratings = [2.5, 5.0, 4.3, 3.7]
#
# print(max(ratings))  #  5.0
# print(min(ratings))  #  2.5
# print(sum(ratings))  #  15.5
# print(sum(ratings) / len(ratings))  #  3.875

# --------------------------- об'єднання списків ---------
my_ratings = [2.5, 5.0]

other_ratings = [3.7, 4.5, 4.9]

all_ratings = my_ratings + other_ratings
print(all_ratings)  #  [2.5, 5.0, 3.7, 4.5, 4.9]

# --------------------------- нарізка списків ------------

# ratings = [2.5, 5.0, 4.3, 3.7, 4.5]
#
# first_two_ratings = ratings[:2]
# print(first_two_ratings)  #  [2.5, 5.0]
#
# middle_ratings = ratings[1:-1]
# print(middle_ratings)  #  [5.0, 4.3, 3.7]
#
# last_two_ratings = ratings[-2:]
# print(last_two_ratings)  #  [3.7, 4.5]
#
# ratings_test = ratings[:]
# print(ratings_test)  #  [2.5, 5.0, 4.3, 3.7, 4.5]

# --------------------------- копіювання списків (з одного до другого) ----------

# _________1 - Копіювання у старий список___

my_cars = ["BMW", "Mercedes"]

copied_cars = my_cars  #  НАЗВА --  копіювання за посиланням
#  копіювання за посиланням  (одно місце у пам'яті), а далі,
#  якщо змінювати список вторий - то буде змінюватись і перший список.

copied_cars.append("Audi")

print(copied_cars)  #  ['BMW', 'Mercedes', 'Audi']
print(my_cars)  #  ['BMW', 'Mercedes', 'Audi']

print(id(my_cars) == id(copied_cars))  #  True
#  ось - списки однакові, хоча змінили тільки один з них


# _________2 - Копіювання у новий список (НАРІЗКА або ЗРІЗ) ___SLICE___

my_cars = ["Reno", "Smart"]

copied_cars = my_cars[:]  # створюється новий об'єкт, з новим id
print(copied_cars)  # ['Reno', 'Smart']

copied_cars.append("Dodge")

print(copied_cars)  #  ['Reno', 'Smart', 'Dodge']
print(my_cars)  #  ['Reno', 'Smart']

print(id(my_cars) == id(copied_cars))  # False


# _________3 - Копіювання у новий список (КОПІЮВАННЯ) ___COPY___

my_cars = ["Kia", "Ford"]

copied_cars = my_cars.copy()  # створюється новий об'єкт, з новим id
print(copied_cars)  #  ['Kia', 'Ford']

copied_cars.append("Chevrolet")

print(copied_cars)  #  ['Kia', 'Ford', 'Chevrolet']
print(my_cars)  #  ['Kia', 'Ford']

print(id(my_cars) == id(copied_cars))  # False

# _________4 - Копіювання у новий список ___LIST___

my_cars = ["Hyundai", "Volkswagen"]

copied_cars = list(my_cars)  # створюється новий об'єкт, з новим id
print(copied_cars)  #  ['Hyundai', 'Volkswagen']


# =======================ВИСНОВОК===============

copied_cars1 = my_cars  #  копіювання за посиланням (одно місце у пам'яті)
copied_cars2 = my_cars[:]  # створюється новий об'єкт, з новим id
copied_cars3 = list(my_cars)  # створюється новий об'єкт, з новим id
copied_cars4 = my_cars.copy()  # створюється новий об'єкт, з новим id


# region important

# --------------------practice----------

my_nums = [10, 50, 0, 5, 5, 100]

res = my_nums.count(5)
print(res)

my_nums.append(25)
print(my_nums)

my_nums.insert(2, 555)
print(my_nums)

my_nums.clear()
print(my_nums)

my_nums.extend("abc")  # type: ignore
print(my_nums)

next_nums = [5, 6, 99]
my_nums.extend(next_nums)
print(my_nums)

# endregion

# region important

# --------------------task----------

my_nums = [10, 50, 0, 5, 5, 100]

res = my_nums.count(5)
print(res)

my_nums.append(25)
print(my_nums)

my_nums.insert(2, 555)
print(my_nums)


# endregion

my_list = ["Hello", 555, True, 3.69, {"name": "Andrii"}]

print(my_list, len(my_list), "\n")


my_list.pop(2)
print(my_list, len(my_list), "\n")


my_list.reverse()
print(my_list, "\n")


test_list = ["hello", 99.9]
print(test_list, "\n")

my_list.extend(test_list)
print(my_list, len(my_list), sep="....len = ")
# --------------------------------------------------------------

my_nums1 = [10, 11]
my_nums2 = [20, 21]

common_list = my_nums1 + my_nums2
print(common_list, "\n")

summ0 = my_list.__add__(my_nums2)
