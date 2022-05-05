from p_acquisition import m_acquisition as mac
from p_analysis import m_analysis as man
from p_reporting import m_reporting as mre
from p_wrangling import m_wrangling as mwr


import pandas as pd # importar la librería pandas

import streamlit as st

import numpy as np # importar la librería numpy

import requests # importar la librería requests

from selenium import webdriver # Habrá que descargar el webdriver de chrome para realizar las distintas operaciones

from selenium.webdriver.support.ui import WebDriverWait # Cuando cargamos una página web a veces el HTML tarda un poco en cargarse sugún nuestra velocidad de conexión pues hasta ciertos elementos no carguen tendremos que esperar

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.action_chains import ActionChains

import cv2

import matplotlib.pyplot as plt

import numpy as np

import time

import re

import json

import os

from geopy.geocoders import Nominatim

import time

import math

import folium

from geopy.geocoders import Nominatim

import ee

import geemap.foliumap as geemap

import glob

import plotly.express as px

from IPython.display import Javascript

import warnings

from PIL import Image

from streamlit_folium import folium_static

import folium

st.set_page_config(layout="wide")


#Definir el título

col1, col2, col3 = st.columns([2,6,1])

with col1:
    st.write("")

with col2:
    st.title('Calcule su instalación fotovoltaica')

with col3:
    st.write("")


col1, col2, col3 = st.columns(3)

col1, col2, col3 = st.columns([1,6,1])

with col1:
    st.write("")

with col2:
    st.image("https://postgradoindustrial.com/wp-content/uploads/energia-solar-termica.jpg")

with col3:
    st.write("")


col1, col2, col3 = st.columns(3)

with col1:
    st.image("Images/foto1.png")
    st.subheader('AHORRO EN TU FACTURA')
    st.caption("Con la energía que producirás y la compensación de excedentes podrás reducir tu factura hasta un 70%.")



with col2:
    st.image("Images/foto2.png")
    st.subheader('ENERGÍA 100% VERDE')
    st.caption("Contribuyes a cuidar el planeta, reduciendo hasta 80 tonelada de CO2 en 25 años, equivalente a plantar 320 árboles.")

with col3:
    st.image("Images/foto3.png")
    st.subheader('AYUDAS Y SUBVENCIONES')
    st.caption("Reduce el coste de la instalación hasta en un 50% gracias a subvenciones o reducciones en el pago del IBI.")
    
for i in range(5):
    st.write("")
    
col1, col2, col3, col4, col5 = st.columns([1,3,3,1,3])    
with col1:
    for i in range(4):
        st.write("")
    st.image("Images/foto10.png")
    for i in range(7):
        st.write("")
with col2:
    for i in range(3):
        st.write("")
    st.subheader('*ESTUDIO GRATUITO*')
    st.caption("***Resolvemos todas tus dudas sobre el autoconsumo y estudiamos tu situación para ofrecerte una solución 100% personalizada.***")
    for i in range(5):
        st.write("")
with col1:
    for i in range(4):
        st.write("")
    st.image("Images/foto12.png")
    for i in range(7):
        st.write("")
with col2:
    for i in range(3):
        st.write("")
    st.subheader('*PRESUPUESTO SIN COMPROMISO*')
    st.caption("***Diseñamos un presupuesto con la mejor calidad y el precio más bajo del mercado. Trabajamos con todas las marcas de paneles e inversores.***")
    for i in range(5):
        st.write("")

with col1:
    for i in range(4):
        st.write("")
    st.image("Images/foto13.png")
with col2:
    for i in range(3):
        st.write("")
    st.subheader('*MEMORIA Y LICENCIA*')
    st.caption("***Olvídate de todos los trámites. Nosotros nos encargamos de realizar la memoria y solicitar la licencia de obra menor para la instalación fotovoltaica.***")
    
with col3:
    st.image("Images/foto11.png")


