from tkinter import *
from tkinter.messagebox import showerror
window=Tk()
window.title('Tkinter MessageBox')
window.resizable(False,False)
window.geometry('350x300')
l=Label(window,text="CALCULATOR")
l.grid(row=0,columnspan=7)
l1=Label(window,text="Enter Number 1")
l1.grid(row=1,columnspan=4,padx=10,pady=10,ipadx=5,ipady=5)
e1=Entry(window)
e1.grid(row=1,column=3,columnspan=4)
l2=Label(window,text="Enter Number2")
l2.grid(row=2,columnspan=4,padx=10,pady=10,ipadx=5,ipady=5)
e2=Entry(window)
e2.grid(row=2,column=3,columnspan=4)

def addition():
    try:
        x=int(e1.get())
        y=int(e2.get())
        result["text"]=x+y
    except ValueError as e:
        showerror(title='Error',message="ERROR")
b1=Button(window,text="+",command=addition)
b1.grid(row=3,column=0,padx=10,pady=10,ipadx=5,ipady=5)

def subtraction():
    try:
        x=int(e1.get())
        y=int(e2.get())
        result["text"]=x-y
    except ValueError as e:
        showerror(title='Error',message="ERROR")
b2=Button(window,text="-",command=subtraction)
b2.grid(row=3,column=1,padx=10,pady=10,ipadx=5,ipady=5)

def multiplication():
    try:
        x=int(e1.get())
        y=int(e2.get())
        result["text"]=x*y
    except ValueError as e:
        showerror(title='Error',message="ERROR")
b3=Button(window,text="*",command=multiplication)
b3.grid(row=3,column=2,padx=10,pady=10,ipadx=5,ipady=5)

def division():
    try:
        x=int(e1.get())
        y=int(e2.get())
        result["text"]=x/y
    except ValueError as e:
        showerror(title='Error',message="ERROR")
    except ZeroDivisionError as a:
        showerror(title='Error',message='Error: Zero Division Error')
b4=Button(window,text="/",command=division)
b4.grid(row=3,column=3,padx=10,pady=10,ipadx=5,ipady=5)

def doubledivision():
    try:
        x=int(e1.get())
        y=int(e2.get())
        result["text"]=x//y
    except ValueError as e:
        showerror(title='Error',message="ERROR")
    except ZeroDivisionError as a:
        showerror(title='Error',message='Error: Zero Division Error')
b5=Button(window,text="//",command=doubledivision)
b5.grid(row=3,column=4,padx=10,pady=10,ipadx=5,ipady=5)

def power():
    try:
        x=int(e1.get())
        y=int(e2.get())
        result["text"]=x**y
    except ValueError as e:
        showerror(title='Error',message="ERROR")
b6=Button(window,text="**",command=power)
b6.grid(row=3,column=5,padx=10,pady=10,ipadx=5,ipady=5)

def remainder():
    try:
        x=int(e1.get())
        y=int(e2.get())
        result["text"]=x%y
    except ValueError as e:
        showerror(title='Error',message="ERROR")
    except ZeroDivisionError as a:
        showerror(title='Error',message='Error: Zero Division Error')
b7=Button(window,text="%",command=remainder)
b7.grid(row=3,column=6,padx=10,pady=10,ipadx=5,ipady=5)

def cancel():
    e1.delete(0,END)
    e2.delete(0,END)

result=Label(window,text="Result")
result.grid(row=5,columnspan=7,padx=10,pady=10,ipadx=5,ipady=5)
b2=Button(window,text="C",command=cancel)
b2.grid(row=4,columnspan=7,)
window.mainloop()