import cv2

def iniciar_captura():
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Erro ao acessar a webcam.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow('Captura de Vídeo', frame)

        # Pressione 'q' para sair
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
