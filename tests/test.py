from domain.manager import *
def test_all():
    test_adunare_baza_p()
    test_scadere_baza_p()
    test_inmultire_baza_b()
    test_impartire_baza_b()
    test_conversii_rapide_2_4()
    test_conversii_rapide_2_8()
    test_conversii_rapide_2_16()
    test_conversii_rapide_4_2()
    test_conversii_rapide_4_16()
    test_conversii_rapide_8_2()
    test_conversii_rapide_16_2()
    test_conversii_rapide_16_4()
    test_conversie_substitutie()
    test_conversie_baza_intermediara()
    test_conversie_impartiri_succesive()

def test_adunare_baza_p():
    result = adunare_baza("123450", "3FE2", 16)
    assert result == "127432"
    result = adunare_baza("FFFFEC1111", "555CB88", 16)
    assert result == "1000541DC99"
    result = adunare_baza("285539809ABBB", "90048297395", 16)
    assert result == "28E53E0331F50"
    result = adunare_baza("285539809ABBB", "90048297395", 12)
    assert result == "2925424376394"
    result = adunare_baza("14124331232", "23141334", 5)
    assert result == "14203023121"

def test_scadere_baza_p():
    result = scadere_baza("14124331232", "23141334", 5)
    assert result == "14101134343"
    result = scadere_baza("1153AAAFBCCCBEEEE8", "23141334AABABAFF", 16)
    assert result == "1130969C88220433E9"
    result = scadere_baza("1153AAAFBCCCBEEEE8AABBABBABAEEEFFCCCDDDD", "1133248AAAEEEFFFCCCEEE", 16)
    assert result == "1153AAAFBCCCBEEEE8998887300FFFFFFD000EEF"
    result = scadere_baza("425FFAAADDDD1428745BBABBABAEEEFFCCC24536658576435", "1133248AAAEEEFFFCCCEEE", 16)
    assert result == "425FFAAADDDD1428745BBABBABADDBCD841796476588A9547"
    result = scadere_baza("AABBC425897104974AACAACC", "489373063ABC", 13)
    assert result == "AABBC42589708903A7A67010"

def test_inmultire_baza_b():
    result = inumultire_baza("AABBC425897104974AACAACC", "5", 13)
    assert result == "4227797C248951A8AB22C22C8"
    result = inumultire_baza("AABBC425897104974AACAACC", "5", 16)
    assert result == "355AAD4BBAF3516F4755F55FC"
    result = inumultire_baza("AABBAC39839478857685344545543563456746354", "7", 16)
    assert result == "4AB21B592990F4BA63DA46DE4E54D75B6E5D2EB74C"
    result = inumultire_baza("456746354", "9", 16)
    assert result == "270A177DF4"
    result = inumultire_baza("134542356354330939EDEDECEDECEEDECDEABBAFAFA", "3", 16)
    assert result == "39CFC6A029FC991BADC9C9C6C9C6CC9C69C0330F0EE"

def test_impartire_baza_b():
    cat, rest = impartire_baza("134542356354330939EDEDECEDECEEDECDEABBAFAFA", "3", 16)
    assert cat == "66C6B67211C1103134F4F4EF9F9A4F4EF4E3E8FE53"
    assert rest == "1"
    cat, rest = impartire_baza("CEDECEEDECDEABBAFAFA", "9", 16)
    assert cat == "16FC4FE18C18BDBF7138"
    assert rest == "2"
    cat, rest = impartire_baza("69524425543567654325364757654CEDECEEDECDEABBAAA", "9", 15)
    assert cat == "B088C1DDDC090C58C03DAA774258D19D4B9ED4B847E97C"
    assert rest == "7"
    cat, rest = impartire_baza("69654325364757654BAAA", "5", 12)
    assert cat == "14383305A3815B13596B9"
    assert rest == "1"
    cat, rest = impartire_baza("6654325364757654251245341345434536", "7", 9)
    assert cat == "858303308358733157805817818443204"
    assert rest == "5"

def test_conversii_rapide_2_4():
    result = conversii_rapide_2_4("1101010101010110101010110")
    assert result == "1222222311112"
    result = conversii_rapide_2_4("1101010101")
    assert result == "31111"
    result = conversii_rapide_2_4("11010101010101111010101010100010101011010101")
    assert result == "3111111322222202223111"
    result = conversii_rapide_2_4("11110000001111110000011000011110101011010101")
    assert result == "3300033300120132223111"
    result = conversii_rapide_2_4("101001010101101010000011110101011010101")
    assert result == "11022231100132223111"

