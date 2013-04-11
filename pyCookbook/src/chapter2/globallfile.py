import glob,os
def all_file(pattern,search_path,pathsep=os.pathsep):
    for path in search_path.split(pathsep):
        for match in glob.glob(os.path.join(path,pattern)):
            yield match
