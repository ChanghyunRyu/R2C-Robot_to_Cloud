# R2C-Robot_to_Cloud


### Konkuk University, 2022, 2nd semester, Next-generation distributed system class, 3 team:  
 
R2C(Robot-to-Cloud) is a simple project of implementing Cloud Server that computes SLAM mapping and merging for robots.  

This project was written for a final team project for Next-generation distributed system class. R2C is proposed to provide operations that are difficult in robotic embedded systems. To this end, we implement a cloud server using Kubernetes. 

## Project Outline

![outline](https://user-images.githubusercontent.com/83490220/204951928-420247f3-1f13-4239-a7b6-2da13c96c081.png)

First, improving performance of SLAM is not the goal of this project. the goal is providing SLAM mapping to several robots. Also even if the number of robots increase, It is to maintain the service by appropriately responding to the traffic.

We will run several robots using ROS's gazebo for testing.  

Deploy the services providing to robots. And we will use Metric Sever and HPA to deal with traffic with auto-scaling.

## Presentation
https://konkukackr-my.sharepoint.com/:b:/g/personal/dks01972_konkuk_ac_kr/EeacwefZDnVIu2Bmefw5XbEBoLrK_e4iL9imbd84UzzUDw?e=XvGZBB

## Demonstration
https://konkukackr-my.sharepoint.com/:v:/g/personal/dks01972_konkuk_ac_kr/ETtF1npiv8lNgZlKtEI-m9UBNDDnqVUMsuOiH3yQKSrzPw?e=32RtYU
