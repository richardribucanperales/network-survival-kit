#we're importing libraries from outside
import sys;
import socket;

#defining what the heck we're doing
remoteServer = raw_input("Enter host: ")
portmindef = int(input("Enter start port: "))
portmaxdef = int(input("Enter end port: "))
remoteServerIP = socket.gethostbyname(remoteServer);
portmin = portmindef;
portmax = portmaxdef;

#tells you what we're doing
print ("scanning for ports with the IP provided: ", remoteServerIP)
print ("start port", portmin)
print ("end port", portmax)

#actual process
for port in range(portmin, portmax):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print ("Port {}: OPEN" % (port,))
        sock.close()


#tells you when we're done
print ("scanning done, thank you")