def test_conversii_rapide_2_8():
    result = conversii_rapide_2_8("101001010101101010000011110101011010101")
    assert result == "5125520365325"
    result = conversii_rapide_2_8("1110101011111010101001011010101")
    assert result == "16537251325"
    result = conversii_rapide_2_8("1110101011010101011010101111010101101")
    assert result == "1653253257255"
    result = conversii_rapide_2_8("111011010110101010101010")
    assert result == "73265252"
    result = conversii_rapide_2_8("11111110101010101010101")
    assert result == "37652525"

def test_conversii_rapide_2_16():
    result = conversii_rapide_2_16("1110101011111010101001011010101")
    assert result == "757D52D5"
    result = conversii_rapide_2_16("10101101010101010101010")
    assert result == "56AAAA"
    result = conversii_rapide_2_16("1101010001100001011111111110101")
    assert result == "6A30BFF5"
    result = conversii_rapide_2_16("110101011011111011011111010111010110001101111111011010100110")
    assert result == "D5BEDF5D637F6A6"
    result = conversii_rapide_2_16("1111110111101111111000111110100111111000110")
    assert result == "7EF7F1F4FC6"

def test_conversii_rapide_4_2():
    result = conversii_rapide_4_2("12221303102130030231330122033231301")
    assert result == "110101001110011010010011100001100101101111100011010001111101101110001"
    result = conversii_rapide_4_2("1213130131012010310200310301001033032222302")
    assert result == "1100111011100011101000110000100110100100000110100110001000001001111001110101010110010"
    result = conversii_rapide_4_2("3203030223")
    assert result == "11100011001100101011"
    result = conversii_rapide_4_2("233230302011020303020230302030302010")
    assert result == "101111101100110010000101001000110011001000101100110010001100110010000100"
    result = conversii_rapide_4_2("122202000333030302203020203202030200222003")
    assert result == "11010100010000000111111001100110010100011001000100011100010001100100000101010000011"

def test_conversii_rapide_4_16():
    result = conversii_rapide_4_16("1222310131010131203032322030222")
    assert result == "1AB47447633BA32A"
    result = conversii_rapide_4_16("33310030223212302323020232012321230212302123")
    assert result == "FD0CAE6CBB22E1B9B26C9B"
    result = conversii_rapide_4_16("1333333333323232021023210210230212010")
    assert result == "1FFFFFBB892E492C984"
    result = conversii_rapide_4_16("203020302030120110201232")
    assert result == "8C8C8C61486E"
    result = conversii_rapide_4_16("12323121221201203210222")
    assert result == "1BB66986392A"

def test_conversii_rapide_8_2():
    result = conversii_rapide_8_2("13434567654322345605432123045432123405654302")
    assert result == "1011100011100101110111110101100011010010011100101110000101100011010001010011000100101100011010001010011100000101110101100011000010"
    result = conversii_rapide_8_2("7654353654674524042563054104563054340763524142536")
    assert result == "111110101100011101011110101100110111100101010100000100010101110011000101100001000100101110011000101100011100000111110011101010100001100010101011110"
    result = conversii_rapide_8_2("656473560405345647654654063040504506504")
    assert result == "110101110100111011101110000100000101011100101110100111110101100110101100000110011000100000101000100101000110101000100"
    result = conversii_rapide_8_2("54366476354115213243534250604305052")
    assert result == "101100011110110100111110011101100001001101010001011010100011101011100010101000110000100011000101000101010"
    result = conversii_rapide_8_2("35353532424535444444553404320204050504030")
    assert result == "11101011101011101011010100010100101011101100100100100100100101101011100000100011010000010000100000101000101000100000011000"

def test_conversii_rapide_16_2():
    result = conversii_rapide_16_2("14905ABEDDCECDABABADCEECEDFED24225")
    assert result == "1010010010000010110101011111011011101110011101100110110101011101010111010110111001110111011001110110111111110110100100100001000100101"
    result = conversii_rapide_16_2("192433ABCDEEFDDBABA24905342")
    assert result == "110010010010000110011101010111100110111101110111111011101101110101011101000100100100100000101001101000010"
    result = conversii_rapide_16_2("24044091ABBEFF32059ABBDEBE39095")
    assert result == "10010000000100010000001001000110101011101111101111111100110010000001011001101010111011110111101011111000111001000010010101"
    result = conversii_rapide_16_2("AB344B244225DEDEFE")
    assert result == "101010110011010001001011001001000100001000100101110111101101111011111110"
    result = conversii_rapide_16_2("ABBDBEBFB34503923")
    assert result == "10101011101111011011111010111111101100110100010100000011100100100011"

