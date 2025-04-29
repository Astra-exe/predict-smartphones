<div align="center" id="readme-top">
  <img src="Frontend/juan_logo_white.png" alt="Logo" width="50%">

  <p align="center">
    <b>Predict Smartphones</b> es un proyecto de regresión lineal multivariable desde cero para predecir precios de smartphones refabricados.
    <br />
  </p>
</div>

<details>
  <summary>Tabla de Contenidos</summary>
  <ol>
    <li><a href="#sobre-el-proyecto">Sobre el Proyecto</a></li>
    <li><a href="#construido-con">Construido con</a></li>
    <li><a href="#conoce-al-autor">Conoce al Autor</a></li>
    <li>
      <a href="#empezando">Empezando</a>
      <ul>
        <li><a href="#prerrequisitos">Prerrequisitos</a></li>
        <li><a href="#instalación">Instalación</a></li>
      </ul>
    </li>
    <li><a href="#uso">Uso</a>
      <ul>
        <li><a href="#pasos">Pasos</a></li>
        <li><a href="#pruebas">Pruebas</a></li>
      </ul>
    </li>
    <li><a href="#consideraciones">Consideraciones</a></li>
  </ol>
</details>

## Sobre el Proyecto
**Predict Smartphones** es una implementación manual de regresión lineal multivariable cuyo objetivo es predecir el precio de smartphones refabricados.

El proyecto abarca:
- Código desde cero, sin usar librerías de machine learning como scikit-learn.
- Procesamiento de datos, normalización y codificación de variables categóricas.
- Entrenamiento de un modelo utilizando descenso de gradiente.
- Análisis de la evolución del costo de error.

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>

## Construido con
* [![Python][Python.js]][Python-url]
* [![NumPy][NumPy.js]][NumPy-url]
* [![Pandas][Pandas.js]][Pandas-url]

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>

## Conoce al Autor
- [Juan Ramírez (Astra)](https://github.com/Astra-exe) - Analista y científico de datos JR.

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>

## Empezando

### Prerrequisitos
Asegúrate de tener instalado:
- Python 3.11 o superior
- pip

Dependencias:
```bash
pip install numpy pandas matplotlib
```

### Instalación
1. Clona el repositorio:
```bash
git clone https://github.com/Astra-exe/predict-smartphones.git
```
2. Accede al proyecto:
```bash
cd predict-smartphones
```
3. Instala los requerimientos:
```bash
pip install -r requirements.txt
```

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>

## Uso

### Pasos
1. Abre el notebook `eda_phones.ipynb` en tu entorno preferido (Jupyter, VSCode, etc.). Si es que deseas jugar con los datos o ver como se relacionan las variables entre si.
2. Ejecuta el script `src/main.py` para que el modelo sea entrenado y preparado paso a paso paso a paso:
   - Preparación de datos
   - Implementación de la regresión lineal desde cero
   - Entrenamiento del modelo
   - Visualización de resultados
3. Ajusta parámetros como `learning rate` o `número de iteraciones` para experimentar mejoras.
4. Ejecuta la API en Flask en el archivo `Api/app.py`
5. Una vez corriendo la API puedes hacer pruebas con el frontend `Frontend/index.html`

### Pruebas
* Analiza el comportamiento de la función de costo (gráfica de convergencia).
* Realiza predicciones para nuevos dispositivos cambiando las variables de entrada.

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>

## Consideraciones
- No se manejan todas las técnicas de regularización o validación cruzada.
- Es fundamental realizar una buena codificación de variables categóricas para obtener mejores resultados.
- El dataset utilizado puede ser muy pequeño; para resultados más confiables, puede ser necesario un conjunto de datos más grande y diverso.

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>

<div align="center">
  <h3 align="center">💜 Gracias por visitar el proyecto 💜
  </h3>
</div>

[Python.js]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[NumPy.js]: https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white
[NumPy-url]: https://numpy.org/
[Pandas.js]: https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white
[Pandas-url]: https://pandas.pydata.org/
[Matplotlib.js]: https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=matplotlib&logoColor=white
[Matplotlib-url]: https://matplotlib.org/
[Jupyter.js]: https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white
[Jupyter-url]: https://jupyter.org/