with col4:
    for i in range(4):
        st.write("")
    st.image("Images/foto14.png")
    for i in range(7):
        st.write("")
with col5:
    for i in range(3):
        st.write("")
    st.subheader('*INSTALACIÓN Y PUESTA EN MARCHA*')
    st.caption("***Nuestro personal está cualificado y tiene años de experiencia en instalaciones de autoconsumo. Todo quedará listo para generar tu energía.***")
    for i in range(5):
        st.write("")
with col4:
    for i in range(4):
        st.write("")
    st.image("Images/foto15.png")
    for i in range(7):
        st.write("")
with col5:
    for i in range(3):
        st.write("")
    st.subheader('*BOLETÍN Y LEGALIZACIÓN*')
    st.caption("***Emitiremos un boletín y realizaremos todos los trámites para la legalización de la instalación ante industria y la distribuidora.***")
    for i in range(5):
        st.write("")

with col4:
    for i in range(4):
        st.write("")
    st.image("Images/foto16.png")
with col5:
    for i in range(3):
        st.write("")
    st.subheader('*EXCEDENTES*')
    st.caption("***Olvídate de todos los trámites. Nosotros nos encargamos de realizar la memoria y solicitar la licencia de obra menor para la instalación fotovoltaica.***")
    

for i in range(10):
    st.write("")
col1, col2, col3 = st.columns([1,6,1])

with col1:
    st.write("")

with col2:
    st.markdown("# Nos adaptamos al tipo de instalación que necesites")

with col3:
    st.write("")
    
    
    
col1, col2, col3 = st.columns([4,6,2])

with col1:
    st.write("")

with col2:
    st.caption("## Donde hay sol, hay energía. Aprovéchala.")

with col3:
    st.write("")


col1, col2, col3, col4  = st.columns(4)

with col1:
    st.image("Images/foto4.png")
    st.subheader('Viviendas conectadas a red')
    st.caption("Aumenta mensualmente tu ahorro gracias a la compensación de excedentes hasta reducir a 0 el coste de consumo eléctrico.")



with col2:
    st.image("Images/foto5.png")
    st.subheader('Comunidad de vecinos')
    st.caption("Reduce el coste general de la luz en tu comunidad e incluso la factura de todos los vecinos con el autoconsumo compartido.")

with col3:
    st.image("Images/foto6.png")
    st.subheader('Empresas')
    st.caption("Si dispones de un negocio ahora puedes ahorrar un 70% en tu factura de luz, aumentando así tus beneficios.")

with col4:
    st.image("Images/foto7.png")
    st.subheader('Viviendas Aisladas')
    st.caption("Para clientes que quieren desconectarse de la red eléctrica usando su propia energía acompañada de baterías.")


for i in range(5):
    st.write("")
    
col1, col2, col3 = st.columns([2,6,2])
with col2:
    st.markdown("### Rellene la información solicitada a continuación si quiere realizar un cálculo aproximado de la instalación solar fotovoltaica para autoconsumo de su vivienda o negocio. También podrá ver el coste de su intalción y cuanto tiempo tardará en amortizarla, también tendrá una estimación de la energía que producirá su instalación durante todo el año.")
    for i in range(5):
        st.write("")

col1, col2 = st.columns(2)
with col1:
    agree = st.checkbox('Sé mi consumo medio mensual?')
    with st.expander(' ¿Cómo puedo averiguar mi consumo medio mensual?'):
            st.image('Images/foto8.png')


with col2:
    agree2 = st.checkbox('Calcular mi consumo medio mensual?')
    with st.expander(' ¿Comó se calcula mi consumo mensual?'):
            st.markdown('#### Si conocemos los electrodomésticos que se usarán en la vivienda exactamente, entonces se sumarán los consumos diarios de cada uno de los electrodomésticos (receptores).')

col1, col2 = st.columns(2)

