from dalsi_pojistenec import DalsiPojistenec

dalsi_pojistenec = DalsiPojistenec()
seznam_pojistenych = []


pokracovat = True
while pokracovat:
    print("---------------------------")
    print("Evidence pojištěných")
    print("---------------------------")
    print("Vyberte si akci a potvrďte tlačítkem enter: ")
    print("1 - Přidat nového pojištěného")
    print("2 - Vypsat všechny pojištěné")
    print("3 - Vyhledat pojištěného podle jména, příjmení nebo obojího")
    print("4 - Konec")

    operace = int(input())
    if operace == 1:
        novy_pojistenec = dalsi_pojistenec.pridani_pojisteneho()
        seznam_pojistenych.append(novy_pojistenec)
        input("Data byla uložena. Pokračujte libovolnou klávesou...")



    elif operace == 2:
        dalsi_pojistenec.vypsani_pojistenych(seznam_pojistenych)
        input("Pokračujte libovolnou klávesou...")


    elif operace == 3:
        dalsi_pojistenec.vyhledani_pojistenych(seznam_pojistenych)
        input("Pokračujte libovolnou klávesou...")



    elif operace == 4:
        pokracovat = False
        print("Děkujeme za použití Naší evidence!")
        input("Evidenci ukončíte libovolnou klávesou.")
    else:
        input("Chybná operace, pro zopakování akce stiskněte libovolnou klávesu...")