import unittest
import cv2
from src.capture import iniciar_captura

class TestCapture(unittest.TestCase):
    
    def test_captura(self):
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        self.assertTrue(ret)
        cap.release()

if __name__ == '__main__':
    unittest.main()
