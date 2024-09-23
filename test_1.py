import cv2 # importamos open CV
import numpy as np # importamos numPy

# Iniciar la cámara (funcion de la libreria de Open CV)
cap = cv2.VideoCapture(0)

# Crear un objeto de fondo para el método de sustracción de fondo
fgbg = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=16, detectShadows=False)

# usamos un while True para que sea infinito hasta que se decida salir
while True:
    # Capturar el frame de la cámara
    frame = cap.read()

    # Aplicar el sustractor de fondo para obtener la máscara
    fgmask = fgbg.apply(frame)

    # Contar los píxeles no negros en la máscara
    non_zero_count = np.count_nonzero(fgmask)

    # Si hay suficientes píxeles no negros, se asume que hay un objeto
    if non_zero_count > 500:  # Puedes ajustar este valor dependiendo de la sensibilidad
        print("Objeto detectado")
    else:
        print("No hay objeto")

    # Salir si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar las ventanas
cap.release()
cv2.destroyAllWindows()
