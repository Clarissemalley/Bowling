import tkinter as tk

def partie():
    print("La fonction partie se lance")

fenetre = tk.Tk()
photo = tk.PhotoImage(file="B.png")

canvas = tk.Canvas(fenetre,width=960, height=539)
canvas.create_image(480, 270, image=photo)
canvas.pack()

Bouton_Partie = tk.Button(fenetre, text ='Partie', command = partie)
Bouton_Partie.pack()

Bouton_Options = tk.Button(fenetre, text = 'Options', command = fenetre)
Bouton_Options.pack()

Bouton_Quitter = tk.Button(fenetre, text = 'Quitter', command = fenetre.destroy)
Bouton_Quitter.pack()

fenetre.mainloop()
