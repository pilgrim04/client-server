import socket

sock = socket.socket()
sock.connect(('localhost', 1234))

print '1 - add'
print '2 - edit'
print '3 - read'
print '4 - read multiple'
print '5 - delete one element'
print '6 - delete all elements'
print '7 - close connection'
print 'Your choice: ',

while True:
  user_choice = raw_input()
  # Read one element
  if user_choice == str(3):
    print 'pls type key to see value'
    print '<<<',
    sock.send('3')
    user_key = raw_input()
    sock.send(str(user_key))

  # Read all dict
  elif user_choice == str(4):
    sock.send('4')

  # Exit (close connection)
  elif user_choice == str(7):
    sock.send('exit')

  # IO Error 
  else:
    print 'no such choice'

  data = sock.recv(1024)
  print '>>>',data
