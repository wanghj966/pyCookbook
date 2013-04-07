'''
Created on 2013-4-7

@author: buaa
'''

import re
astring='abc  edf    txf'
revwords=re.split(r'(\s+)',astring);
print revwords
revwords.reverse()
revwords=''.join(revwords)
