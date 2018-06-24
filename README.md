# Mind Controlled Nao-Robot

# Description
This is a ROS package to control the nao robot using facial expressions by integrating the Emotiv Epoc+ EEG sensor. Its easy to use, just build in your catkin workspace and download the dependencies and you ready to go :)

# Dependencies
these are the two python libraries that you should install before using this package, other libraries used in the package are already installed with the regular python installation

- cypes
- naoqi library

# How it works?
This a really basic ROS package used to explore the cababilities of the Emotiv Epoc+ sensor
there is two nodes the first one which is the "expression_publisher.py" is using the Emotiv APIs to get the signal and process it, after that the signal is published to the topic "/emo_state".
the subscrber reads which expression is published there and then give the command to the robot to move.

the available moves are the following :
- Smilimg -> Moving Forward
- Clenching -> Stopping
- Eye-brow -> Rotating right
- Furbrow -> Rotating left

# How to use?
first change the username for the directory to your computer username

After that basically run the two nodes separately by using the following commands

rosrun nao_mind_controlled expression_publisher.py

rosrun nao_mind_controlled nao_subscriber.py

And then start using your facial expressions to move the robot around 

make sure to change the permission of the python files to be executable by running the following command, after moving to the /scripts directory

chmod +x file_name.py
