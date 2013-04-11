#/usr/bin/env python
import os,sys
'''
Created on 2013-4-10

@author: buaa
'''
nargs=len(sys.argv)
if not 3<=nargs<=5:
    print "usage:%s search_text repalce_text[infile [outfile]]" % os.path.basename(sys.argv[0])
else:
    stext=sys.argv[1]
    rtext=sys.argv[2]
    input_file=sys.stdin
    output_file=sys.stdout
    if nargs>3:
        input_file=sys.argv[3]
    if nargs>4:
        output_file=sys.argv[4]
    for s in input_file:
        output_file.write(s.replace(stext,rtext))
    output_file.close()
    input_file.close()
    

output_file.write(input_file.read( ).replace(stext, rtext))