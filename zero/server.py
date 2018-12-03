
import zerorpc

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
# zerorpc
s = zerorpc.Server(RPCServer())
s.bind('tcp://0.0.0.0:4243')
s.run()


