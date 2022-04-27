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


#Definir el título
st.title('Calcule su instalación fotovoltaica')

st.image("https://postgradoindustrial.com/wp-content/uploads/energia-solar-termica.jpg")

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



st.markdown("#### Rellene la información solicitada a continuación si quiere realizar un cálculo aproximado de la instalación solar fotovoltaica para autoconsumo de su vivienda o negocio. También podrá ver si la ins.")


