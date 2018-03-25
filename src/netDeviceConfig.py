import socket
import struct

def conf_hostname(env, os, name):
    config_template = env.get_template('hostname.txt')
    config_rendered = config_template.render(hostname=name)
    return config_rendered


def conf_test(env, os, parameters):
    # Debug module. Leave blank if not needed for anything
    return 


def conf_superUser( env, os, parameters):   
        try:
            username = parameters['un']
            password = parameters['pw']
        
            config_template = env.get_template('superUser.txt')
            config_rendered = config_template.render(un=username, pw=password)
        
            return config_rendered
        except KeyError:
            print("There are no credentials for generating a super user account. Skipping...")
            return 

def conf_mgmtPort( env, os, parameters):
        try:
            cidr = parameters['mgmtIP']
            
            if(os=="Juniper"):
                config_template = env.get_template('mgmtPort.txt')
                config_rendered = config_template.render(CIDR=cidr)
            else:
                ipAddr = cidr_to_netmask(cidr)
                config_template = env.get_template('mgmtPort.txt')
                config_rendered = config_template.render(IP=ipAddr[0], mask=ipAddr[1])
                
            return config_rendered
        except KeyError:
            print("There are IPs for the MGMT interface. Skipping...")
            return 


def conf_ntp( env, os, parameters):
        try:
            ntp = parameters['ntp']
        
            config_template = env.get_template('ntp.txt')
            config_rendered = config_template.render(ntp=ntp)
        
            return config_rendered
        except KeyError:
            print("A valid NTP entry was not found. Skipping...")
            return


def conf_vlan( env, os, parameters):
        try: 
            config_rendered = ""
            for i in range(0, len(parameters['vlans'])):
                cidr = parameters['vlans'][i][2]
                vlanID = parameters['vlans'][i][1]
                vlanName = parameters['vlans'][i][0]
                if(os=="Juniper"):
                    ipAddr, mask = cidr.split("/")
                else:
                    ipAddr, mask = cidr_to_netmask(cidr)
                
                config_template = env.get_template('vlan.txt')
                config_rendered += config_template.render(name=vlanName,IP=ipAddr, \
                                                          mask=mask, vlanID=vlanID) + "\n"
                
                
            return config_rendered 
        except KeyError:
            print("No vlans. Skipping...")
            return
        
    

def cidr_to_netmask(cidr):
    # takes standard CIDR notation and spits out netmask and network
    # e.g. 192.168.0.1/24 becomes 192.168.0.1 and 255.255.255.0
    
    network, net_bits = cidr.split('/')
    host_bits = 32 - int(net_bits)
    netmask = socket.inet_ntoa(struct.pack('!I', (1 << 32) - (1 << host_bits)))
    return network, netmask
