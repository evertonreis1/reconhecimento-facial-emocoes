import unittest
import cv2
from src.face_detection import detectar_face

class TestFaceDetection(unittest.TestCase):
    
    def test_detectar_face(self):
        img = cv2.imread('data/images/test_face.jpg')
        frame, faces = detectar_face(img)
        self.assertGreater(len(faces), 0)

if __name__ == '__main__':
    unittest.main()
