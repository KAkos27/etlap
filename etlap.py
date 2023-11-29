def jelsor(jel,db):
    print(jel*db)

def szoveg_ar(szoveg, ar, etlap_meret):
    print(f"{szoveg}{ar:>{etlap_meret-len(szoveg)}}")

def cimsor(jel, szoveg, jel2, etlap_meret):
    hossz: int= etlap_meret - (len(jel) + len(jel2))
    print(f"{jel}{szoveg:^{hossz}}{jel}")

