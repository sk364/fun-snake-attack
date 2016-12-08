from mastermind_import import *
from settings import *

import threading
from time import gmtime, strftime

class ServerChat(MastermindServerTCP):
    def __init__(self):
        MastermindServerTCP.__init__(self, 0.5,0.5,10.0) #server refresh, connections' refresh, connection timeout

        self.key = [None]*scrollback
        self.mutex = threading.Lock()

    def callback_connect          (self):
        #Something could go here
        return super(ServerChat,self).callback_connect()
    def callback_disconnect       (self):
        #Something could go here
        return super(ServerChat,self).callback_disconnect()
    def callback_connect_client   (self, connection_object):
        #Something could go here
        return super(ServerChat,self).callback_connect_client(connection_object)
    def callback_disconnect_client(self, connection_object                       ):
        #Something could go here
        return super(ServerChat,self).callback_disconnect_client(connection_object)
    
    def callback_client_receive   (self, connection_object):
        #Something could go here
        return super(ServerChat,self).callback_client_receive(connection_object)
    def callback_client_handle    (self, connection_object, data):
	if data=='':
		pass
	else:
		self.mutex.acquire()
		self.key = self.key[1:] + [data]
		self.mutex.release()        
	self.callback_client_send(connection_object, self.key)
    def callback_client_send      (self, connection_object, data,compression=None):
        #Something could go here
        return super(ServerChat,self).callback_client_send(connection_object, data,compression)

if __name__ == "__main__":
    server = ServerChat()
    server.connect(server_ip,port)
    try:
        server.accepting_allow_wait_forever()
    except:
        #Only way to break is with an exception
        pass
    server.accepting_disallow()
    server.disconnect_clients()
    server.disconnect()
