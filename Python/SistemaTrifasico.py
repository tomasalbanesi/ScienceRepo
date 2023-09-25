import numpy as np
import matplotlib.pyplot as plt

# Parámetros
frecuencia = 50  # Frecuencia en Hz
amplitud = 230    # Amplitud de la tensión en V
angulo = 0        # Ángulo de fase en grados
periodos = 3      # Número de periodos a graficar

# Generar tensiones trifásicas balanceadas
t = np.arange(0, (1/frecuencia)*periodos, 1/10000)  # Vector de tiempo con tres periodos
voltageA = amplitud * np.sqrt(2) * np.sin(2 * np.pi * frecuencia * t + np.deg2rad(angulo))
voltageB = amplitud * np.sqrt(2) * np.sin(2 * np.pi * frecuencia * t + np.deg2rad(angulo - 120))
voltageC = amplitud * np.sqrt(2) * np.sin(2 * np.pi * frecuencia * t + np.deg2rad(angulo + 120))

# Plotear las tensiones en un solo gráfico
plt.figure(1)
plt.plot(t, voltageA, 'r', linewidth=1.5)
plt.gca().set_prop_cycle(None)  # Reiniciar el ciclo de colores
plt.plot(t, voltageB, 'g', linewidth=1.5)
plt.plot(t, voltageC, 'b', linewidth=1.5)

# Resaltar la línea horizontal del eje y en negrita
plt.axhline(0, color='k', linewidth=1)

plt.title('Tensiones Trifásicas')
plt.xlabel('Tiempo (s)')
plt.ylabel('Tensión (V)')
plt.legend(['Fase R', 'Fase S', 'Fase T'])
plt.grid(True)
plt.axis('tight')
plt.show()
