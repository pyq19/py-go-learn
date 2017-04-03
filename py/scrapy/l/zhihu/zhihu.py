import requests
import re, time
import os.path
try:
    import cookielib # 2
except:
    import http.cookiejar as cookielib
try:
    from PIL import Image
except:
    print('导入PIL->Image失败..')


# 构造Request headers
agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
headers = {
    'Host': 'www.zhihu.com',
    'Referer': 'https://www.zhihu.com/',
    'User-Agent': agent
}

# 使用登陆cookie信息
session = requests.session()
session.cookies = cookielib.LWPCookieJar(filename='cookies')
try:
    session.cookies.load(ignore_discard=True)
except:
    print('cookie未能加载')


# 通过查看用户个人信息来判断是否已经登陆 
def isLogin():
    url = 'https://www.zhihu.com/settings/profile'
    sta_code = session.get(url, headers=headers, allow_redirects=False).status_code
    return sta_code == 200


# 获取登陆时需要的_xsrf
# <input type="hidden" name="_xsrf" value="725c7b92bf2f520660a4be4df1c255b5"/>
def getXsrf():
    url = 'https://www.zhihu.com'
    response = session.get(url, headers=headers)
    reg = r'.*name="_xsrf" value="(.*?)"/>' # .* !!!
    obj = re.match(reg, response.text)
    if obj:
        return obj.group(1)
    else:
        print('_xsrf获取为空')
        return ''


def getCaptcha():
    t = str(int(time.time() * 1000))
    captcha_url = 'https://www.zhihu.com/captcha.gif?r=' + t + '&type=login' 
    response = session.get(captcha_url, headers=headers)
    with open('captcha.jpg', 'wb') as f:
        f.write(response.content)
        f.close()
    # !!! 调用pillow的Image显示验证码
    try:
        im = Image.open('captcha.jpg')
        im.show()
        im.close()
    except:
        print('请到%s目录下找到captcha.jpg手动输入验证码..' % os.path.abspath('captcha.jpg'))
    captcha = input('请输入验证码\n>')
    return captcha


def login(account, password):
    # 通过输入的用户名判断是否是手机号
    if re.match(r'^1\d{10}$', account):
        print('手机号登录')
        post_url = 'https://www.zhihu.com/login/phone_num'
        post_data = {
            '_xsrf': getXsrf(),
            'password': password,
#            'captcha': getCaptcha(),
            'phone_num': account,
        }
    else:
        print('EMAIL LOGIN')
    # 输入验证码才能登陆成功
    post_data['captcha'] = getCaptcha()
    response = session.post(post_url, data=post_data, headers=headers)
    login_code = response.json() # !!
    print(login_code['msg'])
    # 完成登陆..
    session.cookies.save()


try:
    input = raw_input # !!!
except:
    print('...input...exception')
    pass


if __name__ == '__main__':
    if isLogin():
        print('已经登录了')
    else:
        account = input('请输入用户名\n>')
        password = input('密码\n>')
        login(account, password)
