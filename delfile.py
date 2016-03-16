import os, shutil

def delfiles(rootdir):
    filelist = []
    # rootdir = "result"
    filelist = os.listdir(rootdir)
    for f in filelist:
        filepath = os.path.join(rootdir, f)
        if os.path.isfile(filepath):
            os.remove(filepath)
            print(filepath + " removed!")
        elif os.path.isdir(filepath):
            shutil.rmtree(filepath, True)
            print("dir " + filepath + " removed!")

if __name__ == '__main__':
    delfiles('/root/gupiao/data')
    delfiles('/root/gupiao/data2')
    delfiles('/root/gupiao/result')
    delfiles('/root/gupiao/result2')
    delfiles('/root/gupiao/result3')

