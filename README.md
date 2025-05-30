# 📈 Proyecto: Simulación de Lectura y Visualización de Sensor DHT11

## Descripción general

Este proyecto demuestra cómo simular la lectura de datos desde un sensor DHT11 usando un entorno virtual (Proteus + Arduino IDE), enviar los datos mediante comunicación serial virtual a un script en Python, graficarlos en tiempo real, y almacenar las lecturas en un archivo CSV.
El objetivo es mostrar cómo integrar hardware simulado con visualización y análisis en Python, combinando electrónica y programación para un propósito demostrativo.

---

## 💂 Estructura de archivos

```
/Resources/
    DHT11/
        DHT11.ino            # Código Arduino para lectura y envío de datos del DHT11
    Simulador.pdsprj         # Proyecto Proteus para simular el circuito
    circuito.png             # Imagen del circuito, útil si no puedes abrir el archivo de Proteus

data_graphica.py             # Script Python para graficar en tiempo real y guardar datos en CSV
requirements.txt             # Dependencias de Python necesarias para correr el proyecto
```

---

## ⚙️ Requisitos

* **Hardware/software**:

  * Arduino IDE
  * Proteus Professional (para simular el circuito)

* **Python (>=3.7)**:

  * `matplotlib`
  * `pandas`
  * `pyserial`

Instala las dependencias ejecutando:

```bash
pip install -r requirements.txt
```

---

## 🚀 Cómo usarlo

1️⃣ Abre `Simulador.pdsprj` en Proteus, asegúrate de cargar el código del archivo `DHT11.ino` en la placa Arduino virtual.

2️⃣ Verifica que el puerto COM configurado en Proteus coincida con el que usarás en Python (`data_graphica.py`). Por defecto, está en `'COM6'`, pero puedes ajustarlo en el código.

3️⃣ Ejecuta la simulación en Proteus.

4️⃣ Luego corre en tu terminal:

```bash
python data_graphica.py
```

Esto abrirá una ventana con dos gráficos: temperatura (°C) y humedad (%), ambos mostrando también las líneas de umbral ajustables.

5️⃣ Los datos leídos se guardarán automáticamente en el archivo `lecturas_sensor.csv` en la carpeta raíz del proyecto. **Nota:** este archivo se sobrescribirá en cada ejecución.

---

## 💪 Cómo detenerlo

* Cierra manualmente la ventana de la gráfica, o
* Presiona `Ctrl + C` en la terminal para interrumpir el script.

---

## 💡 Posibles mejoras

Aquí algunas ideas para evolucionar el proyecto:

✅ **En Arduino (`DHT11.ino`):**

* Enviar un bit adicional indicando el estado ON/OFF del motor para visualizarlo en Python.
* Añadir histéresis para evitar que el motor encienda/apague constantemente cerca del umbral.
* Incluir más sensores (por ejemplo, sensores de luz, gas, etc.).

✅ **En Python (`data_graphica.py`):**

* Guardar múltiples sesiones de datos con timestamps únicos para no sobrescribir el CSV.
* Añadir alertas visuales/sonoras si los umbrales son superados.
* Optimizar el guardado del CSV para hacerse solo al final, evitando sobrecarga durante la ejecución.

---

## 📜 Notas importantes

⚠ **Asegúrate siempre de:**

* Configurar correctamente el puerto COM.
* Ejecutar primero el simulador antes de correr el script Python.
* Tener cuidado con los archivos CSV: actualmente se sobrescriben.

---

Si tienes dudas, sugerencias o quieres contribuir, ¡no dudes en abrir un issue o proponer mejoras!
