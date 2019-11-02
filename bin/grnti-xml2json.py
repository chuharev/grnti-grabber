#!python3

from xmljson import parker, Parker
from xml.etree.ElementTree import fromstring
from json import dumps
import sys

FILENAME = sys.argv[1]

with open(FILENAME, 'r') as f:
    xmlString = f.read()
    print(dumps(parker.data(fromstring(xmlString)), ensure_ascii=False, indent=4))