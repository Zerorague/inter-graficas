from ctypes import alignment
from tkinter import *
from tkinter import ttk

from matplotlib.pyplot import margins
from numpy import place
# he creado mi primera ventana en python
raiz = Tk()
raiz.title("Estudiante Python")
# el primero corresponde al ancho y el segundo a alto 0,0 false (no se puede redimencionar)
raiz.resizable(1, 1)
raiz.iconbitmap("asd.ico")
# raiz.geometry("650x350")
raiz.config(background="#22D4B6")

miframe = Frame(raiz, width=650, height=350)
miframe.pack(fill=BOTH, expand=True)
miframe.config(background="white", relief=SUNKEN, cursor="pirate")


# si no quiero ocupar la variable puedo dejar asi => ///Label(miframe, text="hola mundo).place(x=100,y=200")///
milabe = Label(miframe, text="Hola mundo",
               fg="red", font=("Comic Sans MS", 18))
milabe.place(x=100, y=200)  # para ubicar algo dentro un lugar con coordenadas

imagen = PhotoImage(file="cartel.png", width=100, height=100)

Label(miframe, image=imagen).place(x=0, y=0)

raiz.mainloop()  # debe estar en un loop permanente
