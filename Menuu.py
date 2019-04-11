import tkinter as tk

fenetre = tk.Tk()
photo = tk.PhotoImage(file="B.png")

canvas = tk.Canvas(fenetre,width=960, height=539)
canvas.create_image(480, 270, image=photo)
canvas.pack()

fenetre.mainloop()