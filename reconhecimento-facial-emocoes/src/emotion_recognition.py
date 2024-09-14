from deepface import DeepFace
import cv2

def reconhecer_emocoes(frame):
    try:
        analise = DeepFace.analyze(frame, actions=['emotion'])
        emocao_dominante = analise['dominant_emotion']
        cv2.putText(frame, emocao_dominante, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        return frame, emocao_dominante
    except Exception as e:
        print(f"Erro no reconhecimento de emoções: {str(e)}")
        return frame, None
