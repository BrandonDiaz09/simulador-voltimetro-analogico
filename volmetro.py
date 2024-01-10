import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
import random
import serial

class VolmetroAnalogico:
    def __init__(self, master):
        # Configuración inicial de la ventana principal
        self.master = master
        self.master.title("Simulador de Voltímetro Analógico")

        frame_volimetro = tk.Frame(self.master, bg='white', relief='solid')
        frame_volimetro.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        frame_grafica = tk.Frame(frame_volimetro, bg='#2B2B2B',borderwidth=10, relief='solid')
        frame_grafica.pack(side=tk.BOTTOM,fill=tk.X,expand=False,anchor='n', padx=15, pady=15)


        self.fig, self.ax = plt.subplots(subplot_kw={'projection': 'polar'})
        self.canvas = FigureCanvasTkAgg(self.fig, master=frame_grafica)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.X, expand=False) 

        # Agregar una línea divisoria
        linea_divisoria = tk.Frame(frame_grafica, bg='black', height=10) 
        linea_divisoria.pack(side=tk.TOP, fill=tk.X, expand=False)

        frame_bg = tk.Frame(frame_grafica, bg='#2B2B2B', relief='solid', height=50)
        frame_bg.pack(side=tk.TOP, fill=tk.BOTH, expand=True)  

    
        titulo_label = tk.Label(frame_volimetro, text="Voltímetro Analógico", font=("Arial", 18, "bold"), bg='white', fg='black')
        titulo_label.pack(side=tk.TOP, fill=tk.X, pady=[10,0]) 

        # Label para mostrar el valor del voltaje
        self.voltaje_label = tk.Label(frame_bg, text="0 V", font=("Digital-7", 60), bg='#2B2B2B', fg='#19D3AE')
        self.voltaje_label.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


        # Inicialización y configuración del medidor
        self.needle, = self.ax.plot([], [], 'r-')  # Aguja inicialmente vacía
        self.ax.text(np.pi/2, 0.4, "V", fontsize=30, va='center', ha='center')  # Símbolo de voltaje

        self.draw_meter()  # Dibuja el medidor

    def update_needle(self, value):
        # Actualiza la posición de la aguja basada en el valor de voltaje proporcionado
        max_value = 60
        min_angle = 0.5
        max_angle = np.pi - 0.5
        normalized_value = (value - 0) / (max_value - 0)
        angle = min_angle + normalized_value * (max_angle - min_angle)
        self.needle.set_data([angle, angle], [0, 1])
        # Definir umbrales
        umbral_bajo = 0.2 * max_value
        umbral_alto = 0.8 * max_value

        # Cambiar colores según el valor del voltaje
        if value < umbral_bajo:
            color = '#7FDBFF'  # Azul claro
        elif umbral_bajo <= value < umbral_alto:
            color = '#2ECC40'  # Verde
        else:
            color = '#FF4136'  # Rojo
        self.voltaje_label.config(text=f"{value:.2f} V")
        self.needle.set_color(color)
        self.voltaje_label.config(fg=color)
        self.canvas.draw_idle()


    def draw_meter(self):
        # Establecer el rango del eje radial (eje y)
        self.ax.set_ylim(0, 1)  # Esto asegura que solo se muestra la mitad superior

        # Establecer el rango angular
        self.ax.set_thetamin(0)    # Mínimo ángulo en grados
        self.ax.set_thetamax(180)  # Máximo ángulo en grados
        # Dibuja las marcas y etiquetas del medidor
        divisions = 60
        max_value = 60
        for i in range(divisions + 1):
            value = i * (max_value / divisions)
            angle = 0.5 + i * (np.pi - 1) / divisions
            if i % 10 == 0:
                self.ax.plot([angle, angle], [0.8, 1], color='k')
                self.ax.text(angle, 1.1, str(int(value)), horizontalalignment='center', verticalalignment='center')
            elif i% 5==0:
                self.ax.plot([angle, angle], [0.86, 1], color='k')
            else:
                self.ax.plot([angle, angle], [0.9, 1], color='k')
        self.ax.set_theta_zero_location("W")
        self.ax.set_theta_direction(-1)
        self.ax.axis('off')

SIMULATED = True
# Funciones para leer datos del serial o simular datos
def leer_serial_simulado():
    simulated_bin_value = random.randint(0, 255)
    return (simulated_bin_value * 235.2941) / 1000

def leer_serial_real(ser):
    linea = ser.readline().decode('utf-8').rstrip()
    return int(linea) * 235.2941 / 1000

def leer_serial():
    if SIMULATED:
        return leer_serial_simulado()
    else:
        ser = serial.Serial('COM3', 19200)
        return leer_serial_real(ser)

# Inicialización y ejecución de la aplicación
if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("550x700")  # Ancho x Alto
    vm = VolmetroAnalogico(root)

    def actualizar():
        voltaje = leer_serial()
        vm.update_needle(voltaje)
        root.update()
        root.after(1000, actualizar)  # Continúa actualizando el voltaje

    actualizar()
    root.mainloop()