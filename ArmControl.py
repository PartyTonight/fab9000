#!/usr/bin/python
# Filename: ArmControl.py
version = '1.0'

# VIRTUAL CONTROL ARM PROGRAMMING LANGUAGE
# INSPIRED IN LOGO LANGUAGE

# Created by Francisco from Fab Academy 2013 in Fab lab Barcelona
# May 2013
# Released under MIT license http://opensource.org/licenses/MIT

# ======= Characters =======
# -------------------------- 
# Motor | CW char | CCW char
# --------------------------
#   1   |    (    |    )
#   2   |    [    |    ]
#   3   |    {    |    }
#   4   |    <    |    >
# --------------------------
# LED off         |    $
# LED red         |    -
# LED green       |    .
# LED blue        |    /
# --------------------------

import serial
import time
import numpy
import math
import os
import sys
import pyttsx

#
# init the TTS engine
#
engine = pyttsx.init()

#
# Parameters
#
port='/dev/tty.usbserial-A100RTDG' # serial communication port
baud=9600 # connection speed in baud
name='Francisco' # write your name here
max_delay=.1 # seconds
accel_delay=.005 # seconds


#
# open serial port
#
    def OpenSerial(self,port,baud):
        # Open serial port
        ser = serial.Serial(port,baud)
        print'ArmControl: Serial communication opened'
        return

#
# close serial port
#
    def CloseSerial(self):
       # CLose serial port
       ser.close()
       print'ArmControl: Serial communication closed'
       return

#
# define clearscreen()
#
def clearscreen(numlines=100):
    #Clear the console.
    #numlines is an optional argument used only as a fall-back.
    #
    if os.name == "posix":
        # Unix/Linux/MacOS/BSD/etc
        os.system('clear')
    elif os.name in ("nt", "dos", "ce"):
        # DOS/Windows
        os.system('CLS')
    else:
        # Fallback for other operating systems.
        print '\n' * numlines
    print 'Welcome to ArmControl.py version '+ version
    print 'Created by Francisco Sanchez Arroyo. Fab Academy 2013'
    print 'Type help() for help'
    print 'System Ready!'
    ser.write('-')
    ser.write('$')
    ser.write('.')
    ser.write('$')
    ser.write('/')
    ser.write('$')
    engine.say('Arm System Ready.')
    engine.runAndWait()
    
#
# define help()
#
def help():
        print '#####################################'
        print '# ArmControl.py currently supports: #'
        print '#####################################'
        print ''
        print '  help() # This help'
        print '  clearscreen() # Clears the console'
        print ''
        print '  Arm movements:'
        print '  --------------'
        print '  arm.zero() # Resets coordinates'
        print '  arm.pos() # Returns current coordinates'
        print '  arm.rotate(steps,speed) # Rotate arm angle'
        print '  arm.shoulder(steps,speed) # Rotate shoulder angle'
        print '  arm.elbow(steps,speed) # Rotate elbow angle'
        print '  arm.wrist(steps,speed) # Rotate wrist angle'
        print ''
        print '  Colors:'
        print '  -------'
        print '  arm.red() # Change color to red'
        print '  arm.green() # Change color to green'
        print '  arm.blue() # Change color to blue'
        print '  arm.yellow() # Change color to yellow'
        print '  arm.cyan() # Change color to cyan'
        print '  arm.magenta() # Change color to magenta'
        print '  arm.white() # Change color to white'
        print '  arm.dark() # Turn off the LED'
        print ''
        print '  exit() # Quit to shell'
        print '  ######################'

        
