def conversii_rapide_2_4(val: str):
    while len(val) % 2 != 0:
        val = "0" + val
    
    result = ""
    for i in range (0, len(val), 2):
        grup = val[i:i+2]
        match grup:
            case "00":
                result += "0"
            case "01":
                result += "1"
            case "10":
                result += "2"
            case "11":
                result += "3"
    return result

def conversii_rapide_2_8(val: str):
    while len(val) % 3 != 0:
        val = "0" + val
    result = ""
    for i in range (0, len(val), 3):
        grup = val[i:i+3]
        match grup:
            case "000":
                result += "0"
            case "001":
                result += "1"
            case "010":
                result += "2"
            case "011":
                result += "3"
            case "100":
                result += "4"
            case "101":
                result += "5"
            case "110":
                result += "6"
            case "111":
                result += "7"
    return result

def conversii_rapide_2_16(val: str):
    while len(val) % 4 != 0:
        val = "0" + val
    result = ""
    for i in range (0, len(val), 4):
        grup = val[i:i+4]
        match grup:
            case "0000":
                result += "0"
            case "0001":
                result += "1"
            case "0010":
                result += "2"
            case "0011":
                result += "3"
            case "0100":
                result += "4"
            case "0101":
                result += "5"
            case "0110":
                result += "6"
            case "0111":
                result += "7"
            case "1000":
                result += "8"
            case "1001":
                result += "9"
            case "1010":
                result += "A"
            case "1011":
                result += "B"
            case "1100":
                result += "C"
            case "1101":
                result += "D"
            case "1110":
                result += "E"
            case "1111":
                result += "F"
    return result

def conversii_rapide_4_16(val: str):
    while len(val) % 2 != 0:
        val = "0" + val
    result = ""
    for i in range (0, len(val), 2):
        grup = val[i:i+2]
        match grup:
            case "00":
                result += "0"
            case "01":
                result += "1"
            case "02":
                result += "2"
            case "03":
                result += "3"
            case "10":
                result += "4"
            case "11":
                result += "5"
            case "12":
                result += "6"
            case "13":
                result += "7"
            case "20":
                result += "8"
            case "21":
                result += "9"
            case "22":
                result += "A"
            case "23":
                result += "B"
            case "30":
                result += "C"
            case "31":
                result += "D"
            case "32":
                result += "E"
            case "33":
                result += "F"
    return result

def conversii_rapide_4_2(val: str):
    result = ""
    for i in range(0, len(val)):
        match val[i]:
            case "0":
                result += "00"
            case "1":
                result += "01"
            case "2":
                result += "10"
            case "3":
                result += "11"
    result = result.lstrip("0")
    return result

def conversii_rapide_8_2(val: str):
    result = ""
    for i in range(0, len(val)):
        match val[i]:
            case "0":
                result += "000"
            case "1":
                result += "001"
            case "2":
                result += "010"
            case "3":
                result += "011"
            case "4":
                result += "100"
            case "5":
                result += "101"
            case "6":
                result += "110"
            case "7":
                result += "111"
    result = result.lstrip("0")
    return result

def conversii_rapide_16_2(val: str):
    result = ""
    for i in range(0, len(val)):
        match val[i].upper():
            case "0":
                result += "0000"
            case "1":
                result += "0001"
            case "2":
                result += "0010"
            case "3":
                result += "0011"
            case "4":
                result += "0100"
            case "5":
                result += "0101"
            case "6":
                result += "0110"
            case "7":
                result += "0111"
            case "8":
                result += "1000"
            case "9":
                result += "1001"
            case "A":
                result += "1010"
            case "B":
                result += "1011"
            case "C":
                result += "1100"
            case "D":
                result += "1101"
            case "E":
                result += "1110"
            case "F":
                result += "1111"
    result = result.lstrip("0")
    return result

