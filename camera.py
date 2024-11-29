import cv2

# Inicializar la cámara USB (por lo general, la cámara USB se encuentra en el índice 1 o 0, dependiendo de si hay una cámara integrada)
cap = cv2.VideoCapture(0, cv2.CAP_V4L2) 

# Verificar si la cámara se ha abierto correctamente
if not cap.isOpened():
    print("Error: No se pudo abrir la cámara.")
    exit()

# Establecer las características del video (resolución)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)  # Ancho del frame
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)  # Alto del frame

# Definir el codec y el archivo de salida
fourcc = cv2.VideoWriter_fourcc(*'MP4V')  # Codec de video 
out = cv2.VideoWriter('output.mp4', fourcc, 30.0, (480, 320))  # Guardar video en 'output.avi'

while True:
    # Capturar frame por frame
    ret, frame = cap.read()

    if not ret:
        print("Error: No se pudo recibir el frame.")
        break

    # Escribir el frame en el archivo de salida
    out.write(frame)

    # Mostrar el frame en una ventana
    cv2.imshow('Grabar Video', frame)

    # Salir cuando se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar las ventanas
cap.release()
out.release()
cv2.destroyAllWindows()
