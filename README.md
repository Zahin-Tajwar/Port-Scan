## Port-Scan
A pretty advanced port scanner program written in python.

**Port Scanners are primarily used for Penetration Testing and Information Gathering. Essentially, we are looking for open ports in a host for one of two reasons. To ensure our servers are secure or to exploit those of someone else. An unnecessarily opened port means vulnerability and comes with a lack of security.**

### Importing Libraries
- Socket will be used for our connection attempts to the host at a specific port.
- Threading will allow us to run multiple scanning functions simultaneously.
- Queue is a data structure that will help us to manage the access of multiple threads on a single resource, which in our case will be the port numbers. Since our threads run simultaneously and scan the ports, we use queues to make sure that every port is only scanned once.
- IPy is used to check if the target is a IP address or Domain. And if its a Domain then find its IP.

### Instructions
- Run the main.py file
- As target choose an IP of a device you own or have permission to hack and as a fake IP-address choose a random but still valid address. 
- Select a suitable mode and you will get the result
