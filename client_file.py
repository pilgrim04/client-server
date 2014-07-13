import socket

sock = socket.socket()
sock.connect(('localhost', 1234))

print '1 - add'
print '2 - edit'
print '3 - read'
print '4 - read multiple'
print '5 - delete one element'
print '6 - delete all elements'
print '\' exit\' - close connection'
print 'Your choice: ',

while True:
  user_choice = raw_input()

  # Add one element
  if user_choice == str(1):
    sock.send('1')
    print 'your key: ',
    user_key = raw_input()
    sock.send(user_key)
    print 'your value: ',
    user_value = raw_input()
    sock.send(user_value)

  # Edit one element
  elif user_choice == str(2):
    sock.send('2')
    print 'print KEY of element to edit: ',    
    user_key = raw_input()
    sock.send(user_key)
    print 'your new value: ',
    user_new_value = raw_input()
    sock.send(user_new_value)

  # Read one element
  elif user_choice == str(3):
    print 'pls type key to see value'
    print '<<<',
    sock.send('3')
    user_key = raw_input()
    sock.send(str(user_key))

  # Read all dict
  elif user_choice == str(4):
    sock.send('4')

  elif user_choice == str(5):
    sock.send('5')
    print 'print KEY of element to delete: ',    
    user_key = raw_input()
    sock.send(user_key)

  elif user_choice == str(6):
    print 'deleting all items. Are you sure? (y/n)'
    user_answer = raw_input()
    if user_answer == 'y':
      sock.send('6')
    elif user_answer == 'n':
      pass
    else:
      print 'Y or N!'
  


  # Exit (close connection)
  elif user_choice == 'exit':
    sock.send('7')

  # IO Error 
  else:
    print 'no such choice'
    continue

  data = sock.recv(1024)
  print '>>>',data
  if data == 'bye':
    break
