import sys
reload(sys)
sys.setdefaultencoding('utf-8')

s = 'look into my eyes look into my eyes the eyes'
words = s.split(' ')
print words
# ['look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes', 'the', 'eyes']

from collections import Counter

word_counts = Counter(words)
top_three = word_counts.most_common(3)
print top_three # [('eyes', 3), ('into', 2), ('my', 2)]
print word_counts['look'] # 2
