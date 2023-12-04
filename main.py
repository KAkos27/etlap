import etlap
import rendlogika

etlap_meret: int = 36

fo_lista=["Rántott pisztráng","Rib-eye Steak","Roston csirkemell","Grillezet tofu"]
fo_ar_lista=[2390,2760,2290,2560]

koret_lista=["Rízs","Krumplipüré","Steak burgonya"]
koret_ar_lista=[400,470,510]

desz_lista=["Tiramisu","Pisztácia kulfi","Brownie"]
desz_ar_lista=[1790,1580,1990]


etlap.cimsorkiiras("FŐÉTELEK",etlap_meret,"*")

etlap.kiiras(fo_lista,fo_ar_lista,etlap_meret)

etlap.cimsorkiiras("KÖRETEK",etlap_meret,"*")

etlap.kiiras(koret_lista,koret_ar_lista,etlap_meret)

etlap.cimsorkiiras("DESSZERTEK",etlap_meret,"*")

etlap.kiiras(desz_lista,desz_ar_lista,etlap_meret)
etlap.jelsor("=", etlap_meret)


rendlogika.rendeles(fo_lista,fo_ar_lista,koret_lista,koret_ar_lista,desz_lista,desz_ar_lista,etlap_meret)



