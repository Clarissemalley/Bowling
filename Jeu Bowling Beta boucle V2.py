import tkinter as tk

Pos_X=720 #Position Initial de la boule sur l'axe X
Pos_Y=130 #Position Initial de la boule sur l'axe Y

fen = tk.Tk()
#Création du Canvas qui sert de Piste
canvas = tk.Canvas(fen,width = 800, height = 310, bd=0, bg="white")
canvas.grid(row=1,column=1,padx=10,pady=5)

Touractuel=-1

quille1= 0
quille2= 0
quille3= 0
quille4= 0
quille5= 0
quille6= 0
quille7= 0
quille8= 0
quille9= 0
quille10= 0

boule= canvas.create_oval(0,0,0,0, fill='black')

def Créationboule():
    global boule,dx,dy
    X1, Y1, X2, Y2 = canvas.coords(boule)
    # Création de la Boule
    boule = canvas.create_oval(Pos_X,Pos_Y,Pos_X+40,Pos_Y+40, fill='black')

def videpiste():
   canvas.delete(quille1)
   canvas.delete(quille2)
   canvas.delete(quille3)
   canvas.delete(quille4)
   canvas.delete(quille5)
   canvas.delete(quille6)
   canvas.delete(quille7)
   canvas.delete(quille8)
   canvas.delete(quille9)
   canvas.delete(quille10)

def miseenplace():
    #Création des quilles
    global quille1,quille2,quille3,quille4,quille5,quille6,quille7,quille8,quille9,quille10,Touractuel
    Touractuel=Touractuel+1
    videpiste()
    quille1= canvas.create_oval(20, 85,40,105,fill='black')
    quille2= canvas.create_oval(20, 125,40,145,fill='black')
    quille3= canvas.create_oval(20, 165,40,185,fill='black')
    quille4= canvas.create_oval(20, 205,40,225,fill='black')
    quille5= canvas.create_oval(60,105,80,125,fill='black')
    quille6= canvas.create_oval(60,145,80,165,fill='black')
    quille7= canvas.create_oval(60,185,80,205,fill='black')
    quille8= canvas.create_oval(100,125,120,145,fill='black')
    quille9= canvas.create_oval(100,165,120,185,fill='black')
    quille10= canvas.create_oval(140,145,160,165,fill='black')

def deplacement():
    """Gère les déplacements de la boule et ses collisions avec les objets et
    les bords de la piste"""
    global dx, dy, boule
    X1, Y1, X2, Y2 = canvas.coords(boule)
    canvas.move(boule,dx,dy)
    fen.after(20,deplacement)

    # Fais rebondir la boule sur les bords de la piste en fonction de son angle d'arrivée
    if Y1<=0:
        dy=-angle.get()
    if Y2>=310:
        dy=angle.get()

    score()

    if X1<0:
        canvas.delete(boule)
        dx=0
        dy=0
        boule = canvas.create_oval(Pos_X,Pos_Y,Pos_X+40,Pos_Y+40, fill='black')



def score():
    global quille1,quille2,quille3,quille4,quille5,quille6,quille7,quille8,quille9,quille10
    if len(canvas.find_overlapping(20, 85,40,105))>1:
        canvas.delete(quille1)
        list_tour[Touractuel].set(list_tour[Touractuel].get()+1)
    if len(canvas.find_overlapping(20, 125,40,145))>1:
        canvas.delete(quille2)
        list_tour[Touractuel].set(list_tour[Touractuel].get()+1)
    if len(canvas.find_overlapping(20, 165,40,185))>1:
        canvas.delete(quille3)
        list_tour[Touractuel].set(list_tour[Touractuel].get()+1)
    if len(canvas.find_overlapping(20, 205,40,225))>1:
        canvas.delete(quille4)
        list_tour[Touractuel].set(list_tour[Touractuel].get()+1)
    if len(canvas.find_overlapping(60,105,80,125))>1:
        canvas.delete(quille5)
        list_tour[Touractuel].set(list_tour[Touractuel].get()+1)
    if len(canvas.find_overlapping(60,145,80,165))>1:
        canvas.delete(quille6)
        list_tour[Touractuel].set(list_tour[Touractuel].get()+1)
    if len(canvas.find_overlapping(60,185,80,205))>1:
        canvas.delete(quille7)
        list_tour[Touractuel].set(list_tour[Touractuel].get()+1)
    if len(canvas.find_overlapping(100,125,120,145))>1:
        canvas.delete(quille8)
        list_tour[Touractuel].set(list_tour[Touractuel].get()+1)
    if len(canvas.find_overlapping(100,165,120,185))>1:
        canvas.delete(quille9)
        list_tour[Touractuel].set(list_tour[Touractuel].get()+1)
    if len(canvas.find_overlapping(140,145,160,165))>1:
        canvas.delete(quille10)
        list_tour[Touractuel].set(list_tour[Touractuel].get()+1)



