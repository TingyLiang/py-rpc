
import time
import xmlrpclib

# SimpleXMLRPCServer
def xmlrpc_client():
    print('xmlrpc client')
    c = xmlrpclib.ServerProxy('http://localhost:4242')
    data = {str(i): i for i in range(100)}
    start = time.clock()
    for i in range(5000):
        c.getObj()
    for i in range(5000):
        c.sendObj(data)
    print('xmlrpc total time %s' % (time.clock() - start))
