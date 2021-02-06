# This is  face recognition on a Raspberry Pi.
# This program will print out the names of anyone it recognizes to the console.

# To run this, you need a Raspberry Pi 2 (or greater) with face_recognition and
# the picamera[array] module installed.

import face_recognition
import picamera
import numpy as np
import os 

# Get a reference to the Raspberry Pi camera.
# If this fails, make sure you have a camera connected to the RPi and that you
# enabled your camera in raspi-config and rebooted first.
camera = picamera.PiCamera()
camera.resolution = (320, 240)
output = np.empty((240, 320, 3), dtype=np.uint8)

#directory of know faces 
knowdirectory = r'known_faces'
known_faces=[]
known_faces_encodings=[]
known_faces_names=[]
matches=[]
k=0

# Load  known faces and encode it.
for filename in os.listdir(knowdirectory):
    known_faces_names.append(filename)
    known_faces.append(face_recognition.load_image_file("known_faces/{}".format(filename)))
    known_faces_encodings.append(face_recognition.face_encodings(known_faces[k])[0])
    k=k+1


print("Loading known face image(s)")
obama_image = face_recognition.load_image_file("obama_small.jpg")
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

# Initialize some variables
face_locations = []
face_encodings = []

while True:
    print("Capturing image.")
    # Grab a single frame of video from the RPi camera as a numpy array
    camera.capture(output, format="rgb")

    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(output)
    print("Found {} faces in image.".format(len(face_locations)))
    face_encodings = face_recognition.face_encodings(output, face_locations)

    # Loop over each face found in the frame to see if it's someone we know.
    for face_encoding in face_encodings:
      # See if the face is a match for the known face(s)
      matches=(face_recognition.compare_faces(known_faces_encodings, face_encoding))
      #set the name as unknown
      name = "Unknown"
      #use the known face with the smallest distance to the new face as the  valuable one
      #calcolate array of face distance
      face_distances = face_recognition.face_distance(known_faces_encodings, face_encoding)
      #take the best one as the argmin 
      best_match_index = np.argmin(face_distances)
      if matches[best_match_index]:
                name = known_faces_names[best_match_index]
                #if a person is found print it .
                print("found a person named {}".format(name))