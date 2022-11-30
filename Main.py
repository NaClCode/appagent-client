import User,Help,AppManager

def user():
    cmd = input('您的用户操作是').lower().title()
    if cmd == 'Login': User.login()
    elif cmd == 'Register': User.register()
    elif cmd == 'Exit': exit()
    elif cmd == 'Help': 
        Help.userhelp()
        user()
    else: 
        print('输入了无效指令，请您重新输入，如果您忘记了指令，请输入Help')
        user()

def appmanager():
    cmd = input('您的项目操作：').lower().title()
    if cmd == 'Create':
        AppManager.Create()
        appmanager()
    elif cmd == 'Listdir':
        AppManager.Listdir()
        appmanager()
    elif cmd == 'Pull':
        AppManager.Pull()
        appmanager()
    elif cmd == 'Dockerapp':
        app = AppManager.dockerapp()
        app.main()
        appmanager()
    elif cmd == 'Help':
        Help.appmanager()
        appmanager()
    elif cmd == 'Exit': exit()   
    else:
        print('输入了无效指令，请您重新输入，如果您忘记了指令，请输入Help')
        appmanager()
    

    