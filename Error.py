import os,json,Main
        
def neterror():
    jsonpath = f'{os.path.dirname(__file__)}\Config.json'
    print('无法连接服务器，您可以')
    print('按1为换服务器url')
    print('按2为重启程序')
    print('按其余键为退出程序')
    cmd = input('请输入您的操作：')
    if cmd == '1':
        myurl = input('服务器url：')
        with open(jsonpath,"w+") as url:
            json.dump({"Server":{"url":myurl}},indent = True,fp = url)
    elif cmd == '2': pass
    else: exit()

def error(ret:str)->int:
    if ret.get('code') == 400:
        print(f'操作失败（问题为{error}），请再次尝试，如果有疑问，请联系管理员或者NaCl')
        return -1
    elif ret.get('code') == 405:
        print('请重新登陆')
        Main.main()
        return 1
    else:
        print('操作成功')
        return 0