'''
Created on 2013-4-7

@author: buaa
'''
def isAString(anObject):
    return isinstance(anObject,basestring)
def isExactlyAString(anobj):
    return type(anobj) is type('')
def isStringLike(anobj):
    try:anobj+''
    except:return False
    else:return True
    