'''
Python3
Programmazione ad oggetti
'''

class moto:

    # Attributi di Classe
    garanzia = 1
    assicurazione = True
    parcoMoto = 0

    #Metodo costruttore
    def __init__(self,proprietario, marca, modello, cilidrata, cavalli, colore):

        # Attributi di Istanza
        self.proprietario = proprietario
        self.marca = marca
        self.modello = modello
        self.cilindrata = cilidrata
        self.cavalli = cavalli
        self.colore = colore
        
        moto.parcoMoto +=1

    #Metodo di tipo Get
    def scheda(self):
        return f'\nScheda "{self.proprietario}"\n Marca: {self.marca}\n Modello: {self.modello}\n Cilindrata: {self.cilindrata}\n Cavalli: {self.cavalli}\n colore: {self.colore}\n assicurazione: {self.assicurazione}' 
    
giovanni = moto("alberto","ktm","duke",690, 73, "arancione")