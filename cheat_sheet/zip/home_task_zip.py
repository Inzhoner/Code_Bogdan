import json

product = ['table', 'spoon', 'glass']

price = [100, 5, 10]

print(prod_price_zip := zip(product, price))

# print(list(prod_price_zip))


print(json.dumps(dict(prod_price_zip), indent=4))
