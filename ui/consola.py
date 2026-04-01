from domain.manager import *
def meniu_principal():
    print("Bălătici Alexandra-Maria, grupa 211")
    print ("1. Conversii intre baze")
    print ("2. Conversii rapide")
    print ("3. Operatii aritmetice intr-o baza introdusa de la tastatura")
    print ("4. Exit")

def conversii_rapide_ui():
    try:
        p = int(input("Introduceti una dintre bazele 2, 4, 8, 16: "))
        if p not in [2, 4, 8, 16]:
            raise ValueError
        match p:
            case 2:
                conversii_rapide_2_ui()
            case 4:
                conversii_rapide_4_ui()
            case 8:
                conversii_rapide_8_ui()
            case 16:
                conversii_rapide_16_ui()
    except ValueError as e:
        print (f"Va rugam introduceti date valide. Eroare: {e}")

def meniu_operatii_aritmetice():
    print ("1. Adunare")
    print ("2. Scadere")
    print ("3. Inmultire")
    print ("4. Impartire")

def conversii_rapide_8_ui():
    try:
        val = input("Introduceti un numar in baza 8 care sa fie transformat in baza 2: ")
        for ch in val:
            if ch not in ['0', '1', '2', '3', '4', '5', '6', '7']:
                raise ValueError("Numarul nu poate contine alte cifre in afara de 0, 1, 2, 3, 4, 5, 6 sau 7")
        result = conversii_rapide_8_2(val)
        print(f"{val}(4) = {result}(2)")
    except ValueError as e:
        print (f"Va rugam introduceti date valide. Eroare: {e}")

def conversii_rapide_16_ui():
    try:
        p = int(input("Introduceti una dintre bazele 2, 4: "))
        if p not in [2, 4]:
            raise ValueError("Bazele trebuie sa fie 2 sau 4: ")
        val = input("Introduceti un numar in baza 16: ")
        for ch in val:
            if ch not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'c', 'd', 'e', 'f']:
                raise ValueError("Numarul nu poate contine alte cifre in afara de 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, a, B, b, C, c, D, d, E, e, F sau f")
        if p == 2:
            result = conversii_rapide_16_2(val)
            print(f"{val}(16) = {result}(2)")
        if p == 4:
            result = conversii_rapide_16_4(val)
            print(f"{val}(16) = {result}(4)")
    except ValueError as e:
        print(f"Va rugam introduceti date valide. Eroare: {e}")

def conversii_rapide_4_ui():
    try:
        p = int(input("Introduceti una dintre bazele 2, 16: "))
        if p not in [2, 16]:
            raise ValueError("Bazele trebuie sa fie 2 sau 16: ")
        val = input("Introduceti un numar in baza 4: ")
        for ch in val:
            if ch not in ['0', '1', '2', '3']:
                raise ValueError("Numarul nu poate contine alte cifre in afara de 0, 1, 2 sau 3")
        if p == 2:
            result = conversii_rapide_4_2(val)
            print(f"{val}(4) = {result}(2)")
        if p == 16:
            result = conversii_rapide_4_16(val)
            print(f"{val}(4) = {result}(16)")
    except ValueError as e:
        print (f"Va rugam introduceti date valide. Eroare: {e}")

def conversii_rapide_2_ui():
    try:
        p = int(input("Introduceti una dintre bazele 4, 8, 16: "))
        if p not in [4, 8, 16]:
            raise ValueError("Bazele trebuie sa fie 4, 8 sau 16: ")
        val = input("Introduceti un numar in baza 2: ")
        for ch in val:
            if ch not in ['0', '1']:
                raise ValueError("Numarul nu poate contine alte cifre in afara de 0 si 1")
        if p == 4:
            result = conversii_rapide_2_4(val)
            print(f"{val}(2) = {result}(4)")
        if p == 8:
            result = conversii_rapide_2_8(val)
            print(f"{val}(2) = {result}(8)")
        if p == 16:
            result = conversii_rapide_2_16(val)
            print(f"{val}(2) = {result}(16)")
    except ValueError as e:
        print (f"Va rugam introduceti date valide. Eroare: {e}")