def conversii_rapide_16_4(val: str):
    result = ""
    for i in range(0, len(val)):
        match val[i].upper():
            case "0":
                result += "00"
            case "1":
                result += "01"
            case "2":
                result += "02"
            case "3":
                result += "03"
            case "4":
                result += "10"
            case "5":
                result += "11"
            case "6":
                result += "12"
            case "7":
                result += "13"
            case "8":
                result += "20"
            case "9":
                result += "21"
            case "A":
                result += "22"
            case "B":
                result += "23"
            case "C":
                result += "30"
            case "D":
                result += "31"
            case "E":
                result += "32"
            case "F":
                result += "33"
    result = result.lstrip("0")
    return result

def adunare_baza(val1: str, val2: str, baza: int):
    val1 = val1[::-1]
    val2 = val2[::-1]
    n = max(len(val1), len(val2))
    result = ""
    t = 0
    for i in range (n):
        if i < len(val1):
            val1_curent = conversie_zecimala(val1[i])
        else:
            val1_curent = 0
        if i < len(val2):
            val2_curent = conversie_zecimala(val2[i])
        else:
            val2_curent = 0
        suma = val1_curent + val2_curent + t
        cifra = suma % baza
        t = suma // baza
        result += conversie_numar_litera(cifra)
    if t != 0:
        result += conversie_numar_litera(t)
    result = result[::-1]
    return result

def scadere_baza(val1: str, val2: str, baza: int):
    val1 = val1[::-1]
    val2 = val2[::-1]
    n = max(len(val1), len(val2))
    result = ""
    t = 0
    for i in range (n):
        if i < len(val1):
            val1_curent = conversie_zecimala(val1[i])
        else:
            val1_curent = 0
        if i < len(val2):
            val2_curent = conversie_zecimala(val2[i])
        else:
            val2_curent = 0
        diferenta = val1_curent - val2_curent - t
        if diferenta >= 0:
            cifra = diferenta
            t = 0
        else:
            cifra = diferenta + baza
            t = 1
        result += conversie_numar_litera(cifra)
    result = result[::-1]
    return result

def inumultire_baza(val1: str, val2: str, baza: int):
    val2 = conversie_zecimala(val2)
    val1 = val1[::-1]
    result = ""
    t = 0
    for i in range (len(val1)):
        val1_curent = conversie_zecimala(val1[i])
        produs = val1_curent * val2 + t
        cifra = produs % baza
        t = produs // baza
        result += conversie_numar_litera(cifra)
    if t > 0:
        result += conversie_numar_litera(t)
    result = result[::-1]
    result = result.lstrip("0")
    return result

def impartire_baza(val1: str, val2: str, baza: int):
    val2 = conversie_zecimala(val2)
    result = ""
    t = 0
    for i in range (len(val1)):
        val1_curent = conversie_zecimala(val1[i])
        deimp = t * baza + val1_curent
        cifra = deimp // val2
        t = deimp % val2
        result += conversie_numar_litera(cifra)
    rest = conversie_numar_litera(t)
    result = result.lstrip("0")
    if result == "":
         result = "0"
    return result, rest

def conversie_zecimala(cif):
    cifre = "0123456789ABCDEF"
    cif = cif.upper()
    if cif in cifre:
        return cifre.index(cif)
    else:
        raise ValueError(f"Se accepta doar numere in bazele 2-16. {cif} nu este valida.")

