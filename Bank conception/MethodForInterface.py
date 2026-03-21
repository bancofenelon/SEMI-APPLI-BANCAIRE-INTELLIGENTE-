from tkinter.messagebox import showwarning

import banqueCodeProject as bkcode

import ClasseBancaire

import tkinter as tk



#calcul pour centrer une fenêtre
def centreur1(nom_fenetre=" ",largeur_fenêtre = 110,hauteur_fenêtre = 110):

    largeur_ecran = int(nom_fenetre.winfo_screenwidth())
    hauteur_ecran = int(nom_fenetre.winfo_screenheight())

    pos_X = ((largeur_ecran) // 2) - (largeur_fenêtre // 2)
    pos_y = ((hauteur_ecran) // 2) - (hauteur_fenêtre // 2)

    arg_geo = "{}x{}+{}+{}".format(largeur_fenêtre, hauteur_fenêtre, pos_X, pos_y)

    return arg_geo

def centreur(fenetre, largeur_fenetre=320, hauteur_fenetre=180):
    largeur_ecran = fenetre.winfo_screenwidth()
    hauteur_ecran = fenetre.winfo_screenheight()
    x = (largeur_ecran - largeur_fenetre) // 2
    y = (hauteur_ecran - hauteur_fenetre) // 2
    return f"{largeur_fenetre}x{hauteur_fenetre}+{x}+{y}"



"""fonction pour la gestion des exceptions surtout avec des fenêtres modales """
def value_erreur():

    from tkinter import messagebox
    messagebox.showerror("erreur".upper(),message="un probleme est survenu")



def errorofvalue(type=ValueError):
        from tkinter import messagebox
        messagebox.showwarning("error".upper(),message="les montants sont des nombres ")




"""les méthodes ou fonctions pour faire des commandes"""



##+**      essaie de tout factoriser en une  fonction  pour toutes les opérations     ****++++++=========*********
def fonc_op(operation):

    """ fonction de création de fenêtre pour réaliser """ +str(operation)
    import tkinter as tk
    fen_op = tk.Toplevel()
    fen_op.title(operation)
    fen_op.geometry(centreur(fen_op))
    fen_op.resizable(False, False)
    fen_op.configure(bg="#f0f0f0")  # couleur de fond de la fenêtre

    # ======= Montant =======
    label = tk.Label(fen_op, text="Montant :", bg="#f0f0f0")
    label.grid(row=0, column=0, sticky="e", padx=10, pady=10)

    var_entry = tk.StringVar()
    entry = tk.Entry(fen_op, textvariable=var_entry, width=20)
    entry.grid(row=0, column=1, padx=10, pady=10)

    var_montant = tk.StringVar()
    montant_label = tk.Label(fen_op, textvariable=var_montant, bg="#f0f0f0")
    montant_label.grid(row=1, column=1, padx=10, pady=5)
    var_montant.set("Entrez un montant")

    # ======= Numéro de compte =======
    label_compte = tk.Label(fen_op, text="Numéro de compte :", bg="#f0f0f0")
    label_compte.grid(row=2, column=0, sticky="e", padx=10, pady=10)

    num_entry = tk.StringVar()
    num = tk.Entry(fen_op, textvariable=num_entry, width=20)
    num.grid(row=2, column=1, padx=10, pady=10)

    var_num = tk.StringVar()
    num_label = tk.Label(fen_op, textvariable=var_num, bg="#f0f0f0")
    num_label.grid(row=3, column=1, padx=10, pady=5)
    var_num.set("Entrez le numéro de compte")

    # ======= Bouton Retirer =======
    bt = tk.Button(fen_op, text=operation, state="disabled", width=15)
    bt.grid(row=4, column=1, pady=15)

    # ======= Fonctions de validation =======
    def check_inputs(*args):
        # Vérifie montant
        montant_str = var_entry.get()
        compte_str = num_entry.get()

        valid = True

        # Validation du montant
        if montant_str.strip() == "":
            var_montant.set("Champ vide")
            montant_label.config(fg="red")
            valid = False
        else:
            try:
                valeur = float(montant_str)
                var_montant.set(f"{valeur} est la valeur entrée")
                montant_label.config(fg="green")
            except ValueError:
                var_montant.set("Erreur : entrez un nombre")
                montant_label.config(fg="red")
                valid = False

        # Validation du compte
        if compte_str.strip() == "":
            var_num.set("Champ vide")
            num_label.config(fg="red")
            valid = False
        else:
            var_num.set("Compte OK")
            num_label.config(fg="green")

        # Activation/désactivation du bouton
        if valid:
            bt.config(state="normal")
        else:
            bt.config(state="disabled")

    def valider_operation():
        var_montant.set(f"Montant {var_entry.get()}  pour : {operation} !")
        var_num.set(f"Compte {num_entry.get()} validé")
        bt.config(state="disabled")  # désactive après operation

    # Lier les entrées à la fonction check_inputs
    var_entry.trace("w", check_inputs)
    num_entry.trace("w", check_inputs)
    bt.config(command=valider_operation)


#je veux retouver mes opération a chaque clique maintenant
op_list=["Dépôt","Retrait","Emprunt","consultation solde","Transfert","Rembourser"]

def Depot():
    """c'est celle ci qui sera maintenant ma commande pour le dépôt  """
    fonc_op(op_list[0])

def Retrait():
    """c'est celle ci qui sera maintenant ma commande  pour le retrait """
    fonc_op(op_list[1])



def Emprunt():
    """c'est celle ci qui sera maintenant ma commande """
    fonc_op(op_list[2])

def consultation_solde():
    """c'est celle ci qui sera maintenant ma commande  pour la consultation du solde """
    """ici on veut juste afficher des informations ,alors on  le fera a partir d'un  """


    import tkinter as tk
    cons = tk.Toplevel()
    cons.title("consultation_solde")
    cons.geometry(centreur(cons))
    cons.resizable(False, False)
    cons.configure(bg="#f0f0f0")  # couleur de fond de la fenêtre


    # ======= Numéro de compte =======
    label_compte = tk.Label(cons, text="Numéro de compte :", bg="#f0f0f0")
    label_compte.grid(row=2, column=0, sticky="e", padx=10, pady=10)

    # === saisie du numero de compte =======
    var_entry=tk.StringVar()

    entry_compte = tk.Entry(cons, textvariable=var_entry, width=20)

    entry_compte.grid(row=2, column=1, sticky="e", padx=10, pady=10)

    # ======  Label de contôle ============
    control_Label_var=tk.StringVar()

    control_Label=tk.Label(cons,textvariable=control_Label_var)
    control_Label.grid(row=3, column=1, sticky="e", padx=10, pady=10)
    control_Label_var.set("Entrez le numéro du compte ")

    # ======= Bouton  =======
    bt = tk.Button(cons, text="Ok", state="disabled", width=15)
    bt.grid(row=4, column=1, pady=15)

    def conformite_compte(*args):
        num_compte = var_entry.get()
        if num_compte.strip() == "":
             control_Label_var.set("Champ vide")
             control_Label.config(fg="red")
             valid = False
        else:

             for i in "@#{[[||`\\^@]}=)°=*µ¤^²é!:;,":
                 while i in num_compte:
                     control_Label_var.set("Pas de caractères spéciaux pour un numéro de compte ")
                     control_Label.config(fg="red")
                     valid = False
                 else:
                     control_Label_var.set(" {} est le numero entré".format(num_compte))
                     control_Label.config(fg="green")
                     valid = True

        #validation du bt
        if valid:
            bt.config(state="normal")
        else:
            bt.config(state="disabled")

    # consultation proprement dite
    def affiche_consultation():
        app=tk.Tk()
        app.title("consultation_solde")
        app.geometry(centreur(app))
        app.resizable(False, False)
        sms = tk.Message(app, text="chers {},votre compte au numéro {} a un solde de :{}")
        sms.pack()

        app.mainloop()

    # liaison avec la fonction conformité
    var_entry.trace("w", conformite_compte)
    bt.config(command=affiche_consultation)




def Transfert():
    """c'est celle ci qui sera maintenant ma commande  pour le transfert """
    fonc_op(op_list[4])

def Rembourser():
    """c'est celle ci qui sera maintenant ma commande """
    fonc_op(op_list[5])



#programme principal
