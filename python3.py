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

iosv_s4 = {
    'device_type' : 'cisco_layer2',
    'ip' : '10.1.1.4',
    'username' : 'admin',
    'password' : 'cisco',
}

iosv_s5 = {
    'device_type' : 'cisco_layer2',
    'ip' : '10.1.1.5',
    'username' : 'admin',
    'password' : 'cisco',
}

with open ('base_template') as f:
    lines = f.read().splitlines()
print(lines)

all_devices = [iosv_s1, iosv_s2, iosv_s3]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output)

with open('trunk_port') as f:
    lines= f.read().splitlines()
print(lines)

all_devices = [iosv_s1, iosv_s2, iosv_s3, iosv_s4, iosv_s5]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output)
