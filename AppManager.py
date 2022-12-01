import Net,Token,Exception,Main,Help
def Create():
    remotepath = input('远程仓库地址(只支持http网址形式)：')
    gitname = input('Git用户名：')
    gitpassword = input('Git用户密码：')
    Exception.exception(Net.net('Main/Create',{'gitname':gitname,'gitpassword':gitpassword,'remotepath':remotepath},Token.gettoken(),'POST'))
    
def Listdir():
    listpath = input('文件夹地址：')
    ret = Net.net('Main/Listdir',{'listpath':listpath},Token.gettoken(),'POST')
    if Exception.exception(ret) == 0:
        dirname = ret.get('body').replace('{"Listdir":["','').replace('"]}','').split('","')
        print(f'{listpath}目录下的文件有：')
        for i in dirname:
            print(i)

def Pull():
    gitpath = input('git远程仓库地址：')
    pullurl = input('拉取到本地的地址：')
    Exception.exception(Net.net('Main/Pull',{'gitpath':gitpath,'pullurl':pullurl},Token.gettoken(),'POST'))

class dockerapp:
    def __init__(self):
        self.__ymlpath = input('项目中docker-compose.yml地址：')
        self.__container = input('应用的容器名：')
    def main(self):
        cmd = input('你的容器操作：').lower().title()
        if cmd == 'Exit': Main.appmanager()
        elif cmd == 'Remove': Exception.exception(Net.net(f'Main/{cmd}',{'ymlpath':self.__ymlpath,'container':self.__container},Token.gettoken(),'Delete'))
        else:
            if cmd in ['Log','Stop','Restart']: Exception.exception(Net.net(f'Main/{cmd}',{'ymlpath':self.__ymlpath,'container':self.__container},Token.gettoken(),'POST'))
            elif cmd == 'Help': Help.dockerapphelp()
            else: Exception.cmdexception()
            self.main()