if agree:
    with col2:
        adress=st.text_input("Introduzca su dirección. Ejem: Calle Zaragoza, Fuenlabrada, Madrid")
        provincia_usuario = adress.split(",")
        if len(provincia_usuario) == 3:
            provincia_usuario = provincia_usuario[2]
            provincia_usuario = provincia_usuario.lower().strip()
            diccionario = man.read_datos_provincias()
            for i, y in diccionario.items():
                if provincia_usuario == i.lower():
                    st.write(y)
                else:
                    pass
        elif len(provincia_usuario) == 2:
            provincia_usuario = provincia_usuario[1]
            provincia_usuario = provincia_usuario.lower().strip()
            diccionario = man.read_datos_provincias()
            for i, y in diccionario.items():
                if provincia_usuario == i.lower():
                    st.write(y)
                else:
                    pass
        elif len(provincia_usuario) == 1:
            pass

    with col1:
        if adress == "":
            folium_static(mre.map_dirección_usuario("Madrid", zoom_start1=2))
        else:
            folium_static(mre.map_dirección_usuario(adress))


    with col2:
        consumo_mensual=st.number_input("Introduzca su Consumo eléctrico medio mensual")
        Precio=st.number_input("Introduzca su Precio de compra de la Electricidad (Opcional)")
        with st.expander(' ¿Cómo puedo averiguar mi consumo medio mensual?'):
            st.image('Images/foto9.png')
        if st.button("Press me"):
            mac.pvgis(adress)
        Numero_paneles=(mwr.Numero_paneles_consumo_mensual(consumo_mensual))
    a = mre.obtener_amortización(Numero_paneles)
    for i in range(8):
        st.write("")
    for i in a["Importe del presupuesto"]:
        b = i
    for i in a["Total (21% IVA incluido)"]:
        c = i
    for i in a["Producción anual"]:
        d = i
    for i in a["Ahorro anual"]:
        e = i
    for i in a["Amortización de la inversión"]:
        f = i
    for i in a["Número de paneles"]:
        g = i
    for i in a["Potencia del Inversor"]:
        h = i
    for i in a["Potencia del Generador Fotovoltaico"]:
        i = i
    col1a, col2a, col3a, col4a = st.columns(4)
    
    
    col1a.metric("Número de paneles", str(g)+ " Paneles")
    col2a.metric("Potencia del Generador Fotovoltaico", str(i)+" Kw")
    col3a.metric("Potencia del Inversor", str(h)+" Kw")
    col4a.metric("Producción anual",d)
    
    for i in range(8):
        st.write("")
    if Numero_paneles == 0:
        col1b, col2b, col3b, col4b = st.columns(4)        
        col1b.metric("Importe del presupuesto",b , "0%")
        col2b.metric("Total Incluido IVA", c, "0%", delta_color="inverse")
        col3b.metric("Ahorro anual",e , "0%")
        col4b.metric("Amortización de la inversión",f , "0%")
    elif Numero_paneles != 0:
        col1c, col2c, col3c, col4c = st.columns(4)        
        col1c.metric("Importe del presupuesto",b , "0%")
        col2c.metric("Total Incluido IVA", c, "21%", delta_color="inverse")
        col3c.metric("Ahorro anual",e , "15%")
        col4c.metric("Amortización de la inversión",f , "6.4%")
    st.plotly_chart(mre.energía_generador_fotovoltaico(Numero_paneles), use_container_width=True)   
        
        
        
        
        
