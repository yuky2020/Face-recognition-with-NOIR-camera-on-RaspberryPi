'''
The following code will import PiCamera module, snap 5 pictures and save it in a directory you specify, wait  2 second  and start again.
the fotoresistor meanwhile will set the ir led to needed light emmission. 
'''
import picamera
from time import sleep
camera = picamera.PiCamera()
camera.resolution=(320,240)

while True:
    camera.start_preview()
    sleep(1)
    camera.capture('photo/image0.jpg')
    camera.capture('photo/image1.jpg')
    camera.capture('photo/image2.jpg')
    camera.capture('photo/image3.jpg')
    camera.capture('photo/image4.jpg')
    camera.capture('photo/image5.jpg')
    camera.capture('photo/image6.jpg')
    camera.capture('photo/image7.jpg')
    camera.capture('photo/image8.jpg')
    camera.capture('photo/image9.jpg')
    camera.stop_preview()
