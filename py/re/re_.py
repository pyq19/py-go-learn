#coding:utf8

import re

# 校验数字的表达式
num = '^[0-9]*$'                        # 数字
num2 = '^\d{n}$'                        # n位的数字
num3 = '^\d{n,}$'                       # 至少n位的数字
num4 = '^\d{m,n}$'                      # m-n位的数字
num5 = '^(0|[1-9][0-9]*)$'              # 0和非0开头的数字               
num6 = '^([1-9][0-9]*)+(.[0-9]{1,2})?$' # 非0开头的，最多带2位小数的数字 # 12.34
num7 = '^(\-)?\d+(\.\d{1,2})?$'         # 带1-2位小数的正数或负数
num8 = '^(\-|\+)?\d+(\.\d+)?$'          # 正数负数和小数
num9 = '^[0-9]+(\.[0-9]{2})?$'          # 有2位小数的正实数
num10 = '^[0-9]+(\.[0-9]{1,3})?$'       # 有1-3位小数的正实数
num11 = '^[1-9]\d*$' or '^([1-9][0-9]*){1,3}$' or '^\+?[1-9][0-9]*$'    # 非0的正整数
num12 = '^\-[1-9][0-9]*$' or '^-[1-9]\d*$'                              # 非0的负整数
num13 = '^\d+$' or '^[1-9]\d*|0$'       # 非负整数
num14 = '^-[1-9]\d*|0$' or '^((-\d+)|(0+))$' # 非正整数
num15 = '^\d+(\.\d+)?$' or '^[1-9]\d*\.\d*|0\.\d*[1-9]\d*|0?\.0+|0$'    # 非负浮点数
num16 = '^((-\d+(\.\d+)?)|(0+(\.0+)?))$' or '^(-([1-9]\d*\.\d*|0\.\d*[1-9]\d*))|0?\.0+|0$' # 非正浮点数
num19 = '^(-?\d+)(\.\d+)?$'
# print re.search(num6, '12345.67').group()

# 校验字符的表达式
str1 = u'^[\u4e00-\u9fa5]*$'            # 汉字
# print(re.search(str1, u'啊事实上').group()) # 啊事实上
str2 = '^[A-Za-z0-9]+$'                 # 英文和数字
str3 = '^.{3,8}$'                       # 长度为3-8的所有字符
str8 = '^\w+$'                          # 数字，26个英文字母，下划线 组成的字符串
