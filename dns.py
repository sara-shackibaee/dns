



import requests
from requests.exceptions import HTTPError
import urllib.request
import threading

from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from warnings import filterwarnings
import threading
from threading import Lock
import dns.resolver
import urllib3
import socket


http = urllib3.PoolManager()
filterwarnings(action="ignore")
lock = threading.Lock()


p = []

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# q =queue.Queue()
with open(r"C:\Users\Administrator\Documents\url1.txt", 'r') as f:
    lines = f.readlines()

threshold = 100
fileID = 0
while fileID < len(lines) / float(threshold):
    with open(r"C:\Users\Administrator\Documents\New folder\url1.txt" + str(fileID) + '.txt',
              'w') as currentFile:
        for currentLine in lines[threshold * fileID:threshold * (fileID + 1)]:
            currentFile.write(currentLine)
        fileID += 1
        p.append(currentFile.name)


class test(threading.Thread):
    def __init__(self, p):
        threading.Thread.__init__(self)
        self.path = p

    def run(self):
        mywhois(self.path)


def mywhois(p):
    c = open(p, 'r')
    writer = open(r"C:\Users\Administrator\Documents\url1j.txt", "a")
    writer1 = open(r"C:\Users\Administrator\Documents\url1jj.txt", "a")

    q = []
    for line in c:
        #print(p,line)
        n = line.split('\n')
        #print(n[0])

        urljadid = "http://" + n[0]
        # urljadid1 = "https://" + n[0]


        try:
            myResolver = dns.resolver.Resolver()   #dnsresolve
            myAnswers = myResolver.query(n[0])
            host_ip = socket.gethostbyname(n[0])

            response = requests.get(urljadid ,timeout=20)
            if response.status_code == 200:

                    lock.acquire()
                    #q.append(n[0])
                    print(n[0] + "     " + host_ip)
                    writer.writelines(n[0] + "     " + host_ip)
                    writer.write('\n')
                    writer1.writelines(host_ip)
                    writer1.write('\n')
                    lock.release()

        except Exception as e:
            print(e)

try:
    threadi = []
    for i in range(len(p)):
        name = 'thread name is:' + str(i)
        ti = threading.Thread(target=mywhois, args=(p[i],))
        threadi.append(ti)

    for t in threadi:
        t.start()
    for t in threadi:
        t.join()

except Exception as e:
    print(e)







