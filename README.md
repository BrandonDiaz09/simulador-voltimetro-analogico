# Simulador de Voltímetro Analógico

Este proyecto es un simulador de voltímetro analógico creado con Python, utilizando la librería Tkinter para la interfaz gráfica y Matplotlib para la representación gráfica del voltímetro. Está diseñado para simular la funcionalidad de un voltímetro analógico, permitiendo a los usuarios visualizar las mediciones de voltaje en una interfaz gráfica que simula un medidor analógico con una aguja móvil.

## Características

- **Interfaz Gráfica**: Una representación visual del voltímetro con una aguja que indica el valor del voltaje medido.
- **Simulación de Datos**: Capacidad para simular mediciones de voltaje a través de datos generados aleatoriamente o leer datos en tiempo real desde una conexión serial.
- **Personalización**: Posibilidad de adaptar la escala del medidor, el rango de valores y la apariencia general según las necesidades específicas.

## Tecnologías Utilizadas

- **Python**: Lenguaje de programación utilizado para desarrollar la lógica del simulador.
- **Tkinter**: Biblioteca de Python para la creación de interfaces gráficas.
- **Matplotlib**: Biblioteca de Python para la visualización de datos con gráficos de calidad.
- **Serial**: Comunicación con dispositivos externos para la obtención de mediciones reales.

## Cómo Usarlo

Sigue estos pasos para configurar y ejecutar el simulador de voltímetro analógico:

### Instalación

1. **Clona el Repositorio**: Clona este repositorio a tu máquina local usando `git clone`.

2. **Python**: Asegúrate de tener Python instalado en tu sistema. Este proyecto es compatible con Python 3.x.

3. **Entorno Virtual** (Opcional, pero recomendado):  
   - Crea un entorno virtual para el proyecto:  
     ```
     python -m venv venv
     ```
   - Activa el entorno virtual:  
     - En Windows: `.\venv\Scripts\activate`
     - En Unix o MacOS: `source venv/bin/activate`

4. **Instalar Dependencias**: Instala todas las dependencias necesarias usando el archivo `requirements.txt` incluido en el repositorio:
     ```
     pip install -r requirements.txt
     ```
  

### Ejecución

- **Corre el Simulador**: Una vez configurado el entorno y las dependencias, ejecuta el script `volmetro_analogico.py` para iniciar la interfaz gráfica y el simulador:
  ```
  python volmetro_analogico.py
  ```

### Uso del Simulador

- **Simulación/Conexión Serial**: Puedes alternar entre usar datos simulados o leer desde un puerto serial para obtener mediciones de voltaje reales. Asegúrate de configurar correctamente el puerto serial en el código si optas por la lectura real.

## Contribuciones

Las contribuciones son bienvenidas. Si tienes ideas para mejorar la aplicación o añadir nuevas funcionalidades, por favor, considera enviar un pull request o abrir un issue.
