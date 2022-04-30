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
    
    csv_files = glob.glob('../../../Downloads/*.csv')
    
    csv_pvgis =("").join(csv_files).split("/")[-1]
    
    df = pandas.read_csv(f'../../../../mohamedelmarraki/Downloads/{csv_pvgis}', sep="\t", header=[4]).head(12)
    
    df = df.loc[:, ["year", "month","H(i_opt)_m", "T2m"]]
    
    irrandiacia_zona = ((df["H(i_opt)_m"]) * 1000)/31
    
    HSP = irrandiacia_zona / 1000
    
    energía_generada = (HSP * N_paneles * N_paneles)/1000
    
    df_potencia = pd.DataFrame(energía_generada).rename(columns={"H(i_opt)_m" : "Energía Generada en Kwh"})

    df_concat = pd.concat([df["month"], df_potencia], axis =1)
    
    return fig.show()