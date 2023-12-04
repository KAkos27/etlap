def kerdes(szoveg):
    valasz: str = str(input(szoveg))
    while not((valasz =="i") or (valasz =="I") or (valasz =="n") or (valasz =="N")):
        print("Rossz betűt adtál meg!")
        valasz: str = str(input(szoveg))
    return valasz

def rendfelvetel(etel_lista,rendszoveg,):
        rend_lista = []
        print("Kérlek add meg a rendelni kívánt étel számát. Írj 0-át, ha már nem kérsz többet")
        rendindex:int = int(input(rendszoveg))
        while rendindex != 0:
            rend_lista.append(etel_lista[rendindex-1])
            rendindex:int = int(input(rendszoveg))
        return rend_lista

def arkereses(rend_lista,lista,ar_lista):
    rend_ar_lista = []
    for a in range(0,len(rend_lista),1):
        for i in range(0,len(lista),1):
            if rend_lista[a] == lista[i]:
                rend_ar_lista.append(ar_lista[i])
        i = 0
    return rend_ar_lista

def szamolas(rend_ar_lista):
    osszeg = 0
    for i in range(0,len(rend_ar_lista),1):
        osszeg += rend_ar_lista[i]
    return osszeg


def rendeles(fo_lista,fo_ar_lista,koret_lista,koret_ar_lista,desz_lista,desz_ar_lista,etlap_meret):
    foetelszoveg:str="Szeretnél főételt?(I/N): "
    foetelrendszoveg:str="Melyik főételt szeretnéd?: "
    koretrendszoveg:str="Melyik köretet szeretnéd?: "
    deszrendszoveg:str="Melyik desszertet szeretnéd?: "
    desszertszoveg:str="Szeretnél desszertet?(I/N): "
    reszosszeg:int = 0
    vegosszeg:float = 0

    igennem:str=kerdes(foetelszoveg)
    print("-" * etlap_meret)

    if igennem == "i" or igennem == "I":
        frend_lista = rendfelvetel(fo_lista,foetelrendszoveg)

        if len(frend_lista) > 0:
            print("-" * etlap_meret)
            krend_lista = []
            print(f"Válassz {len(frend_lista)} köretet!")

            for i in range(0,len(frend_lista),1):
                rendindex:int = int(input(koretrendszoveg))
                krend_lista.append(koret_lista[rendindex-1])
                
    
    digennem:str=kerdes(desszertszoveg)
    print("-" * etlap_meret)

    if digennem == "i" or digennem == "I":
        drend_lista=rendfelvetel(desz_lista,deszrendszoveg)
    
    input("Nyugta nyomtatáshoz üss egy entert!")

    if len(frend_lista) > 0:
        frend_ar_lista = arkereses(frend_lista,fo_lista,fo_ar_lista)
        krend_ar_lista = arkereses(krend_lista,koret_lista,koret_ar_lista)
        freszosszeg = szamolas(frend_ar_lista)
        kreszosszeg = szamolas(krend_ar_lista)

    drend_ar_lista = arkereses(drend_lista,desz_lista,desz_ar_lista)

    
    dreszosszeg = szamolas(drend_ar_lista)

    reszosszeg = freszosszeg + kreszosszeg + dreszosszeg
    vegosszeg = reszosszeg*1.15

    print(reszosszeg)
    print(vegosszeg)




