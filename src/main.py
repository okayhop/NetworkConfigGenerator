# Written By: Korey Hopkins/okayhop
# Date: 3/25/2018
#
# This is an extendible program for developing the initial configuration
# for various network gear. Any and all vendors (Cisco, Juniper, Arista, 
# Palo Alto, F5, etc) can get a function added here. Common initial config 
# items such as super user accounts, MGMT port IP, NTP, and VLANs are
# generated here before being saved off to a file. A user simply needs
# to input a YAML file. A sample file is in the /data folder structure.

from jinja2 import FileSystemLoader, Environment, Template, PackageLoader
from netDeviceConfig import *
from parameters import *
from Tkinter import Tk
import tkFileDialog
import yaml
import os

def main():
    # Create user defined variables
    networkTemplatesPath, networkConfigPath, configOptions, osType = makeVariables()
    osType = [x.lower() for x in osType]
    
    # Housekeeping! Get current directory if nothing was defined above in the 
    # global args section. Both NETWORKTEMPLATES and NETWORKCONFIG must be defined
    # in order for the global args to work.
    if ((not networkConfigPath) and (not networkTemplatesPath)):
        chDir = os.getcwd()
        os.chdir("..")
        newDir = os.path.abspath(os.getcwd())
        
        networkConfigPath = newDir + "/data/config"
        networkTemplatesPath = newDir + "/data/templates"
        
        os.chdir(chDir)
    
    # Prompt user to select a yaml file (GUI) and open it up
    root = Tk()
    root.withdraw()
    
    filePath = tkFileDialog.askopenfilename(filetypes=(("Yaml File", "*.yml"), \
                                                       ("All Files", "*.*")), \
                                                       title="Choose a file.")
    
    f = open(filePath, 'r')
    networkConfig = yaml.safe_load(f)
     
    # Loop over input and put together a config based on the inputs
    for i in range(0, len(networkConfig)):
        # Open file for outputting the configuration that is about to be generated
        generatedConfig = ""
        
        deviceName = networkConfig.keys()[i]
        deviceType = networkConfig[deviceName]['type']
        
        # **Add in OS check here**
        if deviceType.lower() in osType:
        
            configPath = "%s/%s" % (networkTemplatesPath, deviceType)
            env = Environment (loader=FileSystemLoader(configPath))
    
            # The key/hostname field is a base requirement for this to work, so we will
            # just put it here to be evaluated
        
            hostname = conf_hostname(env, deviceType, deviceName)
            generatedConfig+= hostname + "\n"
        
            # loop over defined config options and run. If they pass validation checks,
            # the relevant configuration will get returned
            for j in range(0, len(networkConfig[deviceName])):
                configuration = configOptions[j](env, deviceType, networkConfig[deviceName])
                try:
                    generatedConfig+=configuration + "\n"
                except:
                    # Do nothing if parameter not declared
                    pass
                
        else:
            print("The declared device type is not supported. Skipping the config for "+deviceName)
         
        # Save off config
        print("Saving the config for " + deviceName +" to file.")
        fileName = "%s/%s.%s" % (networkConfigPath, deviceName, "txt")
        outFile = open(fileName, "w")
        outFile.write(generatedConfig)
        outFile.close()
    

######## 
main ()
