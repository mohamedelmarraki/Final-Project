
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

import os

from geopy.geocoders import Nominatim

import time

import math

from IPython.display import Javascript

import warnings

warnings.filterwarnings('ignore')




url_iberdrola = "https://www.iberdrola.es/blog/energia/cual-es-la-potencia-necesaria-para-los-electrodomesticos"
def pot_elctro_iberd(url):
    
    options = webdriver.ChromeOptions()
    
    options.add_argument("--start-maximized")
    
    options.add_argument("--disable-extensions")
    
    driver_path = '/Users/mohamedelmarraki/ironhack/Final-Project/chromedriver'
    
    driver = webdriver.Chrome(driver_path, chrome_options = options)
    
    driver.get(url)


    potencia_electro1 = driver.find_element_by_xpath("/html/body/div[1]/main/div[4]/div[1]/div[3]/ul[2]")
    potencia_electro1 = potencia_electro1.text

    time.sleep(1)
    
    driver.close()
    
    archi1=open("../data/datos_iberdrola.txt","w")
    
    archi1.write(potencia_electro1)
    
    archi1.close()
    


    
url_bajapotencia = "http://www.bajatelapotencia.org/la-potencia-que-necesitas/"
def pot_bajapotencia(url):
    
    options = webdriver.ChromeOptions()
    
    options.add_argument("--start-maximized")
    
    options.add_argument("--disable-extensions")
    
    driver_path = '/Users/mohamedelmarraki/ironhack/Final-Project/chromedriver'
    
    driver = webdriver.Chrome(driver_path, chrome_options = options)
    
    driver.get(url)


    WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/section/article/table/tbody")))


    potencia_electro2 = driver.find_element_by_xpath("/html/body/div[2]/section/article/table/tbody")
    potencia_electro2 = potencia_electro2.text

    time.sleep(1)
    
    driver.close() 
    
    archi2=open("../data/datos_bajapotencia.txt","w") 
    
    archi2.write(potencia_electro2)
    
    archi2.close()
    
    


url_electricaplicada = "https://www.electricaplicada.com/potencia-consumo-equipos-electricos/"
def pot_electricaplicada(url):
    
    options = webdriver.ChromeOptions()
    
    options.add_argument("--start-maximized")
    
    options.add_argument("--disable-extensions")
    
    driver_path = '/Users/mohamedelmarraki/ironhack/Final-Project/chromedriver'
    
    driver = webdriver.Chrome(driver_path, chrome_options = options)
    
    driver.get(url)


    WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.XPATH, "//*[@id='post-4887']/div/div")))


    potencia_electro3 = driver.find_element_by_xpath("//*[@id='post-4887']/div/div")
    potencia_electro3 = potencia_electro3.text

    time.sleep(1)
    
    driver.close()
    
    archi3=open("../data/datos_electricaplicada.txt","w") 
    
    archi3.write(potencia_electro3)
    
    archi3.close()
    



def pvgis (dire):
    
    import glob
    
    from os import remove
    
    csv_files = glob.glob('../../Downloads/*.csv')
    
    csv_pvgis = ("").join(csv_files).split("/")
    
    lista = []
    
    for i in csv_pvgis:
        if "M" in i:
            lista.append(i.replace("..", ""))
    
    for i in lista:
        remove(f'../../Downloads/{i}')
        
    geo = Nominatim(user_agent = "MyApp")
    if dire == "":
        loc = geo.geocode("Madrid")
    
        coordenadas = loc.latitude, loc.longitude
    else:
        loc = geo.geocode(dire)
        
        coordenadas = loc.latitude, loc.longitude
    
    options = webdriver.ChromeOptions()
    
    options.add_argument("--start-maximized")
    
    options.add_argument("--disable-extensions")
    
    driver_path = '/Users/mohamedelmarraki/ironhack/Final-Project/chromedriver'
    
    driver = webdriver.Chrome(driver_path, chrome_options = options)
    
    driver.get("https://joint-research-centre.ec.europa.eu/pvgis-photovoltaic-geographical-information-system_en")
    
    time.sleep(0.5)
    
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.wt-link cck-actions-button".replace(" ", "."))))\
        .click()
    
    time.sleep(0.5)
    
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.ecl-link ecl-link--primary".replace(" ", "."))))\
        .click()
    
    time.sleep(0.5)
    
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH, "//*[@id='cookie-consent-banner']/div/div/div[2]/a")))\
        .click()
    
    time.sleep(0.5)
    
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#inputLat")))\
        .send_keys(coordenadas[0])
    
    time.sleep(0.5)
    
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#inputLon")))\
        .send_keys(coordenadas[1])
    
    time.sleep(0.5)
    
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button#btninputLatLon".replace(" ", "."))))\
        .click()
    
    time.sleep(0.5)
    
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span#tr_mondat")))\
        .click()
    
    time.sleep(0.5)
    
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#optrad")))\
        .click()
    
    time.sleep(0.5)
    
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#avtemp")))\
        .click()
    
    time.sleep(0.5)
    
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH, "//*[@id='mstartyear']")))\
        .click()
    
    time.sleep(0.5)
    
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH, "//*[@id='mstartyear']/option[16]")))\
        .click()
    
    time.sleep(0.5)
    
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH, "//*[@id='mendyear']")))\
        .click()
    
    time.sleep(0.5)
    
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH, "//*[@id='mendyear']/option[16]")))\
        .click()
    
    time.sleep(0.5)
    
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div#monthdownloadcsv")))\
        .click()
    
    time.sleep(0.5)
    
    driver.close()

    
    
    
