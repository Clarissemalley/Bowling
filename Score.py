import tkinter as tk

fenetre = tk.Tk()

#Scores manches 1 à 10
tr1 = tk.IntVar(0)
tr2 = tk.IntVar(0)
tr3 = tk.IntVar(0)
tr4 = tk.IntVar(0)
tr5 = tk.IntVar(0)
tr6 = tk.IntVar(0)
tr7 = tk.IntVar(0)
tr8 = tk.IntVar(0)
tr9 = tk.IntVar(0)
tr10 = tk.IntVar(0)

tr1.set(2)
tr2.set(8)
tr3.set(6)
tr4.set(3)
tr5.set(9)
tr6.set(2)
tr7.set(0)
tr8.set(10)
tr9.set(5)
tr10.set(1)

#Score total
total = tr1.get()+tr2.get()+tr3.get()+tr4.get()+tr5.get()+tr6.get()+tr7.get()+tr8.get()+tr9.get()+tr10.get()

#Création du tableau
tk.Label(fenetre, text='Tour', borderwidth=1).grid(row=1, column=1)
tk.Label(fenetre, text='J1', borderwidth=1).grid(row=2, column=1)

tk.Label(fenetre, text=total, borderwidth=3).grid(row=2, column=12)
tk.Label(fenetre, text='Total', borderwidth=3).grid(row=1, column=12)

for colonne in range(2, 12):
    tk.Label(fenetre, text=str(colonne-1), borderwidth=3).grid(row=1, column=colonne)
    tk.Label(fenetre, textvar=tr1, borderwidth=3).grid(row=2, column=2)
    tk.Label(fenetre, textvar=tr2, borderwidth=3).grid(row=2, column=3)
    tk.Label(fenetre, textvar=tr3, borderwidth=3).grid(row=2, column=4)
    tk.Label(fenetre, textvar=tr4, borderwidth=3).grid(row=2, column=5)
    tk.Label(fenetre, textvar=tr5, borderwidth=3).grid(row=2, column=6)
    tk.Label(fenetre, textvar=tr6, borderwidth=3).grid(row=2, column=7)
    tk.Label(fenetre, textvar=tr7, borderwidth=3).grid(row=2, column=8)
    tk.Label(fenetre, textvar=tr8, borderwidth=3).grid(row=2, column=9)
    tk.Label(fenetre, textvar=tr9, borderwidth=3).grid(row=2, column=10)
    tk.Label(fenetre, textvar=tr10, borderwidth=3).grid(row=2, column=11)

fenetre.mainloop()
