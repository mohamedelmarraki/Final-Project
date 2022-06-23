import folium
import pandas as pd
from geopy.geocoders import Nominatim
import time
import math
import ee
import geemap.foliumap as geemap
import glob
import plotly.express as px





def map_dirección_usuario(adress = "Madrid", zoom_start1 = 17.5):
    
    geo = Nominatim(user_agent = "MyApp")


    loc = geo.geocode(adress)

    coordenadas = loc.latitude, loc.longitude
    
    tooltip = loc
    
    m = folium.Map(location=[coordenadas[0],coordenadas[1]], zoom_start=zoom_start1)
    
    html=f"""
        <div style="font-family: times new roman; color: blue">
        <h><b> {tooltip} </b></h></div>
        """
    iframe = folium.IFrame(html=html, width=600, height=53)
    popup = folium.Popup(iframe, max_width=2650)
    
    marker = folium.Marker(location=[coordenadas[0],coordenadas[1]], 
                           popup=popup,
                           icon=folium.Icon(color="black",icon="home"),
).add_to(m)

    m.save('map.html')
    
    return m


def energía_generador_fotovoltaico(N_paneles):
    import pandas
    
    csv_files = glob.glob('../../Downloads/*.csv')
    
    csv_pvgis =("").join(csv_files).split("/")[-1]
    
    df = pandas.read_csv(f'../../Downloads/{csv_pvgis}', sep="\t", header=[4]).head(12)
    
    df = df.loc[:, ["year", "month","H(i_opt)_m", "T2m"]]
    
    irrandiacia_zona = ((df["H(i_opt)_m"]) * 1000)/31
    
    HSP = irrandiacia_zona / 1000
    
    energía_generada = (HSP * N_paneles * 450)/1000
    
    df_potencia = pd.DataFrame(energía_generada).rename(columns={"H(i_opt)_m" : "Energía Generada en Kwh"})

    df_concat = pd.concat([df["month"], df_potencia], axis =1)
    
    fig = px.bar(df_concat, x = "month", y = "Energía Generada en Kwh", title="Producción de energía eléctrica mensualmente")
    
    return fig



def obtener_amortización(Numero_paneles):
    a = pd.read_csv("data/Datos de amortización.csv")
    if Numero_paneles ==0:
        return a[(a["Número de paneles"] == 0) & (a["Potencia del Inversor"]==0)]
    if Numero_paneles ==1:
        return a[(a["Número de paneles"] == 4) & (a["Potencia del Inversor"]==2)]
    if Numero_paneles ==2:
        return a[(a["Número de paneles"] == 4) & (a["Potencia del Inversor"]==2)]
    if Numero_paneles ==3:
        return a[(a["Número de paneles"] == 4) & (a["Potencia del Inversor"]==2)]
    if Numero_paneles ==4:
        return a[(a["Número de paneles"] == Numero_paneles) & (a["Potencia del Inversor"]==2)]
    if Numero_paneles ==5:
        return a[(a["Número de paneles"] == Numero_paneles) & (a["Potencia del Inversor"]==3)]
    if Numero_paneles ==6:
        return a[(a["Número de paneles"] == Numero_paneles) & (a["Potencia del Inversor"]==3)]
    if Numero_paneles ==7:
        return a[(a["Número de paneles"] == Numero_paneles) & (a["Potencia del Inversor"]==4)]
    if Numero_paneles ==8:
        return a[(a["Número de paneles"] == Numero_paneles) & (a["Potencia del Inversor"]==4)]
    if Numero_paneles ==9:
        return a[(a["Número de paneles"] == Numero_paneles) & (a["Potencia del Inversor"]==5)]
    if Numero_paneles ==10:
        return a[(a["Número de paneles"] == Numero_paneles) & (a["Potencia del Inversor"]==5)]
    if Numero_paneles ==11:
        return a[(a["Número de paneles"] == Numero_paneles) & (a["Potencia del Inversor"]==5)]
    if Numero_paneles ==12:
        return a[(a["Número de paneles"] == Numero_paneles) & (a["Potencia del Inversor"]==6)]
    if Numero_paneles ==13:
        return a[(a["Número de paneles"] == Numero_paneles) & (a["Potencia del Inversor"]==6)]
    if Numero_paneles ==14:
        return a[(a["Número de paneles"] == Numero_paneles) & (a["Potencia del Inversor"]==7)]
    if Numero_paneles ==15:
        return a[(a["Número de paneles"] == Numero_paneles) & (a["Potencia del Inversor"]==7)]
    if Numero_paneles ==16:
        return a[(a["Número de paneles"] == Numero_paneles) & (a["Potencia del Inversor"]==8)]
    if Numero_paneles ==17:
        return a[(a["Número de paneles"] == Numero_paneles) & (a["Potencia del Inversor"]==8)]
    if Numero_paneles ==18:
        return a[(a["Número de paneles"] == Numero_paneles) & (a["Potencia del Inversor"]==9)]
    if Numero_paneles ==19:
        return a[(a["Número de paneles"] == Numero_paneles) & (a["Potencia del Inversor"]==9)]
    if Numero_paneles ==20:
        return a[(a["Número de paneles"] == Numero_paneles) & (a["Potencia del Inversor"]==9)]
    if Numero_paneles ==21:
        return a[(a["Número de paneles"] == Numero_paneles) & (a["Potencia del Inversor"]==9)]
    if Numero_paneles ==22:
        return a[(a["Número de paneles"] == Numero_paneles) & (a["Potencia del Inversor"]==9)]
    if Numero_paneles >22:
        return a[(a["Número de paneles"] == 22) & (a["Potencia del Inversor"]==9)]
