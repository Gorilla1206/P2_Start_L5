class pizza:
    def __init__(self, naam, groote, toppings, prijs ):
        self.naam = naam
        self.groote = groote
        self.toppings = toppings
        self.prijs = self.bereken_prijs()
    def toon_informatie(self):
        print(f"Naam: {self.naam}")
        print(f"groote:  {self.groote}")
        print(f"toppings: {self.toppings}")
        print(f"prijs:{self.prijs}")
    def bereken_prijs(self):
        basisprijs=0.0
        if self.groote == "small":
            basisprijs =8.99
        elif self.groote == "medium":
            basisprijs = 10.99
        basisprijs += len(self.toppings)  *1.5
        return basisprijs



pizza1 = pizza("Margherita", "small", ["kaas", "tomatensaus"],"8.99 euro")
pizza2 = pizza("funghi", "medium", ["kaas", "tomatensaus"],"10.99 euro")
print(f'prijs: {pizza1.bereken_prijs()})')
print(f'prijs: {pizza2.bereken_prijs()})')




pizza1.toon_informatie()
pizza2.toon_informatie()