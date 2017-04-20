import os

file_path = '/Users/Mccree/p/py-go-learn/py/merge-two-dictionaries.py'
directory = os.path.dirname(file_path) 
print(directory) # /Users/Mccree/p/py-go-learn/py


try:
    os.stat(directory)
    print(os.stat(directory))
# posix.stat_result(st_mode=16877, st_ino=6098642, st_dev=16777220, st_nlink=15, st_uid=501, st_gid=20, st_size=510, st_atime=1491194491, st_mtime=1491194490, st_ctime=1491194490)
except:
    os.mkdir(directory)
    print('exceptiion....')


# f = file(filename)
# print(f)

def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)



