# AutomationScriptsPython
- python1 script - using getpass and telnetlib libraries, we are able to utilize getting user credentials and telnetting into network devices
- I used Cisco IOSvL2 15.2 for switches and IOSv 15.6 for L3 and a docker network automation container all within GNS3

- python2 script utilizing Netmiko - multi vendor SSH Python library which builds on paramiko which is the defacto SSH library in Python
- variable containings switch dictionary (ip, type, user/pass)
- then connect via net_connect and send show ip int brief then print the output
- then a list of config commands listed in code (later iteration would have a longer list of commands in a separate file the script can read from)
- for loop representing vlan creating in numerical order

- python3 script - we add 2 core switches to the topology with S1-3 being access and S4-5 being core)
- 2 files (base_template) and trunk_port templates
- apply base to access and trunk to all else from respective files

![gns3](https://github.com/kim6jj/AutomationScriptsPython/blob/84c9d8dae236c49f4c27c926a6a04c5e7d0a8553/gns3.JPG)
