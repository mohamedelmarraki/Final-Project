### :arrow_right: **Diamond Price Predition** 
En este proyecto he analizado los datos de más de 40.000 diamantes y he utilizado diferentes modelos de Machine Learning para predecir el precio de otros diamantes.

![Image](https://actoresproductivos.com/wp-content/uploads/2020/12/fotovoltaica.jpg)



### :white_check_mark: **Estado**
Projecto módulo 3 Ironhack Analisis De Datos: Predicción del precio del diamante.


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
└── ih_datamadpt1121_project_m3
    ├── .gitignore
    ├── README.md
    ├── Notebooks
    │   ├── Modelo 1 " los datos codificados con dummies, escalados y sin escalar con todos los modelos probados ".ipynb
        ├── Modelo 2 " codificar los datos dando valor y preferencia a los mejores diamantes".ipynb'
    │   ├── Modelo 3 "Scalar los datos del modolo 2".ipynb
        ├── Modelo 4 "eliminar la columna city del modelo 3".ipynb
        ├── Modelo 5 "Afinar los hyperparametros del modelo 4".ipynb
        ├── Modelo 6 "Predecir los valores de la columna Z ".ipynb
        ├── Modelo 7 "Predecir los valores de la columna x ".ipynb
        ├── Modelo 8 "Predecir los valores de la columna y ".ipynb
        ├── Modelo 9 "Sustituir los valores 0 de las columnas z,x,y por los valors predicidos anteriormente[El Mejor Modelo].ipynb
        ├── 
    └── Data
        ├── diamonds_train.db
        ├── diamonds_test.csv
        
    └── Submissions
    
```   



### :love_letter: Contact info
Doubts? Advice? Drop me a line! :hugs: