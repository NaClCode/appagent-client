import os

path = os.path.dirname(__file__)

def settoken(ret:dict):
    with open(f'{path}/user.token','w+') as Token:
        Token.write(ret.get('body'))

def gettoken()->dict:
    with open(f'{path}/user.token','r+') as Token:
        token = Token.read()
    return {'token':token.replace('"','')}



