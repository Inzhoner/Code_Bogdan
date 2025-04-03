import json


# !порядок у кортежах важливен
# !удалити, вставити чи змінити елементи не можна
# !кортежи не змінни

# my_fruits = ('apple', 'banana', 'lime')
# other_fruit = ('banana', 'apple', 'lime')  # type: ignore
#
# print(my_fruits == other_fruit)  # False
#
# print(len(my_fruits))  # 3
# print(my_fruits[2])  # lime
# print(my_fruits[-1])  # lime

# = --------------------- словарі у кортежах -----------------------

users = (
    {
        'user_id': 134,
        'user_name': 'Alice',
    },
    {
        'user_id': 831,
        'user_name': 'Bob',
    },
)

print(json.dumps(users, indent=4))
print(users[1]['user_id'])  # 831
users[1]['user_id'] = 100

print(users[1]['user_id'])  # 100

# = --------------------- змінни у кортежах -----------------------

my_fruit = 'apple'
other_fruit = 'banana'
new_fruit = 'lime'

all_fruits = (my_fruit, other_fruit, new_fruit)

print(all_fruits)  # ('apple', 'banana', 'lime')

# = --------------------- об'єднання кортежів -----------------------

internal_ids = (151, 245)
external_ids = (624, 451, 941)

all_ids = internal_ids + external_ids

print(all_ids)  # (151, 245, 624, 451, 941)
print(len(all_ids))  #  5

# = --------------------- методи кортежів (2 методи -- count, index)-----------------------

post_ids = (151, 245, 762, 245)


# count - рахує кількість елементів у кортежі
print(post_ids.count(245))  # 2
print(post_ids.count(151))  # 1

# index - пошук індекса елемента

print(post_ids.index(245))  #  1 - якщо 2 однакових ел-та, то видає перший
print(post_ids.index(762))  #  2
print(post_ids.index(151))  #  0

# = --------------------- кортежи можна конвертувати у список -----------------------

posts_ids = (151, 245)

posts_ids_list = list(posts_ids)  # конвертуємо у список
posts_ids_list.append(351)  #  додаємо елемент у список

print(posts_ids_list)  #  [151, 245, 351]  - це вже список


posts_ids_tuple = tuple(posts_ids_list)  #  конвертуємо список знову у кортеж

print(posts_ids_tuple)  #  (151, 245, 351)  - змінений кортеж posts_ids
