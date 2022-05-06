# :sun_with_face: **Calculate Photovoltaic Installations** 
In this project I have created a Streamlit page to calculate an estimate of the size of the photovoltaic installation that the user needs and also the cost data of the installation and how long it would take to amortize its installation

![Image](https://actoresproductivos.com/wp-content/uploads/2020/12/fotovoltaica.jpg)

&nbsp;

---

## :white_check_mark: **Estado**
Final-Project Ironhack data analysis :Calculate Photovoltaic Installations

![Employee data](/Users/mohamedelmarraki/ironhack/Final-Project/Images/foto17.png?raw=true "Employee Data title")

&nbsp;

---

## :computer: **Technology stack**
In this project several Python libraries have been used, such as:

- Install [pandas](https://pandas.pydata.org/docs/user_guide/index.html) library. Copy and paste next command in your master branch:
    ```
    pip install pandas
    ```
- Install [numpy](https://numpy.org/doc/) library. Copy and paste next command in your master branch:
    ```
    pip install numpy 
    ```
- Install [selenium](https://selenium-python.readthedocs.io/) library. Copy and paste next command in your master branch:
    ```
    pip install selenium
    ```
- Install [plotly-express](https://plotly.com/python-api-reference/plotly.express.html) library. Copy and paste next command in your master branch:
    ```
    pip install plotly-express
    ```
- Install [os](https://docs.python.org/3/library/os.html) library. Copy and paste next command in your master branch:
    ```
    pip install os
    ```
- Install [geopy](https://geopy.readthedocs.io/en/stable/) library. Copy and paste next command in your master branch:
    ```
    pip install geopy
    ```
- Install [ipython](https://ipython.org/documentation.html) library. Copy and paste next command in your master branch:
    ```
    pip install ipython
    ```
- Install [math](https://docs.python.org/3/library/math.html) library. Copy and paste next command in your master branch:
    ```
    pip install python-math
    ```
- Install [time](https://docs.python.org/3/library/time.html) library. Copy and paste next command in your master branch:
    ```
    pip install times
    ```
- Install [folium](https://python-visualization.github.io/folium/) library. Copy and paste next command in your master branch:
    ```
    pip install folium
    ```
- Install [glob](https://docs.python.org/3/library/glob.html) library. Copy and paste next command in your master branch:
    ```
    pip install glob2
    ```

To create the necessary functions that perform the calculations of the dimensions of the facilities and obtain the data of the irradiance and temperature data of all the coordinates of the world and the amortization data of the facilities.

&nbsp;

---

## :scroll: **sources**

[Iberdrola](https://www.iberdrola.es/blog/energia/cual-es-la-potencia-necesaria-para-los-electrodomesticos)

[Bajatelapotencia](http://www.bajatelapotencia.org/la-potencia-que-necesitas/)

[electricaplicada](https://www.electricaplicada.com/potencia-consumo-equipos-electricos/)

[Pvgis](https://joint-research-centre.ec.europa.eu/pvgis-photovoltaic-geographical-information-system_en)

[autoconsumoaldetalle](https://www.autoconsumoaldetalle.es/calcule-su-instalacion/#l)

[kaylon](https://precioinstalacionplacassolares.com/)

&nbsp;

---

## :page_facing_up: **ETL Results (Extract, Transform and load)**
- The data extraction process was the most complex of the three processes in which I used the selenium library of both the python and javascript languages.

- and to transform the data obtained with selenium I have used the python pandas library which I handle quite well and with which I have worked comfortably in this process

- In the end I have loaded the data in files such as .csv, . jsony . text and with which I have started the EDA process


&nbsp;

---


## :zap: **EDA Results**
Tras el proceso exploratorio de los datos en  teníamos las siguientes conclusiones:

- El quilate es la característica más relevante del precio de un diamante.

- Fair es la forma de corte que tienen los diamantes con mayor quilate. Esta es la razón por la que aun siendo la peor forma de corte, tienen un precio promedio más alto.

- La forma de corte premium junto con los colores I y J, son los diamantes más caros aunque estos colores son dos de los de menor calidad. Esto se debe al peso en quilates de los diamantes I y J.

- En cuanto a la claridad, I1 y SI2 tienen dos de las calidades de claridad más bajas pero, como hay muchos diamantes de color I y J, el precio es más alto.

&nbsp;

---


## :file_folder: Folder structure
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

&nbsp;

---

### :love_letter: Contact info
Doubts? Advice? Drop me a line! :hugs: mohamedelmarraki609@gmail.com

&nbsp;

---