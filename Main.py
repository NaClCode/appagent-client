import User,Help,AppManager,Exception

def user():
    cmd = input('您的用户操作是：').lower().title()
    if cmd == 'Exit': exit()
    else:
        if cmd == 'Login': User.login()
        elif cmd == 'Register': User.register()
        elif cmd == 'Help': Help.userhelp()
        else: Exception.cmdexception()
        user()

def appmanager():
    cmd = input('您的项目操作：').lower().title()
    if cmd == 'Exit': user()
    else:
        if cmd == 'Create': AppManager.Create()
        elif cmd == 'Listdir': AppManager.Listdir()
        elif cmd == 'Pull': AppManager.Pull()
        elif cmd == 'Dockerapp': 
            app = AppManager.dockerapp()
            app.main()
        elif cmd == 'Help': Help.appmanagerhelp() 
        else: Exception.cmdexception()
        appmanager()

if __name__ == '__main__':
    user()


    