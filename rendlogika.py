import metodusok
import etlap
import math

def rendeles(fo_lista,fo_ar_lista,koret_lista,koret_ar_lista,desz_lista,desz_ar_lista,etlap_meret):
    foetelszoveg:str="Szeretnél főételt?(I/N): "
    foetelrendszoveg:str="Melyik főételt szeretnéd?: "
    koretrendszoveg:str="Melyik köretet szeretnéd?: "
    deszrendszoveg:str="Melyik desszertet szeretnéd?: "
    desszertszoveg:str="Szeretnél desszertet?(I/N): "
    frend_lista = []
    krend_lista = []
    drend_lista = []
    freszosszeg:int = 0
    kreszosszeg:int = 0
    dreszosszeg:int = 0
    reszosszeg:int = 0
    vegosszeg:float = 0

    igennem:str=metodusok.kerdes(foetelszoveg)
    etlap.jelsor("-",etlap_meret)

    if igennem == "i" or igennem == "I":
        frend_lista = metodusok.rendfelvetel(fo_lista,foetelrendszoveg)

        if len(frend_lista) > 0:
            etlap.jelsor("-",etlap_meret)
            krend_lista = []
            print(f"Válassz {len(frend_lista)} köretet!")

            for i in range(0,len(frend_lista),1):
                rendindex:int = int(input(koretrendszoveg))
                while rendindex > len(koret_lista) or rendindex <= 0:
                    print("Hiba! Nincs ilyen köret")
                    rendindex:int = int(input(koretrendszoveg))

                krend_lista.append(koret_lista[rendindex-1])
            etlap.jelsor("-",etlap_meret)
                
    
    digennem:str=metodusok.kerdes(desszertszoveg)
    etlap.jelsor("-",etlap_meret)

    if digennem == "i" or digennem == "I":
        drend_lista=metodusok.rendfelvetel(desz_lista,deszrendszoveg)
    
    input("Nyugta nyomtatáshoz üss egy entert!")

    if len(frend_lista) == 0 and len(drend_lista) == 0:
        etlap.cimsorkiiras("NYUGTA",etlap_meret,"=")
        print("Nem rendeltél semmit")
    elif len(frend_lista) != 0 and len(drend_lista) != 0:
        frend_ar_lista = metodusok.arkereses(frend_lista,fo_lista,fo_ar_lista)
        krend_ar_lista = metodusok.arkereses(krend_lista,koret_lista,koret_ar_lista)
        drend_ar_lista = metodusok.arkereses(drend_lista,desz_lista,desz_ar_lista)
        freszosszeg = metodusok.szamolas(frend_ar_lista)
        kreszosszeg = metodusok.szamolas(krend_ar_lista)
        dreszosszeg = metodusok.szamolas(drend_ar_lista)
        etlap.cimsorkiiras("NYUGTA",etlap_meret,"=")
        etlap.kiiras(frend_lista,frend_ar_lista,etlap_meret)
        etlap.jelsor("-",etlap_meret)
        etlap.kiiras(krend_lista,krend_ar_lista,etlap_meret)
        etlap.jelsor("-",etlap_meret)
        etlap.kiiras(drend_lista,drend_ar_lista,etlap_meret)
    elif len(frend_lista) != 0 and len(drend_lista) == 0:
        frend_ar_lista = metodusok.arkereses(frend_lista,fo_lista,fo_ar_lista)
        krend_ar_lista = metodusok.arkereses(krend_lista,koret_lista,koret_ar_lista)
        freszosszeg = metodusok.szamolas(frend_ar_lista)
        kreszosszeg = metodusok.szamolas(krend_ar_lista)
        etlap.cimsorkiiras("NYUGTA",etlap_meret,"=")
        etlap.kiiras(frend_lista,frend_ar_lista,etlap_meret)
        etlap.jelsor("-",etlap_meret)
        etlap.kiiras(krend_lista,krend_ar_lista,etlap_meret)
    elif len(frend_lista) == 0 and len(drend_lista) !=0:
        drend_ar_lista = metodusok.arkereses(drend_lista,desz_lista,desz_ar_lista)
        dreszosszeg = metodusok.szamolas(drend_ar_lista)  
        etlap.cimsorkiiras("NYUGTA",etlap_meret,"=")
        etlap.kiiras(drend_lista,drend_ar_lista,etlap_meret) 

    etlap.jelsor("=",etlap_meret)

    reszosszeg = freszosszeg + kreszosszeg + dreszosszeg
    szervizdij = math.floor(reszosszeg*0.1)
    vegosszeg = reszosszeg + szervizdij

    etlap.szoveg_ar("Összesen:",str(reszosszeg)+" Ft",etlap_meret)
    etlap.szoveg_ar("Szervízdíj:",str(szervizdij) +" Ft",etlap_meret)
    etlap.jelsor("-",etlap_meret)
    etlap.szoveg_ar("Fizetendő:",str(vegosszeg)+" Ft",etlap_meret)
    
    



