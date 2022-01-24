from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()
authorizer.add_user("balerion","Balerion1997", "/home/balerion/testdir", perm="elradfmw")
authorizer.add_anonymous("/home/balerion/testdir", perm="elradfmw")

handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(("localhost", 1026), handler)
server.serve_forever()
