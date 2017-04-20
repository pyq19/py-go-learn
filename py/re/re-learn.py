import re

txt = ''
with open('./txt', 'r') as f:
    txt = f.read()

# print txt
# <html lang="en-US" >
# </code></pre>
# <p>下面是调用它:</p>
# <span class="hljs-keyword">while</span> candidates:
# <span class="hljs-keyword">return</span> result
# <p>为了理解yield有什么用,首先得理解generators,而理解generators前还要理解iterables</p>
# <span class="hljs-keyword">return</span> result
# <p>这段代码有几个有意思的地方:</p>
# $<span class="hljs-number">100</span>
# <p>它对于一些不断变化的值很有用,像控制你资源的访问.</p>
# <div><script style="display: none;" type="application/javascript">

# reg = r'<span.*?>(\w+)</span>'
# obj = re.search(reg, txt)
# if re.search(reg, txt):
#     print(obj.group()) # <span class="hljs-keyword">while</span>

# reg = r'<span.*?>(\w+)</span>'
# obj = re.findall(reg, txt)
# if obj:
#     print(obj) # ['while', 'return', 'return', '100']

# reg = r'.*?<span.*?>(\w+)</span>.*'
# obj = re.match(reg, txt)
# if obj:
#     print(obj)
# else:
#     print("doesn't find")
# doesn't find
