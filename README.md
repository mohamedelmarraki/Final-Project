### :sun_with_face: **Calculate Photovoltaic Installations** 
En este proyecto he analizado los datos de más de 40.000 diamantes y he utilizado diferentes modelos de Machine Learning para predecir el precio de otros diamantes.

![Image](https://actoresproductivos.com/wp-content/uploads/2020/12/fotovoltaica.jpg)



### :white_check_mark: **Estado**
Final-Project Ironhack data analysis :Calculate Photovoltaic Installations


### :computer: **Technology stack**
En este proyecto se ha utilizado varias librerías de Python como:

- Pandas

- Numpy

- Matplotlib

- Seaborn 

- Sklearn

Para Elaborar un proceso exploratorio de los datos y dibujar algunos graficos explicativos y diferentes modelos de Machine Learning para predicir el precio de distintos diamantes y lograr el menor RMSE posible.



### :zap: **EDA Results**
Tras el proceso exploratorio de los datos en el módulo 2 teníamos las siguientes conclusiones:

- El quilate es la característica más relevante del precio de un diamante.

- Fair es la forma de corte que tienen los diamantes con mayor quilate. Esta es la razón por la que aun siendo la peor forma de corte, tienen un precio promedio más alto.

- La forma de corte premium junto con los colores I y J, son los diamantes más caros aunque estos colores son dos de los de menor calidad. Esto se debe al peso en quilates de los diamantes I y J.

- En cuanto a la claridad, I1 y SI2 tienen dos de las calidades de claridad más bajas pero, como hay muchos diamantes de color I y J, el precio es más alto.



### :rocket: **Resultados de la predicción de modelo de Machine Learning**
El mejor modelo para predecir el precio de los distintos diamantes es el LGBMRegressor con un RMSE de aproximadamente 533



### :wrench: Tools
- Python==3.9
- pandas==1.3.4
- seaborn==0.11.2
- numpy==1.21.2
- Sklearn==1.0.2
- 
[...]


### :file_folder: Estructura de carpetas
```
└── Final-Project :Calculate Photovoltaic Installations
    ├── README.md
    ├── .gitignore
    ├── Main.py
    ├── chromedriver
    ├── requirements.txt
    ├── Notebooks
    │   ├── Calcular el consumo conociendo los electrodomesticos.ipynb
        ├── Calcular la instalación conociendo el consumo eléctrico medio mensual.ipynb
        ├── Devolver los datos de amortización.ipynb
        ├── graficar la energía generada de un sistema fotovoltaico.ipynb
        ├── Información de cada ciudad española.ipynb
        ├── leer los datos de de las provincias.ipynb
        ├── Map.ipynb
        ├── Pruebas.ipynb
        ├── Selenium de los datos de amortización.ipynb
        ├── Selenium de los datos de pvgis.ipynb
    ├── p_acquisition
        ├── m_acquisition
    ├── p_analysis
        ├── m_analysis
    ├── p_reporting
        ├── m_reporting
    ├── p_wrangling
        ├── m_wrangling
    └── data
        ├── Datos da cada provincia Española.csv
        ├── Datos de amortización.csv
        ├── datos_bajapotencia.txt
        ├── datos_electricaplicada.txt
        ├── datos_iberdrola.txt
        ├── pot_electrodomesticos.json
    
```   



### :love_letter: Contact info
Doubts? Advice? Drop me a line! :hugs: