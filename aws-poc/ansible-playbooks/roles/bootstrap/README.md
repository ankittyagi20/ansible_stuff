Role Name:
------------
bootstrap

A brief description of the role goes here:
------------
This is the role to bootstrap the target (ec2) machines to make it manageable via core ansible modules. Target modules require certain python packages that this module installs using raw module of ansible. Raw module doesn't require python to connect to the target machine.

Requirements:
-------------
SSH is the only requirement for this module to be executed successfully.

Role Variables:
--------------
No variable set for this module.

Dependencies
------------
Following role should be executed before this role:
-ec2

License
-------
BSD
