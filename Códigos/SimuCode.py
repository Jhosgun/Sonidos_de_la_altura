import math
import matplotlib.pyplot as plt 
import numpy as np

# Constantes
g = 9.81  # Aceleración debido a la gravedad (m/s^2)
rho = 1.0  # Densidad de la bola (kg/m^3, valor hipotético)
alpha = 0.6  # Coeficiente de restitución (valor hipotético)
I_0 = 1e-12  # Intensidad de referencia para decibeles (W/m^2)

def calcular_masa(diametro):
    """
    Calcula la masa de la bola a partir de su diámetro.
    """
    radio = diametro / 2
    volumen = (4/3) * math.pi * radio**3
    return rho * volumen

def calcular_decibeles_primer_impacto(diametro, altura):
    """
    Calcula los decibeles del primer impacto de la bola.
    """
    #masa = calcular_masa(diametro)
    #print("MASA: ",masa)
    masa = 0.01
    energia_inicial = masa * g * altura
    #return 10 * math.log10(energia_inicial / I_0)
    #return 10 * math.log10(energia_inicial / I_0)
    return (   30*np.log10(diametro) + 10*np.log10(altura) + 95   )*(np.pi/4)

def calcular_tiempo_entre_impactos(altura):
    """
    Calcula el tiempo entre los dos primeros impactos.
    """
    t1 = math.sqrt(2 * altura / g)  # Tiempo de caída
    t2 = t1 + 2 * math.sqrt(2 * alpha * altura / g)  # Tiempo hasta el segundo impacto
    return t2 - t1


# Test the functions with the provided heights
alturas = [10, 30, 50, 60, 80, 90, 120]
decibeles = []
tiempos = []

for altura in alturas:
    diametro_bola = 2  # 10 cm
    decibeles_primer_impacto = calcular_decibeles_primer_impacto(diametro_bola, altura)
    tiempo_entre_impactos = calcular_tiempo_entre_impactos(altura)

    decibeles.append(decibeles_primer_impacto)
    tiempos.append(tiempo_entre_impactos)

# Plotting the results
plt.figure(figsize=(12, 6))

# Decibels vs Heights
plt.subplot(1, 2, 1)
plt.plot(alturas, decibeles, marker='o')
plt.title('SPL vs Altura')
plt.xlabel('h [cm]')
plt.ylabel('SPL (dB)')

# Time between impacts vs Heights
plt.subplot(1, 2, 2)
plt.plot(alturas, tiempos, marker='o', color='green')
plt.title('Tiempo entre impactos vs altura')
plt.xlabel('h [cm]')
plt.ylabel('Tiempo (s)')

plt.tight_layout()
plt.show()