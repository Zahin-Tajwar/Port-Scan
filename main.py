from queue import Queue
import socket
import threading
from IPy import IP
target = input("Enter Target:")
proxy_ip = input("Enter a Proxy IP:")#'94.245.56.147'

print("""
  _____           _          _____                 
 |  __ \         | |        / ____|                
 | |__) |__  _ __| |_ _____| (___   ___ __ _ _ __  
 |  ___/ _ \| '__| __|______\___ \ / __/ _` | '_ \ 
 | |  | (_) | |  | |_       ____) | (_| (_| | | | |
 |_|   \___/|_|   \__|     |_____/ \___\__,_|_| |_|

""")

queue = Queue()
open_ports = []

def get_banner(s):
    s.recv(1024)

def check_ip(ip):
    try:
        IP(ip)
        target = ip
        return target
    except ValueError:
        target = socket.gethostbyname(ip)
        return target

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((check_ip(target), port))
        sock.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        sock.sendto(("Host: " + proxy_ip + "\r\n\r\n").encode('ascii'), (target, port))
        return sock
        return True
    except:
        return False

def get_ports(mode):
    if mode == 1:
        for port in range(1, 1025):
            queue.put(port)
    elif mode == 2:
        for port in range(1, 48129):
            queue.put(port)
    elif mode == 3:
        ports = [20, 21, 22, 23, 25, 53, 80, 110, 443]
        for port in ports:
            queue.put(port)

    elif mode == 4:
        start = int(input("Enter starting port:"))
        end = int(input("Enter ending port:"))
        for port in range(start, end):
            queue.put(port)

    elif mode == 5:
        ports = input("Enter your ports (seperate by blank):")
        ports = ports.split()
        ports = list(map(int, ports))
        for port in ports:
            queue.put(port)

def worker():
    while not queue.empty():
        port = queue.get()
        config = portscan(port)
        if config:
            try:
                banner = get_banner(config)
                print("Port {} is open!".format(port)+' : '+str(banner.decode().stip('\n')))
            except:
                print("Port {} is open!".format(port))
            open_ports.append(port)
        else:
            print("Port {} is closed!".format(port))

def run_scanner(threads, mode):

    get_ports(mode)

    thread_list = []

    for t in range(threads):
        thread = threading.Thread(target=worker)
        thread_list.append(thread)

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()

    print("Open ports are:", open_ports)

mode = int(input("Enter Mode[1:1-1024, 2:1-48128, 3:Selected Few, 4:Custom(Range), 5:Custom(Specific)]:"))
threads = int(input("Enter the number of threads:"))
run_scanner(threads, mode)