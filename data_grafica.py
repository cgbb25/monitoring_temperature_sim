import serial
import time
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 1. Configurar puerto serie
ser = serial.Serial('COM6', 9600, timeout=1)

# 2. Preparar figura con dos ejes apilados
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6), sharex=True)
fig.suptitle("Lectura en tiempo real: Temperatura y Humedad")
ax1.set_ylabel("Temperatura (°C)")
ax2.set_ylabel("Humedad (%)")
ax2.set_xlabel("Tiempo (s)")

# listas para datos
tiempos, temps, hums, umbrales_temps, umbrales_hums = [], [], [], [], []
fechas_hora = []  # Para almacenar las fechas y horas
t0 = time.time()

# DataFrame para almacenar los datos
df = pd.DataFrame(columns=["Fecha-Hora", "Temperatura(°C)", "Humedad(%)", "Umbral_Temperatura", "Umbral_Humedad"])

def leer_sensor():
    linea = ser.readline().decode('utf-8').strip()
    if not linea:
        return None, None, None, None
    try:
        t, h, umbral_t, umbral_h = map(float, linea.split(','))
        return t, h, umbral_t, umbral_h
    except ValueError:
        return None, None, None, None

def guardar_datos():
    global df
    # Guardar los datos en el archivo CSV
    df = pd.DataFrame({
        "Fecha-Hora": fechas_hora,
        "Temperatura(°C)": temps,
        "Humedad(%)": hums,
        "Umbral_Temperatura": umbrales_temps,
        "Umbral_Humedad": umbrales_hums
    })
    df.to_csv("lecturas_sensor.csv", index=False)

def actualizar(frame):
    temp, hum, umbral_temp, umbral_hum = leer_sensor()
    if temp is None:
        return

    # Obtener el tiempo transcurrido
    ts = time.time() - t0
    tiempos.append(ts)
    temps.append(temp)
    hums.append(hum)
    umbrales_temps.append(umbral_temp)
    umbrales_hums.append(umbral_hum)

    # Obtener la fecha y hora actual
    fecha_hora_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    fechas_hora.append(fecha_hora_actual)

    # Limitar el historial de datos
    tiempos[:] = tiempos[-100:]
    temps[:]   = temps[-100:]
    hums[:]    = hums[-100:]
    umbrales_temps[:] = umbrales_temps[-100:]
    umbrales_hums[:] = umbrales_hums[-100:]
    fechas_hora[:] = fechas_hora[-100:]

    # Guardar datos en CSV cada vez que se actualiza
    guardar_datos()

    # Limpiar y volver a dibujar la gráfica
    ax1.clear()
    ax2.clear()

    ax1.plot(tiempos, temps, marker='o')
    ax1.plot(tiempos, umbrales_temps, marker='o')
    ax1.set_ylabel("Temperatura (°C)")
    ax1.grid(True)

    ax2.plot(tiempos, hums, marker='x')
    ax2.plot(tiempos, umbrales_hums, marker='x')
    ax2.set_ylabel("Humedad (%)")
    ax2.set_xlabel("Tiempo (s)")
    ax2.grid(True)

# 3. Lanzar animación cada 1 s
ani = FuncAnimation(fig, actualizar, interval=1000, cache_frame_data=False)

try:
    plt.show()
except KeyboardInterrupt:
    print("\nPrograma interrumpido por el usuario.")
finally:
    if ser.is_open:
        ser.close()
        print("Puerto serie cerrado correctamente.")
