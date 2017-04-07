# urg_node

This set of instructions will help you install and test the Hokuyo URG Laser.


#### Install the driver (ROS Package) for publishing the laser scan data.
1. `sudo apt-get install ros-kinetic-urg-node`
* Change directories to the root of your Catkin Workspace: 
2. `cd ~/catkin_ws`
3. `catkin_make`
* Configure the Hokuyo Laser
* Create udev rules so that the read-write permissions for the laser are automatically setup every time it is connected.
* Switch to super user mode in order to update Udev rules:
4. `sudo su`
5. `nano 99-urg.rules`
* Add the following line in the newly created file and then save upon exit by entering Ctrl-x, then answer 'y', and finally hit 'Enter'.
6. `SUBSYSTEMS=="usb", ATTRS{idVendor}=="15d1", ATTRS{idProduct}=="0000", MODE="0666", SYMLINK+="lidar_hokuyo", GROUP="dialout"`
7. `echo 'SUBSYSTEM=="tty", ATTRS{idProduct}=="0003", ATTRS{idVendor}=="2639", ATTRS{manufacturer}=="Xsens", SYMLINK+="mti300", ACTION=="add", GROUP="dialout", MODE="0660"' >> /etc/udev/rules.d/99-xsens.rules`
* Reload the rules
8. `udevadm control --reload-rules`
* Exit from super user mode
9. `exit`

####  Test the Hokuyo Laser

* Ensure the URG-04LX is connected to two USB ports on the computer.  
* Start ROS core
1. `roscore`

* In a seperate terminal, start the publisher node by typing:
2. `rosrun urg_node urg_node`

* If the node started correctly, then you should be able to see the /scan topic by entering:
3. `rostopic list`
* You can echo (or display) the information being published to that topic by typing:
4. `rostopic echo /scan`
* You can gain more information about the /scan topic, as well as more information on the data structure of the LaserScan message type by entering these commands:
5. `rostopic info /scan`
6. `rosmsg show sensor_msg/LaserScan`
* You can also see more information about a particular message type by using online [ROS documentation](http://docs.ros.org/api/sensor_msgs/html/msg/LaserScan.html)
* The LaserScan data structure is part of the [sensor_msgs](http://wiki.ros.org/sensor_msgs) group of data types, but it is also common in ROS to use data types a part of [std_msgs](http://wiki.ros.org/std_msgs).

