Role Name
=========

A brief description of the role goes here.

Requirements
------------
Python on target machine
ssh to the target machine

Role Variables
--------------
work_dir: "work directory on the target machine where all the artifacts will be placed"

This role configures and deployes default wordpress docker container on the target ec2 machine.

Dependencies
------------
Following roles should be executed first:
- ec2
- bootstrap 

License
-------
BSD
