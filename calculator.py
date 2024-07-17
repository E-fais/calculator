import tkinter as tk
from tkinter import *

root=tk.Tk()
root.title('calculator')
root.iconbitmap('calc.ico')


entry=tk.Entry(root,width='35',borderwidth=5)
entry.grid(row=0,column=0,columnspan=3,padx=10,pady=10)



def btnclick(num):
    current_num=entry.get()
    entry.delete(0,END) #delete existing num from the memory
    entry.insert(0,str(current_num)+str(num))  #concatenate current variable with new entry

def addition_btn():
     global operator_var #variable declared for assigning operators   +,-,*./
     global first_num
     num1=entry.get()
     first_num=int(num1)
     entry.delete(0,END)
     operator_var='+'

def subtract_btn():
     global operator_var 
     global first_num
     num1=entry.get()
     first_num=int(num1)
     entry.delete(0,END)
     operator_var='-'

def multiply_btn():
     global operator_var
     global first_num
     num1=entry.get()
     first_num=int(num1)
     entry.delete(0,END)
     operator_var='*'

def divide_btn():
     global operator_var
     global first_num
     num1=entry.get()
     first_num=int(num1)
     entry.delete(0,END)
     operator_var='/'


def btn_clear():
    entry.delete(0,END)
    


def equal_btn():
    global result
    second_num=entry.get()
    entry.delete(0,END)
    if operator_var=="+":
         result=int(first_num)+int(second_num)
         entry.insert(0,result)
         print(result)
         
    

button1=tk.Button(text=1,padx=40,pady=10,command=lambda:btnclick(1))  #lambda is like using {} inside react hooks to run javascript,here without lambda cannot pass arguments
button1.grid(row=1,column=0)

button2=tk.Button(text=2,padx=40,pady=10,command=lambda:btnclick(2))
button2.grid(row=1,column=1)

button3=tk.Button(text=3,padx=40,pady=10,command=lambda:btnclick(3))
button3.grid(row=1,column=2)

button4=tk.Button(text=4,padx=40,pady=10,command=lambda:btnclick(4))
button4.grid(row=2,column=0)

button5=tk.Button(text=5,padx=40,pady=10,command=lambda:btnclick(5))
button5.grid(row=2,column=1)

button6=tk.Button(text=6,padx=40,pady=10,command=lambda:btnclick(6))
button6.grid(row=2,column=2 )

button7=tk.Button(text=7,padx=40,pady=10,command=lambda:btnclick(7))
button7.grid(row=3,column=0)

button8=tk.Button(text=8,padx=40,pady=10,command=lambda:btnclick(8))
button8.grid(row=3,column=1)

button9=tk.Button(text=9,padx=40,pady=10,command=lambda:btnclick(9))
button9.grid(row=3,column=2 )

button0=tk.Button(text=0,padx=40,pady=10,command=lambda:btnclick(0))
button0.grid(row=4,column=0 )

button_pls=tk.Button(text='+',padx=40,pady=10,command=addition_btn)
button_pls.grid(row=4,column=1 )

button_equal=tk.Button(text='=',padx=40,pady=10,command=equal_btn)
button_equal.grid(row=4,column=2 )

button_clr=tk.Button(text='clear',padx=79,pady=10,command=btn_clear)
button_clr.grid(row=5,column=0,columnspan=2)

button_subtaract=tk.Button(text='-',padx=42,pady=10,command=subtract_btn)
button_subtaract.grid(row=5,column=2)

button_multiply=tk.Button(text='*',padx=40,pady=10,command=multiply_btn)
button_multiply.grid(row=6,column=0)

button_divide=tk.Button(text='*',padx=90,pady=10,command=divide_btn)
button_divide.grid(row=6,column=1,columnspan=2)


root.mainloop()