def Lancer(event):
    """ Permet de lancer la Boule en appuyant sur la flèche du haut"""
    global dx, dy
    X1, Y1, X2, Y2 = canvas.coords(boule)
    dy = -angle.get()
    dx = -vitesse.get()
def Bas():
    """Permet de deplacer la boule vers le Bas"""
    X1, Y1, X2, Y2 = canvas.coords(boule)
    canvas.coords(boule,X1,Y1+20,X2,Y2+20)

def Haut():
    """Permet de deplacer la boule vers le Haut"""
    X1, Y1, X2, Y2 = canvas.coords(boule)
    canvas.coords(boule,X1,Y1-20,X2,Y2-20)

# Création des variables scores
list_tour=[tk.IntVar(0),
 tk.IntVar(0),
 tk.IntVar(0),
 tk.IntVar(0),
 tk.IntVar(0),
 tk.IntVar(0),
 tk.IntVar(0),
 tk.IntVar(0),
 tk.IntVar(0),
 tk.IntVar(0)]

list_tour[0].set(0)
list_tour[1].set(0)
list_tour[2].set(0)
list_tour[3].set(0)
list_tour[4].set(0)
list_tour[5].set(0)
list_tour[6].set(0)
list_tour[7].set(0)
list_tour[8].set(0)
list_tour[9].set(0)

#Score total
total = list_tour[0].get()+list_tour[1].get()+list_tour[2].get()+list_tour[3].get()+list_tour[4].get()+list_tour[5].get()+list_tour[6].get()+list_tour[7].get()+list_tour[8].get()+list_tour[9].get()

#Création du tableau
tk.Label(fen, text='Tour', borderwidth=1).grid(row=3, column=8)
tk.Label(fen, text='J1', borderwidth=1).grid(row=4, column=8)

tk.Label(fen, text=total, borderwidth=3).grid(row=4, column=20)
tk.Label(fen, text='Total', borderwidth=3).grid(row=3, column=20)

for colonne in range(10, 20):
    tk.Label(fen, text=str(colonne-9), borderwidth=3).grid(row=3, column=colonne)
    tk.Label(fen, textvar=list_tour[0], borderwidth=3).grid(row=4, column=10)
    tk.Label(fen, textvar=list_tour[1], borderwidth=3).grid(row=4, column=11)
    tk.Label(fen, textvar=list_tour[2], borderwidth=3).grid(row=4, column=12)
    tk.Label(fen, textvar=list_tour[3], borderwidth=3).grid(row=4, column=13)
    tk.Label(fen, textvar=list_tour[4], borderwidth=3).grid(row=4, column=14)
    tk.Label(fen, textvar=list_tour[5], borderwidth=3).grid(row=4, column=15)
    tk.Label(fen, textvar=list_tour[6], borderwidth=3).grid(row=4, column=16)
    tk.Label(fen, textvar=list_tour[7], borderwidth=3).grid(row=4, column=17)
    tk.Label(fen, textvar=list_tour[8], borderwidth=3).grid(row=4, column=18)
    tk.Label(fen, textvar=list_tour[9], borderwidth=3).grid(row=4, column=19)




angle = tk.DoubleVar(value=0)# Variable qui représente l'angle de la boule
vitesse= tk.DoubleVar(value=0)# Variable qui représente la vitesse de la boule
#Création des Boutons Scales permettant de gérer la direction et la vitesse de la boule
scaledir=tk.Scale(fen, orient='vertical', from_=10, to=-10,
      resolution=1, length=250,
      variable = angle,
      label='Direction',)
scaledir.grid(row=1,column=6,padx=15)

scalePui=tk.Scale(fen, orient='horizontal', from_=10, to=1,
      resolution=1, length=250,
      variable = vitesse,
      label='Puissance')
scalePui.grid(row=2,column=1,pady=5)


dx=0
dy=0

# Création du Bouton permettant de fermer le programme
Bouton_Quitter=tk.Button(fen, text ='Quitter', command = fen.destroy)
Bouton_Quitter.grid(row=5,column=1,sticky='')
#Permet de récuperer le fait que le joueur appuie sur le bouton "fleche du haut"
canvas.bind_all('<Up>', Lancer)
# Création des Boutons qui permettent de lancer les fonctions "Haut" et "Bas"
tk.Button(fen,text='Bas',command=Bas).grid(row=1,column=2,sticky='sw',
         padx=5,pady=5)
tk.Button(fen,text='Haut',command=Haut).grid(row=1,column=2,sticky='nw',
         padx=5,pady=5)
tk.Button(fen,text='Quille',command=miseenplace).grid(row=3,column=1,sticky='ne',
         padx=5,pady=5)
tk.Button(fen,text='Boule',command=Créationboule).grid(row=3,column=1,sticky='nw',
         padx=5,pady=5)

deplacement()

fen.mainloop()
