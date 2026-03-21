#coding:utf-8

#help(property)
class Client:
    """docstring for Client:classe des clients pour une banque"""

    nbre_clients=0

    def __init__(self, nom, prenom,sexe,date_naissance,adresse):
        """docstring for constructeur"""
        print(" Nous avons un nouveau client ....")
        Client.nbre_clients += 1
        self.nom = nom
        self.prenom = prenom
        self._sexe = sexe
        self.date_naissance = date_naissance
        self.adresse = adresse
        self.solde = 0
        self.numero_compte = self.prenom[:3] +self.nom[:3]  + date_naissance[-2:]+self.sexe[:1].upper() +self.adresse[:3]+ "-"+str(Client.nbre_clients)


    def Information(self):#fonction qui renseigne les info

        """docstring for Information qui idenditie chacun des clients """
        information= "Cher client,voici vos informations\n"+"\nNom                  : {} \nPrénom               : {} \nSexe                 : {}\nDate de naissance    : le {}\nRésidence            : {}\nIdentifiant bancaire : {}\nSolde actuel         : {}€ ".format(self.nom.upper(),self.prenom.capitalize(),self.sexe.capitalize(),self.date_naissance,self.adresse,self.numero_compte,self.solde)
        print(information)
    @property
    def sexe(self):#mon getter
        return self._sexe

    @sexe.setter
    def sexe(self, sexe):
        self._sexe = sexe
        return self._sexe


    def emprunter(self,montant=0):#  methode du client qui consiste àemprunter du sous


        if montant  <=0:
            montant=0
            print("pas de prêt négatifs possible,on le compte comme nul")

        # pratiquer un taux pour diférencier le retrait de l'emprunt
        i = 0.05
        interêt = montant * i
        montantactu= montant + interêt
        self.solde -= montantactu
        print("Emprunt  de {} fais avec succès au taux de {}%....".format(montant,i))
        return self.solde


    def deposer(self,montant=0):#method for give money in my "compte" in bank
        if montant <=0:
            montant=0
            print("votre montant est mis à 0")
        self.solde= self.solde+montant
        print("Dépot de {} fais avec succès....".format(montant))
        return self.solde


    def retirer(self,montant=0 ):

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
            return "Vous n'avez que {} comme solde ".format(self.solde)
        except TypeError:
            print('Erreur : Vous ne pouvez que retirer un montant positif')
        else:
            return "Retrait  de {} avec succès....".format(montant)



    def consulter_solde(self):
        if self._sexe.strip().lower() == "féminin":
            stat= " Mme "
        else:
            stat= " Mr "
        if self.solde < 0:
            return stat+"{},vous avez un crédit de : {}€".format( self.nom+" "+self.prenom,- self.solde)
        else:
            return  stat + "{},votre solde est de {}€".format( self.nom+" "+self.prenom, self.solde)



#programme principal
client_1=Client("BANCO AKOWE","Fénelon","masculin","17-05-2006","Calavi")


#client_sam= Client("BANCO AKOWE ","Salem","mascuin","16-11-2003","calavi")

def renseigner_client(leClient):#fonction pour l'enrégistrement utilisable par le banquier

    nom=input("Entrez le nom du client: ")
    prenom=input("Entrez le prenom du client: ")
    sexe=input("Entrez le sexe du client: ")
    Date_de_naissance=input("Entrez le date de naissance du client: ")
    adrresse=input("Entrez le adresse du client: ")
    leClient=Client(nom,prenom,sexe,Date_de_naissance,adrresse)
    return leClient.Information()



def clientNamePourBanq():

    X=str(Client.nbre_clients)
    clientX="client"+ X
    leClient=str(clientX)
    return  leClient

"""""
#lançement
leClient=clientNamePourBanq()
print(leClient)
print(renseigner_client(leClient))
"""""

LeClient=Client("TOTO","Fabegas","Masculin","17-09-1978","Machester united")
LeClient.deposer(200)
LeClient.Information()
print(clientNamePourBanq())
print(Client.consulter_solde( LeClient))
print("*"*12)


LeClient=Client("MOUSSA","Aliou","Masculin","17-10-1998"," Niamey")
LeClient.Information()
print(clientNamePourBanq())
print(Client.nbre_clients)
LeClient.retirer(300)

print(Client.consulter_solde( LeClient))
