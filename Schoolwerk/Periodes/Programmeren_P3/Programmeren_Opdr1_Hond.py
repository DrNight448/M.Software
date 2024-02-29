""" 
    Marvin Bader 
    Opdracht 1 Visual Studio Code en een klasse 
"""
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

hond1.blaf()
hond2.blaf()
hond3.blaf()

hondenlijst = [hond1, hond2, hond3]

for hond in hondenlijst:
    hond.blaf()