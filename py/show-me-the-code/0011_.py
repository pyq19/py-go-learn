#coding:utf8

# 第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，
# 当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。


# https://github.com/Show-Me-the-Code/python/blob/master/AK-wang/0011/filtered_words.py
def filtered_words(f_file):
    filtered_list = []
    with open(f_file, 'r') as f:
        for line in f:
            filtered_list.append(line.strip())
    return filtered_list


def check_user_input(user_input, filtered_list):
    if user_input in filtered_list:
        return 'freedom'
    return 'human rights'


if __name__ == '__main__':
    input_word = raw_input('>')
    print check_user_input(input_word, filtered_words('0011_words.txt'))



# https://github.com/Show-Me-the-Code/python/blob/master/renzongxian/0011/0011.py

def filter_words(words):
    file_object = open('0011_words.txt', 'r')
    filtered_words = []
    for line in file_object:
        filtered_words.append(line.strip('\n'))
    file_object.close()

    filtered = False
    for filtered_word in filtered_words:
        if filtered_word in words:
            filtered = True
            break

    if filtered is True:
        print 'freedom'
    else:
        print 'human rights'

if __name__ == '__main__':
    while True:
        input_words = raw_input('>')
        filter_words(input_words)
