import socket;
target = "208.67.222.222"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
targetresponse = socket.gethostbyaddr(target)
print("The hostname is: " + targetresponse[0])