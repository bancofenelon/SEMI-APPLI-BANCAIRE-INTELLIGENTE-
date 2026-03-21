#coding:utf-8
from datetime import date, datetime
import os
import uuid

class Client:
    """"Classe des client lesquels ont des comptes"""


    nbr_client = 0                         # je compte mes clients


    def __init__(self, nom:str, prenom:str, sexe:str, date_naissance:datetime.date , adresse:str):



        # verification des noms et prénoms
        if not nom or not prenom or not sexe or not date_naissance or not adresse:
            raise ValueError("Les informations ne sont pas totales ")

        self.nom = nom.strip().capitalize()
        self.prenom = prenom.strip().capitalize()

        #encapsulation de sexe ( annonce )

        self._sexe = None                        #le sexe privé,reservé à l'encapsulation :aux accesseurs getter et setter notament
        self.sexe = sexe                         #l'entrée ,le sexe qui peut être n'importe quoi



        self.adresse = adresse
        self.comptes = []  # Liste de comptes du client

        # Conversion automatique si date_naissance est une chaîne
        if isinstance(date_naissance, str):
            try:
                self.date_naissance: date = datetime.strptime(date_naissance, "%d-%m-%Y").date()
            except ValueError:
                raise ValueError("La date doit être au format JJ-MM-AAAA")
        elif isinstance(date_naissance, date):
            self.date_naissance = date_naissance
        else:
            raise TypeError("date_naissance doit être un str ou un objet date")

        # un client est crée
        Client.nbr_client += 1
        print(f"✅ Nouveau client créé : {self.nom} {self.prenom}")


    @property                                     #Debut des propriétés ,encapsulation
    def sexe(self) -> str:
        """Le getter qui retourne le sexe du compte"""
        return self._sexe

    @sexe.setter                                  #2eme décorateur :le setter qui encapsule réellement le sexe
    def sexe(self,valeur:str ):
        """Le setter qui définit le sexe du client et vérifie si il est correct """
        valeur=valeur.strip().lower()
        if valeur in ["masculin","féminin"]:
            self._sexe = valeur.strip().capitalize()
        else:
            raise ValueError("Le sexe doit être entre masculin et  féminin")



#methode por mettre les comptes des clients dans une liste car une personne peut avoir many comptes

    def ajouter_compte(self, compte : 'CompteBancaire') -> None :#met les comptes des clients dans une liste car une personne peut avoir many comptes
        """les comptes pour un clients """
        self.comptes.append(compte)





    #c'est la fonction si on veut connaitres les comptes eistants pour un client donné

    def afficher_comptes(self) -> None:
        """Affiche tous les comptes du client."""
        if not self.comptes:
            print(f"{self.nom} {self.prenom} n'a aucun compte.")
        else:
            for compte in self.comptes:
                print(compte)

    #Une nouvelle methode pour rechercher un compte  connaissant son numéro

    def obtenir_compte(self,numero:str )  -> 'CompteBancaire | None':
        """Retourne le compte correspondant au numéro ou None."""
        for compte in self.comptes:
            if compte.numero == numero:
                return compte
        return None




    """                 Affichage propre des info sur le client                              """

    def __str__(self) -> str:
        return (f"Client {Client.nbr_client}: {self.nom} {self.prenom}\n"
                f"Sexe et date de naissance: {self.sexe} {self.date_naissance.strftime('%d-%m-%Y')}\n"
                f"Adresse: {self.adresse}")

""""*********************** une nouvelle classe pour les comptes de la banque *******************"""

class CompteBancaire:

    """"Classe des comptes bancaires,le client poura faire des opérations """


    #compteur de compte pour attribuer le numéro
    nbr_compte=0

    #ficher pour réaliser l'histirique
    fichier_operations = "Operation.txt"


    # Création automatique du fichier au lancement
    if not os.path.exists(fichier_operations):
        with open(fichier_operations, "w", encoding="utf-8") as f:
            f.write(" identifiant interne (UUI) ; Prénom ; Nom ; Nature ; Montant ; Date\n")
        print(f"✅ Fichier '{fichier_operations}' créé avec succès")



