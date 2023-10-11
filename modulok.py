import etlap
nyugta_meret = 24
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
    etlap.szoveg_ar("Szervízdíj", str(szervizdij) + " Ft", nyugta_meret)

    etlap.jelsor("_", nyugta_meret)

    print("")
    etlap.szoveg_ar("Fizetendő", str(fizetendo) + " Ft", nyugta_meret)

    etlap.jelsor("_", nyugta_meret)


def rendeles(halar,husar,fagyiar,browniear):
    igennem: str = str(input("Szeretnél-e előételt?(I/N)"))

    mennyiseg=0
    dmennyiseg=0

    desszert_ar=0
    eloetel_ar=0

    if igennem == "I":
        mennyiseg: int = int(input("Hány előételt szeretnél?"))

        print("Hal --- 1\nHús --- 2")
        eloetel_fajta: int = int(input("Melyik előételt szeretné?"))

        if eloetel_fajta == 1:
            eloetel_ar = halar
            print("Halat válaszott --",halar)
        elif eloetel_fajta == 2:
            eloetel_ar = husar


        digennem: str = str(input("Szeretnél-e desszertet?(I/N)"))
        if digennem == "I":
            dmennyiseg: int = int(input("Hány desszertet szeretnél?"))

            print("Fagyi --- 1\nBrownie --- 2")
            dfajta: int = int(input("Melyik desszertet szeretné?"))

            if dfajta == 1:
                desszert_ar = fagyiar
            elif dfajta == 2:
                desszert_ar = browniear

        elif digennem == "N":
            print("Nem kértél desszertet")
        else:
            print("Rosszbbetűt adtál meg")
    elif igennem == "N":
        digennem: str = str(input("Szeretnél-e desszertet?(I/N)"))
        if digennem == "I":
            dmennyiseg: int = int(input("Hány desszertet szeretnél?"))
        elif digennem == "N":
            print("Nem kértél desszertet")
        else:
            print("Rosszbbetűt adtál meg")
    else:
        print("Rossz betűt adtál meg")

    szamolas(eloetel_ar, mennyiseg, desszert_ar, dmennyiseg)





