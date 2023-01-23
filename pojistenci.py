class Pojistenci:

    def __init__(self, jmeno, prijmeni, vek, tel_cislo):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.tel_cislo = tel_cislo

    def __str__(self):
        return("{0} {1} {2} {3}".format(self.jmeno, self.prijmeni, self.vek, self.tel_cislo))