#                    LE CONSTRUCTECTEUR
    def __init__(self, proprietaire, solde=0):
        """constructeur du CompteBancaire: instanciateur  pour la création d'un compte avec ses attributs """

        CompteBancaire.nbr_compte += 1                  #incrémentation pour connaitre le nombre de compte crés au toatal
        self.proprietaire = proprietaire                # Instance de Client
        self.solde = solde
        self.numero = self.generer_numero_public(self.proprietaire.nom, self.proprietaire.prenom)      # ---------------->>>   #appel a la création du num public dans notre constructeur
        self.__id=self.generer_numero_interne()    #Double undescore alors à protégé cette variable   -------------------------------------------->>>      #appel a la création du num interne  dans notre constructeur
        proprietaire.ajouter_compte(self)                          # ---------------->>> Liaison automatique

    @property          #décorateur pour l'id
    def id_interne(self):
        """Retourne l'UUID interne (lecture seule)"""
        return self.__id



    def __str__(self):
        return f"Compte N°{self.numero} - Solde: {self.solde:}€"

    """________________LES METHODES DE GESTIONS DE LA BANQUE_______________
        # conception pratitique et prudente des numéros privé(s)  (du public)
___________________"""

    def generer_numero_interne(self):
        """methode pour avoir un id interne prudent ,difficille a deviner par quiconque"""
        return uuid.uuid4()


    # conception des numeros publiques

    def generer_numero_public(self, nom, prenom):
       """methode pour avoir un numero assez particulier et individuel reservé au public (client)"""

       info = "BEN2025"
       prefix = nom[:3].upper() + prenom[:3].upper()
       unique_part = str(uuid.uuid4()).replace("-", "")[:6].upper()
       return f"{info}/{prefix}-{unique_part}"

    #enregistreur des opérations

    def enregistrer_operation(self,nature,montant=0):
        """Enregistre l'opération dans un ficher texte """
        date_du_jour = datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
        with open (CompteBancaire.fichier_operations,"a",encoding="utf-8") as f:
            f.write( " {} , {} , {} , {} ,{} , {}  \n".format(self.id_interne,self.proprietaire.nom,self.proprietaire.prenom,nature,montant,date_du_jour))


    #myself---Fonction pour opérer de l'emprunt
    def emprunter(self,montant=0):#  methode du client qui consiste àemprunter du sous

        if montant  <=0:
            montant=0
            print("pas de prêt négatifs possible,on le compte comme nul")
        i = 0.05                  # pratiquer un taux pour diférencier le retrait de l'emprunt
        inter = montant * i       #inter pour dire interêt ......
        montantactu= montant + inter
        self.solde -= montantactu
        print("Emprunt  de {} fais avec succès au taux de {}%....".format(montant,i))
        self.enregistrer_operation("Emprunt ", montant)
        return self.solde


    #methode pour le dépôt

    def deposer(self,montant=0):#method for give money in my "compte" in bank

        if montant <=0:
            print("Requête impossible,pas de montant négatif pour un dépôt")
        self.solde= self.solde+montant
        print("Dépot de {} fais avec succès....".format(montant))
        self.enregistrer_operation("Dépôt ",montant)
        return self.solde

#        methode pour le retrait
    def retirer(self,montant=0 ):
        """Methode pour le retrait"""
        try:#création d'exception quand le montant est négatif et inférieur au solde dispo
            if montant > 0:
                if self.solde>=montant:
                    self.solde = self.solde - montant
                else:
                    print("Vôtre solde est insuffisant ")
                    raise ValueError
            else:
                raise TypeError


        except ValueError:
            return "Retrait impossible \nVous n'avez que {} comme solde ".format(self.solde)
        except TypeError:
            print('Erreur : pas de montant négatif pour un retrait ')
        else:
            self.enregistrer_operation("Retrait  ", montant)
            return "Retrait  de {} avec succès....".format(montant)

    #Définition d'une methode pour le transfert
    def transferer(self,montant, compte_destinataire):
        if montant > 0:                                          # positivité du montant
            if self.solde >= montant:                            #compatibilité du solde
                self.solde -=  montant                 #Retrait sur le compte source
                self.enregistrer_operation("Transfer  vers {} ".format(compte_destinataire.numero ), montant)  #appel de l'enrégistreur

                compte_destinataire.solde +=montant               #dépôt sur sur le compte cible
                compte_destinataire.enregistrer_operation(f"Transfert depuis {self.numero}", montant) #écriture de l'opération dans notree ficher texte
            else:
                print("Votre solde est insuffisant pour un transfert  de {} ".format(montant))
        else:
            print("Pas de montant négatif ")



    #methode pour consulter le solde du compte
    def consulter_solde(self):

        if self.proprietaire.sexe.strip().lower() == "féminin":
            stat= " Mme "
        elif self.proprietaire.sexe.strip().lower() == "masculin":
            stat= " Mr "
        else:
            stat= " Veuillez choisir entre féminin ou masculin  "   # a revoir ,le mieux est d'encapsuler sexe
        if self.solde < 0:
            return stat+"{},vous avez un crédit de : {}€".format( self.proprietaire.nom+" "+self.proprietaire.prenom,- self.solde)
        else:
            return  stat + "{},votre solde est de {}€".format( self.proprietaire.nom+" "+self.proprietaire.prenom, self.solde)






    @staticmethod
    def heure_actuelle():
        now = datetime.now()
        return f"{now:%H:%M:%S}"



#programme principal