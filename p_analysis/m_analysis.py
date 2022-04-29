import pandas
import re
import json



archivo_iberdrola = "../data/datos_iberdrola.txt"
def iberdrola_trans(archivo):

    archi1=open(archivo,"r")
    
    potencia_electro1=archi1.read()
    
    archi1.close()
    
    potencia_electro1 = potencia_electro1.split("\n")
    
    potencia_electro1_list1 = []
    
    for i in potencia_electro1:
        i = i.replace("-", "")
        i = i.replace(":", "")
        i = i.replace(".", "")
        i = i.replace("  ", " ")
        potencia_electro1_list1.append(re.split('\s|(?<!\d)[,.](?!\d)', i))
        
    potencia_electro1_list2 = []
    
    for i in potencia_electro1_list1:
        if i[0] == 'Aire':
            i[0] = 'Aire acondicionado'
            del i[1]
        potencia_electro1_list2.append(i)
   
    df1 = pandas.DataFrame(potencia_electro1_list2)
    
    df1.drop([3], axis=1, inplace=True)
    
    return df1




archivo_bajapotencia = "../data/datos_bajapotencia.txt"
def bajapotencia_trans(archivo):
    
    archi2=open(archivo,"r")
    
    potencia_electro2=archi2.read()
    
    archi2.close()
    
    potencia_electro2 = potencia_electro2.split("\n")
    potencia_electro2 = potencia_electro2[7:-1]
    
    potencia2 = []
    
    for i in potencia_electro2:
        i = i.split("(")
        potencia2.append(i)
        
    potencia2a = []
    
    for i in potencia2:
        potencia2a.append(re.split('\s|(?<!\d)[,.](?!\d)', i[0]))
        
    potencia2b = []
    
    for i in potencia2a:
        if i[0] == 'Aire':
            i[0] = 'Aire acondicionado'
            del i[1]
        elif i[0] == "Calefacción":
            i[0] = 'Calefacción eléctrica'
            del i[1]
        potencia2b.append(i)
    
    
    df2 = pandas.DataFrame(potencia2b)
    
    df2.drop([2, 5], axis=1, inplace=True)
    df2.drop([0], axis=0, inplace=True)
    
    df2.rename(columns={3:2, 4:3}, inplace=True)
    
    df2.drop([3], axis=1, inplace=True)
    
    return df2




archivo_electricaplicada ="../data/datos_electricaplicada.txt"
def electricaplicada_trans(archivo):
    
    archi3=open(archivo,"r")
    
    potencia_electro3=archi3.read()
    
    archi3.close()
    
    x = re.split("esenciales.", str(potencia_electro3), 1)
    
    x = x[1]
    
    x = x.split("\n")
    
    lista = []
    
    for i in x:
        if re.findall("[1-9]", i):
            lista.append(i)
            
    lista2 = []
    
    for i in lista:
        if "–" not in i and "*" not in i and  "/" not in i and  "(" not in i and "-" not in i:
            lista2.append(i)
            
    potencia_electro3 = lista2[:-2]
    
    potencia_electro3[0] = "Licuadora 500W"
    
    lista3 = []
    
    for i in potencia_electro3:
        lista3.append(list(i.rpartition(" ")))
    
    df3 = pandas.DataFrame(lista3)
    
    df3 = df3.iloc[[0, 2, 7, 18, 23, 42]]
    
    lista4 = []
    
    for i in df3[2]:
        lista4.append(i.replace("W", ""))
        
    df3[3] = lista4
    
    df3.drop([1, 2], axis=1, inplace=True)

    
    return df3




def pot_electrodomesticos(df1, df2, df3):
    
    df_conc = pandas.concat([df1, df2], axis=0)
    
    df_conc.drop([5],axis=0, inplace=True)
    
    df_conc[[1, 2]] = df_conc[[1, 2]].apply(pandas.to_numeric)
    
    df_conc[3] = df_conc[[1, 2]].median(axis=1)
    
    df_conc.drop([1,2], axis=1, inplace=True)
    
    df_conc2 = pandas.concat([df_conc, df3], axis=0)
    
    df_conc2.reset_index(inplace=True)
    
    df_conc2.drop("index", axis=1, inplace=True)
    
    df_conc2 = df_conc2.rename(columns={0: 'Electrodomesticos', 3: 'Potencia'})
    
    df_conc2["Potencia"] = df_conc2["Potencia"].apply(pandas.to_numeric)
    
    pot_electrodomesticos = {k: v for k, v in zip(list(df_conc2["Electrodomesticos"]), list(df_conc2["Potencia"]))}
    
    tf = open("../data/pot_electrodomesticos.json", "w")
    
    json.dump(pot_electrodomesticos,tf)
    
    tf.close()

def read_datos_provincias():
    import pandas as pd
    datos_provinicias = pd.read_csv("data/Datos da cada provincia Española.csv")
    datos_provinicias.drop("Unnamed: 0", axis=1, inplace=True)
    datos_provinicias.drop(0, axis=0, inplace=True)
    diccionario = {}
    for provincia, informacion in zip(datos_provinicias["Provincias"], datos_provinicias["Información de cada Provincia"]):
        diccionario[provincia]=informacion
    return diccionario
