import pandas as pd # importar la librería pandas

import numpy as np # importar la librería numpy

import requests # importar la librería requests

from selenium import webdriver # Habrá que descargar el webdriver de chrome para realizar las distintas operaciones

from selenium.webdriver.support.ui import WebDriverWait # Cuando cargamos una página web a veces el HTML tarda un poco en cargarse sugún nuestra velocidad de conexión pues hasta ciertos elementos no carguen tendremos que esperar

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.action_chains import ActionChains

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

warnings.filterwarnings('ignore')