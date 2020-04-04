from contextlib import closing
import socket


def choose_opened_port(ip):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((ip, 0))
        port = sock.getsockname()[1]
        return port