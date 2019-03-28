from tkinter import *

fenetre = Tk()

Label(fenetre, text='Tour', borderwidth=1).grid(row=1, column=1)
Label(fenetre, text='J1', borderwidth=1).grid(row=2, column=1)

tr1 = IntVar(0) #variable spéciale
tr2 = IntVar(0)
tr3 = IntVar(0)
tr4 = IntVar(0)
tr5 = IntVar(0)
tr6 = IntVar(0)
tr7 = IntVar(0)
tr8 = IntVar(0)
tr9 = IntVar(0)
tr10 = IntVar(0)

tr1.set(2)
tr2.set(8) #s=8
tr3.set(6)
tr4.set(3)
tr5.set(9)
tr6.set(2)
tr7.set(0)
tr8.set(10)
tr9.set(5)
tr10.set(1)

total = tr1.get()+tr2.get()+tr3.get()+tr4.get()+tr5.get()+tr6.get()+tr7.get()+tr8.get()+tr9.get()+tr10.get()

for colonne in range(2, 12):
    Label(fenetre, text=str(colonne-1), borderwidth=1).grid(row=1, column=colonne)
    Label(fenetre, textvar=tr1, borderwidth=1).grid(row=2, column=2)
    Label(fenetre, textvar=tr2, borderwidth=1).grid(row=2, column=3)
    Label(fenetre, textvar=tr3, borderwidth=1).grid(row=2, column=4)
    Label(fenetre, textvar=tr4, borderwidth=1).grid(row=2, column=5)
    Label(fenetre, textvar=tr5, borderwidth=1).grid(row=2, column=6)
    Label(fenetre, textvar=tr6, borderwidth=1).grid(row=2, column=7)
    Label(fenetre, textvar=tr7, borderwidth=1).grid(row=2, column=8)
    Label(fenetre, textvar=tr8, borderwidth=1).grid(row=2, column=9)
    Label(fenetre, textvar=tr9, borderwidth=1).grid(row=2, column=10)
    Label(fenetre, textvar=tr10, borderwidth=1).grid(row=2, column=11)

Label(fenetre, text=total, borderwidth=1).grid(row=2, column=12)
Label(fenetre, text='Total', borderwidth=1).grid(row=1, column=12)

fenetre.mainloop()
