import socket

def scan(host, ports):
    open_ports = []
    for port in ports:
        try:
            with socket.create_connection((host, port), timeout=1):
                open_ports.append(port)
        except:
            continue
    return open_ports
