# Zad.1
class Prostokat:
    def __init__(self,dlugosc, szerokosc):
        self.a=dlugosc
        self.b=szerokosc
    def pole(self):
        return self.a*self.b
    def obwod(self):
        return self.a*2+self.b*2
# p = Prostkokat(2,5)
# print(p.pole()," ", p.obwod())

# Zad.2
class ProstokatExtra(Prostokat):
    def __init__(selfself,x,y):
        super.__init__(x,y)
    def wyswietl_pole(self):
        print(f"Pole prostokata o bokach {self.a} i {self.b} wynosi {self.pole()}")
    def wyswietl_obwod(self):
        print(f"Pole prostokata o bokach {self.a} i {self.b} wynosi {self.obwod()}")
p2=ProstokatExtra(3,4)
p2.wyswietl_pole()
