#fichier 2 pour banqueCodeProject
import os
from datetime import datetime
import  uuid

import csv
class CompteBancaire:

    """"Classe des comptes bancaires,le client poura faire des opérations """


    #compteur de compte pour attribuer le numéro
    nbr_compte=0

    #ficher pour réaliser l'histirique
    #fichier_operations = "Operation.txt" au fait ce code  est inssufisant lorsque je lance le code depuis un autre dossier


    fichier_operations = os.path.join(os.path.dirname(__file__), "Operation.txt")

    """pourquoi la ligne précedente , eh bien car :
    Explication  :

    __file__ → chemin complet du fichier Python courant.

    os.path.dirname(__file__) → dossier du fichier Python.

    os.path.join(...) → crée le chemin complet vers Operation.txt dans ce dossier.

✅ Résultat : même si je lance ton script depuis un autre dossier, le fichier sera toujours créé et utilisé au bon endroit.
    
    """

    # Création automatique du fichier au lancement
    if not os.path.exists(fichier_operations):
        with open(fichier_operations, "w", encoding="utf-8") as f:
            f.write(" identifiant interne (UUID) ; Prénom ; Nom ; Nature ; Montant ; Date\n")
        print(f"✅ Fichier '{fichier_operations}' créé avec succès")



    #Création du ficher csv lequel est pratique pour l'analyse des données plus tard dans excel ou dans  pandas
    fichier_csv = os.path.join(os.path.dirname(__file__), "Operation.csv")
    if not os.path.exists(fichier_csv):
        with open(fichier_csv, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Numéro Public", "Nom", "Prénom", "Nature", "Montant", "Date"])

    #                    LE CONSTRUCTECTEUR
    def __init__(self, proprietaire : 'Client', solde : float =0.0):
        """constructeur du CompteBancaire: instanciateur  pour la création d'un compte avec ses attributs """


        """le constructeur ne prendra pas de montant initial négatif """
        if solde < 0:
            raise ValueError("Le solde initial ne peut pas être négatif")

        CompteBancaire.nbr_compte += 1                  #incrémentation pour connaitre le nombre de compte crés au toatal
        self.proprietaire = proprietaire                # Instance de Client
        self.solde = solde
        """Fabrication du numéro public visuble par le client """
        self.numero = self.generer_numero_public(self.proprietaire.nom, self.proprietaire.prenom)      # ----->>>   #appel a la création du num public dans notre constructeur

        # Numéros interne privé UUID

        self.__id=self.generer_numero_interne()
        """#Double undescore alors à protégé cette variable   ------>>>      #appel a la création du num interne  dans notre constructeur
        """
        proprietaire.ajouter_compte(self)         #liaison automatique  du compte au client
        print(f"✅ Compte créé pour {proprietaire.nom} {proprietaire.prenom} avec solde initial {solde}€")
        # les propriétés ou encapsulation
    @property          #décorateur pour l'id
    def id_interne(self):
        """Retourne l'UUID interne (lecture seule)"""
        return self.__id

    def __str__(self)  -> str:
        return f"Compte N°{self.numero} - Solde: {self.solde:.2f}€\n Propriétaire :{self.proprietaire.nom} {self.proprietaire.prenom}"


    """________________LES METHODES DE GESTIONS DE LA BANQUE_________________________
    # conception pratitique et prudente des numéros                      (privé(s)  (du public))
    #methode pour avoir un id interne prudent ,difficille a deviner par quiconque
    _________"""


    def generer_numero_interne(self) -> str:
        """ Cette methode génère un numéro aléatoire dont le client sera gardé  impossible à deviner pour la
                                                                           sécurisations des info """
        return uuid.uuid4()


    # conception des numeros publiques    pour avoir un numero assez particulier et individuel reservé au public (client)
    def generer_numero_public(self, nom, prenom) -> str:
        """ Cette methode génère un numéro pseudo- aléatoire dont le client aura connaissance  difficile à deviner
        du fait de la petite partie aléatoire pour la sécurisations des info """
        info = "BEN" + str(datetime.now().year)
        prefix = nom[:3].upper() + prenom[:3].upper()
        unique_part = str(uuid.uuid4()).replace("-", "")[:6].upper()
        return f"{info}/{prefix}-{unique_part}"

    #enregistreur des opérations

    def enregistrer_operation(self,nature : str ,montant :float = 0.0):
        """Enregistre l'opération dans un ficher texte """
        date_du_jour = datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
        with open (CompteBancaire.fichier_operations,"a",encoding="utf-8") as f:
            f.write( " {} , {} , {} , {} ,{} , {}  \n".format(self.id_interne,self.proprietaire.nom,self.proprietaire.prenom,nature,montant,date_du_jour))


    #enrégistrer dans un ficher csv
    def enregistrer_operation_csv(self, nature: str, montant: float = 0.0) -> None:
        """Enregistre l'opération dans un fichier CSV pour analyse ultérieure."""
        fichier = os.path.join(os.path.dirname(__file__), "Operation.csv")
        with open(fichier, mode="a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([
                self.numero,
                self.proprietaire.nom,
                self.proprietaire.prenom,
                nature,
                f"{montant:.2f}",
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ])

    def retirer(self, montant: float) -> float:
        """    #methode pour retirer un montant"""
        if montant <= 0:
            raise ValueError("Le montant à retirer doit être positif")
        if montant > self.solde:
            return    "Solde insuffisant"
        self.solde -= montant
        self.enregistrer_operation("Retrait", montant)
        self.enregistrer_operation_csv("Retrait", montant)
        return self.solde

    #methode pour l'emprunt
    def emprunter(self, montant: float) -> float:
        """
        Permet au client de faire un emprunt.
        Applique un intérêt fixe et débite le compte.
        """
        if montant <= 0:
            raise ValueError("Le montant de l'emprunt doit être positif")

        taux_interet = 0.05
        montant_total = montant * (1 + taux_interet)
        self.solde -= montant_total

        print(f"Emprunt de {montant:.2f}€ effectué avec succès, intérêt de {taux_interet * 100:.0f}% inclus.")

        self.enregistrer_operation("Emprunt", montant)
        self.enregistrer_operation_csv("Emprunt", montant)
        return self.solde

    #methode pour le dépôt
    def deposer(self, montant: float) -> float:
        """
        Dépose un montant positif sur le compte et l'enregistre.
        """
        if montant <= 0:
            raise ValueError("Le montant à déposer doit être positif")

        self.solde += montant
        print(f"Dépôt de {montant:.2f}€ effectué avec succès.")

        self.enregistrer_operation("Dépôt", montant)
        self.enregistrer_operation_csv("Dépôt", montant)
        return self.solde

    #Définition d'une methode pour le transfert
    def transferer(self, montant: float, compte_destinataire: 'CompteBancaire') -> None:
        """
        Transfère un montant vers un autre compte.
        Enregistre l'opération dans les fichiers texte et CSV pour les deux comptes.
        """
        if montant <= 0:
            raise ValueError("Le montant à transférer doit être positif")

        # Vérifier et retirer le montant du compte expéditeur
        resultat = self.retirer(montant)
        if isinstance(resultat, str):  # Solde insuffisant
            raise ValueError(resultat)
       # Déposer le montant sur le compte destinataire
        compte_destinataire.deposer(montant)

        # Enregistrer le transfert pour l'expéditeur
        self.enregistrer_operation(f"Transfert vers {compte_destinataire.numero}", montant)
        self.enregistrer_operation_csv(f"Transfert vers {compte_destinataire.numero}", montant)

        # Enregistrer le transfert pour le destinataire
        compte_destinataire.enregistrer_operation(f"Transfert reçu de {self.numero}", montant)
        compte_destinataire.enregistrer_operation_csv(f"Transfert reçu de {self.numero}", montant)

        print(f"✅ Transfert de {montant:.2f}€ vers {compte_destinataire.proprietaire.nom} "
              f"{compte_destinataire.proprietaire.prenom} effectué avec succès.")
        return f"✅ Transfert de {montant:.2f}€ vers {compte_destinataire.proprietaire.nom} "+f"{compte_destinataire.proprietaire.prenom} effectué avec succès."


    #Methode pour consulter le solde

    def consulter_solde(self) -> str:
        """
        Retourne un message clair sur le solde du compte.
        - Si solde > 0 : montant disponible
        - Si solde = 0 : solde nul
        - Si solde < 0 : montant dû (crédit)
        """

        # Déterminer le titre
        titre = "Mme" if self.proprietaire.sexe.lower() == "féminin" else "Mr"

        nom_complet = f"{self.proprietaire.nom} {self.proprietaire.prenom}"

        if self.solde > 0:
            return f"{titre} {nom_complet}, votre solde est de {self.solde:.2f} €"
        elif self.solde == 0:
            return f"{titre} {nom_complet}, votre solde est nul (0 €)"
        else:  # solde < 0
            return f"{titre} {nom_complet}, vous êtes débiteur de {-self.solde:.2f} €"

    @staticmethod
    def heure_actuelle():
        now = datetime.now()
        return f"{now:%H:%M:%S}"



#programme principal