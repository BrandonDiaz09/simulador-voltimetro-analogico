import serial
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# Configurar la conexión serial
ser = serial.Serial('COM3', 19200)  # Ajusta a tu configuración

def leer_serial():
    # Leer desde serial y decodificar
    linea = ser.readline().decode('utf-8').rstrip()
    # Convertir a valor de voltaje
    valor_binario = int(linea)  # Asegúrate de que los datos sean correctos
    voltaje = (valor_binario * 19.6078) / 1000  # Ajustar según tus cálculos
    return voltaje

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