def test_conversii_rapide_16_4():
    result = conversii_rapide_16_4("ABBDBEBFB34503923")
    assert result == "2223233123322333230310110003210203"
    result = conversii_rapide_16_4("19342490AFFEEEDDFDEDCAA")
    assert result == "121031002102100223333323232313133313231302222"
    result = conversii_rapide_16_4("2494AAFEEDFEEEEAAADD")
    assert result == "210211022223332323133323232322222223131"
    result = conversii_rapide_16_4("2490940ADEEEDDFEDDEDFFC209438095")
    assert result == "210210021100022313232323131333231313231333330020021100320002111"
    result = conversii_rapide_16_4("AADD249025994DDDEDDEFDC130408935")
    assert result == "2222313102102100021121211031313132313132333130010300100020210311"

def test_conversie_substitutie():
    result = conversie_substitutie("110010010101,01010110", 2, 7)
    assert result == "3221,3359375"
    result = conversie_substitutie("110010010101,01010110", 5, 7)
    assert result == "58672526,0416768"
    result = conversie_substitutie("AAF24903509,012059ADE", 16, 10)
    assert result == "11747348985097,0043998765"
    result = conversie_substitutie("AA0439094923,02582103A", 12, 10)
    assert result == "8051111840043,0171765912"
    result = conversie_substitutie("130492831209A49,14254425", 11, 10)
    assert result == "484699144853735,1258382991"
    result = conversie_substitutie("13042831204,14254425", 9, 10)
    assert result == "4669733596,1640751916"
    result = conversie_substitutie("13244343423545434543,14343423", 6, 10)
    assert result == "961353586229535,2952335533"

def test_conversie_baza_intermediara():
    result = conversie_baza_intermediara("0101010101,101001", 2, 3, 10)
    assert result == "110122,1220220001"
    result = conversie_baza_intermediara("10100202044344523,100310240", 6, 3, 11)
    assert result == "101021020222101202212120020,01112002121"
    result = conversie_baza_intermediara("12390434394,AB3483", 12, 4, 12)
    assert result == "1010301311000000200,322112100211"
    result = conversie_baza_intermediara("94292509ABECDE234538309,95902583ABDBEBDDFE", 16, 7, 12)
    assert result == "241101651313424252124523065214111,404251110102"
    result = conversie_baza_intermediara("2534312536543142563543,42543425365434253", 9, 16, 11)
    assert result == "F69E4F9D7093723C7,7A0696FBFB2"
    result = conversie_baza_intermediara("1324324543423,033143143", 6, 13, 10)
    assert result == "4291066CB,138767C510"
    result = conversie_baza_intermediara("AABB204420543ABB320524,4504842", 14, 2, 20)
    assert result == "101001110000100010110110100111111000111001100011110100010101001101011000011111110100,01001111101101000011"
    result = conversie_baza_intermediara("AABB204420543ABB320524", 14, 2, 0)
    assert result == "101001110000100010110110100111111000111001100011110100010101001101011000011111110100"
    result = conversie_baza_intermediara("1324324543423", 6, 13, 0)
    assert result == "4291066CB"
    result = conversie_baza_intermediara("2534312536543142563543", 9, 16, 0)
    assert result == "F69E4F9D7093723C7"
    result = conversie_baza_intermediara("0101010101", 2, 3, 0)
    assert result == "110122"

def test_conversie_impartiri_succesive():
    result = conversie_impartiri_succesive("1039821342", 10, 16)
    assert result == "3DFA6A1E"
    result = conversie_impartiri_succesive("1039821342", 11, 16)
    assert result == "910EE5EB"
    result = conversie_impartiri_succesive("130243132ABABA39024", 12, 9)
    assert result == "265858884182326066031"
    result = conversie_impartiri_succesive("1324534", 8, 16)
    assert result == "5A95C"
    result = conversie_impartiri_succesive("312424", 5, 2)
    assert result == "10100001111100"

test_all()