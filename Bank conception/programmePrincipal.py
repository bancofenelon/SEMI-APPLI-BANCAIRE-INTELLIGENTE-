



from banqueCodeProject import *
import MethodForInterface as metItface

client1 = Client("Banco", "Fénelon", "Masculin", "17-05-2006", "Calavi")

compte1 = CompteBancaire(proprietaire=client1, solde=500)
compte2 = CompteBancaire(proprietaire=client1, solde=1000)

client1.afficher_comptes()




client2 = Client("DOSSOU"," Melvin","Féminin","12-09-2005","Calavi")
compte11 = CompteBancaire(proprietaire=client2, solde=1000)
client2.ajouter_compte(compte11)

client3 = Client("KPOVIESSI"," Pascal","Masculin","12-09-1990","Dangbo")
compte_pascal = CompteBancaire(proprietaire=client3, solde=1000)
client3.ajouter_compte(compte_pascal)
client3.afficher_comptes()
compte_pascal.deposer(10000000)


client_pote = Client("KIKI"," Godwin","Masculin","12-09-1990","Calavi")
compte_god = CompteBancaire(client_pote)
client_pote.ajouter_compte(compte_god)
client_pote.afficher_comptes()