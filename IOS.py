import getpass
import sys
import telnetlib

HOST = "192.168.10.162" #IP address of your IOS router interface
user = raw_input("Enter your username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST,timeout = 5) ## include timeout as well

tn.read_until("Username: ")
tn.write(user + "\n")

if password:
    tn.read_until("Password:")
    tn.write(password + "\n")

tn.write("en\n")
tn.write("config t\n")
tn.write("int lo0\n")
tn.write("ip add 1.1.1.1 255.255.255.255\n")
tn.write("end\n")
tn.write("exit\n")

print tn.read_all()
