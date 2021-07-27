from tkinter import *

root = Tk()

def añadir():
    lista.insert(END, ingrediente.get())
def eliminar():
    lista.delete(lista.curselection())

root.geometry("200x350")
root.title("Lista")
root.resizable(0,0)


titulo = Label(root, text="Lista de la compra",font=("Arial",15))
titulo.pack()


lista = Listbox(root)
lista.config(bg="grey",
                font=("Arial",15),
                justify=CENTER)
lista.insert(0,"ejemplo")
lista.pack()

ingrediente = Entry(root, text="escriba ingredientes")
ingrediente.pack()


añadir = Button(root,text="Añadir",command=añadir)
añadir.pack()

eliminar = Button(root,text="Eliminar",command=eliminar)
eliminar.pack()


root.mainloop()