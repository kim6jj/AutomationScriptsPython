from netmiko import ConnectHandler

iosv_s1 = {
    'device_type' : 'cisco_layer2os',
    'ip' : '10.1.1.1',
    'username' : 'admin',
    'password' : 'cisco',
}

iosv_s2 = {
    'device_type' : 'cisco_layer2os',
    'ip' : '10.1.1.2',
    'username' : 'admin',
    'password' : 'cisco',
}

iosv_s3 = {
    'device_type' : 'cisco_layer2',
    'ip' : '10.1.1.3',
    'username' : 'admin',
    'password' : 'cisco',
}

all_devices = [iosv_s1, iosv_s2, iosv_s3]

for devices in all_devices:
        net_connect = ConnectHandler(**devices)
        for n in range (2,21):
            print ("Creating VLAN " +str(n))
            config_commands = ['vlan ' + str(n), 'name VLAN ' + str(n)]
            output = net_connect.send_config_set(config_commands)
            print (output)