"""An implementation of the varlink protocol

See U{https://www.varlink.org} for more information about the varlink protocol and interface definition
files.

For server implementations use the L{varlink.Server} class.

For client implementations use the L{varlink.Client} class.

For installation and examples, see the GIT repository U{https://github.com/varlink/python}.
or the source code of L{varlink.tests.test_orgexamplemore}

"""

__all__ = ['VarlinkEncoder', 'VarlinkError',
           'InterfaceNotFound', 'MethodNotFound', 'MethodNotImplemented', 'InvalidParameter',
           'ClientInterfaceHandler', 'SimpleClientInterfaceHandler', 'Client',
           'Service', 'Interface', 'Scanner', 'ConnectionError',
           'get_listen_fd', 'Server', 'ThreadingServer', 'ForkingServer', 'RequestHandler']

from .client import (Client, ClientInterfaceHandler, SimpleClientInterfaceHandler)
from .error import (VarlinkEncoder, VarlinkError, InvalidParameter, InterfaceNotFound, MethodNotImplemented,
                    MethodNotFound, ConnectionError, BrokenPipeError)
from .scanner import (Scanner, Interface)
from .server import (Service, get_listen_fd, Server, ThreadingServer, ForkingServer, RequestHandler)


# There are no tests here, so don't try to run anything discovered from
# introspecting the symbols (e.g. FunctionTestCase). Instead, all our
# tests come from within varlink.tests.
def load_tests(loader, tests, pattern):
    import os.path
    # top level directory cached on loader instance
    this_dir = os.path.dirname(__file__)
    return loader.discover(start_dir=this_dir, pattern=pattern)
