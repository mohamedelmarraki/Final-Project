import folium
import pandas as pd
from geopy.geocoders import Nominatim
import time
import math
import ee
import geemap.foliumap as geemap
import glob
import plotly.express as px



def map_dirección_usuario(adress):
    
    geo = Nominatim(user_agent = "MyApp")


    loc = geo.geocode(adress)

    coordenadas = loc.latitude, loc.longitude
    
    m = folium.Map(location=[coordenadas[0],coordenadas[1]], zoom_start=17.5)

    tooltip = loc
    
    marker = folium.Marker(location=[coordenadas[0],coordenadas[1]], 
                       tooltip=f"<b>{tooltip}</b><br><br>", 
                       popup='<h1>Happy&nbsp;New&nbsp;Year!</h1><br><br>www:&nbsp;<a href="https://stackoverflow.com">Stackoverflow.com</a><br><br>date:&nbsp;2021.01.01')
    marker.add_to(m)

    m.save('map.html')
    
    return m




ee.Authenticate()

# Create an interactive map
Map = geemap.Map(plugin_Draw=True, Draw_export=False)
# Add a basemap
Map.add_basemap("TERRAIN")
# Retrieve Earth Engine dataset
dem = ee.Image("USGS/SRTMGL1_003")
# Set visualization parameters
vis_params = {
    "min": 0,
    "max": 4000,
    "palette": ["006633", "E5FFCC", "662A00", "D8D8D8", "F5F5F5"],
}
# Add the Earth Engine image to the map
Map.addLayer(dem, vis_params, "SRTM DEM", True, 0.5)
# Add a colorbar to the map
Map.add_colorbar(vis_params["palette"], 0, 4000, caption="Elevation (m)")
# Render the map using streamlit
Map.to_streamlit()




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