import pysftp
import face_recognition
import os 
#the hostname or address of the raspberry pi
myHostname = "192.168.1.6"
#the username of the pi
myUsername = "pi"
#the pass of the pi 
myPassword = "facerec1"
#directory of know faces 
knowdirectory = r'known_faces'
known_faces=[]
known_faces_encoding=[]
k=0
#iterate trouhght all 
for filename in os.listdir(knowdirectory):
    known_faces[k]=face_recognition.load_image_file(filename)
    known_faces_encoding[k]=face_recognition.face_encodings(known_faces[k])
    k=k+1

with pysftp.Connection(host=myHostname, username=myUsername, password=myPassword) as sftp:
    print("Connection succesfully stablished ... ")
    while(True):
        for i in range(5):
            # Define the file that you want to download from the raspberry directory
            remoteFilePath = 'photo/image{}.jpg'.format(i)
            # Define the local path where the file will be saved
            localFilePath = 'unknow/unknow{}.jpg'.format(i)
            #get the file from raspberry
            sftp.get(remoteFilePath, localFilePath)
            #load the image and extrapolate faces using viola-jones algorithm  
            unknown_image = face_recognition.load_image_file("your_file.jpg")
            face_locations = face_recognition.face_locations(unknown_image)
            #encode the face in a standard format 
            unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
            #iterate comparison between all saved image encoding
            for k in list:
                #operate comparison between encoding  
                results = face_recognition.compare_faces(known_faces_encoding[k], unknown_face_encoding)



# connection closed automatically at the end of the with-block
