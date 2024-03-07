""" 
    Marvin Bader 
    Opdracht 1 Visual Studio Code en een klasse 
"""

import random

class Hond:
    def __init__(self, naam, leeftijd, geluid="Woef", ras=""):
        self.naam = naam
        self.leeftijd = leeftijd
        self.geluid = geluid
        self.ras = ras
        self.is_blaffend = False

    def blaf(self):
        print(self.geluid)

    def set_blaffend(self, waarde):
        self.is_blaffend = waarde


hond1 = Hond("Princess Bubblegum", 1, "Woef woef", "Labrador")
hond2 = Hond("Megetron Destroyer of worlds", 5, "RROAAAWWRHHH", "Golden Retriever")
hond3 = Hond("Lilly", 3, "GRRRrrrr", "Duitse Herder")
hond4 = Hond("Lordvoldemort", 5, "Woof", "Duitse Herder")
hond5 = Hond("Lilly", 3, "GRRrrrrbhh", "Duitse Herder")
hond6 = Hond("Billy", 3, "GRRRawwrrrr", "Duitse Herder")
hond7 = Hond("Silly", 3, "GRRRuurrrrrr", "Duitse Herder")
hond8 = Hond("Lolly", 3, "GRRRieerrrrr", "Duitse Herder")
hond9 = Hond("Jilly", 3, "GRRReeeeerrrr", "Duitse Herder")
hond10 = Hond("Jolly", 3, "GRRRerrrr", "Duitse Herder")

nummerlijst = []

blafLoop = 0
while blafLoop != 10:
    blafLoop += 1
    x = random.randint(1, 10)
    nummerlijst.append(x)
    #print(nummerlijst)
    if x == nummerlijst:
        blafLoop -= 1
        continue
    match x:
        case 1:
            hond1.blaf()
        case 2:
            hond2.blaf()
        case 3:
            hond3.blaf()
        case 4:
            hond4.blaf()
        case 5:
            hond5.blaf()
        case 6:
            hond6.blaf()
        case 7:
            hond7.blaf()
        case 8:
            hond8.blaf()
        case 9:
            hond9.blaf()
        case 10:
            hond10.blaf()