def conversie_substitutie(val: str, baza_initiala, precizie: int):
    """
    Converteste un numar val din baza initiala in baza 10 prin substitutie
    :param val: numarul care trebuie convertit, este de forma "12345,6789"
    :param baza_initiala: baza in care este numarul de convertit
    :return: numarul in baza 10
    """
    if "," in val:
        partea_intreaga_str, partea_fractionara_str = val.split(",", 1)
    else:
        partea_intreaga_str = val
        partea_fractionara_str = ""
    # partea_intreaga_str = partea_intreaga_str[::-1]
    partea_intreaga = 0
    putere = 0
    for cif in reversed(partea_intreaga_str):
        if cif == "":
            continue
        cif_curenta = conversie_zecimala(cif)
        partea_intreaga += cif_curenta * (baza_initiala ** putere)
        putere += 1
    partea_fractionara = Fraction(0, 1)
    putere = 1
    for cif in partea_fractionara_str:
        cif_curenta = conversie_zecimala(cif)
        partea_fractionara += Fraction(cif_curenta, baza_initiala ** putere)
        putere += 1
    # result = str(partea_intreaga + partea_fractionara)
    # result = str(result)
    result = Fraction(partea_intreaga, 1) + partea_fractionara
    # result = result.replace(".", ",")
    partea_int = result.numerator // result.denominator
    rest = result.numerator % result.denominator
    if rest == 0:
        return str(partea_int)
    zecimale = []
    for i in range(precizie):
        rest *= 10
        cifra = rest // result.denominator
        rest = rest % result.denominator
        zecimale.append(str(cifra))
        if rest == 0:
            break
    return str(partea_int) + "," + "".join(zecimale)

from fractions import Fraction

def conversie_numar_litera(numar):
    litere = "ABCDEF"
    if numar < 10:
        return str(numar)
    numar -= 10
    return litere[numar]

def conversie_baza_intermediara(val: str, baza_initiala: int, baza_finala: int, precizie: int):
    """
    Convertim prima oara pe val din baza initiala in baza 10, ca mai apoi sa il convertim in baza finala
    :param val: valoarea numarului
    :param baza_initiala: baza in care se afla numarul val initial
    :param baza_finala: baza in care in convertim pe val
    :return: val convertit in baza finala
    """
    result_baza_10 = conversie_substitutie(val, baza_initiala, precizie)
    if "," not in result_baza_10:
        partea_intreaga_10 = int(result_baza_10)
        partea_fractionara_10 = ""
    else:
        partea_intreaga_10, partea_fractionara_10 = result_baza_10.split(",")
        partea_intreaga_10 = int(partea_intreaga_10)
        partea_fractionara_10 = int(partea_fractionara_10) / (10 ** len(partea_fractionara_10))

    partea_intreaga = ""
    partea_fractionara = ""
    if partea_intreaga_10 == 0:
            partea_intreaga = "0"
    else:
        while partea_intreaga_10 != 0:
            rest = partea_intreaga_10 % baza_finala
            partea_intreaga_10 //= baza_finala
            partea_intreaga += str(conversie_numar_litera(rest))
        partea_intreaga = partea_intreaga[::-1]

    for i in range(precizie):
        partea_fractionara_10 *= baza_finala
        p_intreaga = int(partea_fractionara_10)
        partea_fractionara_10 -= p_intreaga
        partea_fractionara += str(conversie_numar_litera(p_intreaga))

    if partea_fractionara != "":
        result = partea_intreaga + "," + partea_fractionara
    else:
        result = partea_intreaga
    return result

def numar_validat(val, baza: int):
    for c in str(val):
        if c != ',' and conversie_zecimala(c) >= baza:
            return False
    return True

def bigger_equal (val1: str, val2: str):
    if len(val1) > len(val2):
        return True
    if len(val1) < len(val2):
        return False
    for i in range(len(val1)):
        if val1[i] < val2[i]:
            return False
    return True


def conversie_impartiri_succesive(val: str, baza_initiala: int, baza_finala: int):
    """
    Converteste valoarea val din baza initiala in baza finala
    :param val: valoarea de convertit
    :param baza_initiala: baza initiala
    :param baza_finala: baza finala
    :return: numarul convertit in baza finala (str)
    """
    numar_10 = 0
    putere = 0
    for cif in reversed(val):
        cif_curenta = conversie_zecimala(cif)
        numar_10 += cif_curenta * (baza_initiala ** putere)
        putere += 1
    if numar_10 == 0:
        return "0"
    rezultat = ""
    while numar_10 > 0:
        rest = numar_10 % baza_finala
        numar_10 //= baza_finala
        rezultat += conversie_numar_litera(rest)
    return rezultat[::-1]
