import requests
try:
    import cookielib # 2
except:
    import http.cookiejar as cookielib # 3

import re, time, os, os.path
try:
    from PIL import Image
except:
    print('pillow导入失败')


agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
headers = {
    'Host': 'www.zhihu.com',
    'Referer': 'https://www.zhihu.com/',
    'User-Agent': agent,
}


# 使用登陆cookie信息
session = requests.session()
session.cookies = cookielib.LWPCookieJar(filename='cookies.txt') # 保存cookie！！！
try:
    session.cookies.load(ignore_discard=True)
except:
    print('cookie 未加载')


def get_xsrf():
    url = 'https://www.zhihu.com'
    response = session.get(url, headers=headers)
    text = response.text
#    reg = '.*name="_xsrf" value="(.*?)"/>'
    reg = '.*type="hidden" name="_xsrf" value="(.*?)"/>'
    obj = re.match(reg, text)
    if obj:
        print(obj.group(1))
        return obj.group(1)
    else:
        print(response.text)
        print('***' * 50)
        return ''


def get_captcha():
    t = str(int(time.time()*1000))
    captcha_url = 'https://www.zhihu.com/captcha.gif?r=' + t + '&type=login'
    r = session.get(captcha_url, headers=headers)
    with open('captcha.jpg', 'wb') as f:
        f.write(r.content)
    # 用pillow的Image显示验证码
    try:
        im = Image.open('captcha.jpg')
        im.show()
        im.close()
    except:
        l = op.path.abspath('captcha.jpg')
        print('请到%s目录找到captcha.jpg手动输入验证码' % l)


def isLogin():
    # 通过查看用户个人信息来判断是否登陆
    url = 'https://www.zhihu.com/settings/profile'
    login_code = session.get(url, allow_redirects=False).status_code
    if int(x=login_code) == 200: #!!!!
        return True
    else:
        return False


def zhihu_login(account, password):
    # 知乎登陆
    if re.match('^1\d{10}', account):
#        print('phone num login...\n'）
        post_url = 'https://www.zhihu.com/login/phone_num'
        postdata = {
            '_xsrf': get_xsrf(),
            'password': password,
            'phone_num': account,
        }
    else:
        print('EMAIL LOGIN..\n')
        post_url = 'https://www.zhihu.com/login/email'
        postdata = {
            '_xsrf': get_xsrf(),
            'password': password,
            'email': account,
        }
#    try:
        # 如果不用验证码直接登陆成功
#        login_page = session.post(post_url, data=postdata, headers=headers)
#        login_code = login_page.text
#        print(login_page.status)
#        print(login_code)
#    except:
    # 如果需要验证码才能登陆
    postdata['captcha'] = get_captcha()
    login_page = session.post(post_url, data=postdata, headers=headers)
    login_code = eval(login_page.text) # eval ??!!
    print(login_code['msg'])
    print(login_page.status)
    session.cookies.save()

try:
    input = raw_input
except:
    pass

if __name__ == '__main__':
    if isLogin():
        print('已登陆')
    else:
        account = input('请输入用户名:\n>')
        password = input('密码:\n>')
        zhihu_login(account, password)

