from flask import Flask, render_template, request, jsonify
from face_detection import FaceShapeDetector
import cv2
import numpy as np
import time

app = Flask(__name__)
detector = FaceShapeDetector("shape_predictor_68_face_landmarks.dat")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    file = request.files['image']
    npimg = np.frombuffer(file.read(), np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
    time.sleep(10)
    face_shape = detector.detect_face_shape(img)
    return jsonify({'face_shape': face_shape})

if __name__ == '__main__':
    app.run()
