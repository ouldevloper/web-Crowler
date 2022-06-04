from curses import noecho
from tokenize import String
import requests
import sys
import re
from pprint import pprint
url = sys.argv[1]

result = []
def getResponse(url:str)->str:
    ret = None
    try:
        resp = requests.get(f"https://{url}")
        ret = resp.text
    except:
        try:
            resp = requests.get(f"http://{url}")    
            ret = resp.text
        except:
            print("Error! try to enter url in correct format.")
            ret = None
    return ret
def extractUrls(urlContent:str)->None:
    hrefs = re.compile(r'<a.+?\s*href\s*=\s*["\']?([^"\'\s>]+)["\']?')
    res = hrefs.findall(urlContent)
    return res;

def crowler(url:str)->None:
    pass
