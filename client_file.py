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

  if user_choice == str(1):  # Add element
    sock.send('1')
    print 'your key: ',
    user_key = raw_input()
    sock.send(user_key)
    print 'your value: ',
    user_value = raw_input()
    sock.send(user_value)

  elif user_choice == str(2):  # Edit element
    sock.send('2')
    print 'print KEY of element to edit: ',    
    user_key = raw_input()
    sock.send(user_key)
    print 'your new value: ',
    user_new_value = raw_input()
    sock.send(user_new_value)

  elif user_choice == str(3):  # Read one element
    print 'pls type key to see value'
    print '<<<',
    sock.send('3')
    user_key = raw_input()
    sock.send(str(user_key))

  elif user_choice == str(4):  # Read all dict
    sock.send('4')

  elif user_choice == str(5):  # Delete one element
    sock.send('5')
    print 'print KEY of element to delete: ',    
    user_key = raw_input()
    sock.send(user_key)

  elif user_choice == str(6):  # Delete all elements in dict
    print 'deleting all items. Are you sure? (y/n)'
    user_answer = raw_input()
    if user_answer == 'y':
      sock.send('6')
    elif user_answer == 'n':
      pass
    else:
      print 'Y or N!'
  
  elif user_choice == 'exit':  # Exit from server (close connection)
    sock.send('7')

  else:
    print 'no such choice'  # IO Error 
    continue

  data = sock.recv(1024)
  print '>>>',data
  if data == 'bye':  # correct exiting from client
    break
