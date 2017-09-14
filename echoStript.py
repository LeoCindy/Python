# coding=UTF-8
clientInput = ''
print 'Type [quit] to quit\nWelcome, now you can type something:'
while clientInput != 'quit':
    clientInput = raw_input('你 > ')
    if( clientInput != 'quit' ) : print '毛毛 > ' + clientInput + "\n"
print 'bye'
