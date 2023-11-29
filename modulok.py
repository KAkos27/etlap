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


def rendeles(fo_lista,fo_ar_lista,koret_lista,koret_ar_lista,desz_lista,desz_ar_lista,etlap_meret):
    foetelszoveg:str="Szeretnél főételt?(I/N): "
    foetelrendszoveg:str="Melyik főételt szeretnéd?: "
    koretrendszoveg:str="Melyik köretet szeretnéd?: "
    deszrendszoveg:str="Melyik desszertet szeretnéd?: "
    desszertszoveg:str="Szeretnél desszertet?(I/N): "

    igennem:str=kerdes(foetelszoveg)
    print("-" * etlap_meret)

    if igennem == "i" or igennem == "I":
        frend_lista = rendfelvetel(fo_lista,foetelrendszoveg)
        if len(frend_lista) > 0:
            print("-" * etlap_meret)
            krend_lista = rendfelvetel(koret_lista,koretrendszoveg)
    
    digennem:str=kerdes(desszertszoveg)
    print("-" * etlap_meret)

    if digennem == "i" or digennem == "I":
        drend_lista=rendfelvetel(desz_lista,deszrendszoveg)
    
    print(frend_lista)
    print(krend_lista)
    print(drend_lista)
    input("Nyugta nyomtatáshoz üss egy entert!")
    





