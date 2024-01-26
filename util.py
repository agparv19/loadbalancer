"""
Generic utilities used in this project
"""

import socket

# Max number of connections in the socket queue
BACKLOG = 5

# Max size of data read from a socket
MAX_DATA_SIZE = 1024

# Encoding style
STYLE = "utf-8"

# Localhost
LOCALHOST = "127.0.0.1"

def setup_server(host, port):
    """
    Returns a socket listening on (host, port)
    """

    # Create a socket object
    # socket.AF_INET: indicates IPv4
    # socket.SOCK_STREAM: indicates TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Allow reuse of the local address the socket is bound to.
    # Avoids the "Address already in use" error that might occur if the server
    # is restarted and the previous socket is still in the TIME_WAIT state.
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind the socket to a specific host and port
    # Should complain if host or port is not valid
    server_socket.bind((host, port))

    # server_socket must be non-blocking for async
    server_socket.setblocking(False)

    # Start listening
    server_socket.listen(BACKLOG)
    print(f"Server listening on {host}:{port}")
    return server_socket