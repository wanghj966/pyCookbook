'''
Created on 2013-4-10

@author: buaa
'''
#-*-coding:utf-8 -*-
all_the_test=open("__init__.py",'r').read()
all_the_data=open("__init__.py","rb").read()

file_object=open("__init__.py",'r')
try:
    all_the_test=file_object.read()
finally:
    file_object.close()

line_of_all_the_lines=open("__init__.py").readlines()   #include \n

#not include \n
list_of_all_the_lines=file_object.read().splitlines()
list_of_all_the_lines=file_object.read().split('\n')
list_of_all_the_lines=[L.rtrip('\n') for L in file_object]

#文本用 ru打开
file_object = open('thefile.txt')
try:
    for line in file_object:
        pass
        #process line
finally:
    file_object.close( )
    
    
file_object = open('abinfile', 'rb')
try:
    while True:
        chunk = file_object.read(100)
        if not chunk:
            break
       # do_something_with(chunk)
finally:
    file_object.close( )
    
#封装函数
file_object=open('abinfile','rb')
def read_file_by_chunks(filename,chunksize=100):
    file_object=open(filename,'rb')
    while True:
        chunk=file_object.read(chunksize)
        if not chunk:
            break
        yield chunk
    file_object.close()
file_object = open('thefile.txt', 'rU')
try:
    for line in file_object:pass
       # do_something_with(line)
finally:
    file_object.close( )