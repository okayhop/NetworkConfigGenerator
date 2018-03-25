from netDeviceConfig import *

def makeVariables():
    # Define both of these if you are not using the local folder structure for 
    # storing templates and config output. If you are not using, set to ""
    
    #networkTemplatesPath = "/Users/koreyhopkins/Documents/NetworkAutomation/templates"
    #networkConfigPath = "/Users/koreyhopkins/Documents/NetworkAutomation/config"
    networkConfigPath = ""
    networkTemplatesPath = ""
    
    # Add any functions created for config creation in netDeviceConfig.py here.
    configOptions = {
        0:conf_test,
        1:conf_test,
        2:conf_superUser,
        3:conf_mgmtPort,
        4:conf_ntp,
        5:conf_vlan
        }
    
    # Declare what network device types you support here.
    osType = {
        "CiscoIos",
        "Juniper"
    }
    
    return networkTemplatesPath, networkConfigPath, configOptions, osType