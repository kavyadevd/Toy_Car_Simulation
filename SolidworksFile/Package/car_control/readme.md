#662 CAD Modelling & Simulation using Gazebo 

---
## Team members
1) Aditi Ramadwar
2) Kavyashree Devadiga



## Overview
Building a car model using Solidworks and simulating it in Gazebo
Dependencies: Ubuntu 18.04 and up
Used ROS Melodic



## Commands.

move the source folder to src in catkin directory and run: 
```
catkin make clean && catkin make
```


Check if roscore is running
```
roscore
```

Launch the project in gazebo:
```
roslaunch car_control template_launch.launch
```


Launch in RVIZ:
```
rviz
```

After launching RVIZ add robot model and lazer

To launch teleop in separate terminal run:
```
rosrun car_control teleop.py
```

To Move the robot using publisher subscriber run following commands in separate terminals:

```
rosrun car_control publisher.py
rosrun car_control subscriber.py
```
