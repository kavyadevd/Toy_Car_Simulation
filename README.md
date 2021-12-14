# Toy Car Simulation

Solidworks | ROS  |  Gazebo

A toy car with LIDAR sensor and PID control simulation in a gazebo world with obstacles

![CarModel](https://user-images.githubusercontent.com/13993518/137058137-7dd3fa47-3071-41f4-9bde-4177766a7db1.png)

#662 CAD Modelling & Simulation using Gazebo 

---
## Team members
1) [Aditi Ramadwar](https://github.com/aditiramadwar)
2) [Kavyashree Devadiga](https://github.com/kavyadevd)



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
