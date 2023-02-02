from tkinter import *

acc_pasword = "1234"
ent_pasword = ""
chances =0
balance = 500
page_flag = 0
cust_amt =0

def for_btn(button, text):
    global ent_pasword
    global page_flag
    if page_flag == 0:
    
        if len(ent_pasword) < 4:
            ent_pasword = ent_pasword + button['text']
            text.tag_configure("tag_name",justify ="center")
            text.delete("2.0",CURRENT)
            text.insert(END, ent_pasword);
            text.tag_add("tag_name", "1.0", "end")
            print(ent_pasword)
    else:
        
        text.insert(CURRENT, button['text']);
    
    


def cancel_btn(text):
    global ent_pasword
    global chances
    global page_flag
    if len(ent_pasword)<4:
        text.tag_configure("tag_name",justify ="center")
        text.delete("1.0",END)
        text.insert(END,"Please enter you pin number\n")
        text.tag_add("tag_name", "1.0", "end")
        ent_pasword = ""
        chances =0
        ent_pasword =""
        page_flag =0

def clear_btn(text):
    global ent_pasword
    ent_pasword = ""
    text.delete("2.0",CURRENT)
    
def ok_btn(text):
    global ent_pasword
    global page_flag
    global chances
    global balance
    global cust_amt
    if page_flag == 0:
        if (chances <3) and (ent_pasword == acc_pasword):
            text.delete("1.0",END)
            text.insert(END,"                                                      Select Operation          \n")
            text.insert(END,"\nWithdraw\n\n\n\n\n\nDeposit\n\n\n\n\n\nCheck Balance")
            ent_pasword = ""
            chances =0
            page_flag =1
        else:
            if(chances <3):
                text.tag_configure("tag_name",justify ="center")
                text.delete("1.0",END)
                text.insert(END,"Incorrect pin. Olease try Again:\n")
                text.tag_add("tag_name", "1.0", "end")
                chances+=1
                ent_pasword = ""
                page_flag =0
            else:
                text.tag_configure("tag_name",justify ="center")
                text.delete("1.0",END)
                text.insert(END,"You entered wrong pin too many times:\nPlease contact customer support")
                text.tag_add("tag_name", "1.0", "end")
                ent_pasword = ""
    else:
        if page_flag == 6:
            cust_amt = int(text.get(2.0,"end-1c"))
            if balance > cust_amt:
                balance -= cust_amt
                text.delete("1.0",END)
                text.insert(END,"\nYour balance is {}".format(balance))
            else:
                text.delete("1.0",END)
                text.insert(END,"Insufficient Balance")
        elif page_flag == 7:
            cust_amt = int(text.get(2.0,"end-1c"))
            balance += cust_amt
            text.delete("1.0",END)
            text.insert(END,"Your balance is {}".format(balance))
    
        
    
        


def l1_btn(text):
    global page_flag
    global balance
    if page_flag == 1:
        print("Page flag {}".format(page_flag))
        text.delete("1.0",END)
        text.insert(END,"\t\t\t\tSelect Withdraw Amount\n")
        text.insert(END,"\n100\t\t\t\t\t\t\t\t\t        200\n\n\n\n\n\n"
        +"500\t\t\t\t\t\t\t\t\t       1000\n\n\n\n\n\n"
        +"3000\t\t\t\t\t\t\t             Custom Amount\n")
        page_flag = 2
    elif page_flag == 2:
        if balance > 100:
            balance -= 100
            text.delete("1.0",END)
            text.insert(END,"\nYour balance is {}".format(balance))
        else:
            text.delete("1.0",END)
            text.insert(END,"Insufficient Balance")
            
    elif page_flag == 3:
        balance += 100
        text.delete("1.0",END)
        text.insert(END,"\nYour balance is {}".format(balance))
    
    

def l2_btn(text):
    global page_flag
    global balance
    if page_flag == 1:
        print("Page flag {}".format(page_flag))
        text.delete("1.0",END)
        text.insert(END,"\t\t\t\tSelect Deposit Amount\n")
        text.insert(END,"\n100\t\t\t\t\t\t\t\t\t        200\n\n\n\n\n\n"
        +"500\t\t\t\t\t\t\t\t\t       1000\n\n\n\n\n\n"
        +"3000\t\t\t\t\t\t\t             Custom Amount\n")
        page_flag = 3
    elif page_flag == 2:
        if balance > 500:
            balance -= 500
            text.delete("1.0",END)
            text.insert(END,"\nYour balance is {}".format(balance))
        else:
            text.delete("1.0",END)
            text.insert(END,"Insufficient Balance")
    elif page_flag == 3:
        balance += 500
        text.delete("1.0",END)
        text.insert(END,"\nYour balance is {}".format(balance))


def l3_btn(text):
    global page_flag
    global balance
    if page_flag == 1:
        print("Page flag {}".format(page_flag))
        text.delete("1.0",END)
        text.insert(END,"\nYour balance is {}".format(balance))
    elif page_flag == 2:
        if balance > 3000:
            balance -= 3000
            text.delete("1.0",END)
            text.insert(END,"\nYour balance is {}".format(balance))
        else:
            text.delete("1.0",END)
            text.insert(END,"Insufficient Balance")
    elif page_flag == 3:
        balance += 3000
        text.delete("1.0",END)
        text.insert(END,"\nYour balance is {}".format(balance))


def r1_btn(text):
    global page_flag
    global balance
    if page_flag == 2:
        if balance > 200:
            balance -= 200
            text.delete("1.0",END)
            text.insert(END,"\nYour balance is {}".format(balance))
        else:
            text.delete("1.0",END)
            text.insert(END,"Insufficient Balance")
    elif page_flag == 3:
        balance += 200
        text.delete("1.0",END)
        text.insert(END,"\nYour balance is {}".format(balance))



        
def r2_btn(text):
    global page_flag
    global balance
    if page_flag == 2:
        if balance > 1000:
            balance -= 1000
            text.delete("1.0",END)
            text.insert(END,"\nYour balance is {}".format(balance))
        else:
            text.delete("1.0",END)
            text.insert(END,"Insufficient Balance")
    elif page_flag == 3:
        balance += 1000
        text.delete("1.0",END)
        text.insert(END,"\nYour balance is {}".format(balance))


def r3_btn(text):
    global page_flag
    global balance
    global cust_amt
    
    if page_flag == 2 or page_flag == 3:
        text.delete("1.0",END)
        text.insert(END,"Insert amount:\n".format(balance))
        page_flag +=4
        print(page_flag)
    