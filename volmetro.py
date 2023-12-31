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

        # Configuración del gráfico de Matplotlib
        self.fig, self.ax = plt.subplots(subplot_kw={'projection': 'polar'})
        frame_grafica = tk.Frame(self.master)
        frame_grafica.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.canvas = FigureCanvasTkAgg(self.fig, master=frame_grafica)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=False)

        # Configuración del botón de Encender/Apagar
        frame_boton = tk.Frame(self.master)
        frame_boton.pack(side=tk.BOTTOM, fill=tk.X)
        boton_encendido = tk.Button(frame_boton, text="Encender/Apagar", command=self.toggle_meter)
        boton_encendido.pack(side=tk.TOP, fill=tk.X)

        # Inicialización y configuración del medidor
        self.needle, = self.ax.plot([], [], 'r-')  # Aguja inicialmente vacía
        self.ax.text(np.pi/2, 0.4, "V", fontsize=24, va='center', ha='center')  # Símbolo de voltaje

        self.draw_meter()  # Dibuja el medidor

    def toggle_meter(self):
        # Funcionalidad del botón para manejar el encendido y apagado del voltímetro
        pass

    def update_needle(self, value):
        # Actualiza la posición de la aguja basada en el valor de voltaje proporcionado
        max_value = 60
        min_angle = 0.5
        max_angle = np.pi - 0.5
        normalized_value = (value - 0) / (max_value - 0)
        angle = min_angle + normalized_value * (max_angle - min_angle)
        self.needle.set_data([angle, angle], [0, 0.9])
        self.canvas.draw_idle()

    def draw_meter(self):
        # Dibuja las marcas y etiquetas del medidor
        divisions = 60
        max_value = 60
        for i in range(divisions + 1):
            value = i * (max_value / divisions)
            angle = 0.5 + i * (np.pi - 1) / divisions
            if i % 10 == 0:
                self.ax.plot([angle, angle], [0.8 - 0.1, 0.9], color='k')
                self.ax.text(angle, 0.9 + 0.08, str(int(value)), horizontalalignment='center', verticalalignment='center')
            else:
                self.ax.plot([angle, angle], [0.9 - 0.1, 0.9], color='k')
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
        # Asumiendo que tienes configurado tu puerto serial correctamente
        ser = serial.Serial('COM3', 19200)
        return leer_serial_real(ser)

# Inicialización y ejecución de la aplicación Tkinter
if __name__ == '__main__':
    root = tk.Tk()
    vm = VolmetroAnalogico(root)

    def actualizar():
        voltaje = leer_serial()
        vm.update_needle(voltaje)
        root.update()
        root.after(1000, actualizar)  # Continúa actualizando el voltaje

    actualizar()
    root.mainloop()