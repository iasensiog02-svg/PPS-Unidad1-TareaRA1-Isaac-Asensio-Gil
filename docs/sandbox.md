# Actividad Unidad 1 – Sandboxing

## Prueba de aplicaciones en un entorno de ejecución controlado (Sandboxing)

En este documento se describe el proceso seguido para crear un entorno de ejecución aislado (*sandbox*) y ejecutar la aplicación **notas** desarrollada en Python. El objetivo es demostrar cómo se puede ejecutar y analizar una aplicación de forma segura, limitando su acceso al sistema mediante herramientas de sandboxing.

---

## 1. Instalación de las herramientas de sandboxing

Para la creación del entorno aislado se instalaron las herramientas **Firejail** y **Firetools**, que permiten ejecutar aplicaciones dentro de un entorno controlado.

```bash
sudo apt install firejail firetools

```

![foto](/Capturas/instalacion.png)


---

## 2. Creación y activación del entorno virtual de Python

Con el objetivo de aislar las dependencias de la aplicación y evitar conflictos con el sistema, se creó un entorno virtual de Python dentro del proyecto

```bash
python3 -m venv .venv
source .venv/bin/activate
```


---

## 3. Instalación de dependencias de la aplicación

Una vez activado el entorno virtual, se procedió a instalar las dependencias necesarias para la ejecución de la aplicación `notas.py`

```bash
pip install -r requeriments.txt
pip install -e .

```
![foto](/Capturas/requirement.png)

---

## 4. Ejecución de la aplicación dentro del sandbox
La aplicación se ejecutó dentro de un entorno aislado utilizando `Firejail`

```bash
firejail --private=. python3 src/notas/notas.py
```
![foto](/Capturas/ejecutar.png)

--

## 5.Ejecución de pruebas unitarias
Para comprobar el correcto funcionamiento de la aplicación, se ejecutaron las pruebas unitarias incluidas en el proyecto

```bash
PYTHONPATH=src python3 -m unittest tests/test_notas_unittest.py -v

```

![foto](/Capturas/test.png)

---


