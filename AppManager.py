import Net,Token,Exception,Main,Help
def Create():
    print('创建一个项目：')
    remotepath = input('远程仓库地址：')
    ymlpath = input('项目中docker-compose.yml地址：')
    Exception.exception(Net.net('/Main/Create',{'remotepath':remotepath,'ymlpath':ymlpath},Token.gettoken(),'POST'))
    
def Listdir():
    print('列出指定文件夹的子文件')
    listpath = input('文件夹地址：')
    Exception.exception(Net.net('/Main/Listdir',{'listpath':listpath},Token.gettoken(),'POST'))

def Pull():
    print('从git拉取内容')
    gitpath = input('git远程仓库地址：')
    pullurl = input('拉取到本地的地址：')
    Exception.exception(Net.net('/Main/Pull',{'gitpath':gitpath,'pullurl':pullurl},Token.gettoken(),'POST'))

class dockerapp:
    def __init__(self):
        print('指定一个docker app容器')
        self.__ymlpath = input('项目中docker-compose.yml地址：')
        self.__container = input('应用的容器名：')
    def main(self):
        cmd = input('你的容器操作：').lower().title()
        if cmd in ['Log','Stop','Restart','Remove']:
            Exception.exception(Net.net(f'/Main/{cmd}',{'ymlpath':self.__ymlpath,'container':self.__container},Token.gettoken(),'POST'))
            if cmd == 'Remove': Main.appmanager()
            else: self.main()
        elif cmd == 'Exit': 
            Main.appmanager()
        elif cmd == 'Help': 
            Help.dockerapphelp()
            self.main()
        else: 
            print('输入了无效指令，请您重新输入，如果您忘记了指令，请输入Help')
            self.main()

