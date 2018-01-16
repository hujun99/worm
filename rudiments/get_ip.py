import socket
print(socket.gethostname())
local_ip = socket.gethostbyname(socket.gethostname())
print(local_ip)
ip_lists = socket.gethostbyname_ex(socket.gethostname())
print(ip_lists)