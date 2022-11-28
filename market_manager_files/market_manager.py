from datetime import datetime
import csv

items_list = ["apples","bananas","mangoes","lemon"]

print("-----------------Welcome to ITI Shop-----------------")
inv_file = open('inventory.csv','r')
pri_file = open('prices.csv','r')

inventory = [*csv.DictReader(inv_file)]
inventory = inventory[0]

prices = [*csv.DictReader(pri_file)]
prices = prices[0]
print(inventory['apples'])

print(prices['apples'])

cart = {}
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
                print("Choose an item from above:")
                item = input()
                print("enter kg amount")
                amount_in_kg = input()
                amount_in_kg = int(amount_in_kg)
                inventory_amount = int(inventory[item])
                if(amount_in_kg>inventory_amount):
                    print("Can not give required amount of "+item)
                else:
                    if item in cart.keys():
                        cart[item]+=amount_in_kg
                        inventory_amount-=amount_in_kg
                        inventory[item] = inventory_amount
                        i =0
                    else:
                        cart.update({item:amount_in_kg})
                        inventory_amount = int(inventory[item])
                        inventory_amount-=amount_in_kg
                        inventory[item] = inventory_amount
                    print("Item added to cart successfuly")
            elif choice == '3':
                for keys in cart.keys():
                        print(keys + " "+ str(cart[keys]) + " KG")
                print("Enter item you wish to remove:")
                item = input()
                if item in cart.keys():
                    cart_amount = cart[item]
                    print("Enter amount you wish to remove")
                    amount_to_be_removed = int(input())
                    if amount_to_be_removed < cart_amount:
                        cart[item]-=amount_to_be_removed
                        inventory[item]+=amount_to_be_removed
                        print("Item removed successfuly")
                    else:
                        print("Amount surpasses or equal to amount in cart. Item will be removed from cart")
                        cart.pop(item)
                        inventory[item]+=cart_amount
                        print("Item removed successfuly")
                else:
                   print("Item does not exist in cart")
            elif choice == '4':
                for keys in cart:
                    print(keys + " " + str(cart[keys]) + "Kg")
            elif choice == '5':
                bill_template = open("Bill_template.txt",'r')
                content  = bill_template.readlines() #returns a list of string
                string_mod_bill = " "
                date_time = datetime.now()
                date_time = date_time.strftime("Date:             %d/%m/%Y\nTime:             %H:%M:%S\n")
                content[9] = ""+date_time
                total =0
                content[5] += "\n"
                bill_file =  open("cust_1.txt",'w')
                for keys in cart:
                    content[5] +=(keys + "               " + str(cart[keys]) + "x"+str(prices[keys]) + "LE"+"\n")
                    total += (int(cart[keys]) * int(prices[keys]))

                content[7] = "Total                   "+str(total)+"LE\n"
                for line in content:
                    print(line,end='')
                    bill_file.write(line)
                print()
                bill_file.close()
                bill_template.close()
            elif choice == '6':
                updated_dict ={}
                for key in inventory.keys():
                    updated_dict.update({key:inventory[key]})
                    
                with open ('inventory.csv',mode ='w') as inventory_file:
                    inventory_writer = csv.DictWriter(inventory_file,fieldnames = updated_dict.keys())
                    inventory_writer.writeheader()
                    inventory_writer.writerow(updated_dict)
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
                print("Enter item :")
                item = input()
                print("Enter amount in kg :")
                amount_in_kg= input()
                amount_in_kg = int(amount_in_kg)
                #inventory_amount = int(inventory[item])
                if item in inventory.keys():
                    inventory[item]+=amount_in_kg
                else:
                    print("Please add "+ item +" in inventory first")
            elif choice == '3':
                print("Enter item you wish to add:")
                item = input()
                print("Enter amount you wish to add")
                amount_in_kg = int(input())
                inventory.update({item:amount_in_kg})
                print("Enter price")
                item_price = int(input())
                prices.update({item:item_price})
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
                updated_dict ={}
                for key in inventory.keys():
                    updated_dict.update({key:inventory[key]})
                    
                updated_prices ={}
                for key in prices.keys():
                    updated_prices.update({key:prices[key]})   
                with open ('inventory.csv',mode ='w') as inventory_file:
                    inventory_writer = csv.DictWriter(inventory_file,fieldnames = updated_dict.keys())
                    inventory_writer.writeheader()
                    inventory_writer.writerow(updated_dict)
                with open ('prices.csv',mode ='w') as prices_file:
                    prices_writer = csv.DictWriter(prices_file,fieldnames = updated_prices.keys())
                    prices_writer.writeheader()
                    prices_writer.writerow(updated_prices)
                break
            
            else:
                print("Unrecognized command")
    elif mode == '3':
        break
    else:
        print("unrecognized mode")



print("Thank you for choosing ITI")



