## GRNTI grabber tools

### Description 

[GRNTI](https://ru.wikipedia.org/wiki/%D0%93%D0%BE%D1%81%D1%83%D0%B4%D0%B0%D1%80%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D1%8B%D0%B9_%D1%80%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D0%B0%D1%82%D0%BE%D1%80_%D0%BD%D0%B0%D1%83%D1%87%D0%BD%D0%BE-%D1%82%D0%B5%D1%85%D0%BD%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%BE%D0%B9_%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D0%B8) stands for russian science classification system (ГРНТИ, Государственный рубрикатор научно-технической информации).

The toolset constist of two utils:

* The first one is designed to grab information from site http://grnti.ru;
* And the last one is used to produce  [EPrints](https://en.wikipedia.org/wiki/EPrints)-compatible XML output.

### Setup

Install pipenv to run grnti-grabber in isolated environment:
```sh
pip3 install --user pipenv
```

Set up pipenv (run inside proect folderj):
```sh
pipenv install -e .
```

### Using

You should have python3 installed on your computer. Utils were tested on Linux OS (debian) only.

The typical usecase is presented below.
```
$ time python3 bin/grnti-download.py > data/grnti-$(date +%Y-%m-%d).txt

real    66m12.275s
user    16m23.076s
sys     0m2.908s

$ python3 bin/grnti-plain2xml.py data/grnti-$(date +%Y-%m-%d).txt > data/grnti-$(date +%Y-%m-%d).xml 
$ python3 bin/grnti-xml2json.py data/grnti-$(date +%Y-%m-%d).xml > data/grnti-$(date +%Y-%m-%d).json 
```
And that is all.


For the purpose of verification I dump it here:
```
$ wc -l data/grnti-$(date +%Y-%m-%d).*
   8028 grnti-2015-10-26.txt
 104394 grnti-2015-10-26.xml
 112422 total

$ ls -l data/grnti-$(date +%Y-%m-%d).*
-rw-r--r-- 1 user user  707758 Oct 26 17:33 grnti-2015-10-26.txt
-rw-r--r-- 1 user user 2420290 Oct 26 18:05 grnti-2015-10-26.xml

$ sha1sum data/grnti-$(date +%Y-%m-%d).*
f0250b68c39eb45204dc165f6970fb4781127014  grnti-2015-10-26.txt
d57b049a56fb7eed5136e2cf12287dabc453d55c  grnti-2015-10-26.xml
```

Grab latest version:
```sh
time python3 bin/grnti-download.py > data/grnti-latest.txt
python3 bin/grnti-plain2xml.py data/grnti-latest.txt > data/grnti-latest.xml 
python3 bin/grnti-xml2json.py data/grnti-latest.xml > data/grnti-latest.json
```

### Contributing

Build package metadata:
```sh
python3 setup.py develop --user
```

Running in pipenv:
```sh
pipenv run python3 bin/grnti-download.py
```

Packaging tutorial: https://python-packaging.readthedocs.io/en/latest/

### Keywords

ГРНТИ, рубрикатор, машиночитаемыe данные, machine-readable data,  XML, EPrints