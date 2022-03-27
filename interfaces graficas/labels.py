from logging import root
from pickle import FRAME
from tkinter import*

raiz = Tk()

miframe = Frame(raiz, width=500, height=500)
miframe.pack()
label = Label(miframe, text="Hola mundo", fg="red",
              font=("Comic Sans MS", 20), borderwidth=5)
label.place(x=10, y=10, width=300)

raiz.mainloop()
