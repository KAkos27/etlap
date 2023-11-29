import etlap, math
nyugta_meret = 36
def szamolas(eloetel_ar, mennyiseg, desszert_ar, dmennyiseg):
    osszesen=(eloetel_ar* mennyiseg)+(desszert_ar*dmennyiseg)
    szervizdij=(osszesen*0.1)
    fizetendo=(osszesen+szervizdij)

    #NYUGTA
    print("")
    print("")
    print("")
    etlap.jelsor("*", nyugta_meret)
    etlap.cimsor("*","NYUGTA","*", nyugta_meret)
    etlap.jelsor("*", nyugta_meret)

    etlap.szoveg_ar("Tétel1", str(eloetel_ar* mennyiseg) + " Ft", nyugta_meret)
    etlap.szoveg_ar("Tétel2", str(desszert_ar*dmennyiseg) + " Ft", nyugta_meret)

    etlap.jelsor("=", nyugta_meret)

    etlap.szoveg_ar("Összesen", str(osszesen) + " Ft", nyugta_meret)
    etlap.szoveg_ar("Szervízdíj", str(math.trunc(int(szervizdij))) + " Ft", nyugta_meret)

    etlap.jelsor("_", nyugta_meret)

    print("")
    etlap.szoveg_ar("Fizetendő", str(math.trunc(int(fizetendo))) + " Ft", nyugta_meret)

    etlap.jelsor("_", nyugta_meret)

def kerdes(szoveg):
    valasz: str = str(input(szoveg))
    while not((valasz =="i") or (valasz =="I") or (valasz =="n") or (valasz =="N")):
        print("Rossz betűt adtál meg!")
        valasz: str = str(input(szoveg))
    return valasz



def rendeles(fo_lista,fo_ar_lista,koret_lista,koret_ar_lista,desz_lista,desz_ar_lista,etlap_meret):
    mennyiseg=0
    dmennyiseg=0

    eloetel_ar=0
    desszert_ar=0

    eloetelszoveg:str="Szeretnél előételt?(I/N)"
    desszertszoveg:str="Szeretnél desszertet?(I/N)"

    igennem:str=kerdes(eloetelszoveg)
    print("-" * etlap_meret)

   

    digennem: str =kerdes(desszertszoveg)
    print("-" * etlap_meret)

        
    input("Nyugta nyomtatáshoz üss egy entert!")
    szamolas(eloetel_ar, mennyiseg, desszert_ar, dmennyiseg)





