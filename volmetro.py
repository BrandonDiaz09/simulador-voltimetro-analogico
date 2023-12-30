import serial
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import random
import time

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

# Configurar la conexión serial

# Configurar la ventana de Tkinter
root = tk.Tk()
root.title("Voltímetro Virtual")

# Configurar el gráfico de Matplotlib
figura = Figure(figsize=(6, 5), dpi=100)
sub_plot = figura.add_subplot(111)
canvas = FigureCanvasTkAgg(figura, master=root)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Función de actualización
def actualizar():
    voltaje = leer_serial()
    sub_plot.clear()
    sub_plot.plot(voltaje)  # Actualizar con el nuevo valor
    canvas.draw()
    root.after(1000, actualizar)  # Actualiza cada segundo

# Iniciar la actualización
actualizar()

# Ejecutar el bucle principal
root.mainloop()
