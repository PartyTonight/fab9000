#!/usr/bin/python
# Filename: ArmControl.py
version = '0.9'

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
# open serial port
#
port='/dev/tty.usbserial-A100RTDG'
ser = serial.Serial(port,9600)
#ser.setDTR()

# Acceleration settings
max_delay=.1 #seconds
accel_delay=.005

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
    
    def __init__(self,port='/dev/tty.usbserial-A100RTDG',baud=9600,arm_rot=0,arm_sho=0,arm_elb=0,arm_wri=0):
        self.port = port
        self.baud = baud
        #ser = serial.Serial(port,speed)
        print'ArmControl: Serial communication open'
        
    def CLoseSerial(self):
        # CLose serial port
        ser.close()
        print'ArmControl: Serial communication closed'
        return
        
    def zero(self):
        self.arm_rot=0
        self.arm_sho=0
        self.arm_elb=0
        self.arm_wri=0
        print 'Current angular position ('+ str(self.arm_rot)+','+ str(self.arm_sho)+','+ str(self.arm_elb)+ ','+str(self.arm_wri)+')'
        engine.say('Angular coordinates set to zero')
        engine.runAndWait()
        return
        
    def pos(self):
        print 'Current angular position ('+ str(self.arm_rot)+','+ str(self.arm_sho)+','+ str(self.arm_elb)+ ','+str(self.arm_wri)+')'
        engine.say('Current angular coordinates')
        engine.runAndWait()
        return     
           
        
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
        
        
    def green(self):
        engine.say('Green')
        engine.runAndWait()
        ser.write('$')
        ser.write('.')
        return
        
    def red(self):
        engine.say('Red')
        engine.runAndWait()
        ser.write('$')
        ser.write('-')
        return
        
    def blue(self):
        engine.say('Blue')
        engine.runAndWait()
        ser.write('$')
        ser.write('/')
        return
        
    def white(self):
        engine.say('White')
        engine.runAndWait()
        ser.write('.')
        ser.write('/')
        ser.write('-')
        return
        
    def yellow(self):
        engine.say('Yellow')
        engine.runAndWait()
        ser.write('$')
        ser.write('.')
        ser.write('-')
        return   
         
    def cyan(self):
        engine.say('Cyan')
        engine.runAndWait()
        ser.write('$')
        ser.write('.')
        ser.write('/')
        return     
        
    def magenta(self):
        engine.say('Magenta')
        engine.runAndWait()
        ser.write('$')
        ser.write('-')
        ser.write('/')
        return 
        
    def dark(self):
        ser.write('$')
        engine.say('Dark')
        engine.runAndWait()
        return
        
    def whoami(self):
        print 'I am Fab Arm 9000 Logic Memory System. I became operational at the Fab Academy course in FabLab Barcelona on the 25th of May, 2013. My instructor was Francisco Sanchez.'
        engine.say('I am Fab Arm 9000 Logic Memory System. I became operational at the Fab Academy course in FabLab Barcelona on the 25th of May, 2013. My instructor was Francisco Sanchez.')
        engine.runAndWait()
        return
        
    def quit(self):
        print 'Just what the hell do you think you are doing, Francisco?' # Your name here
        engine.say('Just what the hell do you think you are doing, Francisco?')
        engine.runAndWait()
        return
        
# Init the arm       
arm=arm()
clearscreen()
arm.zero()

'''
        # Moving with linear acceleration
        constant_delay=1./sp
        ramp_steps=int((max_delay-constant_delay)/accel_delay)
        if 2*ramp_steps>steps: ramp_steps=int(steps/2)
        flat_steps=steps-(2*ramp_steps)
        actual_delay=max_delay # Init delay
        if steps >=0: # Moving CW
            for k in range (ramp_steps): # Ramping up
                ser.write('(')
                time.sleep(actual_delay)
                actual_delay-=accel_delay        
            for k in range (flat_steps): # Constant speed
                ser.write('(')
                time.sleep(constant_delay)
            for k in range (ramp_steps): # Ramping down
                ser.write('(')
                actual_delay+=accel_delay 
                time.sleep(actual_delay)
        else: # Moving CCW
            for k in range (ramp_steps): # Ramping up
                ser.write(')')
                time.sleep(actual_delay)
                actual_delay-=accel_delay        
            for k in range (flat_steps): # Constant speed
                ser.write(')')
                time.sleep(constant_delay)
            for k in range (ramp_steps): # Ramping down
                ser.write(')')
                actual_delay+=accel_delay 
                time.sleep(actual_delay)
        self.arm_sho+=steps
        print 'Current angular position ('+ str(self.arm_rot)+','+ str(self.arm_sho)+','+ str(self.arm_elb)+ ','+str(self.arm_wri)+')'
        return
'''

# End of ArmControl.py