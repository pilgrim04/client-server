import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('', 1234))
sock.listen(1)
conn, addr = sock.accept()

print 'successfully connected', addr

my_dict = dict()
my_dict['Brasil'] = 1
my_dict['German'] = 7
while True:
  data = conn.recv(1024)

  if data == '3':  # show 1 element
    data = conn.recv(1024)
    try:
      a = my_dict[data]
      conn.send(str(a))
    except:
      conn.send('no such data')

  elif data == '4':  # show all elements
    conn.send(str(my_dict))

  elif data == 'exit':  # exit
    print 'exiting...'
    conn.send('bye')
    break

conn.close()
print 'connection close '
