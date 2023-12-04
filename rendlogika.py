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
    print("-" * etlap_meret)

    if igennem == "i" or igennem == "I":
        frend_lista = metodusok.rendfelvetel(fo_lista,foetelrendszoveg)

        if len(frend_lista) > 0:
            print("-" * etlap_meret)
            krend_lista = []
            print(f"Válassz {len(frend_lista)} köretet!")

            for i in range(0,len(frend_lista),1):
                rendindex:int = int(input(koretrendszoveg))
                krend_lista.append(koret_lista[rendindex-1])
                
    
    digennem:str=metodusok.kerdes(desszertszoveg)
    print("-" * etlap_meret)

    if digennem == "i" or digennem == "I":
        drend_lista=metodusok.rendfelvetel(desz_lista,deszrendszoveg)
    
    input("Nyugta nyomtatáshoz üss egy entert!")

    if len(frend_lista) == 0 and len(drend_lista) == 0:
        print("Nem rendeltél semmit")
    elif len(frend_lista) != 0 and len(drend_lista) != 0:
        frend_ar_lista = metodusok.arkereses(frend_lista,fo_lista,fo_ar_lista)
        krend_ar_lista = metodusok.arkereses(krend_lista,koret_lista,koret_ar_lista)
        drend_ar_lista = metodusok.arkereses(drend_lista,desz_lista,desz_ar_lista)
        freszosszeg = metodusok.szamolas(frend_ar_lista)
        kreszosszeg = metodusok.szamolas(krend_ar_lista)
        dreszosszeg = metodusok.szamolas(drend_ar_lista)
    elif len(frend_lista) != 0 and len(drend_lista) == 0:
        frend_ar_lista = metodusok.arkereses(frend_lista,fo_lista,fo_ar_lista)
        krend_ar_lista = metodusok.arkereses(krend_lista,koret_lista,koret_ar_lista)
        freszosszeg = metodusok.szamolas(frend_ar_lista)
        kreszosszeg = metodusok.szamolas(krend_ar_lista)
    elif len(frend_lista) == 0 and len(drend_lista) !=0:
        drend_ar_lista = metodusok.arkereses(drend_lista,desz_lista,desz_ar_lista)
        dreszosszeg = metodusok.szamolas(drend_ar_lista)   
   
    reszosszeg = freszosszeg + kreszosszeg + dreszosszeg
    vegosszeg = math.floor(reszosszeg*1.15)

    print(reszosszeg)
    print(vegosszeg)




