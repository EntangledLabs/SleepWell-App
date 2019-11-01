import cv2
import pickle

imagePath = "images/4/image4.png"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')

image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("./recognizers/face-trainner.yml")

labels = {"person_name": 1}
with open("pickles/face-labels.pickle", 'rb') as f:
	og_labels = pickle.load(f)
	labels = {v:k for k,v in og_labels.items()}

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5
)

for (x, y, w, h) in faces:
    roi_gray = gray[y:y+h, x:x+w] #(ycord_start, ycord_end)
    # recognize? deep learned model predict keras tensorflow pytorch scikit learn
    id_, conf = recognizer.predict(roi_gray)
    print(labels[id_])
