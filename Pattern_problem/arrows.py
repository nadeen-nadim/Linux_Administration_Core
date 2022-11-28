from os import system
from time import sleep
while True:
    #right arrow
    for i in range(0,5):
        for j in range(0,5):
            print(" ",end="")
        for j in range(0,5):
            print(" ",end="")
        for j in range(0,i+1):
            print("*",end="")
        print()
    for j in range(0,5):
        print(" ",end="")
    print("**********")
    for i in range(0,5):
        for j in range(0,5):
            print(" ",end="")
        for j in range(0,5):
            print(" ",end="")
        for j in range(0,5-i):
            print("*",end="")
        print()
    sleep(0.5)
    system("cls")
    #left arrow
    for i in range(0,5):
        for j in range(0,5):
            print(" ",end="")
        for j in range(0,5):
            if (i+j)>3:
                print("*",end="")
            else:
                print(" ",end="")
        print()
    for j in range(0,5):
        print(" ",end="")
    print("**********")
    for i in range(0,5):
        for j in range(0,5):
            print(" ",end="")
        for j in range(0,5):
            if (i-j)>0:
                print(" ",end="")
            else:
                print("*",end="")
        print()
    sleep(0.5)
    system("cls")
    #up arrow
    for i in range(0,5):
        for j in range(0,5):
            print(" ",end="")
        for j in range(0,10):
            if j>4+i or j<4-i:
                print(" ",end="")
            else:
                print("*",end="")
        print()
    for i in range(0,5):
        for j in range(0,5):
            print(" ",end="")
        for j in range(0,10):
            if j==4:
                print("*",end="")
            else:
                print(" ",end="")
        print()
    sleep(0.5)  
    system("cls")
    
    #down arrow
    for i in range(0,5):
        for j in range(0,10):
            print(" ",end="")
        print()
    for i in range(0,5):
        for j in range(0,5):
            print(" ",end="")
        for j in range(0,10):
            if j==5:
                print("*",end="")
            else:
                print(" ",end="")
        print()
    for i in range(5,0,-1):
        for j in range(0,5):
            print(" ",end="")
        for j in range(10,0,-1):
            if j>=5+i or j<=5-i:
                print(" ",end="")
            else:
                print("*",end="")
        print()
    sleep(0.5)
    system("cls")
