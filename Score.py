from tkinter import *

fenetre = Tk()

#multirow et multicolumn pour plus grande colonne et ligne
#val = s.get() -> obtient la valeur de s

Label(fenetre, text='Tour', borderwidth=1).grid(row=1, column=1)
Label(fenetre, text='J1', borderwidth=1).grid(row=2, column=1)
s = IntVar(0)
s.set(8) #s=8
for colonne in range(2, 13):
    Label(fenetre, text=str(colonne-1), borderwidth=1).grid(row=1, column=colonne)
    Label(fenetre, textvar=s, borderwidth=1).grid(row=2, column=colonne)
Label(fenetre, text='Total', borderwidth=1).grid(row=1, column=12)
fenetre.mainloop()
