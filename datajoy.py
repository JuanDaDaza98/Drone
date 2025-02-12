import socket
from gpiozero import LED

# Configuración de los LEDs
led1 = LED(17)
led2 = LED(27)
led3 = LED(22)

# Configuración del socket del servidor para recibir datos
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("192.168.1.16", 5000))  # Dirección IP del servidor
server_socket.listen(1)

print("Esperando conexión...")

client_socket, client_address = server_socket.accept()
print(f"Conexión recibida de {client_address}")

leds_on = False
button2_prev_state = 0

try:
    while True:
        data = client_socket.recv(1024)
        if data:
            # Convertir los datos recibidos en una lista de enteros
            joystick_data = list(map(int, data.decode().split(',')))
            x1_value, y1_value, x2_value, y2_value, button1_state, button2_state = joystick_data
            print(f"{x1_value},{y1_value},{x2_value},{y2_value},{button1_state},{button2_state}") # Controlar los LEDs según el estado del primer botón
            if button2_state == 1 and button2_prev_state == 0:
                if not leds_on:
                    led1.on()
                    led2.on()
                    led3.on()
                    leds_on = True
                else:
                    led1.off()
                    led2.off()
                    led3.off()
                    leds_on = False
except KeyboardInterrupt:
    client_socket.close()
    server_socket.close()
