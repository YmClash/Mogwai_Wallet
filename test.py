import socket

bot = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
bot.bind(('127.0.0.1',5000))
# bot.connect((socket.gethostname(),5001))
bot.listen(5)
print(bot.getpeername())


# print(bot.recv(1024).decode())
# print(bot.recv(1024).decode())

