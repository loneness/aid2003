from select import select
from time import sleep

from socket import socket

s = socket()
s.bind(('0.0.0.0', 6666))
s.listen(5)

f = open('mylog', 'r')

print('IO监控')
sleep(5)
rs, ws, xs = select([s], [], [])
print('rlist:', rs)
print('wlist:', ws)
print('xlist:', xs)