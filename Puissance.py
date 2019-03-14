from tkinter import * 

fenetre = Tk()


scale=Scale(fenetre, orient='vertical', from_=10, to=0,
      resolution=1, tickinterval=2, length=350,
      label='Puissance')
scale.pack()

fenetre.mainloop()