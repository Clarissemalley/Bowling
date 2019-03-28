import tkinter as tk

Pos_Xba=200
Pos_Yba=330

Pos_Xqu=200
Pos_Yqu=20

def deplacement():
    global dx, dy
    x1, y1, x2, y2 = canvas.coords(balle1)
    if y1<canvas.coords(quille)[3]:
        dy=-1*dy
    canvas.move(balle1,dx,dy)
    fen.after(20,deplacement)
    if y1 == canvas.coords(quille)[3]:
        canvas.coords(balle1,x1,y1,x2,y2)

def haut(event):
    global dx, dy
    dx=0
    dy=-5

def Droite():
    x1, y1, x2, y2 = canvas.coords(balle1)
    canvas.coords(balle1,x1+20,y1,x2+20,y2)

def Gauche():
    x1, y1, x2, y2 = canvas.coords(balle1)
    canvas.coords(balle1,x1-20,y1,x2-20,y2)

fen = tk.Tk()
canvas = tk.Canvas(fen,width = 500, height = 400 , bd=0, bg="white")
canvas.pack(padx=10,pady=10)

balle1 = canvas.create_oval(Pos_Xba,Pos_Yba,Pos_Xba+50,Pos_Yba+50,fill='red')
quille= canvas.create_oval(Pos_Xqu,Pos_Yqu,Pos_Xqu+20,Pos_Yqu+20,fill='black')
 
dx=0
dy=0


Bouton_Quitter=tk.Button(fen, text ='Quitter', command = fen.destroy)
Bouton_Quitter.pack()

canvas.bind_all('<Up>', haut)
 
tk.Button(fen,text='Droite',command=Droite).pack()
tk.Button(fen,text='Gauche',command=Gauche).pack()

 
deplacement()

fen.mainloop()