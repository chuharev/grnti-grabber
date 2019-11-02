#!python3

from urllib.request import urlopen
from bs4 import BeautifulSoup

MY_URL = "http://grnti.ru"


def get_page(lnk, level):
    tab = '  '*level
    html = urlopen(lnk)
    bs = BeautifulSoup(html.read());

    lst = bs.find_all('ul', class_="grnt_list")
    lst  = lst[0].find_all("a")

    for subj in lst:
        if subj.get("href").startswith('#'):
            return

        newlnk =  MY_URL + subj.get("href")

        txt = subj.get_text()
        if txt[-2:] ==  '\r\n':
            txt = txt[:-2]

        print(tab, txt)
        get_page(newlnk, level + 1)

    return

get_page(MY_URL, 0 )

