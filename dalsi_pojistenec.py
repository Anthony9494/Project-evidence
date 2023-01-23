from pojistenci import Pojistenci

class DalsiPojistenec:
    def __init__(self):
        pass

    def pridani_pojisteneho(self):
        jmeno = input("Zadejte jméno pojištěného:\n")
        prijmeni = input("Zadejte příjmení: \n")

        vek = input("Zadejte věk: \n")

        tel_cislo = input("Zadejte telefonní číslo: \n")

        novy_pojistenec = Pojistenci(jmeno, prijmeni, vek, tel_cislo)
        return novy_pojistenec

    def vypsani_pojistenych(self, seznam_pojistenych):
        print("Výpis všech pojištěných:")
        for i in seznam_pojistenych:
            print(i)

    def vyhledani_pojistenych(self, seznam_pojistenych):
        jmeno_hledaneho = input("Zadejte jméno: \n")
        prijmeni_hledaneho = input("Zadejte příjmení: \n")
        for i in seznam_pojistenych:
            if (jmeno_hledaneho == i.jmeno) and (prijmeni_hledaneho == i.prijmeni):
                print(i)
            elif (jmeno_hledaneho == i.jmeno) and (prijmeni_hledaneho == ""):
                print(i)
            elif (jmeno_hledaneho == "") and (prijmeni_hledaneho == i.prijmeni):
                print(i)
            else:
                pass












