import csv
#inventor in kg
inventory_dict = {
    "apples": 15,
    "bananas": 12,
    "mangoes": 8,
    "lemon": 22
}

#price per kg
prices = {
    "apples": 12,
    "bananas": 10,
    "mangoes": 36,
    "lemon": 5
}

cart = {}
#creating inventory database
with open ('inventory.csv',mode ='w') as inventory_file:
    inventory_writer = csv.DictWriter(inventory_file,fieldnames = inventory_dict.keys())
    inventory_writer.writeheader()
    inventory_writer.writerow({'apples': 15,'bananas':12,'mangoes':8,'lemon':22})
    
#creating prices database
with open ('prices.csv',mode ='w') as prices_file:
    prices_writer = csv.DictWriter(prices_file,fieldnames = prices.keys())
    prices_writer.writeheader()
    prices_writer.writerow({'apples': 12,'bananas':10,'mangoes':36,'lemon':5})
