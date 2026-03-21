import time
from tkinter import StringVar

print(time.strftime("%d/%m/%Y", time.localtime()))
print("**")
print(time.strftime("%d/%m/%Y", time.localtime()))

print(" - "*12)

import uuid

# UUID aléatoire (version 4)
identifiant = uuid.uuid4()
print(identifiant)

# UUID basé sur l'adresse MAC et l'heure (version 1)
identifiant2 = uuid.uuid1()
print(identifiant2)

class Essaie:
    def __init__(self):
        self.nom = ""
    def generer_numero_compte(self):
        prefix = "BEN"
        annee = "2025"
        code_unique = str(self.id_interne).replace("-", "")[:8].upper()
        return f"{prefix}-{annee}-{code_unique}"
    #print(generer_numero_compte())
    #with open("fichertexte.txt", "a", encoding="utf-8") as f:
        #f.write("Hello Fénelon\n")
a=Essaie()

#print(Essaie.generer_numero_compte(a))
    #print("Fichier créé dans ce dossier :", __file__)


    #en route pour l'observeur

def observeur(*args):
    var_label.set(var_entry.get())

import tkinter as tk
app=tk.Tk()


var_entry=tk.StringVar()
entry=tk.Entry(app,textvariable=var_entry)
var_entry.trace("w",observeur)


var_label=tk.StringVar()
lbl=tk.Label(app,text="Nom de la personne",textvariable=var_label)
var_label.set("hello ")


lbl.pack()
entry.pack()
app.geometry("300x300")
app.mainloop()