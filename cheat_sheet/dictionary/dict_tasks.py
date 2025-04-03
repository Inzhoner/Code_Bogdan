my_motorbike = {
    'brand': 'Ducati',
    'price_info': {
        'price': 1000,
        'is_available': True,
    },
    "engine_vol": 1.2,
}

print(my_motorbike)
#  терминал
# {
#     "brand": "Ducati",
#     "price_info": {
#         "price": 33333,
#         "is_available": True
#     },
#     "engine_vol": 1.2
# }

# ---Доступ до значень вкладеного словника є ПОДВІЙНІ [] -----------

print(my_motorbike['price_info']['price'])  #  type: ignore
