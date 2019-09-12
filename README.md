# Mind Controlled Nao-Robot

## Description
This is a ROS package to control the nao robot using facial expressions by integrating the Emotiv Epoc+ EEG sensor. It is easy to use, just build in your catkin workspace and download the dependencies and you ready to go :)

## Dependencies
these are the two python libraries that you should install before using this package, other libraries used in the package are already installed with the regular python installation

- ctypes
- naoqi

## How it works?
This a really basic ROS package used to explore the capabilities of the Emotiv Epoc+ sensor
there is two nodes the first one which is the "expression_publisher.py" is using the Emotiv APIs to get the signal and process it, after that the signal is published to the topic "/emoState".
the subscriber reads which expression is published there and then give the command to the robot to move.

the available moves are the following :
- Smiling -> Moving Forward
- Clenching -> Stopping
- Eye-brow -> Rotating right
- Furbrow -> Rotating left
** tested only on Ubuntu 16.04 64bit with ROS kinetic ** 

