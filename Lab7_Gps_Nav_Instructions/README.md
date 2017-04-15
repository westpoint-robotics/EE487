# Waypoint Navigation using a GPS and IMU

This set of instructions supplements your lab handout.


### Create a publisher for the Adafruit 9DOF sensor.
1. Provided in this folder you will see a Python script titled, 'imu_9dof_driver.py'.  Your task is to convert this code into a ROS publisher.
    + You will see that the driver reads the chip's accelerometer, magnetometer, and gyroscope.  
    + From the accelerometer and magnetometer data, the code calculates a tilt-compensated heading.  Other information such as roll and pitch angles are also calculated.
    + At a minimum, your code must publish the tilt-compensated heading to a topic, so that you can have your robot navigate toward a waypoint. 
    + You should publish this information at a rate of 10 Hz.  The sensor is capable of providing data at faster rate, but this isn't necessary for your application.  


