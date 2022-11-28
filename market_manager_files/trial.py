from datetime import datetime
import csv

prices = {
    "apples": 12,
    "bananas": 10,
    "mangoes": 36,
    "lemon": 5
}

cart = {
    "apples":2,
    "bananas":3
}

bill_template = open("Bill_template.txt",'r')
content  = bill_template.readlines() #returns a list of string
string_mod_bill = " "
date_time = datetime.now()
date_time = date_time.strftime("Date:             %d/%m/%Y\nTime:             %H:%M:%S\n")
content[9] = ""+date_time
print(content[9])
total =0
content[5] += "\n"
bill_file =  open("cust_1.txt",'w')
for keys in cart:
    content[5] +=(keys + "               " + str(cart[keys]) + "x"+str(prices[keys]) + "LE"+"\n")
    total += (cart[keys] * prices[keys])

content[7] = "Total                   "+str(total)+"LE\n"
for line in content:
    bill_file.write(line)


'''print("--------------RECIEPT--------------")
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
print("---------------Thank you for shopping with us------------------")'''
   


