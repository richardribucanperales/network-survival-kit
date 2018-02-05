#here's the start lets import the stuff
import sys;
import socket;

#IDK what to say about this
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#make it look fancy
print("-"*60)
print("RICHARD'S ALL IN ONE TOOL LOADED SUCCESSFULLY")
print("-"*60)
print("AWAITING PARAMETERS")
print("-"*60)

#figuring out what they have
print("INPUT YOUR CHOICE:")
print("1. FIND IP")
print("2. FIND DOMAIN")
print("3. RUN PORT SCAN WITH IP")
print("4. RUN PORT SCAN WITH DOMAIN")
print("5. FIND INFORMATION WITH MAC ADDRESS")
print("6. EXIT")
choice = int(input("AWAITING INPUT: "))

if choice == 1:
	domainTarget = raw_input("INPUT DOMAIN: ")
	domainResponse = socket.gethostbyname(domainTarget)
	print("THE IP ADDRESS OF THE TARGET IS: " + domainResponse)
elif choice == 2:
	ipTarget = raw_input("INPUT IP ADDRESS: ")
	ipResponse = socket.gethostbyaddr(ipTarget)
	print("THE HOSTNAME OF THE TARGET IS: " + ipResponse[0])
elif choice == 3:
	domainPTarget = raw_input("INPUT DOMAIN: ")
	domainPResponse = socket.gethostbyaddr(domainPTarget)
	domainPportmindef = int(input("START PORT: "))
	domainPportmaxdef = int(input("END PORT: "))
	domainPportmin = domainPportmindef;
	domainPportmax = domainPportmaxdef;

	print("SCANNING DOMAIN WITH PORTS PROVIDED, PLEASE HOLD")