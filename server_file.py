import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('', 1234))
sock.listen(1)
conn, addr = sock.accept()

print 'successfully connected', addr

my_dict = dict()
#my_dict['Brasil'] = 1
#my_dict['German'] = 7
while True:
  data = conn.recv(1024)

  if data == '1': # add 1 element
    key_data = conn.recv(1024)
    value_data = conn.recv(1024)
    my_dict[key_data] = value_data
    conn.send('added successfully') 

  elif data == '2': # edit 1 element
    key_data = conn.recv(1024)
    value_data = conn.recv(1024)
    my_dict[key_data] = value_data
    conn.send('edited successfully')

  elif data == '3':  # show 1 element
    data = conn.recv(1024)
    try:
      a = my_dict[data]
      conn.send(str(a))
    except:
      conn.send('no such data')

  elif data == '4':  # show all elements
    conn.send(str(my_dict))

  elif data == '5':
    key_data = conn.recv(1024)
    try: 
       del my_dict[key_data]
       conn.send('successfully deleted')
    except:
       conn.send('no such element')

  elif data == '6':
    my_dict.clear()
    conn.send('dict is empty, sir')


  elif data == '7':  # exit
    print 'exiting...'
    conn.send('bye')
    break

conn.close()
print 'connection closed'
