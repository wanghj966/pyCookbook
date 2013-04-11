import types,tempfile,os
CHUNK_SIZE=16*1024
def adapt_file(fileObj):
    if isinstance(fileObj, file):return file
    tempFileObj=tempfile.TemporaryFile() 
    while True:
        data=fileObj.read(CHUNK_SIZE)
        if not data:break
        tempFileObj.write(data)
        tempFileObj.seek(0)
    fileObj.close()
    tempFileObj.seek(0)
    return tempFileObj
 
import StringIO
fileObj=StringIO.StringIO()
fileObj.write("abc\ndsafadsfsddef\n")
fileObj.seek(0)
f=adapt_file(fileObj)
print f.read()