import socket
import concurrent.futures


def scan(ip):
    opened_port = []
    socket.setdefaulttimeout(2)

    def run(ip, port):
        scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if scanner.connect_ex((ip, port)) == 0:
            opened_port.append(port)
        scanner.close()

    with concurrent.futures.ThreadPoolExecutor(max_workers=500) as executor:
        for port in range(65535):
            executor.submit(run, ip, port + 1)

    return opened_port


def exist(ip):
    try:
        socket.gethostbyname(ip)
        return True
    except socket.gaierror:
        return False
