FAB 9000
========

This is the public repository for the project `Robotic Arm Fab9000`. Fab 9000 is an Open Source harware robotic arm and an Open Source real time control framework for robotic arms. The CAD is fully parametrical and has been entirely designed in `kokopelli`.

The goal of this project is to create a common open source framework for constructing and operating robotic arms. If you feel that you can help in this goal, please feel free to fork the code and improve it.

Mark I version
==============
This was the version developed for my Fab Academy 2013 final project. The hardware consists of a network of attiny electronic boards connected to a computer via serial communication and controlled in real time with a python script. The boards were also designed in `kokopelli`. The usage is the following:

Open a terminal window in the directory where the files are located, and load a python interpreter, usually typing:

`python`

In the terminal window. You will see that the bash changes to `>>>` and then run:

`>>> from ArmControl import *`

And then follow the on screen instructions. As seen on: http://academy.cba.mit.edu/2013/students/sanchez.francisco/index.html

Mark II version
===============
This is the version which is currently being developed for the Maker Faire Rome 2013, the european edition. The hardware consists of Arduino and easydriver stepper drivers. It shares the python script control with Mark I version but it also has full manual overrride control.

One of the goals of Mark II is to port the arduino and the easydriver design to `kokopelli`.


