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

col1, col2, col3 = st.columns([6,4,3])


with col2:
    adress=st.text_input("Introduzca la calle en la que vive")
    provincia_usuario = adress.split(",")
    if len(provincia_usuario) == 2:
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
    if adress is "":
        folium_static(mre.map_dirección_usuario("Madrid", zoom_start1=2))
    else:
        folium_static(mre.map_dirección_usuario(adress))


with col3:
    for i in range(15):
        st.write("")
    st.markdown(" ¿Cómo puedo averiguar mi consumo medio mensual?")



