#
# DEFINE CLASS ARM
#
class arm:
    
    def __init__(self,arm_rot=0,arm_sho=0,arm_elb=0,arm_wri=0):
                
    # define routine for zeroing coordinates
    def zero(self):
        self.arm_rot=0
        self.arm_sho=0
        self.arm_elb=0
        self.arm_wri=0
        print 'Current angular position ('+ str(self.arm_rot)+','+ str(self.arm_sho)+','+ str(self.arm_elb)+ ','+str(self.arm_wri)+')'
        engine.say('Angular coordinates set to zero')
        engine.runAndWait()
        return
        
    # define routine for return current coordinates
    def pos(self):
        print 'Current angular position ('+ str(self.arm_rot)+','+ str(self.arm_sho)+','+ str(self.arm_elb)+ ','+str(self.arm_wri)+')'
        engine.say('Current angular coordinates')
        engine.runAndWait()
        return                  
        
    # define routine for rotating the arm
    def rotate(self,steps,sp):
        engine.say('Rotating Arm')
        engine.say(steps)
        engine.say('steps at')
        engine.say(sp)
        engine.say('steps per second')
        engine.runAndWait()
        # Moving step by step
        constant_delay=1./sp
        print constant_delay
        if steps >= 0:
            for k in range (steps):
                ser.write('(')
                time.sleep(constant_delay)
        else:
            for k in range (-steps):
                ser.write(')')
                time.sleep(constant_delay)
        self.arm_rot+=steps
        print 'Current angular position ('+ str(self.arm_rot)+','+ str(self.arm_sho)+','+ str(self.arm_elb)+ ','+str(self.arm_wri)+')'
        return
        
        
    # define routine for moving shoulder joint
    def shoulder(self,steps,sp):
        engine.say('Rotating shoulder')
        engine.say(steps)
        engine.say('steps at')
        engine.say(sp)
        engine.say('steps per second')
        engine.runAndWait()
        # Moving step by step
        constant_delay=1./sp
        print constant_delay
        if steps >= 0:
            for k in range (steps):
                ser.write('[')
                time.sleep(constant_delay)
        else:
            for k in range (-steps):
                ser.write(']')
                time.sleep(constant_delay)
        self.arm_rot+=steps
        print 'Current angular position ('+ str(self.arm_rot)+','+ str(self.arm_sho)+','+ str(self.arm_elb)+ ','+str(self.arm_wri)+')'
        return

        
    
    # define routine for moving elbow joint
    def elbow(self,steps,sp):
        engine.say('Rotating elbow')
        engine.say(steps)
        engine.say('steps at')
        engine.say(sp)
        engine.say('steps per second')
        engine.runAndWait()
        # Moving step by step
        constant_delay=1./sp
        print constant_delay
        if steps >= 0:
            for k in range (steps):
                ser.write('{')
                time.sleep(constant_delay)
        else:
            for k in range (-steps):
                ser.write('}')
                time.sleep(constant_delay)
        self.arm_rot+=steps
        print 'Current angular position ('+ str(self.arm_rot)+','+ str(self.arm_sho)+','+ str(self.arm_elb)+ ','+str(self.arm_wri)+')'
        return
               
    # define routine for moving wrist joint
    def wrist(self,steps,sp):
        engine.say('Wrist moving')
       # engine.say(steps)
        #engine.say('steps at')
       # engine.say(sp)
       # engine.say('steps per second')
        engine.runAndWait()
        # Moving step by step
        constant_delay=1./sp
        print constant_delay
        if steps >= 0:
            for k in range (steps):
                ser.write('<')
                time.sleep(constant_delay)
        else:
            for k in range (-steps):
                ser.write('>')
                time.sleep(constant_delay)
        self.arm_rot+=steps
        print 'Current angular position ('+ str(self.arm_rot)+','+ str(self.arm_sho)+','+ str(self.arm_elb)+ ','+str(self.arm_wri)+')'
        return
        
    # define routine for turning LED to green       
    def green(self):
        engine.say('Green')
        engine.runAndWait()
        ser.write('$')
        ser.write('.')
        return
        
    # define routine for turning LED to red       
    def red(self):
        engine.say('Red')
        engine.runAndWait()
        ser.write('$')
        ser.write('-')
        return
        
    # define routine for turning LED to blue       
    def blue(self):
        engine.say('Blue')
        engine.runAndWait()
        ser.write('$')
        ser.write('/')
        return
        
    # define routine for turning LED to white       
    def white(self):
        engine.say('White')
        engine.runAndWait()
        ser.write('.')
        ser.write('/')
        ser.write('-')
        return
        
    # define routine for turning LED to yellow       
    def yellow(self):
        engine.say('Yellow')
        engine.runAndWait()
        ser.write('$')
        ser.write('.')
        ser.write('-')
        return   
         
    # define routine for turning LED to cyan       
    def cyan(self):
        engine.say('Cyan')
        engine.runAndWait()
        ser.write('$')
        ser.write('.')
        ser.write('/')
        return     
        
    # define routine for turning LED to magenta       
    def magenta(self):
        engine.say('Magenta')
        engine.runAndWait()
        ser.write('$')
        ser.write('-')
        ser.write('/')
        return 
        
    # define routine for turning LED off       
    def dark(self):
        ser.write('$')
        engine.say('Dark')
        engine.runAndWait()
        return
        
    # define routine for saying whoami       
    def whoami(self):
        print 'I am Fab Arm 9000 Logic Memory System. I became operational at the Fab Academy course in FabLab Barcelona on the 25th of May, 2013. My instructor was Francisco Sanchez.'
        engine.say('I am Fab Arm 9000 Logic Memory System. I became operational at the Fab Academy course in FabLab Barcelona on the 25th of May, 2013. My instructor was Francisco Sanchez.')
        engine.runAndWait()
        return
        
    # define routine for turning turning off FAB 9000       
    def quit(self):
        print 'Just what do you think you are doing, Francisco?' # Your name here
        engine.say('Just what do you think you are doing, Francisco?')
        engine.runAndWait()
        return

#        
# Init FAB 9000
#
OpenSerial(port,baud) # open serial connection       
arm=arm() # create an instance of the class arm
clearscreen() # clear the screen


# End of ArmControl.py