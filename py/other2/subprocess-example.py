#coding:utf8

import subprocess

# subprocess模块用来取代如下模块和函数
# os.system
# os.spawn*
# os.popen*
# popen2.*
# commands.*

# subprocess.call = os.system
# call只返回命令的返回值
subprocess.call('ls -l /Users/Mccree/p/py-go-learn/py/other2', shell=True)
# -rw-r--r--  1 WRQ  staff  906 Apr 10 16:48 errno.py
# -rw-r--r--  1 WRQ  staff   91 Apr 10 16:38 flatten.py
# -rw-r--r--  1 WRQ  staff  286 Apr 10 16:54 subprocess-example.py

print subprocess.call('exit 1', shell=True) # 1

# 由于安全问题不建议使用shell=True，可以把命令拆分成列表
subprocess.call(['ls', '/Users'], shell=False)
# Mccree  Shared

# 拆分命令最简单的方法是使用shlex模块
import shlex
print shlex.split('ls /sers/Mccree/p/py-go-learn/py/other2')
# ['ls', '/sers/Mccree/p/py-go-learn/py/other2']

# subprocess.check_call # 添加了错误处理的执行系统命令方法，
# 当执行call方法的返回值不为0，就会抛出CalledProcessError异常
# subprocess.check_call('exit 1', shell=True)
# subprocess.CalledProcessError: Command 'exit 1' returned non-zero exit status 1


# Popen 用来执行子进程的类，通过communicate方法获得执行结果
from subprocess import Popen, PIPE
proc = Popen(['echo', 'hello!~~'], stdout=PIPE)
stdout, stderr = proc.communicate()
print stdout # hello!~~

# Popen 类经常用来实现Shell的管道功能，假设要执行'ls /Users/Mccree|grep scrapy'
# 可以使用如下方式
from subprocess import Popen, PIPE
p1 = Popen(['ls', '/Users/Mccree'], stdout=PIPE)
p2 = Popen(['grep', 'scrapy'], stdin=p1.stdout, stdout=PIPE)
stdout, _ = p2.communicate()
print stdout # scrapy.sh



# check_output 在2.7和3都可以使用，比Popen更简单地获得输出，
# 但是要执行的返回值为0，否则仍然抛出CalledProcessError异常
print subprocess.check_output(['ls', '-l', '/Users/Mccree'])
# drwxr-xr-x    5 WRQ   staff   170 Jan 13 20:53 Android
# drwx------+  30 WRQ   staff  1020 Apr 10 12:02 Desktop
# drwx------+  25 WRQ   staff   850 Mar 29 13:09 Documents
# ...
# 出现错误时，可以额外地执行exit 0，就能正常获得输出
print subprocess.check_output('ls /no/such/file; exit 0', stderr=subprocess.STDOUT, shell=True)
# ls: /no/such/file: No such file or directory
