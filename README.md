# Face recognition with NOIR camera on RaspberryPi

## Why:

This is the project for the course of biometric system.

NOIR camera is a rapspberry pi camera module where there is no ir filter, abbinated with 2 ir light let you see image also in low and no light condition with good  contrast in grayscale, so could provide face recognition also in low light condition with direct ir light that make the subject illuminated omogenusly  . 

The model of Raspberry pi that is used is the zero w ( is the  one with lower computational power, lower power consume and wireless connectivity ),  reasonably implementable also in a multimodal biometric system .

## Requirement:

- RaspberryPi ZeroW or 4/3/2

- RaspberryPi NOIR camera + ir lights and fotoresistor .

- Any Kind of server with Docker(could also be another RaspberryPi or a remote server)  (for the not standalone version)

- Any other camera device as a phone cam or a web cam for enrollment (if you don't want to enroll  on the camera directly ).

- Lan connection between server and raspberry

## Prerequisite:

- Ssh connection enable on RaspberryPi

- python 3 on raspberry pi with camera module import avaible 

## Features

- [x] Face recognition in no light with optimal result also with  non coperative users

- [x] Fotoresistor auto turn on ir light in low and no light condiction  

- [ ] Use of  more sequential image (5) and distance mesure for evaluate lan intrusion(if the sequential  probe images presence all the exact same distance there is  with high probably an intrusion in the network )

- [ ] Presence of anti spoofing tecnique

- [x] Fast operation with no buffering 

- [ ] Biometric system as a service in a future multimodal version (array of data from various pi are evaluated to bring a more precise response  )
  
   

## Project structure
