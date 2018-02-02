import socket;
target = "www.roblox.com"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
targetresponse = socket.gethostbyname(target)
print("The IP address of the target is: " + targetresponse)

