import User

def main():
    print('用户操作：')
    print('按1为登录')
    print('按2为注册')
    print('按3为退出')
    cmd = input('您的操作是')
    if cmd == '1': User.login()
    elif cmd == '2': User.register()
    elif cmd == '3': exit()
    else: print('输入了无用数字，请您重新输入')
    user()