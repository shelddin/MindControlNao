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
## How to use?
first change the username for the directory to your computer username, in line 35 you will find the following 
 ```
 35. libPath = "/home/shehabaldeen/catkin_ws/src/nao_mind_controlled/bin/linux64/libedk.so"
 ```
just change the directory to the right path on your computer

After that basically run the two nodes separately by using the following commands
````
rosrun nao_mind_controlled expression_publisher.py
````
````
rosrun nao_mind_controlled nao_subscriber.py
````
also you can echo the expression that being published to the /emoState topic with the following command
```
rostopic echo /emoState
```
And then start using your facial expressions to move the robot around 

make sure to change the permission of the python files to be executable by running the following command, after moving to the /scripts directory
```
chmod +x file_name.py
```

## Contact 
you can contact me on my [linkedin](https://www.linkedin.com/in/shehabeldin-housein-6a2949120/) account for any further questions
