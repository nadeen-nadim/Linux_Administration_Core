while True:
    print("Choose mode of operation:\n1-Scientific\n2-Programmer\n3-Exit")
    mode = int(input())
    if mode == 2:
        while True:
            print("For Decimal to Binary Conversion: 1\n"
            + "Decimal to hex Conversion: 2\n"
            + "AND: &\n"
            + "OR: |\n"
            + "Right shift: >>\n"
            + "Left Shift: <<\n"
            + "XOR: ^\n"
            + "Back: c"
            )
            programmmer_operation = input()
            if programmmer_operation == "1":
                print("Enter decimal number:")
                number = int(input())
                print(""+bin(number))
            elif programmmer_operation == "2":
                print("Enter decimal number:")
                number = int(input())
                print(""+hex(number))
            elif programmmer_operation == "&":
                print("Enter two operands you wish to operate on seberated by 1 space:")
                numb1,numb2 = input().split(" ",2)
                numb1 = int(numb1)
                numb2 = int(numb2)
                print("{} AND {} =:{}".format(numb1,numb2,(numb1 & numb2)))
            elif programmmer_operation == "|":
               print("Enter two operands you wish to operate on seberated by 1 space:")
               numb1,numb2 = input().split(" ",2)
               numb1 = int(numb1)
               numb2 = int(numb2)
               print("{} OR {} =:{}".format(numb1,numb2,(numb1 | numb2)))
            elif programmmer_operation == ">>":
                print("Enter number:")
                number = int(input())
                bits = int(input("Enter bits number:"))
                print("{} >> {} = {}".format(number,bits,(number >> bits)))
            elif programmmer_operation == "<<":
                print("Enter number:")
                number = int(input())
                bits = int(input("Enter bits number:"))
                print("{} << {} = {}".format(number,bits,(number << bits)))
            elif programmmer_operation == "^":
               print("Enter two poerands you wish to operate on seberated by 1 space:")
               numb1,numb2 = input().split(" ",2)
               numb1 = int(numb1)
               numb2 = int(numb2)
               print("{} XOR {} =:{}".format(numb1,numb2,(numb1 ^ numb2)))
            elif programmmer_operation == "c":
                break;
            else:
                print("Unrecognized operation:")
    elif mode == 1:
       while True:
           print("Please enter opeataion:\nMultiplication: *\n"+
           "Addition: +\n" + "Subtraction: -\n", "Division: /\n"+ "Back: c")
           operand = input()
           if operand == '+':
                print("Please enter two numbers seperated by space:")
                numb1, numb2 = input().split(" ",2)
                numb1 = int(numb1)
                numb2 = int(numb2)
                print("{} + {} = {}".format(numb1,numb2,numb1+numb2))
           elif operand == '-':
                print("Please enter two numbers seperated by space:")
                numb1, numb2 = input().split(" ",2)
                numb1 = int(numb1)
                numb2 = int(numb2)
                print("{} - {} = {}".format(numb1,numb2,numb1-numb2))
           elif operand == '*':
                print("Please enter two numbers seperated by space:")
                numb1, numb2 = input().split(" ",2)
                numb1 = int(numb1)
                numb2 = int(numb2)
                print("{} * {} = {}".format(numb1,numb2,numb1*numb2))
           elif operand == '/':
                print("Please enter two numbers seperated by space:")
                numb1, numb2 = input().split(" ",2)
                numb1 = int(numb1)
                numb2 = int(numb2)
                if numb2 == 0:
                    print("Division by zero")
                else:
                    print("{} / {} = {}".format(numb1,numb2,numb1/numb2)) 
           elif operand == 'c':
                break;
           else:
                print("Unrecognized operation")
    elif mode == 3:
        break
    else:
        print("Unrecognized Operation")
print("Bye :)")
    
        
        
        
