
import tkinter as tk
from banqueCodeProject import *
import MethodForInterface as metItface


#              ***              CREATION DE L'INTERFACE GRAPHIQUE AVEC TKINTER           ***



app = tk.Tk()
app.title("le projet banquaire ")

app.geometry(metItface.centreur(app,680,460))
mainmenu = tk.Menu(app)                            #menu principal

firstmenu = tk.Menu(mainmenu, tearoff=False)
firstmenu.add_command(label="Dépôt",command=metItface.Depot)          #ajout d'éléments à la barre des menus

firstmenu.add_command(label="Retrait",command=metItface.Retrait)          #ajout d'éléments à la barre des menus
firstmenu.add_command(label="Emprunt",command=metItface.Emprunt)          #ajout d'éléments à la barre des menus
firstmenu.add_command(label="Consultation solde",command=metItface.consultation_solde)          #ajout d'éléments à la barre des menus
firstmenu.add_command(label="Transfert",command=metItface.Transfert)          #ajout d'éléments à la barre des menus
firstmenu.add_command(label="Rembourser",command=metItface.Rembourser)          #ajout d'éléments à la barre des menus






secondmenu = tk.Menu(mainmenu, tearoff=False)
secondmenu.add_command(label = "Informations")
secondmenu.add_command(label = "Relevé bancaire")
secondmenu.add_command(label = "Autres")
secondmenu.add_command(label = "informations ")


menu3 = tk.Menu(mainmenu, tearoff=False)
menu3.add_command(label = "Acceuil")
#les titres des menus déroulants
mainmenu.add_cascade(label="opérations", menu = firstmenu)
mainmenu.add_cascade(label="Demande", menu = secondmenu)
mainmenu.add_cascade(label="Acceuil", menu = menu3)

app.config(menu=mainmenu)
app.mainloop()

























