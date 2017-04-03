
# 1
from subprocess import call
print(call(['ls', '-l']))

# 2
import os
print(os.popen('echo hello world').read())

# 3 
# import subprocess
# user_input = 'heiheihei'
# print(subprocess.Popen('echo %s' % user_input, stdout=subprocess.PIPE).stdout.read())

# 4
print('#4' * 30)
import subprocess
print(subprocess.Popen('echo Hello world', shell=True, stdout=subprocess.PIPE).stdout.read())

# 5
# print('#5' * 30)
# import subprocess
# u_input = 55555555
# print(subprocess.Popen('echo %s', u_input, shell=True, stdout=subprocess.PIPE).stdout.read())
