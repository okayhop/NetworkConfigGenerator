Written By: Korey Hopkins/okayhop
Date: 3/25/2018
---------------------------------------------

Overview:

This is an extendible program for developing the initial configuration
for various network gear. Any and all vendors (Cisco, Juniper, Arista, 
Palo Alto, F5, etc) can get a function added here. Common initial config 
items such as super user accounts, MGMT port IP, NTP, and VLANs are
generated here before being saved off to a file. A user simply needs
to input a YAML file. A sample file is in the /data folder structure.

Pre-reqs:
    - Python 2.7.14 
        - At this time, code has NOT been tested on Python 3.x
    - JinJa2
    - PyYaml
    
Current Functionality:

Currently, there are some basic config snippets in "../data/templates" to build a bare 
bones config. This is based on my professional experience and having something to test 
against, nothing more, nothing less. To add on to this, do the following:

    - Create a code snippet in the appropriate device OS folder. Follow JinJa2 standards
        for variables
    - Create a def under netDeviceConfig.py to use this new snippet
    - Add the new def to parameters.py
    - test
    
Two device OS types were used for initial development, Cisco IOS and Juniper JunOS 
(w/ ELS). To add device OSs:
    
    - Create a folder under ../data/templates with the name of the Vendor and OS
    - Add in the required templates
    - declare the OS in parameters.py
    - test
    
Once you have the config snippets and OSes that you want, you need data. YAML is the file
format of choice here. There is a sample in ../data/yaml of how the file should look.

Once ran, a configuration is saved off to ../data/config


Future Development/Ideas:

- Automatically push config to devices. Netmiko!
- Further use case testing/error handling checks
- More snippets/OSes



Go forth and configure away!

