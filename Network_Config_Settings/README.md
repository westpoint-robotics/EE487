# Network Configuration Instructions for the Raspberry Pi (RPi)

This set of instructions explains how to connect the Raspberry Pi to different networks.  For instance, depending upon the circumstances, you may wish to connect your Raspberry Pi to the Internet or another computer via the wireless EECSDS3, the wired or wireless EECSnet, or the AT&T Mi-Fi.  In some cases, it may be necessary to establish a peer-to-peer connection between the Raspberry Pi and a laptop using an Ethernet cable.  These instructions are intended to assist you with changing between these network options.  


### Template /etc/network/interfaces file for your Raspberry Pi.
1.  On some installations of Ubuntu-Mate, we have noticed that the GUI network manager is not loading properly and is unavailable.  As a result, it may be best to configure different connections using the "interfaces" file located in the /etc/network directory of Raspberry Pi.     
    + Inside this Github directory, there is a template "interfaces" file that you can copy over to your Raspberry Pi.  The file contains comments on which lines should be uncommented in order to connect to certain networks.
    
### Establishing an Ethernet connection directly between the RPi and a laptop. 
1.  At times, it may be necessary to establish a direct Ethernet connection between your laptop and RPi using a CAT5 cable.  This is especially useful when you encounter wireless trouble and can't connect the RPi to a montior for troubleshooting.
2.  Here are the steps for establishing such a connection:
    + Program your RPi to automatically configure its Ethernet port at every startup so that it is ready for connecting to your laptop.
    + You'll need to find out the name of your ethernet port on the RPi in order update your "interfaces" file.
        + On your RPi, type `ipconfig -a` to show all interfaces, including those that are currently down.


