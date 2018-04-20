#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import smbus,numpy,math

#Global variables

#Device addresses
MAG_ADDRESS = 0x1E 

#magnetometer-related
CTRL_REGA = 0x00
CTRL_REGB = 0x01
CTRL_MODE = 0x02
OUT_X_L_M = 0x04
OUT_X_H_M = 0x03
OUT_Y_L_M = 0x08
OUT_Y_H_M = 0x07
OUT_Z_L_M = 0x06
OUT_Z_H_M = 0x05

#define objects
bus = smbus.SMBus(1)    # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)

#initialize accelerometer
#bus.write_byte_data(ACC_ADDRESS,CTRL_REG1_A,0x27) #bring the accelerometer into normal operation mode with ODR 50Hz
#keep a full scale range +/-2 gauss in continuous data update mode and change the little-endian to a big-endian structure.
#where MSB is located at lower address
#bus.write_byte_data(ACC_ADDRESS,CTRL_REG4_A,0x40)

#initialize magnetometer
#try:

bus.write_byte_data(MAG_ADDRESS,CTRL_MODE,0x00) 
#except IOError:
#    subprocess.call(['i2cdetect', '-y', '1'])
#    flag = 1     #optional flag to signal your code to resend or something

#setup to change board numbering schema to use phyiscal pin layout (not GPIO numbers)
GPIO.setmode(GPIO.BOARD)

#setup GPIO output
GPIO.setup(8, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(16, GPIO.OUT)


#define functions

def getMag():
    magData_xMSB = numpy.uint8(bus.read_byte_data(MAG_ADDRESS,OUT_X_H_M))
    magData_xLSB = numpy.uint8(bus.read_byte_data(MAG_ADDRESS,OUT_X_L_M)) 
    #print magData_xMSB,magData_xLSB

    magData_yMSB = numpy.uint8(bus.read_byte_data(MAG_ADDRESS,OUT_Y_H_M)) 
    magData_yLSB = numpy.uint8(bus.read_byte_data(MAG_ADDRESS,OUT_Y_L_M)) 
    #print magData_yMSB,magData_yLSB

    magData_zMSB = bus.read_byte_data(MAG_ADDRESS,OUT_Z_H_M) 
    magData_zLSB = bus.read_byte_data(MAG_ADDRESS,OUT_Z_L_M) 
    
    Mx = (magData_xMSB << 8) | magData_xLSB
    Mx_int = numpy.int16(Mx) #value is expressed as two's complement, so need numpy casing as int16
    Mz = (magData_zMSB << 8) | magData_zLSB
    Mz_int = numpy.int16(Mz) #value is expressed as two's complement, so need numpy casing as int16
    My = (magData_yMSB << 8) | magData_yLSB
    My_int = numpy.int16(My) #value is expressed as two's complement, so need numpy casing as int16
    #print My_int
    return Mx_int,My_int,Mz_int
        

def calcHeading(x,y):
    heading = math.atan2(y,x) * (180/math.pi)
    if (heading<0):
            heading = heading+360
    return heading



try:
    while (True):        
            #get magnetometer reading
            mX,mY,mZ = getMag()  #if first transition to "Move" state, then record initial mag reading as center position for servo
            heading = calcHeading(mX,mY) 
            if (heading >= 325 and heading <=360) or (heading < 45):
                #light up 'North' LED
                GPIO.output(8,True)
                GPIO.output(10,False)
                GPIO.output(12,False)
                GPIO.output(16,False)
                
            elif (heading >= 45 and heading <135):
                GPIO.output(10,True)
                GPIO.output(8,False)
                GPIO.output(12,False)
                GPIO.output(16,False)
                
            elif (heading >= 135 and heading < 225):
                GPIO.output(12,True)
                GPIO.output(10,False)
                GPIO.output(8,False)
                GPIO.output(16,False)
                
            else:
                #light up 'West' LED
                GPIO.output(16,True)
                GPIO.output(10,False)
                GPIO.output(12,False)
                GPIO.output(8,False)
            print (heading)
            time.sleep(0.3)
except KeyboardInterrupt:
    print ("exiting")
except:
    print ("exit test")
finally:
    GPIO.cleanup()


    

