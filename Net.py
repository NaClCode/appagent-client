import requests
import os,json,Exception

jsonpath = f'{os.path.dirname(__file__)}\Config.json'

def net(neturl:str,payload:dict,headers:dict,method:dict)->dict:
    with open(jsonpath) as url:
        url = json.load(url).get('Server')
    reurl = f'{url.get("url")}/{neturl}'
    try:
        response = requests.request(method = method, url = reurl, headers=headers, data=payload)
        return {'code':response.status_code,'body':response.text,'head':response.headers}
    except: Exception.netexception()