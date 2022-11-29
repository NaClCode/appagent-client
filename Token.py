import os,json,sys
path = f'{os.path.dirname(__file__)}'.replace('AppManager','')
sys.path.append(path)
import Net

def Token()->dict:
    with open(f'{path}/Token.json') as url:
        url = json.load(url).get('token')
    return {'token',url.replace('"','')}


