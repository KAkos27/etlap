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
            while rendindex > len(etel_lista) or rendindex < 0:
                print("Hiba! Nincs ilyen étel az étlapon.")
                rendindex:int = int(input(rendszoveg))
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
