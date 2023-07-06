from curses import noecho
from tokenize import String
import requests
import sys
import re
from pprint import pprint
from urllib.parse import urlparse

url = sys.argv[1]

result = []


def hostInfo(url):
    return urlparse(url).netloc

def getResponse(url:str)->str:
    # ret = None
    try:
        resp = requests.get(f"{url}")
        return resp.text
    except:
        return ""
        # raise Exception('Error! try to enter url in correct format.')
    # return ret

def extractUrls(urlContent:str)->None:
    hrefs = re.compile(r'<a.+?\s*href\s*=\s*["\']?([^"\'\s>]+)["\']?')
    res = hrefs.findall(urlContent)
    return res

host = hostInfo(url=url)
base = url
def crowler(url:str)->None:
    resp = getResponse(url)
    urls = extractUrls(resp)
    # pprint(urls)
    for u in urls:
        if u.startswith('/'):
            u = base+u

        if u not in result:
            print(f'[+] {u}') if not u.startswith('/') else print(f'[+] {base}{u}')

        if host not in u and u.startswith('/'):
            pass 
        else:
            if u not in result:
                result.append(u)
            crowler(u)
            




crowler(sys.argv[1])
pprint(result)
