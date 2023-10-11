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

    etlap.szoveg_ar("Összese n", str(osszesen) + " Ft", nyugta_meret)
    etlap.szoveg_ar("Szervízdíj", str(math.trunc(int(szervizdij))) + " Ft", nyugta_meret)

    etlap.jelsor("_", nyugta_meret)

    print("")
    etlap.szoveg_ar("Fizetendő", str(math.trunc(int(fizetendo))) + " Ft", nyugta_meret)

    etlap.jelsor("_", nyugta_meret)


def rendeles(halar,husar,fagyiar,browniear,nyugta_meret):
    igennem: str = str(input("Szeretnél-e előételt?(I/N) "))
    print("-" * nyugta_meret)

    mennyiseg=0
    dmennyiseg=0

    desszert_ar=0
    eloetel_ar=0

    if igennem == "I":
        print("Igent választottál")
        print("-" * nyugta_meret)
        mennyiseg: int = int(input("Hány előételt szeretnél? "))
        print("-" * nyugta_meret)
        
        print("Hal --- 1\nHús --- 2")
        eloetel_fajta: int = int(input("Melyik előételt szeretnéd? "))

        if eloetel_fajta == 1:
            eloetel_ar = halar
            print("-" * nyugta_meret)
            print(mennyiseg,"db Halat válaszott --",eloetel_ar* mennyiseg,"Ft")
            print("-" * nyugta_meret)
        elif eloetel_fajta == 2:
            eloetel_ar = husar
            print("-" * nyugta_meret)
            print(mennyiseg,"db Húst válaszott --",eloetel_ar* mennyiseg,"Ft")
            print("-" * nyugta_meret)


        digennem: str = str(input("Szeretnél-e desszertet?(I/N) "))
        print("-" * nyugta_meret)

        if digennem == "I":
            print("Igent választottál")
            print("-" * nyugta_meret)
            dmennyiseg: int = int(input("Hány desszertet szeretnél? "))
            print("-" * nyugta_meret)

            print("Fagyi --- 1\nBrownie --- 2")
            dfajta: int = int(input("Melyik desszertet szeretnéd? "))

            if dfajta == 1:
                desszert_ar = fagyiar
                print("-" * nyugta_meret)
                print(dmennyiseg,"db Fagyit válaszott --",desszert_ar*dmennyiseg,"Ft")
                print("-" * nyugta_meret)
            elif dfajta == 2:
                desszert_ar = browniear
                print("-" * nyugta_meret)
                print(dmennyiseg,"db Borwnie-t válaszott --",desszert_ar*dmennyiseg,"Ft")
                print("-" * nyugta_meret)

        elif digennem == "N":
            print("Nem kértél desszertet")
            print("-" * nyugta_meret)
        else:
            print("Rosszbbetűt adtál meg")
    elif igennem == "N":
        print("Nem kértél előételt")
        print("-" * nyugta_meret)
        digennem: str = str(input("Szeretnél-e desszertet?(I/N) "))
        print("-" * nyugta_meret)
        if digennem == "I":
            print("Igent választottál")
            print("-" * nyugta_meret)
            dmennyiseg: int = int(input("Hány desszertet szeretnél? "))
            print("-" * nyugta_meret)

            print("Fagyi --- 1\nBrownie --- 2")
            dfajta: int = int(input("Melyik desszertet szeretnéd? "))

            if dfajta == 1:
                desszert_ar = fagyiar
                print("-" * nyugta_meret)
                print(dmennyiseg,"db Fagyit válaszott --",desszert_ar*dmennyiseg,"Ft")
                print("-" * nyugta_meret)
            elif dfajta == 2:
                desszert_ar = browniear
                print("-" * nyugta_meret)
                print(dmennyiseg,"db Borwnie-t válaszott --",desszert_ar*dmennyiseg,"Ft")
                print("-" * nyugta_meret)
        elif digennem == "N":
            print("Nem kértél semmit")
            print("-" * nyugta_meret)
        else:
            print("Rosszbbetűt adtál meg")
                    
    else:
        print("Rossz betűt adtál meg")

    input("Nyugta nyomtatáshoz üss egy entert!")
    szamolas(eloetel_ar, mennyiseg, desszert_ar, dmennyiseg)





