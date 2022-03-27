from tkinter import Tk, Label, Entry, Button

from matplotlib.pyplot import margins
from numpy import row_stack


def suma():
    n1 = txt_primer_num.get()
    n2 = txt_segundo_num.get()
    r = float(n1)+float(n2)
    txt_resultado_num.delete(0, "end")
    txt_resultado_num.insert(0, r)


def CE():
    txt_primer_num.delete(0, "end")
    txt_segundo_num.delete(0, "end")
    txt_resultado_num.delete(0, "end")


raiz = Tk()
raiz.title("Suma de dos numeros")
# raiz.geometry("400x200")
raiz.resizable(0, 0)

raiz.config(background="white")


eti_primer_num = Label(raiz, text="cota ref")
eti_primer_num.grid(row=0, column=0, sticky="W")
eti_primer_num.config(width=10)

eti_segundo_num = Label(raiz, text="altura")
eti_segundo_num.grid(row=1, column=0, sticky="W")
eti_segundo_num.config(width=10)

eti_resultado_num = Label(raiz, text="resultado")
eti_resultado_num.grid(row=2, column=0, sticky="W")
eti_resultado_num.config(width=10)

# ----------------ventanas------------------------

txt_primer_num = Entry(raiz, background="white")
txt_primer_num.grid(row=0, column=1, padx=10, pady=10)
txt_primer_num.config(width=35)

txt_segundo_num = Entry(raiz, background="white")
txt_segundo_num.grid(row=1, column=1, padx=10, pady=10)
txt_segundo_num.config(width=35)

txt_resultado_num = Entry(raiz, background="white")
txt_resultado_num.grid(row=2, column=1, padx=10, pady=10)
txt_resultado_num.config(width=35)

# ----------boton-----------------

bton = Button(raiz, text="SUM", command=suma)
bton.grid(row=0, column=2, padx=10, pady=10, rowspan=2, sticky="N")
bton.config(width=4, height=4)
bton2 = Button(raiz, text="CE", command=CE)
bton2.grid(row=2, column=2, padx=10, pady=10)
bton2.config(width=4, height=2)

raiz.mainloop()
