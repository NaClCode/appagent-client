import os

path = os.path.dirname(__file__)

def settoken(ret:dict):
    with open(f'{path}/user.token','rw+') as Token:
        Token.write(ret.get('body'))

def gettoken()->dict:
    with open(f'{path}/user.token','rw+') as Token:
        token = Token.read()
    return {'token',token.replace('"','')}



