import pysftp
import face_recognition
import os 
import numpy as np
#run indicate the actual state of the server
run=True
#the hostname or address of the raspberry pi
myHostname = "192.168.1.6"
#the username of the pi
myUsername = "pi"
#the pass of the pi 
myPassword = "facerec1"
#directory of know faces 
knowdirectory = r'known_faces'
known_faces=[]
known_faces_encodings=[]
known_faces_names=[]
k=0
#iterate trouhght all 
for filename in os.listdir(knowdirectory):
    know_faces_names[k]=filename
    known_faces[k]=face_recognition.load_image_file(filename)
    known_faces_encodings[k]=face_recognition.face_encodings(known_faces[k])[0]
    k=k+1

with pysftp.Connection(host=myHostname, username=myUsername, password=myPassword) as sftp:
    print("Connection succesfully stablished ... ")
    while(run):
        #save the distance of the best result  for evry istance and the index of the know person in the  list identificated,
        #if the distance of the best result point to the same person and are equal there is probably an attack on the lan
        # so rise an allarm   
        savedDistances=[]
        savedPersonIndex=[]
        allarmRise=True

        for i in range(5):   
            # Define the file that you want to download from the raspberry directory
            remoteFilePath = 'photo/image{}.jpg'.format(i)
            # Define the local path where the file will be saved
            localFilePath = 'unknown/unknown{}.jpg'.format(i)
            #get the file from raspberry
            sftp.get(remoteFilePath, localFilePath)
            #load the image and extrapolate faces in the image  using viola-jones algorithm  
            unknown_image = face_recognition.load_image_file("unknown/unknown{}".format(i))
            #Save the location for the varius faces 
            unknown_face_locations = face_recognition.face_locations(unknown_image)
            #encode the faces in a standard format 
            unknown_face_encodings = face_recognition.face_encodings(unknown_image,unknown_face_locations)
            #Loop through each face found in the unknown image
            # and operate comparison between encodings
            for (top, right, bottom, left), face_encoding in zip(unknown_face_locations, unknown_face_encodings):
                # See if the face is a match for the known faces, (operate comparison between all encodings
                #using array of true,false value
                matches = face_recognition.compare_faces(known_faces_encodings[k], face_encoding)
                 #set the name as unknown
                name = "Unknown"
                #use the known face with the smallest distance to the new face as the  valuable one
                #calcolate array of face distance
                face_distances = face_recognition.face_distance(known_faces_encodings, face_encoding)
                #take the best one as the argmin 
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_faces_names[best_match_index]
                    #add distance  to the distance list 
                    savedDistances.append(face_distances[best_match_index])
                    #add index to the index list 
                    savedPersonIndex.append(best_match_index)
                    #if a person is found print it .
                    print("found a person named {}".format(name))

        for i in savedPersonIndex:
            if(savedPersonIndex[i]!=savedPersonIndex[i+1] or savedDistances[i]!=savedDistances[i+1]):
                allarmRise=False 
                
        if(allarmRise):
            #close the server  
            print("lan is compromised the server shotdown for security reason ")
            run=False        





# connection closed automatically at the end of the with-block
