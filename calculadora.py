from os import pardir
from tkinter import *

root = Tk()
root.resizable(0,0)
root.title("Calculate")

##FUNCIONES
i = 0
def click(valor):
    global i
    texto.insert(i, valor)
    i+=1

def borrar():
    texto.delete(0, END)

def raiz():
    num = float(texto.get())
    res = pow(num,0.5)
    texto.delete(0, END)
    texto.insert(0, res)
    i=0

def operaciones():
    operacion = texto.get()
    resultado = eval(operacion)
    texto.delete(0, END)
    texto.insert(0, resultado)
    i=0
#ESTRUCTURA
texto = Entry(root)
texto.pack()
numero = Frame(root)
numero.pack()
bt1 = Button(numero,text=1,command=lambda:click(1),width=5,height=2).grid(row=1,column=0)
bt2 = Button(numero,text=2,command=lambda:click(2),width=5,height=2).grid(row=1,column=1)
bt3 = Button(numero,text=3,command=lambda:click(3),width=5,height=2).grid(row=1,column=2)
bt4 = Button(numero,text=4,command=lambda:click(4),width=5,height=2).grid(row=2,column=0)
bt5 = Button(numero,text=5,command=lambda:click(5),width=5,height=2).grid(row=2,column=1)
bt6 = Button(numero,text=6,command=lambda:click(6),width=5,height=2).grid(row=2,column=2)
bt7 = Button(numero,text=7,command=lambda:click(7),width=5,height=2).grid(row=3,column=0)
bt8 = Button(numero,text=8,command=lambda:click(8),width=5,height=2).grid(row=3,column=1)
bt9 = Button(numero,text=9,command=lambda:click(9),width=5,height=2).grid(row=3,column=2)
bt0 = Button(numero,text=0,command=lambda:click(0),width=5,height=2).grid(row=4,column=1)

Del = Button(numero,text="DEL",command=borrar,width=5,height=2).grid(row=4,column=2,padx=4,pady=4)
enter = Button(numero,text="Enter",command=operaciones,width=10,height=2).grid(row=5,column=1)


pariz = Button(numero,text="(",command=lambda:click("("),width=5,height=2).grid(row=5,column=0)
parde = Button(numero,text=")",command=lambda:click(")"),width=5,height=2).grid(row=5,column=2)
div = Button(numero,text="/",command=lambda:click("/"),width=5,height=2).grid(row=1,column=3)
suma = Button(numero,text="+",command=lambda:click("+"),width=5,height=2).grid(row=2,column=3)
resta = Button(numero,text="-",command=lambda:click("-"),width=5,height=2).grid(row=3,column=3)
mult =Button(numero,text="*",command=lambda:click("*"),width=5,height=2).grid(row=4,column=3)
raiz = Button(numero,text="√",command=raiz,width=5,height=2).grid(row=5,column=3)

root.mainloop()