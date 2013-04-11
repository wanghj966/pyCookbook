import os
if os.name=='posix':
    from fcntl import LOCK_EX,LOCK_SH,LOCK_NB:
    def lock(file,flags):
        fcntl.flock(file.fileno(),flags)
    def unlock(file):
        fcntl.flock(file.fileno(),fcntl.LOCK_UN)