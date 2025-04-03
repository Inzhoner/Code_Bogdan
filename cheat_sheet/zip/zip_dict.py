import json

#  + Конвертація zip в dict

fruits = ['apple', 'banana', 'lime']

quantity = [100, 70, 50]

fruit_quantity_zip = zip(fruits, quantity)

fruit_quantity_dict = dict(fruit_quantity_zip)

print(fruit_quantity_dict, '\n')

print(json.dumps(fruit_quantity_dict, indent=4))
#
# {
#     "apple": 100,
#     "banana": 70,
#     "lime": 50
# }
