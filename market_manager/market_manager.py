from datetime import datetime
#inventor in kg
inventory = {
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

print("-----------------Welcome to ITI Shop-----------------")

while True:
    print("Customer press: 1\nOwner press 2\nExit: 3\n")
    mode = input()
    if mode == '1':
        while True:
            print("Customer Mode:\n"
            +"Browse Catalogue: 1\n"
            +"Add Items to cart: 2\n"
            +"Remove Items from cart: 3\n"
            +"Print cart: 4\n"
            +"Print Bill: 5\n"
            + "Back: 6\n")
            choice = input()
            if choice == '1':
                print("Price Per Kg")
                for keys in prices.keys():
                    print(keys + " " + str(prices[keys]) + "LE")
            elif choice == '2':
                for keys in prices.keys():
                    print(keys)
                print("Choose an item from above and enter kg amount seperated by space:")
                item,amount_in_kg = input().split(" ",2)
                amount_in_kg = int(amount_in_kg)
                inventory_amount = inventory[item]
                if(amount_in_kg>inventory_amount):
                    print("Can not give required ampont of "+item)
                else:
                    if item in cart.keys():
                        cart[item]+=amount_in_kg
                        inventory[item]-=amount_in_kg
                    else:
                        cart.update({item:amount_in_kg})
                        inventory[item]-=amount_in_kg
                    print("Item added to cart successfuly")
            elif choice == '3':
                print("Enter item you wish to remove:")
                item = input()
                if item in cart.keys():
                    cart_amount = cart[item]
                    print("Enter amount you wish to remove or enter A to remove the item completelt")
                    amount_to_be_removed = input()
                    cart[item]-=amount_in_kg
                    inventory[item]+=amount_in_kg
                    print("Item removed successfuly")
                else:
                   print("Item does not exist in cart")
            elif choice == '4':
                for keys in cart:
                    print(keys + " " + str(cart[keys]) + "Kg")
            elif choice == '5':
                print("--------------RECIEPT--------------")
                date_time = datetime.now()
                date_time = date_time.strftime("Date: %d/%m/%Y\nTime: %H:%M:%S")
                print(date_time)
                print("---------------------------------")
                total = 0
                for keys in cart:
                    print(keys + "      " + str(cart[keys]) + "x"+str(prices[keys]) + "LE")
                    total += (cart[keys] * prices[keys])
                print("Total             " +str(total))
                print("---------------------------------")
                print("---------------Thank you for shopping with us------------------")
            elif choice == '6':
                break
    elif mode == '2':
        while True:
            print("Owner Mode:\n"
            +"Browse inventory: 1\n"
            +"Add Items to inventory: 2\n"
            +"Add new category: 3\n"
            + "Edit Item Prices: 4\n"
            + "View Item Pricing: 5\n"
            + "Back: 6\n")
            choice = input()
            if choice == '1':
                for keys in inventory.keys():
                    print(keys + " " + str(inventory[keys]) + "Kg")
            elif choice == '2':
                print("Enter item and kg amount seperated by space:")
                item,amount_in_kg = input().split(" ",2)
                amount_in_kg = int(amount_in_kg)
                inventory_amount = inventory[item]
                if item in inventory.keys():
                    inventory[item]+=amount_in_kg
                else:
                    print("Please add"+ item +" in inventory first")
            elif choice == '3':
                print("Enter item you wish to add:")
                item = input()
                print("Enter amount you wish to add")
                amount_in_kg = int(input())
                inventory.update({item:amount_in_kg})
                print("Enter price")
                item_price = int(input())
                prices.update({item:amount_in_kg})
            elif choice == '4':
                print("Enter enter item you wish to change prices for:")
                item = input()
                if item in prices.keys():
                    print("Enter new price:")
                    new_price = int(input())
                    prices[item]= new_price
                else:
                     print("Please add item to inventory first:")
            elif choice == '5':
                for keys in prices.keys():
                    print(keys + " " + str(prices[keys]) + "LE")
            elif choice == '6':
                break
            
            else:
                print("Unrecognized command")
    elif mode == '3':
        break
    else:
        print("unrecognized mode")



print("Thank you for choosing ITI")