import zerorpc
import time
# zerorpc
def zerorpc_client():
    print('zerorpc client')
    c = zerorpc.Client()
    c.connect('tcp://127.0.0.1:4243')
    data = {str(i): i for i in range(100)}
    start = time.clock()
    for i in range(5000):
        c.getObj()
    for i in range(5000):
        c.sendObj(data)
    print('total time %s' % (time.clock() - start))

zerorpc_client()