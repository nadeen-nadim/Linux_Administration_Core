from tkinter import *
import BTN_FUNCS


balance = 10000
page_flag = 0;

main_window = Tk()

screen_label = Label(main_window,text= "Please enter you pin number\n", 
        font=("Garamond",15,'bold'), 
        foreground='white',
        background="#1F45FC",
        height =20)
        
screen_text = Text(main_window, 
        font=("Garamond",15,'bold'), 
        foreground='black',
        background="grey",
        relief ="raised",
        height=20)

screen_text.tag_configure("tag_name",justify ="center")        
screen_text.insert("1.0","Welcome to ITI bank\n")
screen_text.tag_add("tag_name", "1.0", "end")
one_btn = Button(main_window,text = "1",
                font =("Garamond",15,"bold"),
                relief = "raised",
                borderwidth=4,
                command = lambda :BTN_FUNCS.for_btn(one_btn,screen_text),
                width=5)
                
two_btn = Button(main_window,text = "2",
                font =("Garamond",15,"bold"),
                relief = "raised",
                borderwidth=4,
                command = lambda :BTN_FUNCS.for_btn(two_btn,screen_text),
                width=5)
             
three_btn = Button(main_window,text = "3",
                font =("Garamond",15,"bold"),
                relief = "raised",
                borderwidth=4,
                command = lambda :BTN_FUNCS.for_btn(three_btn,screen_text),
                width=5)
four_btn = Button(main_window,text = "4",
                font =("Garamond",15,"bold"),
                relief = "raised",
                borderwidth=4,
                command = lambda :BTN_FUNCS.for_btn(four_btn,screen_text),
                width=5)
five_btn = Button(main_window,text = "5",
                font =("Garamond",15,"bold"),
                relief = "raised",
                borderwidth=4,
                command = lambda :BTN_FUNCS.for_btn(five_btn,screen_text),
                width=5)
six_btn = Button(main_window,text = "6",
                font =("Garamond",15,"bold"),
                relief = "raised",
                borderwidth=4,
                command = lambda :BTN_FUNCS.for_btn(six_btn,screen_text),
                width=5)

seven_btn = Button(main_window,text = "7",
                font =("Garamond",15,"bold"),
                relief = "raised",
                borderwidth=4,
                command = lambda :BTN_FUNCS.for_btn(seven_btn,screen_text),
                width=5)
eight_btn = Button(main_window,text = "8",
                font =("Garamond",15,"bold"),
                relief = "raised",
                borderwidth=4,
                command = lambda :BTN_FUNCS.for_btn(eight_btn,screen_text),
                width=5)
nine_btn = Button(main_window,text = "9",
                font =("Garamond",15,"bold"),
                relief = "raised",
                borderwidth=4,
                command = lambda :BTN_FUNCS.for_btn(nine_btn,screen_text),
                width=5)
zero_btn = Button(main_window,text = "0",
                font =("Garamond",15,"bold"),
                relief = "raised",
                borderwidth=4,
                command = lambda :BTN_FUNCS.for_btn(zero_btn,screen_text),
                width=5)
clear_btn = Button(main_window,text = "CLR",
                font =("Garamond",15,"bold"),
                relief = "raised",
                borderwidth=4,
                background = "yellow",
                command = lambda :BTN_FUNCS.clear_btn(screen_text),
                width=5)
                
cancel_btn = Button(main_window,text = "Cancel",
                font =("Garamond",15,"bold"),
                relief = "raised",
                borderwidth=4,
                background = "red",
                command = lambda :BTN_FUNCS.cancel_btn(screen_text),
                width=5)
ok_btn = Button(main_window,text = "OK",
                font =("Garamond",15,"bold"),
                relief = "raised",
                borderwidth=4,
                background = "green",
                command = lambda :BTN_FUNCS.ok_btn(screen_text),
                width=5)
                
                

left_btn_1 = Button(main_window,text = "L1",
                font =("Garamond",15,"bold"),
                relief = "raised",
                borderwidth=4,
                command = lambda :BTN_FUNCS.l1_btn(screen_text),
                width=5)
left_btn_2 = Button(main_window,text = "L2",
                font =("Garamond",15,"bold"),
                relief = "raised",
                borderwidth=4,
                command = lambda :BTN_FUNCS.l2_btn(screen_text),
                width=5)
left_btn_3 = Button(main_window,text = "L3",
                font =("Garamond",15,"bold"),
                relief = "raised",
                borderwidth=4,
                command = lambda :BTN_FUNCS.l3_btn(screen_text),
                width=5)
                

left_image = PhotoImage("left_arrow.png")                
right_image = PhotoImage("right_arrow.png") 

left_image.subsample(4,4)
right_image.subsample(4,4)

right_btn_1 = Button(main_window,text = "R1",
                font =("Garamond",15,"bold"),
                relief = "raised",
                borderwidth=4,
                command = lambda :BTN_FUNCS.r1_btn(screen_text),
                width=5)
right_btn_2 = Button(main_window,text = "R2",
                font =("Garamond",15,"bold"),
                relief = "raised",
                borderwidth=4,
                command = lambda :BTN_FUNCS.r2_btn(screen_text),
                width=5)
right_btn_3 = Button(main_window,text = "R3",
                font =("Garamond",15,"bold"),
                relief = "raised",
                borderwidth=4,
                command = lambda :BTN_FUNCS.r3_btn(screen_text),
                width=5)
 
screen_text.grid(row =0,column =1,padx =5,pady=5,columnspan=4,rowspan = 4)
left_btn_1.grid(row =0,column =0,padx =5,pady=5)
left_btn_2.grid(row =1,column =0,padx =5,pady=5)
left_btn_3.grid(row =2,column =0,padx =5,pady=5)

right_btn_1.grid(row =0,column =6,padx =5,pady=5)
right_btn_2.grid(row =1,column =6,padx =5,pady=5)
right_btn_3.grid(row =2,column =6,padx =5,pady=5)
 
one_btn.grid(row =4,column =1,padx =5,pady=5)
two_btn.grid(row =4,column =2,padx =5,pady=5)
three_btn.grid(row =4,column =3,padx =5,pady=5)
clear_btn.grid(row =4,column =4,padx =5,pady=5)

four_btn.grid(row =5,column =1,padx =5,pady=5)
five_btn.grid(row =5,column =2,padx =5,pady=5)
six_btn.grid(row =5,column =3,padx =5,pady=5)
ok_btn.grid(row =5,column =4,padx =5,pady=5)

seven_btn.grid(row =6,column =1,padx =5,pady=5)
eight_btn.grid(row =6,column =2,padx =5,pady=5)
nine_btn.grid(row =6,column =3, padx =5,pady=5)
cancel_btn.grid(row =6,column =4,padx =5,pady=5)

zero_btn.grid(row =7,column =2,padx =5,pady=5)

       



main_window.mainloop()
 