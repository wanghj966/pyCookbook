def VersionFile(file_spec,vtype='copy'):
    import os,shutil
    if os.path.isfile(file_spec):
        if vtype not in ('copy','rename'):
            raise ValueError,'unkown vtype %r' % (vtype,)
        n,e=os.path.splitext(file_spec)
        if len(e)==4 and e[1:].isdigit():
            num=1+int(e[1:])
            root=n
        else:
            num=0
            root=file_spec
        for i in xrange(num,1000):
            newfile='%s.%03d'%(root,i)
            if not os.path.exists(newfile):
                if vtype=='copy':
                    shutil.copy(file_spec, newfile)
                else:
                    os.rename(file_spec, newfile)
                return True
        raise RuntimeError,"Can't %s %r, all names taken" %(vtype,file_spec)
        return False