from tkinter import*
from tkinter import messagebox
def f1():
    messagebox.showinfo("Demo","You have clicked red")
def f2():
    messagebox.showinfo("Demo","You have clicked green")
def f3():
    messagebox.showinfo("Demo","You have clicked orange")
def f4():
    messagebox.showinfo("Demo","You have clicked yellow")
t=Tk()
b1=Button(t,text="Red",command=f1,activeforeground="Pink",activebackground="Red",pady=10)
b1.pack(side=TOP)
b2=Button(t,text="Green",command=f2,activeforeground="Pink",activebackground="Green",pady=10)
b2.pack(side=BOTTOM)
b3=Button(t,text="Orange",command=f3,activeforeground="Pink",activebackground="Orange",pady=10)
b3.pack(side=RIGHT)
b4=Button(t,text="Yellow",command=f4,activeforeground="Pink",activebackground="Yellow",pady=10)
b4.pack(side=LEFT)