def meniu_conversii_baze():
    print ("1. Conversie prin impartiri sucesive (intregi)")
    print ("2. Conversie prin substitutie (se accepta zecimale)")
    print ("3. Conversie printr-o baza intermediara (se accepta zecimale)")

def conversie_impartiri_succesive_ui():
    try:
        baza_initiala = int(input("Va rugam introduceti o baza initiala: "))
        if baza_initiala > 16 or baza_initiala < 0:
            raise ValueError(f"Bazele trebuie sa fie =< 16. {baza_initiala} > 16")
        numar = input("Introduceti un numar in baza initiala: ")
        if numar_validat(numar, baza_initiala) == False:
            raise ValueError(f"{numar} nu este un numar in baza {baza_initiala}")
        baza_finala = int(input("Va rugam introduceti o baza finala: "))
        if baza_finala > 16 or baza_finala < 0:
            raise ValueError(f"Bazele trebuie sa fie =< 16. {baza_finala} > 16")
        result = conversie_baza_intermediara(numar, baza_initiala, baza_finala, 0)
        print(f"{numar}({baza_initiala}) = {result}({baza_finala})")
    except ValueError as e:
        print(f"Va rugam introduceti date valide. Eroare: {e}")

def conversie_substitutie_ui():
    try:
        baza = int(input("Va rugam introduceti o baza: "))
        numar = input(f"Introduceti un numar in baza {baza}: ")
        if numar_validat(numar, baza) == False:
            raise ValueError(f"{numar} nu este un numar in baza {baza}")
        precizie = int(input("Introduceti un numarul de zecimale de dupa virgula pe care sa il aiba rezultatul: "))
        if precizie < 0 or precizie > 15:
            raise ValueError(f"Precizia trebuie sa fie intre 0 - 15")
        result = conversie_substitutie(numar, baza, precizie)
        print(f"{numar}({baza}) = {result}(10)")
    except ValueError as e:
        print(f"Va rugam introduceti date valide. Eroare: {e}")

def conversie_baza_intermediare_ui():
    try:
        baza_initiala = int(input("Va rugam introduceti o baza initiala: "))
        if baza_initiala > 16 or baza_initiala < 0:
            raise ValueError(f"Bazele trebuie sa fie =< 16. {baza_initiala} > 16")
        numar = input("Introduceti un numar in baza initiala: ")
        if numar_validat(numar, baza_initiala) == False:
            raise ValueError(f"{numar} nu este un numar in baza {baza_initiala}")
        baza_finala = int(input("Va rugam introduceti o baza finala: "))
        if baza_finala > 16 or baza_finala < 0:
            raise ValueError(f"Bazele trebuie sa fie =< 16. {baza_finala} > 16")
        precizie = int(input("Introduceti un numarul de zecimale de dupa virgula pe care sa il aiba rezultatul: "))
        if precizie < 0 or precizie > 15:
            raise ValueError(f"Precizia trebuie sa fie intre 0 - 15")
        result = conversie_baza_intermediara(numar, baza_initiala, baza_finala, precizie)
        print(f"{numar}({baza_initiala}) = {result}({baza_finala})")
    except ValueError as e:
        print(f"Va rugam introduceti date valide. Eroare: {e}")

def adunare_baza_ui():
    try:
        baza = int(input("Va rugam introduceti o baza: "))
        numar1 = input(f"Va rugam introduceti primul numar in baza {baza}: ")
        if numar_validat(numar1, baza) == False:
            raise ValueError(f"{numar1} nu este un numar in baza {baza}")
        numar2 = input(f"Va rugam introduceti al doilea numar in baza {baza}: ")
        if numar_validat(numar2, baza) == False:
            raise ValueError(f"{numar2} nu este un numar in baza {baza}")
        result = adunare_baza(numar1, numar2, baza)
        print (f"{numar1}({baza}) + {numar2}({baza}) = {result}({baza})")
    except ValueError as e:
        print(f"Va rugam introduceti date valide. Eroare: {e}")

