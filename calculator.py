from tkinter import*
root=Tk()
root.title("simple calculetor")
e=Entry(root,width=45,borderwidth=0)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
def Button_click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))

def button_clear():
    e.delete(0,END)

def Button_add():
    first_number=e.get()
    global f_num
    global math
    math="addition"
    f_num=int(first_number)
    e.delete(0,END)

def button_sub():
    first_number=e.get()
    global f_num
    global math
    math="subtraction"
    f_num=int(first_number)
    e.delete(0,END)

def button_div():
    first_number=e.get()
    global f_num
    global math
    math="division"
    f_num=int(first_number)
    e.delete(0,END)

def button_multi():
    first_number=e.get()
    global f_num
    global math
    math="multiplication"
    f_num=int(first_number)
    e.delete(0,END)

def Button_equal():
    second_number=e.get()
    e.delete(0,END)
    if math=="addition":
        e.insert(0,int(second_number)+f_num)
    elif math=="subtraction":
        e.insert(0,f_num-int(second_number))
    elif math=="division":
         e.insert(0,f_num/int(second_number))
    elif math=="multiplication":
        e.insert(0,int(second_number)*f_num)

mybutton_1=Button(root,text="1", padx=40,pady=20,command=lambda:Button_click(1),bg="light blue")
mybutton_2=Button(root,text="2", padx=40,pady=20,command=lambda:Button_click(2),bg="light blue")
mybutton_3=Button(root,text="3", padx=40,pady=20,command=lambda:Button_click(3),bg="light blue")
mybutton_4=Button(root,text="4", padx=40,pady=20,command=lambda:Button_click(4),bg="light blue")
mybutton_5=Button(root,text="5", padx=40,pady=20,command=lambda:Button_click(5),bg="light blue")
mybutton_6=Button(root,text="6", padx=40,pady=20,command=lambda:Button_click(6),bg="light blue")
mybutton_7=Button(root,text="7", padx=40,pady=20,command=lambda:Button_click(7),bg="light blue")
mybutton_8=Button(root,text="8", padx=40,pady=20,command=lambda:Button_click(8),bg="light blue")
mybutton_9=Button(root,text="9", padx=40,pady=20,command=lambda:Button_click(9),bg="light blue")
mybutton_0=Button(root,text="0", padx=40,pady=20,command=lambda:Button_click(0),bg="light blue")
mybutton_add=Button(root,text="+", padx=39,pady=20,command=Button_add,bg="light blue")
mybutton_clear=Button(root,text="Clear", padx=79,pady=20,command=button_clear,bg="light blue")
mybutton_equal=Button(root,text="=", padx=89,pady=20,command=Button_equal,bg="light blue")

mybutton_sub=Button(root,text="-", padx=40,pady=20,command=button_sub,bg="light blue")
mybutton_div=Button(root,text="/", padx=41,pady=20,command=button_div,bg="light blue")
mybutton_multi=Button(root,text="*", padx=41,pady=20,command=button_multi,bg="light blue")


mybutton_1.grid(row=3,column=0)
mybutton_2.grid(row=3,column=1)
mybutton_3.grid(row=3,column=2)

mybutton_4.grid(row=2,column=0)
mybutton_5.grid(row=2,column=1)
mybutton_6.grid(row=2,column=2)

mybutton_7.grid(row=1,column=0)
mybutton_8.grid(row=1,column=1)
mybutton_9.grid(row=1,column=2)

mybutton_0.grid(row=4,column=0)
mybutton_add.grid(row=5,column=0)
mybutton_clear.grid(row=5,column=1,columnspan=2)
mybutton_equal.grid(row=6,column=1,columnspan=2)

mybutton_sub.grid(row=6,column=0)
mybutton_div.grid(row=4,column=1)
mybutton_multi.grid(row=4,column=2)

button_quit=Button(root,text="Exit",command=root.quit,fg="red",bg='violet',padx=50,pady=20)
button_quit.grid(row=7,column=0,padx=10,pady=10,columnspan=3)

root.mainloop()