import unittest
from src.emotion_recognition import reconhecer_emocoes
import cv2

class TestEmotionRecognition(unittest.TestCase):
    
    def test_reconhecer_emocoes(self):
        img = cv2.imread('data/images/test_face.jpg')
        frame, emocao = reconhecer_emocoes(img)
        self.assertIsNotNone(emocao)

if __name__ == '__main__':
    unittest.main()
