import json


def electro_usuario():
    
    import json
    
    tf = open("../data/pot_electrodomesticos.json", "r")
    
    electro_dict = json.load(tf)
    
    electrodomesticos = list(electro_dict.keys())
    
    print("Previsión de Energía consumida")
    
    print("Si quiere salir del programa introduce la palabra 'salir'")
    
    print("\n")
    
    horas_func = {}
    
    unidades = {}
    
    
    for i in range(len(electrodomesticos)):
        nueva = input(f"¿ Tiene usted {electrodomesticos[i]} en su casa (Sí/No) ? ")
        if nueva.lower() in ["si".lower(), "sí".lower()]:
            unidad = input(f'¿ Cúantas unidades de {electrodomesticos[i]} tiene usted en su casa ? ')
            horas = input(f"Introduce un estimación aproximada de las horas de funcionamiento que va a tener el(a) {electrodomesticos[i]} en los días que esté funcionando : ")
            horas_func[electrodomesticos[i]]=horas
            unidades[electrodomesticos[i]] = unidad
        elif nueva.lower() == "salir":
            break
            
    return horas_func, unidades

'''diccionarios = electro_usuario()
horas_func = diccionarios[0]
unidades = diccionarios[1]'''




def Numero_paneles():
    
    import numpy
    
    import pandas
    
    from itertools import chain
    
    from collections import defaultdict
    
    import json

    tf = open("../data/pot_electrodomesticos.json", "r")
    
    pot_electrodomesticos = json.load(tf)
    
    
    
    lista = []
    
    for i in horas_func.keys():
        lista.append(i)

    potencia = dict(filter(lambda x: x[0] in lista, pot_electrodomesticos.items()))

    dict3 = defaultdict(list)
    
    for k, v in chain(horas_func.items(), unidades.items(), potencia.items()):
        dict3[k].append(int(v))
    dic_final = dict(dict3)

    dic_final2 = {}
    
    lis = []
    
    for i, y in dic_final.items():
        dic_final2[i] = numpy.prod(y)
        
    for i in dic_final2.values():
        a = (i/7)
        lis.append(a)
        print(a)

    consumo_teorico = sum(lis)

    consumo_diario= consumo_teorico/(0.95)

    suma_de_potencia = 0
    
    for i in potencia.values():
        suma_de_potencia  += i
        
    Potencia_Prevista = suma_de_potencia*0.75 
    
    if Potencia_Prevista > 10000:
        print("la instalación necesitará Proyecto de un Ingeniero")
        
    else:
        print("la instalación necesitará una Memoria Técnica de Diseño (MTD) de un Técnico electricista.")
    
    if Potencia_Prevista < 1500:
        tensión = 12
        
    elif 1500 <= Potencia_Prevista < 5000:
        tensión = 48
        
    elif Potencia_Prevista > 5000:
        tensión = 120
    
    csv_files = glob.glob('../../../Downloads/*.csv')
    
    csv_pvgis =("").join(csv_files).split("/")[-1]
    
    df = pandas.read_csv(f'../../../../../Downloads/{csv_pvgis}', sep="\t", header=[4]).head(12)
    
    df = df.loc[:, ["year", "month","H(i_opt)_m", "T2m"]]
    
    irrandiacia_zona = ((df["H(i_opt)_m"].min()) * 1000)/31
    
    HSP = irrandiacia_zona / 1000
    
    energía_producirá_día = HSP * 450 * 0.9
    
    Numero_paneles = consumo_diario / energía_producirá_día
    
    print(consumo_diario)
    
    Numero_paneles = round(Numero_paneles+0.5)
    
    return Numero_paneles




def Numero_paneles_consumo_mensual():
    
    import numpy
    
    import pandas
    
    import glob
    
    consumo_teorico = (int(input("Introduce el consumo eléctrico medio mensual")))
    
    consumo_diario= consumo_teorico*1000/31/(0.95)
    
    csv_files = glob.glob('../../../Downloads/*.csv')
    
    csv_pvgis =("").join(csv_files).split("/")[-1]
    
    df = pandas.read_csv(f'../../../../mohamedelmarraki/Downloads/{csv_pvgis}', sep="\t", header=[4]).head(12)
    
    df = df.loc[:, ["year", "month","H(i_opt)_m", "T2m"]]
    
    irrandiacia_zona = ((df["H(i_opt)_m"].min()) * 1000)/31
    
    HSP = irrandiacia_zona / 1000
    
    energía_producirá_día = HSP * 450 * 0.9
    
    Numero_paneles = consumo_diario / energía_producirá_día
    
    print(Numero_paneles)
    
    Numero_paneles = round(Numero_paneles+0.5)
    
    return Numero_paneles
