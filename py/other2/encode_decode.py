#coding:utf8


import sys, locale

print sys.getdefaultencoding() # 'ascii'

# c = locale.getdefaultlocale()
# print c 
# ValueError: unknown locale: UTF-8

reload(sys) # setdefaultencoding 在初始化时被site.py删掉了

sys.setdefaultencoding('UTF-8') # 重新设置默认编码

s = '中国人' # '\xe4\xb8\xad\xe5\x9b\xbd\xe4\xba\xba'

u = s.decode() # u'\u4e2d\u56fd\u4eba'  utf8 -> unicode

gb = s.encode('gb2312') # '\xd6\xd0\xb9\xfa\xc8\xcb'  utf8 -> gb2312

gb.decode('gb2312') # u'\u4e2d\u56fd\u4eba'  gb2312 -> unicode

gb.decode('gb2312').encode() # '\xe4\xb8\xad\xe5\x9b\xbd\xe4\xba\xba'
# gb2312 -> unicode -> utf8

unicode(gb, 'gb2312')
# gb2312 -> unicode

u.encode()
# unicode -> utf8

u.encode('gb2312')
# unicode -> gb2312

