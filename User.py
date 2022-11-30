import Net,Exception,hashlib,Token

def login():
    print('请登录Appagent')
    name = input('用户名：')
    password = hashlib.sha256(input('密码：')).hexdigest()
    ret = Net.net('Login',{'name':name,'password':password},None,'POST')
    if Exception.exception(ret) == 0: Token.settoken(ret)

def register():
    print('请注册Appagent')
    name = input('用户名：')
    password = input('密码：')
    passwordagain = input('重新输入密码：')
    if password != passwordagain:
        print('抱歉，两次密码不同，请重新注册')
        register()
    else:
        Exception.exception(Net.net('Register',{'name':name,'password':hashlib.sha256(password).hexdigest()},None,'POST'))