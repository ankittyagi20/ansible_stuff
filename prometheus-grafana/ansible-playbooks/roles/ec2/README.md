Role Name
=========
ec2

A brief description of the role goes here.

Requirements
------------
- boto
- python
- aws credentials to be placed in ~/.aws/credentials. refer: http://boto.cloudhackers.com/en/latest/boto_config_tut.html

Role Variables
--------------
- ami_id: "ec2 ami id"
- instance_type: "type of instance to create fo e.g.: t2.micro"
- region: "ec2 region where resources need to be created"
- az: "ec2 availability zone"
- instance_count: "number of ec2 instances"
- root_volume_size: "Size of the root volume attached to ec2 instance"
- delete_volume: "Switch to turn ON or OFF, whether the volume should be deleted after instance is terminated. Possible values: True, False"
- vpc_cidr: "VPC CIDR range for e.g. 172.16.0.0/16 or 192.168.0.0/16"
- subnet_cidr01: "Subnet CIDR range for e.g. 172.16.0.0/24 or 192.168.0.0/24"


Dependencies
------------
No dependency on othe roles as such

License
-------

BSD

