import spidev
from gpiozero import MCP3008
from gpiozero import Button
from time import sleep
import socket

# Configuración del MCP3008 para cada señal de los joysticks
x1_joystick = MCP3008(channel=0, clock_pin=21, mosi_pin=20, miso_pin=19, select_pin=13)  # Eje X del Joystick 1
y1_joystick = MCP3008(channel=1, clock_pin=21, mosi_pin=20, miso_pin=19, select_pin=13)  # Eje Y del Joystick 1
x2_joystick = MCP3008(channel=2, clock_pin=21, mosi_pin=20, miso_pin=19, select_pin=13)  # Eje X del Joystick 2
y2_joystick = MCP3008(channel=3, clock_pin=21, mosi_pin=20, miso_pin=19, select_pin=13)  # Eje Y del Joystick 2

button1 = Button(4)
button2 = Button(26)

# Configurar el socket del cliente para enviar datos
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("192.168.1.16", 5000))  # Dirección IP del servidor

print("Conectado al servidor")

while True:
    # Leer los valores de los ejes del Joystick derecho e invertirlos, y convertir a enteros
    x2_value = int(255 - (x2_joystick.value * 255))
    y2_value = int(255 - (y2_joystick.value * 255))
    
    # Leer los valores de los ejes del Joystick izquierdo y convertir a enteros
    x1_value = int(x1_joystick.value * 255)
    y1_value = int(y1_joystick.value * 255)

    button1_state = 1 if button1.is_pressed else 0
    button2_state = 1 if button2.is_pressed else 0

    # Crear el mensaje a enviar
    message = f"{x1_value},{y1_value},{x2_value},{y2_value},{button1_state},{button2_state}"
    client_socket.send(message.encode())
    print(f"Enviado: {message}")
    sleep(0.5)
