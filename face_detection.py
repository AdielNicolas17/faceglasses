import cv2
import dlib
import numpy as np

class FaceShapeDetector:
    def __init__(self, predictor_path):
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor(predictor_path)

    def detect_face_shape(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = self.detector(gray)

        if len(faces) == 0:
            return "Nenhum rosto detectado"

        face = faces[0]
        landmarks = self.predictor(gray, face)

        landmarks_points = []
        for n in range(0, 68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            landmarks_points.append((x, y))

        jaw_width = np.linalg.norm(np.array(landmarks_points[0]) - np.array(landmarks_points[16]))
        face_height = np.linalg.norm(np.array(landmarks_points[8]) - np.array(landmarks_points[27]))
        jaw_height = np.linalg.norm(np.array(landmarks_points[8]) - np.array(landmarks_points[57]))

        if jaw_width / face_height > 1.5:
            return "Redondo"
        elif jaw_height / face_height > 0.9:
            return "Oval"
        else:
            return "Quadrado"
