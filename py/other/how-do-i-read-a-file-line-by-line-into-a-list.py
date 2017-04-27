#coding:utf8

# I want to read the file line by line and each line is appended to the end of the list.
# http://stackoverflow.com/questions/3277503/how-do-i-read-a-file-line-by-line-into-a-list

#############

fname = './aaa'
with open(fname) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]
print content
# ['adgdfg', 'dfhgfhf', 'fghfghf']

##############

lines = [line.rstrip('\n') for line in open('./aaa')]
print lines
