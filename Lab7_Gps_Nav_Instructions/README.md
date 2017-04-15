# Waypoint Navigation using a GPS and IMU

This set of instructions supplements your lab handout.


### Create a publisher for the Adafruit 9DOF sensor.
1. Provided in this Lab 7 Github folder you will see a Python script titled, 'imu_9dof_driver.py'.  Your task is to convert this code into a ROS publisher.
    + You will see that the driver reads the chip's accelerometer, magnetometer, and gyroscope.  
    + From the accelerometer and magnetometer data, the code calculates a tilt-compensated heading.  Other information such as roll and pitch angles are also calculated.
    + At a minimum, your code must publish the tilt-compensated heading to a topic, which you will use to navigate your robot toward a waypoint.   
    + You should publish this information at a rate of 10 Hz.  The sensor is capable of providing data at faster rate, but this isn't necessary for your application.  

### Incorporate bearing and distance calculator code in waypoint navigator node.
1.  Provided in this Lab Github folder you will see a Python script titled, 'calc_bearing_and_distance.py'.  Experiment with this code and validate its operation using Google Maps to obtain sets of Lat/Lon coordinates.  Also, validate the accuracy of the UTM function by obtaining UTM coordinates from the following [website](https://mappingsupport.com/p/coordinates-utm-google-maps.html).  You can use the code to compare the output of both methods for obtaining bearning and distance.
2.  Use these functions in your navigation node that controls the Traxxas.  
3.  You may wish to only use the bearing and distance resulting from UTM coordinates, or you may wish to average the result of both methods before providing your robot a direction to follow toward a waypoint.
