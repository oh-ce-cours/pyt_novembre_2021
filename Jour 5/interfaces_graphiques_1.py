from tkinter import *
import time

NB_CLICKED = 0


def on_click():
    global NB_CLICKED
    NB_CLICKED += 1
    print(f"cliced {NB_CLICKED} fois")


fenetre = Tk()
bouton = Button(fenetre, text="clicme", command=on_click)
bouton.pack()
fenetre.mainloop()
