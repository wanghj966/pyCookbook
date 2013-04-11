'''
Created on 2013-4-10

@author: buaa
'''
#linecache.getline/clearcache/checkcache
thefilepath=''
lineno=''
import linecache
theline=linecache.getline(thefilepath, lineno)

def getline(thefilepath,lineno):
    if lineno<1:return ''
    for cur_lineno,line in enumerate(open(thefilepath,'rU')):
        if cur_lineno==lineno:return line
    return ''