url_amortización ="https://precioinstalacionplacassolares.com/"
def Datos_amortización(url):
    options = webdriver.ChromeOptions()

    options.add_argument("--start-maximized")

    options.add_argument("--disable-extensions")

    driver_path = '/Users/mohamedelmarraki/ironhack/Final-Project/chromedriver'

    driver = webdriver.Chrome(driver_path, chrome_options = options)

    driver.get(url)

    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH, "//*[@id='portfolio-tabs-navigation']")))\
        .click()


    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH, "//*[@id='portfolio-tabs-navigation']/option[2]")))\
        .click()



    lista1 = []
    for i in range(4,23):
        for y in range(2,11):
            driver.execute_script(f"return document.getElementById('entry').setAttribute('value', {i})")
            driver.execute_script("return document.getElementById('entry').dispatchEvent(new Event('input'))")
            driver.execute_script(f"return document.getElementById('entry2').setAttribute('value', {y})")
            driver.execute_script("return document.getElementById('entry2').dispatchEvent(new Event('input'))")
            lista1.append(driver.find_element_by_xpath("//*[@id='portfolio-card-one']/div").text)
        
    lista2 = []
    for i in range(4,23):
        for y in range(2, 11):
            driver.execute_script(f"return document.getElementById('entry').setAttribute('value', {i})")
            driver.execute_script("return document.getElementById('entry').dispatchEvent(new Event('input'))")
            lista2.append(driver.find_element_by_xpath("//*[@id='pintar3']").text)

    df1 = pd.DataFrame(lista2, columns=["Potencia del Generador Fotovoltaico"])
    df1


    lista3 = []
    for i in lista1:
        lista3.append(i.split("\n"))
    

    df2 = pd.DataFrame(lista3).rename(columns={1:"Importe del presupuesto", 3:"Total (21% IVA incluido)",
                                          6:"Producción anual", 
                                          8:"Ahorro anual", 10:"Amortización de la inversión"})


    df2.drop([0, 2, 4, 5, 7, 9, 11], axis=1, inplace= True)
    df2



    lista4 = []
    for i in range(4, 23):
        for y in range(2, 11):
            lista4.append([i, y])
        

    df3 = pd.DataFrame(lista4, columns=["Número de paneles", "Potencia del Inversor"])


    df_concat = pd.concat([df3, df1, df2], axis=1)


    df_concat.to_csv("../data/Datos de amortización.csv")
    
    
    
    
url_provincias = "https://www.autoconsumoaldetalle.es/calcule-su-instalacion/#"
def datos_provincias(url):
    options = webdriver.ChromeOptions()

    options.add_argument("--start-maximized")

    options.add_argument("--disable-extensions")

    driver_path = '/Users/mohamedelmarraki/ironhack/Final-Project/chromedriver'

    driver = webdriver.Chrome(driver_path, chrome_options = options)

    driver.get(url)
    
    lista1 = []
    
    lista2 = []
    
    for i in range(1, 54):
        WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.XPATH, f"//*[@id='idprovincia']/option[{i}]")))\
            .click()
        time.sleep(0.5)
        lista1.append(driver.find_element_by_xpath(f"//*[@id='idprovincia']/option[{i}]").text)
        time.sleep(0.5)
        lista2.append(driver.find_element_by_xpath("//*[@id='generado']").text)
        time.sleep(0.5)
    
    df1 = pd.DataFrame(lista1, columns=["Provincias"])
    
    df2 = pd.DataFrame(lista2, columns=["Información de cada Provincia"])
    
    df_concat = pd.concat([df1, df2], axis = 1)
    
    df_concat.to_csv("../data/Datos da cada provincia Española.csv")