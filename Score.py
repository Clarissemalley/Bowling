from tkinter import *

fenetre = Tk()

l = LabelFrame(fenetre, text="Tour", padx=20, pady=20)
l.pack(fill="both", expand="yes")
 
Label(l).pack()

# frame 2
Frame2 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame2.pack(side=LEFT, padx=10, pady=10)

# frame 3 dans frame 2
Frame3 = Frame(Frame2, bg="white", borderwidth=2, relief=GROOVE)
Frame3.pack(side=RIGHT, padx=5, pady=5)

#puis mettre frame dans une l pour faire 1/2/3/4/etc...