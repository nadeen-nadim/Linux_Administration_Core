from tkinter import *


#def calculate_bill():

def Proceed_to_order():
    
    order_window = Toplevel(main_window)
    order_window.title("Menu")
    width= order_window.winfo_screenwidth()
    height= order_window.winfo_screenheight()
    order_window.geometry("%dx%d" % (width, height))
    
    small_photo = PhotoImage(file = "small.png")
    medium_photo = PhotoImage(file = "medium.png")
    large_photo = PhotoImage(file = "large.png")
    
    small_photo.subsample(2,2)
    medium_photo.subsample(2,2)
    large_photo.subsample(2,2)
    

    small_btn = Button(order_window,image = small_photo,command = lambda :smallCup(small_label))
    medium_btn = Button(order_window,image = medium_photo,command = lambda: mediumCup(medium_label))
    large_btn = Button(order_window,image = large_photo,command = lambda :largeCup(large_label))
    
    small_minus_btn = Button(order_window,text = "remove 1",command = lambda :smallCupRemove(small_label))
    medium_minus_btn = Button(order_window,text ="remove 1",command = lambda: mediumCupRemove(medium_label))
    large_minus_btn = Button(order_window,text = "remove 1",command = lambda :largeCupRemove(large_label))

    small_btn.place(bordermode = OUTSIDE,relx = 0.3,rely = 0.4,anchor = CENTER)
    medium_btn.place(bordermode = OUTSIDE,relx =0.5,rely = 0.4,anchor = CENTER)
    large_btn.place(bordermode = OUTSIDE,relx = 0.7,rely = 0.4,anchor = CENTER)
    
    small_minus_btn.place(bordermode = OUTSIDE,relx = 0.3,rely = 0.7,anchor = CENTER)
    medium_minus_btn.place(bordermode = OUTSIDE,relx =0.5,rely = 0.7,anchor = CENTER)
    large_minus_btn.place(bordermode = OUTSIDE,relx = 0.7,rely = 0.8,anchor = CENTER)
    
    
    
    small_label = Label(order_window, text = 'Small count: '+str(smallCup.counter)+'\nPrice 5LE',font=('Ariel',15))
    medium_label = Label(order_window, text = 'Medium count: '+str(mediumCup.counter)+'\nPrice 10LE',font=('Ariel',15))
    large_label = Label(order_window, text = 'Large count: '+ str(largeCup.counter)+'\nPrice 15LE',font=('Ariel',15))
    
    
    small_label.place(bordermode = OUTSIDE,relx =0.3,rely = 0.1,anchor = CENTER)
    medium_label.place(bordermode = OUTSIDE,relx =0.5,rely = 0.1,anchor = CENTER)
    large_label.place(bordermode = OUTSIDE,relx =0.7,rely = 0.05,anchor = CENTER)
    
    checkout_btn = Button(order_window,text = 'Checkout',command = lambda :checkout(smallCup.counter,largeCup.counter,mediumCup.counter))
    checkout_btn.place(bordermode = OUTSIDE,relx =0.9,rely = 0.9,anchor = CENTER)

    order_window.mainloop()
    

    
def checkout(small_count,large_count,medium_count):
    checkout_window = Toplevel(main_window)
    total  = ( 5*small_count) +(10*medium_count)+(15*large_count)
    checkout_string = "Item                       Price\n"
    if smallCup.counter > 0:
        checkout_string+="Small Cup          "+str(smallCup.counter)+ "x 5LE\n"
    if mediumCup.counter > 0:
        checkout_string+="Medium Cup          "+str(mediumCup.counter)+ "x 10LE\n"
    if largeCup.counter > 0:
        checkout_string+="Large Cup          "+str(largeCup.counter)+ "x 15LE\n"
     
    checkout_string+= "Total                "+str(total)+"\n"    
    checkout_label = Label(checkout_window, text = checkout_string,font=('Ariel',25))
    checkout_label.place(bordermode = OUTSIDE,relx =0.5,rely = 0.5,anchor = CENTER)


def smallCup(small_label):
   smallCup.counter +=1
   small_label.config(text = 'Small count: '+str(smallCup.counter)+'\nPrice 5LE')
   print("smallCup.counter = ", smallCup.counter)
    
def largeCup(large_label):
    largeCup.counter +=1
    large_label.config(text = 'Large count: '+str(largeCup.counter)+'\nPrice 15LE')
    print("largeCup.counter", largeCup.counter)
    
    
def mediumCup(medium_label):
    mediumCup.counter +=1
    medium_label.config(text = 'Medium count: '+str(mediumCup.counter)+'\nPrice 10LE')
    print("mediumCup.counter", mediumCup.counter)
    


def smallCupRemove(small_label):
   smallCup.counter -=1
   small_label.config(text = 'Small count: '+str(smallCup.counter)+'\nPrice 5LE')
   print("smallCup.counter = ", smallCup.counter)
    
def largeCupRemove(large_label):
    largeCup.counter -=1
    large_label.config(text = 'Large count: '+str(largeCup.counter)+'\nPrice 15LE')
    print("largeCup.counter", largeCup.counter)
    
    
def mediumCupRemove(medium_label):
    mediumCup.counter -=1
    medium_label.config(text = 'Medium count: '+str(mediumCup.counter)+'\nPrice 10LE')
    print("mediumCup.counter", mediumCup.counter)



smallCup.counter  =  0
largeCup.counter  =  0
mediumCup.counter =  0


main_window = Tk()



menu_btn = Button(main_window,text = "Menu",command = Proceed_to_order)

width= main_window.winfo_screenwidth()
height= main_window.winfo_screenheight()

main_window.title("ASAB STORE")
main_window.geometry("%dx%d" % (width, height))
label = Label(main_window, text = 'Welcome to ITI Asab Store',font=('Ariel',40))


label.place(bordermode = INSIDE,height =100,width = 1500)
menu_btn.place(bordermode = INSIDE,relx =0.5,rely = 0.5,anchor = CENTER)



main_window.mainloop()


