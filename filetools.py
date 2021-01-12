import os

def uniqFN(filename, serial=False, iStart=1, returnPrevious=False):
    """
    if we want uniqFN likes file1.jpg, file2.jpg file3.jpg
    we need to have filename="file.jpg"
    """
    fn, ext = os.path.splitext(filename)   #    ext includes .
    i   = iStart
    fnI = "%(fn)s-%(i)d" % {"fn" : fn, "i" : i}
    ofnI = None
    while os.access(fnI + ext, os.F_OK):
        i += 1
        ofnI= fnI
        fnI = "%(fn)s-%(i)d" % {"fn" : fn, "i" : i}

    if not returnPrevious:
        return fnI + ext
    else:
        if ofnI is not None:
            return ofnI + ext, fnI + ext
        else:
            return None, fnI + ext

def make_deep_directory(dirpath):
    """
    dirpath - Absolute or relative path to directory tree to create.  
    """
    pathparts = dirpath.split("/")
    L         = len(pathparts)
    if pathparts[L-1] == "":
        pathparts.pop(L-1)
    spath = ""
    if dirpath[0] == "/":
        spath = "/" 
        pathparts.pop(0)

    L = len(pathparts)

    for i in range(L):
        spath += pathparts[i]
        print(spath)
        if not os.access(spath, os.F_OK):
            os.mkdir(spath)
        if i < L - 1:
            spath += "/"
    return spath
    

    
    
    


    
