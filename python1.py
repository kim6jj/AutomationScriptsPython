import getpass
import telnetlib

host = "localhost"
user = input("Enther your remote account: ")
password = getpass.getpass()

#open file called myswitches which is a list of IPs accessible from the docker container automation server
f = open ('myswitches') 

#for each IP in file, telnet to each switch and enter global config mode
for IP in f:
    IP=IP.strip()
    print ("Configuring Switch " + (IP))
    host = IP
    tn = telnetlib.Telnet(host)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
            tn.read_until(b"Password: ")
            tn.write(password.encore('ascii') + b"\n")
    tn.write(b"conf t\n")

#create vlans 2-20
    for n in range (2,21):
        tn.write(b"vlan " + str(n).encode('ascii') + b"\n")
        tn.write(b"name VLAN " +str(n).encode('ascii') + b"\n")
    
    tn.write(b"end\n")
    tn.write(b"exit\n")
    print(tn.read_all().decode('ascii'))