def scadere_baza_ui():
    try:
        baza = int(input("Va rugam introduceti o baza: "))
        print("Preconditie: numar1 < numar2")
        numar1 = input(f"Va rugam introduceti primul numar in baza {baza}: ")
        if numar_validat(numar1, baza) == False:
            raise ValueError(f"{numar1} nu este un numar in baza {baza}")
        numar2 = input(f"Va rugam introduceti al doilea numar in baza {baza}: ")
        if numar_validat(numar2, baza) == False:
            raise ValueError(f"{numar2} nu este un numar in baza {baza}")
        if (bigger_equal(numar1, numar2) == False):
            raise ValueError(f"{numar1} < {numar2}. Preconditie incalcata.")
        result = scadere_baza(numar1, numar2, baza)
        print (f"{numar1}({baza}) - {numar2}({baza}) = {result}({baza})")
    except ValueError as e:
        print(f"Va rugam introduceti date valide. Eroare: {e}")

def inmultire_baza_ui():
    try:
        baza = int(input("Va rugam introduceti o baza: "))
        numar1 = input(f"Va rugam introduceti primul numar in baza {baza}: ")
        if numar_validat(numar1, baza) == False:
            raise ValueError(f"{numar1} nu este un numar in baza {baza}")
        numar2 = input(f"Va rugam introduceti o cifra in baza {baza}: ")
        if numar_validat(numar2, baza) == False:
            raise ValueError(f"{numar2} nu este un numar in baza {baza}")
        result = inumultire_baza(numar1, numar2, baza)
        print (f"{numar1}({baza}) * {numar2}({baza}) = {result}({baza})")
    except ValueError as e:
        print(f"Va rugam introduceti date valide. Eroare: {e}")

def impartire_baza_ui():
    try:
        baza = int(input("Va rugam introduceti o baza: "))
        numar1 = input(f"Va rugam introduceti primul numar in baza {baza}: ")
        if numar_validat(numar1, baza) == False:
            raise ValueError(f"{numar1} nu este un numar in baza {baza}")
        numar2 = input(f"Va rugam introduceti o cifra in baza {baza}: ")
        if numar_validat(numar2, baza) == False:
            raise ValueError(f"{numar2} nu este un numar in baza {baza}")
        result, rest = impartire_baza(numar1, numar2, baza)
        print (f"{numar1}({baza}) : {numar2}({baza}) = {result}({baza}), rest = {rest}({baza})")
    except ValueError as e:
        print(f"Va rugam introduceti date valide. Eroare: {e}")

def run():
    while True:
        meniu_principal()
        optiune = input("Va rugam alegeti una dintre aceste optiuni: ")
        match optiune:
            case '1':
                meniu_conversii_baze()
                optiune1 = input("Va rugam alegeti una dintre aceste optiuni: ")
                match optiune1:
                    case '1':
                        conversie_impartiri_succesive_ui()
                    case '2':
                        conversie_substitutie_ui()
                    case '3':
                        conversie_baza_intermediare_ui()
                    case _:
                        print ("Va rugam introduceti o optiune valida")
            case '2':
                conversii_rapide_ui()
            case '3':
                meniu_operatii_aritmetice()
                optiune3 = input("Va rugam alegeti una dintre aceste optiuni: ")
                match optiune3:
                    case '1':
                        adunare_baza_ui()
                    case '2':
                        scadere_baza_ui()
                    case '3':
                        inmultire_baza_ui()
                    case '4':
                        impartire_baza_ui()
                    case _:
                        print ("Va rugam introduceti o optiune valida")
            case '4':
                print ("Iesire...")
                break
            case _:
                print ("Va rugam introduceti o optiune valida")

