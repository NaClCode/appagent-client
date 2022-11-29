import os,json,Net,Error
path = os.path.dirname(__file__)

def login():
    print('请登录Appagent')
    name = input('用户名：')
    password = input('密码：')
    ret = Net.net('Login',{'name':name,'password':password},None,'POST')
    if Error.error():
        with open(f'{path}/Config.json','w+') as Token:
            json.dump({'token':ret.get('body')},indent = True,fp = Token)

def register():
    print('请注册Appagent')
    name = input('用户名：')
    password = input('密码：')
    passwordagain = input('重新输入密码：')
    if password != passwordagain:
        print('抱歉，两次密码不同，请重新注册')
        register()
    ret = Net.net('Register',{'name':name,'password':password},None,'POST')
    Error.error()