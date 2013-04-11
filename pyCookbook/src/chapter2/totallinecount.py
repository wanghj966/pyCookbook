'''
Created on 2013-4-10

@author: buaa
'''
thefilepath=''
count = len(open(thefilepath, 'rU').readlines( ))
count = -1
for count, line in enumerate(open(thefilepath, 'rU')):
    pass
count += 1

count=0
thefile=open(thefilepath,'rb')
while True:
    buffer=thefile.read(8102*1024)
    if not buffer:break
    count+=buffer.count("\n")
thefile.close()


#os.popen,read().splitlines();enumerate;read(N)

#bench test
import time
def timeo(fun,n=10):
    start=time.clock()
    for i in xrange(n):fun()
    stend=time.clock()
    thetime=stend-start
    return fun.__name__,thetime

import os
def linecount_popen():
    return int(os.popen("wc -l nunc").read().split())
def linecount_readlines():
    return len(open('nunc').readlines())
def linecount_enumerate():
    count=-1
    for count,line in enumerate(open('func')):pass
    return count+1
def linecount_block():
    count=0
    thefile=open('nuc','rb')
    while True:
        buffer=thefile.read(65536)
        if not buffer:break
        count+=buffer.count('\n')
    return count
for f in linecount_popen, linecount_readlines, linecount_enumerate, linecount_block:
    print f.__name__, f( )
for f in linecount_popen, linecount_readlines, linecount_enumerate, linecount_block:
    print "%s: %.2f"%timeo(f)