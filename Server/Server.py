import pysftp
import face_recognition
myHostname = "192.168.1.6"
myUsername = "pi"
myPassword = "facerec1"

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
            uncknow_image = face_recognition.load_image_file("your_file.jpg")
            face_locations = face_recognition.face_locations(image)
            #encode the face in a standard format 
            unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
            #iterate comparison between all saved face 


# connection closed automatically at the end of the with-block
