'''
Created on 2013-4-7

@author: buaa
'''
def containsAnyOfSet(seq,aset):
    for c in seq:
        if c in aset:return True
    return False

import itertools
def containsAny(seq,aset):
    for item in itertools.ifilter(aset.__contains__,seq):
        return True
    return False
print containsAny('abcdef',set({'a','t'}))

def containsAnySet(seq,aset):
    return bool(set(aset).intersection(seq))

print containsAnySet('abcdef',['g','t'])
def containsOnly(seq,aset):
    for c in seq:
        if c not in aset:return False
    return True
def containsAll(seq,aset):
    return bool(set(aset).difference(seq))

import string
notrans=string.maketrans('','')
def containsAny_string(astr,strSet):
    return len(strSet)!=len(strSet.translate(notrans,astr))
def containsAll_string(astr,strSet):
    return not strSet.translate(notrans,astr)