

def Token()->dict:
    with open(f'{path}/Token.json') as url:
        url = json.load(url).get('token')
    return {'token',url.replace('"','')}
    
def Create():
    print('创建一个项目：')
    remotepath = input('远程仓库地址：')
    ymlpath = input('项目中docker-compose.yml地址：')
    Token.Net.net('/Main/Create',{'remotepath':remotepath,'ymlpath':ymlpath},Token.Token(),'POST')
    