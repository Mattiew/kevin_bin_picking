
Pour lancer la simulation du robot dans Gazebo et demarrer les controlers:

>>roslaunch kevin_gazebo kevin.launch 


Pour lancer Rviz, avec le plugin de moveit! pour la géneration de trajectoires:

>>roslaunch kevin_moveit_config moveit_planning_execution.launch

Un exmple de lecture de la camera de gazebo est diponible en appelant:

>> rosrun image_segmentation reader.py