
class Dier:
    def __init__(self, naam, geluid):
        self.naam = naam
        self.geluid = geluid

    def maak_geluid(self):
        print(f"De {self.naam} zegt '{self.geluid}'.")

kat = Dier ("kat", "meow" )
hond = Dier ("hond" , "woeffffffff")
koe = Dier ("koe" , "moeeeeee")
kat.maak_geluid()
hond.maak_geluid()
koe.maak_geluid()