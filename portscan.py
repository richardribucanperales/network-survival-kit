#we're importing libraries from outside
import sys;
import socket;

#defining what the heck we're doing
remoteServerIP = "216.239.32.20";
portmin = 1;
portmax = 100;

#tells you what we're doing
print ("scanning for ports with the IP provided: ", remoteServerIP)
print ("start port", portmin)
print ("end port", portmax)

#actual process
try:
    for port in range(portmin, portmax):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print "Port {}: OPEN".format(port)
        sock.close()

#if you wanna stop it
except KeyboardInterrupt:
    print "You pressed Ctrl+C"
    sys.exit()

#if you dont know what the heck it is
except socket.gaierror:
    print 'Hostname could not be resolved. Exiting'
    sys.exit()

#if you cant get to it
except socket.error:
    print "Couldn't connect to server"
    sys.exit()

#tells you when we're done
print ("scanning done, thank you")