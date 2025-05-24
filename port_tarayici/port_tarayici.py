import socket

def port_tara(hedef_ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        sonuc = sock.connect_ex((hedef_ip, port))
        if sonuc == 0:
            print(f"Port {port} açık")
        sock.close()
    except socket.error:
        pass

if __name__ == "__main__":
    hedef_ip = input("Hedef IP adresini girin: ")
    for port in range(1, 101):
        port_tara(hedef_ip, port)
                                                                                  

