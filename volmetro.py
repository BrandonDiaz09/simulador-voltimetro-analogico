import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
import serial
import random

class VolmetroAnalogico:
    def __init__(self, master):
        self.master = master
        self.master.title("Simulador de Voltímetro Analógico")
        #tk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
        # Configuración del gráfico
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
        # Inicialización del medidor
        self.ax.set_xlim(0, 61)
        self.ax.set_ylim(0, 1)
        self.needle, = self.ax.plot([], [], 'r-')  # Aguja inicialmente vacía
        # Dibujar el medidor
        self.draw_meter()

    def update_needle(self, value):
        # Actualizar la aguja del medidor según el valor de voltaje
        self.needle.set_data([value, value], [0, 0.5])
        self.canvas.draw_idle()

    def draw_meter(self):
        # Dibujar el medidor con marcas
        #self.ax.axis('off')
        for i in range(61):
            if i%10==0:
                self.ax.plot([i, i], [0.75,1], 'k')  # Marcas del medidor
            else:
                self.ax.plot([i, i], [0.85,1], 'k')  # Marcas del medidor
        self.ax.tick_params(axis='x', bottom=False,labeltop=True,labelbottom=False)
        self.ax.tick_params(axis='y', left=False,labelleft=False)


# Flag para controlar el modo de simulación
SIMULATED = True

def leer_serial_simulado():
    """Esta función simula la lectura de datos desde un puerto serial."""
    # Simula la lectura de un valor binario aleatorio
    simulated_bin_value = random.randint(0, 255)
    # Calcula el voltaje simulado
    voltaje_simulado = (simulated_bin_value * 235.2941) / 1000
    return voltaje_simulado

def leer_serial_real(ser):
    """Esta función lee los datos reales desde un puerto serial."""
    # Leer desde serial y decodificar
    linea = ser.readline().decode('utf-8').rstrip()
    # Convertir a valor de voltaje
    valor_binario = int(linea)  # Asegúrate de que los datos sean correctos
    voltaje = (valor_binario * 235.2941) / 1000  # Ajustar según tus cálculos
    return voltaje

def leer_serial():
    """Esta función decide si leer desde el puerto real o simular la lectura."""
    if SIMULATED:
        return leer_serial_simulado()
    else:
        ser = serial.Serial('COM3', 19200)  # Ajusta a tu configuración
        return leer_serial_real(ser)


if __name__ == '__main__':
    root = tk.Tk()
    vm = VolmetroAnalogico(root)
    # Función de actualización
    def actualizar():
        voltaje = leer_serial()
        vm.update_needle(voltaje)
        root.update()
        root.after(1000, actualizar)  # Actualiza cada segundo

    #print("Hola")
    # Simulando la actualización del voltaje
    #for v in np.linspace(0, 10, 100):
    #    vm.update_needle(leer_serial())
    #    root.update()
    #    root.after(1000)  # Espera un poco antes de actualizar
    actualizar()
    root.mainloop()