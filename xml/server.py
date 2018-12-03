from SimpleXMLRPCServer import SimpleXMLRPCServer

class RPCServer(object):
    """docstring for RPCServer"""

    def __init__(self):
        super(RPCServer, self).__init__()
        self.data = {str(i): i for i in range(100)}
        self.data2 = None

    def getObj(self):
        print('get data')
        return self.data

    def sendObj(self, data):
        print('send data')
        self.data2 = data


# SimpleXMLRPCServer
server = SimpleXMLRPCServer(('localhost', 4242), allow_none=True)
server.register_introspection_functions()
server.register_instance(RPCServer())
server.serve_forever()
