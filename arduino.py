import socket

serverAddressPort = ("192.168.224.176", 4210)

UDPClientSocket = socket.socket(
    family=socket.AF_INET, type=socket.SOCK_DGRAM)



n = input()
bytesToSend = str.encode(n)
UDPClientSocket.sendto(bytesToSend, serverAddressPort)

ans = UDPClientSocket.recvfrom(255)
print(ans)