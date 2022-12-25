import Net,Token,Exception,Main,Help 
class File():
    def __init__(self):
        self.__path = input('文件夹地址：')
    def main(self):
        cmd = input('你的File操作：').lower().title()
        if cmd in ['Tree','Dfh','Rm']:
            Exception.exception(Net.net(f'Main/File/{cmd}',{'listpath':self.__path},Token.gettoken(),'POST'),True)
        elif cmd == 'Help': Help.filehelp()
        else: Exception.cmdexception()
            
class Git:
    def __init__(self) -> None:
        self.__giturl = input('远程仓库地址(只支持http网址形式)：')
        self.__gitbranch = input('Git分支：')
        self.__gitname = input('Git用户名：')
        self.__gitpassword = input('Git用户密码：')
        self.__dest = input('地址：')
    def main(self):
        cmd = input('你的Git操作：').lower().title()
        if cmd == 'Exit': Main.appmanager()
        else:
            if cmd in ['Clone','Pull']: Exception.exception(Net.net(f'Main/Git/{cmd}',{'gitname':self.__gitname,'gitpassword':self.__gitpassword,'giturl':self.__giturl,'branch':self.__gitbranch,'dest':self.__dest},Token.gettoken(),'POST'))
            elif cmd == 'Help': Help.githelp()
            else: Exception.cmdexception()

class dockerapp:
    def __init__(self):
        self.__ymlpath = input('项目中docker-compose.yml地址：')
        self.__container = input('应用的容器名：')
    def main(self):
        cmd = input('你的容器操作：').lower().title()
        if cmd == 'Exit': Main.appmanager()
        elif cmd == 'Remove': Exception.exception(Net.net(f'Main/Docker/{cmd}',{'ymlpath':self.__ymlpath,'container':self.__container},Token.gettoken(),'POST'))
        else:
            if cmd in ['Stop','Restart','Up','Down','Start']: 
                Exception.exception(Net.net(f'Main/Docker/{cmd}',{'ymlpath':self.__ymlpath,'container':self.__container},Token.gettoken(),'POST'))
            elif cmd == 'Log':
                ret = Net.net(f'Main/Docker/{cmd}',{'ymlpath':self.__ymlpath,'container':self.__container},Token.gettoken(),'POST')
                if Exception.exception(ret) == 0:   print(ret.get('body'))
            elif cmd == 'Help': Help.dockerapphelp()
            else: Exception.cmdexception()
            self.main()

