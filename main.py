import etlap
etlap_meret: int = 36
halar: int = 1590
husar: int = 1660
fagyiar: int = 1270
browniear: int = 1490

#ETLAP

etlap.jelsor("*", etlap_meret)
etlap.cimsor("*","FŐÉTELEK","*", etlap_meret)
etlap.jelsor("*", etlap_meret)

etlap.szoveg_ar("Hal", str(halar) + " Ft", etlap_meret)
etlap.szoveg_ar("Hús", str(husar) + " Ft", etlap_meret)

etlap.jelsor("*", etlap_meret)
etlap.cimsor("*","DESSZERTEK","*", etlap_meret)
etlap.jelsor("*", etlap_meret)

etlap.szoveg_ar("Fagyi", str(fagyiar) + " Ft", etlap_meret)
etlap.szoveg_ar("Browniear", str(browniear) + " Ft", etlap_meret)

etlap.jelsor("=", etlap_meret)

#RENDELÉS/SZÁMOLÁS

import modulok
modulok.rendeles(halar,husar,fagyiar,browniear,etlap_meret)



