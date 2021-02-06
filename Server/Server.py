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
matches=[]
k=0
#iterate trouhght all 
for filename in os.listdir(knowdirectory):
    known_faces_names.append(filename)
    known_faces.append(face_recognition.load_image_file("known_faces/{}".format(filename)))
    known_faces_encodings.append(face_recognition.face_encodings(known_faces[k])[0])
    k=k+1
while(run):
    #save the distance of the best result  for evry istance and the index of the know person in the  list identificated,
    #if the distance of the best result point to the same person and are equal there is probably an attack on the lan
    # so rise an allarm   
    savedDistances=[]
    savedPersonIndex=[]
    allarmRise=False
    with pysftp.Connection(host=myHostname, username=myUsername, password=myPassword) as sftp:
        print("Connection succesfully stablished ... ")
        for i in range(10):   
            # Define the file that you want to download from the raspberry directory
            remoteFilePath = 'photo/image{}.jpg'.format(i)
            # Define the local path where the file will be saved
            localFilePath = 'unknown/unknown{}.jpg'.format(i)
            #get the file from raspberry
            sftp.get(remoteFilePath, localFilePath)

    # connection closed automatically at the end of the with-block

    #there is a file losing during real time transfer, one evry 20 frames usualy 
   

    for i in range(10):
        try:    
                #load the image and extrapolate faces in the image using  Histogram of OrientedGradients (HOG)
                #feature combined with a linear classifier, an image pyramid, and sliding window detection scheme.  
                #This type of object detector is fairly general and capable of detecting  also other  types of semi-rigid objects  
                unknown_image = face_recognition.load_image_file("unknown/unknown{}.jpg".format(i))
                #Save the location for the varius faces 
                unknown_face_locations = face_recognition.face_locations(unknown_image)
                #encode the faces in a standard format 
                unknown_face_encodings = face_recognition.face_encodings(unknown_image,unknown_face_locations)
                #Loop through each face found in the unknown image
                # and operate comparison between encodings
                for face_encoding in unknown_face_encodings:
                    # See if the face is a match for the known faces, (operate comparison between all encodings
                    #using array of true,false value
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
                        #add distance  to the distance list 
                        savedDistances.append(face_distances[best_match_index])
                        #add index to the index list 
                        savedPersonIndex.append(best_match_index)

                    #if a person is found print it .
                    print("found a person named {}".format(name))

        except: print("one image is lost during the tranfert")



#if there is more than 8 equal result there is probably a lan introduction       
if len(savedPersonIndex)>=8:
    #check if lan is exoposed
    lanex=True
    for i in savedPersonIndex:
        for j in savedPersonIndex:
            if(savedPersonIndex[i]!=savedPersonIndex[j] or savedDistances[i]!=savedDistances[j]):
                lanex=False
    #if the lan is exposed kill the process
    if lanex:allarmRise=True

    if(allarmRise):
        #close the server  
        print("lan is compromised the server shotdown for security reason ")
        run=False        






