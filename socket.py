import socket
import sys



try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #AF_INET create an IPV4 and SOCK_STREAM makes a TCP connection 
except :
    print('Failed runnning')
    sys.exit()


#print the socket
print(s)

#in order to interact with the www we need to create an host and a port
#host or server is pretty much the same thing
#interact with this server
server = "www.google.com" #it much better use IP Address but since we can't rembber all Ip in the world we will get is soon

#since server is a website we know that port 80 is open.
#we want to comminucate with the port 80
port = 80

#get IP address
try:
    server_ip = socket.gethostbyname(server)
except socket.gaierror:
    print("Host name could not be resolved!")
    sys.exit()
print("---"*20)
print("IPAddress" ,server_ip) #this will print the IP Address on the screen

#now that we know the post and the IPAddress we want to connect to it

s.connect((server_ip, port))
print("---"*20)
print("Socket connected to ",server, "using IP", server_ip)

#send a message to google receive data back and close the socket
#in oder to send a data we make a request.,.

#SENT SCRIPT!
request = "GET  / HTTP/1.1\r\n\r\n"

try:
    s.sendall(request.encode())
except socket.error:
    print("NOT SENT!")
    sys.exit()

print("---"*20)
print("Message sent!")
#END OF SENT SCRIPT

#RECEIVE REPLY SCRIPT!

reply = s.recv(4096)
print(reply.decode())

s.close()

print("Socket close")





