from tkinter import *
 
def deplacement():
    global dx, dy
    x1, y1, x2, y2 = canvas.coords(balle1)
    if y1<- canvas.coords(quille)[3]:
        dy=-1*dy
    #On deplace la balle :
    canvas.move(balle1,dx,dy)
    #On repete cette fonction
    tk.after(20,deplacement)
    if y1== canvas.coords(quille)[3]:
        canvas.coords(balle1,x1,y1,x2,y2)
#Une fonction pour modifier le deplacement vers la droite :
def haut(event):
    global dx, dy
    dx=0
    dy=-5
 
#Coordonnées de la balle au départ:
Pos_Xba=200
Pos_Yba=330
#Déplacement de la balle au départ:
dx=0
dy=0

Pos_Xqu=200
Pos_Yqu=20
#On cree une fenêtre et un canevas:
tk = Tk()
canvas = Canvas(tk,width = 500, height = 400 , bd=0, bg="white")
canvas.pack(padx=10,pady=10)
 
#Création  d'un bouton "Quitter":
Bouton_Quitter=Button(tk, text ='Quitter', command = tk.destroy)
#On ajoute l'affichage du bouton dans la fenêtre tk:
Bouton_Quitter.pack()
 
#On cree une balle:
balle1 = canvas.create_oval(Pos_Xba,Pos_Yba,Pos_Xba+50,Pos_Yba+50,fill='red')
quille= canvas.create_oval(Pos_Xqu,Pos_Yqu,Pos_Xqu+20,Pos_Yqu+20,fill='black')
 
canvas.bind_all('<Up>', haut)
 
deplacement()
 
#On lance la boucle principale:
tk.mainloop()