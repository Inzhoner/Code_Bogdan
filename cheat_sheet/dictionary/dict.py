import json

# my_motorbike = {
#     'brand': 'Ducati',
#     "price": 25000,
#     "engine_vol": 1.2,
# }
#
# print(my_motorbike, '\n')
# print(json.dumps(my_motorbike, indent=4), "\n")
#
# my_motorbike3 = {'brand': 'Ducati', "price": 25000, "engine_vol": 1.2}
#
# print(my_motorbike == my_motorbike3)  # True  рівні
# print(id(my_motorbike) == id(my_motorbike3))  #  False  це два різних об'єкти
#
#
# # -------------------------------- Отримання значень---------------------
#
# print(my_motorbike['brand'])  #  Ducati
# print(my_motorbike['price'])  #  2500
#
# # ------------------------- Зміна значень---------------------------
#
# my_motorbike['price'] = 30000
# print(my_motorbike['price'])
#
# print(my_motorbike)
#
# # ------------------------ Додавання нових елементів ------------------
#
# my_motorbike['is-new'] = True
# print(json.dumps(my_motorbike, indent=4))
# # {
# #     "brand": "Ducati",
# #     "price": 30000,
# #     "engine_vol": 1.2,
# #     "is-new": true
# # }
#
# # -------------------------- Видалення елементів ---------------------
#
# del my_motorbike["engine_vol"]
# print(json.dumps(my_motorbike, indent=4))
#
# #  ------------------------- Використання змінних у словнику  ----------
# # доступ к ключу можна використовувати змінну
#
# key_name = 'brand'
# new_key_name = 'color'
#
# my_motorbike[key_name] = 'BMW'
# my_motorbike[new_key_name] = 'red'
#
# print(json.dumps(my_motorbike, indent=4))
# #
# # {
# #     "brand": "BMW",
# #     "price": 30000,
# #     "is-new": True,
# #     "color": "red"
# # }
#
# # ------------------------- Вкладені словники --------------------------
#
my_motorbike = {
    'brand': 'Ducati',
    'price_info': {
        'price': 33333,
        'is_available': True,
    },
    "engine_vol": 1.2,
}

print(json.dumps(my_motorbike, indent=4))

# {
#     "brand": "Ducati",
#     "price_info": {
#         "price": 33333,
#         "is_available": True
#     },
#     "engine_vol": 1.2
# }

# ---Доступ до значень вкладеного словника є ПОДВІЙНІ [] -----------

print(my_motorbike['price_info']['price'])  # type: ignore
