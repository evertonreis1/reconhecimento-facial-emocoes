import cv2
from src.capture import iniciar_captura
from src.face_detection import detectar_face
from src.emotion_recognition import reconhecer_emocoes

def executar_projeto():
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Erro ao acessar a webcam.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Detecção de faces
        frame, faces = detectar_face(frame)
        
        # Reconhecimento de emoções
        frame, emocao = reconhecer_emocoes(frame)

        # Exibe o vídeo processado
        cv2.imshow('Reconhecimento Facial com Emoções', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    executar_projeto()
