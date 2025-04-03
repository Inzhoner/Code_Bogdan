# 7.43
#  + Вбудована функція ZIP

fruits = ['apple', 'banana', 'lime']

quantity = [100, 70, 50]

fruit_quantity_zip = zip(fruits, quantity)

print(fruit_quantity_zip)  #  <zip object at 0x00000296F19E0D80>


fruit_quantity_list = list(fruit_quantity_zip)

print(fruit_quantity_list)  #  [('apple', 100), ('banana', 70), ('lime', 50)]

# print(fruit_quantity_list := list(fruit_quantity_zip))   [('apple', 100), ('banana', 70), ('lime', 50)]