if agree2:
    tf = open("data/pot_electrodomesticos.json", "r")
    electro_dict = json.load(tf)
    electrodomesticos = list(electro_dict.keys())
    
    horas_func1 = {}
    
    unidades1 = {}

    for i in range(len(electrodomesticos)):
        nueva = st.text_input(f"¿ Tiene usted {electrodomesticos[i]} en su casa (Sí/No) ? ")
        if nueva.lower() in ["si".lower(), "sí".lower()]:
            unidad = st.number_input(f'¿ Cúantas unidades de {electrodomesticos[i]} tiene usted en su casa ? ')
            if nueva.lower() == "salir":
                break
            horas = st.number_input(f"Introduce un estimación aproximada de las horas de funcionamiento que va a tener el(a) {electrodomesticos[i]} en los días que esté funcionando : ")
            horas_func1[electrodomesticos[i]]=horas
            unidades1[electrodomesticos[i]] = unidad

    horas_func = horas_func1

    Numero_paneles=mwr.Numero_paneles(horas_func, unidades1)
    st.markdown(Numero_paneles)
    
    
    
    
    
    col1, col2 = st.columns(2)
    with col2:
        adress=st.text_input("Introduzca su dirección. Ejem: Calle Zaragoza, Fuenlabrada, Madrid")
        provincia_usuario = adress.split(",")
        if len(provincia_usuario) == 3:
            provincia_usuario = provincia_usuario[2]
            provincia_usuario = provincia_usuario.lower().strip()
            diccionario = man.read_datos_provincias()
            for i, y in diccionario.items():
                if provincia_usuario == i.lower():
                    st.write(y)
                else:
                    pass
        elif len(provincia_usuario) == 2:
            provincia_usuario = provincia_usuario[1]
            provincia_usuario = provincia_usuario.lower().strip()
            diccionario = man.read_datos_provincias()
            for i, y in diccionario.items():
                if provincia_usuario == i.lower():
                    st.write(y)
                else:
                    pass
        elif len(provincia_usuario) == 1:
            pass

    with col1:
        if adress == "":
            folium_static(mre.map_dirección_usuario("Madrid", zoom_start1=2))
        else:
            folium_static(mre.map_dirección_usuario(adress))
            
            
            
    
    
    
    with col2:
        Precio=st.number_input("Introduzca su Precio de compra de la Electricidad (Opcional)")
        with st.expander(' ¿Cómo puedo averiguar mi consumo medio mensual?'):
            st.image('Images/foto9.png')
        if st.button("Press me"):
            mac.pvgis(adress)
    a = mre.obtener_amortización(Numero_paneles)
    for i in range(8):
        st.write("")
    for i in a["Importe del presupuesto"]:
        b = i
    for i in a["Total (21% IVA incluido)"]:
        c = i
    for i in a["Producción anual"]:
        d = i
    for i in a["Ahorro anual"]:
        e = i
    for i in a["Amortización de la inversión"]:
        f = i
    for i in a["Número de paneles"]:
        g = i
    for i in a["Potencia del Inversor"]:
        h = i
    for i in a["Potencia del Generador Fotovoltaico"]:
        i = i
    col1, col2, col3, col4 = st.columns(4)
    
    
    col1.metric("Número de paneles", str(g)+ " Paneles")
    col2.metric("Potencia del Generador Fotovoltaico", str(i)+" Kw")
    col3.metric("Potencia del Inversor", str(h)+" Kw")
    col4.metric("Producción anual",d)
    
    for i in range(8):
        st.write("")
    if Numero_paneles == 0:
        col1, col2, col3, col4 = st.columns(4)        
        col1.metric("Importe del presupuesto",b , "0%")
        col2.metric("Total Incluido IVA", c, "0%", delta_color="inverse")
        col3.metric("Ahorro anual",e , "0%")
        col4.metric("Amortización de la inversión",f , "0%")
    elif Numero_paneles != 0:
        col1, col2, col3, col4 = st.columns(4)        
        col1.metric("Importe del presupuesto",b , "0%")
        col2.metric("Total Incluido IVA", c, "21%", delta_color="inverse")
        col3.metric("Ahorro anual",e , "15%")
        col4.metric("Amortización de la inversión",f , "6.4%")
   
    st.plotly_chart(mre.energía_generador_fotovoltaico(Numero_paneles), use_container_width=True)
    
    
    
    
    
     
         
        
        
        
 