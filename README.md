# Face recognition with NOIR camera on RaspberryPi

## Why:

This is the project for the course of biometric system.

NOIR camera is a rapspberry pi camera module where there is no ir filter, abbinated with 2 ir light let you see image also in low and no light condition with good  contrast in grayscale, so could provide face recognition also in low light condition with direct ir light that make the subject illuminated omogenusly  . 

The model of Raspberry pi that is used is the zero w ( is the  one with lower computational power, lower power consume and wireless connectivity ),  reasonably implementable also in a multimodal biometric system .

## Requirement:

- RaspberryPi ZeroW or 4/3/2

- RaspberryPi NOIR camera + ir lights and photoresistor .

- Any Kind of server with Docker(could also be another RaspberryPi or a remote server)  (for the not standalone version)

- Any other camera device as a phone cam or a web cam for enrollment (if you don't want to enroll  on the camera directly ).

- Lan connection between server and raspberry

## Prerequisite:

- Ssh connection enable on RaspberryPi

- python 3 on raspberry pi with camera module import avaible 

## Features

- [x] Face recognition in no light with optimal result also with  non coperative users

- [x] Fotoresistor auto turn on ir light in low and no light condiction  

- [x] Use of  more sequential image (5) and distance mesure for evaluate lan intrusion(if the sequential  probe images presence all the exact same distance there is  with high probably an intrusion in the network )

- [x] Presence of anti spoofing tecnique,done by design, screen and printed face  image reflect badly ir light and make spofing very difficult. 

- [x] Fast operation with no buffering 

- [ ] Biometric system as a service in a future multimodal version (array of data from various pi are evaluated to bring a more precise response  )

## Project structure:

![](https://raw.githubusercontent.com/yuky2020/Face-recognition-with-NOIR-camera-on-RaspberryPi/main/readmeImage/projectStructure.png)

The raspberry pi zero w is connected to the camera and save 10 frames per second.

The ir li

## Design choise:

1.Using  dlib  HOG feature descriptor  to extract the features pixel by pixel with the     help of gradients.

       ![](https://raw.githubusercontent.com/yuky2020/Face-recognition-with-NOIR-camera-on-RaspberryPi/main/readmeImage/Hog.png)

    why not a deep lerning based ones why not use wavelets, why the Hog from dlib?

    Because dilib hog algorithm is generaly faster and works on grayscale images with     low resorces used,  so it's perfect to be used with ir light and to work with real time     video, i have done some testing also with a cnn model, but my system can't     elaborate   more than 5 of  the 10 frames sended every second. even with     paralaization  of the process; so i conclude that using a cnn model is not realiable for     a  multimodal face recognition system.

2.face encodings:Given a image, return the 128-dimension face encoding for each face     in the image.

      ![](https://cdn-images-1.medium.com/max/1600/1*AbEg31EgkbXSQehuNJBlWg.png)
