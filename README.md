## GRNTI grubber tools

### Description 
GRNTI stands for russian science classification system (ГРНТИ, Государственный рубрикатор научно-технической информации).

The toolset constist of two utils:

* The first one is designed to grub information from site http://grnti.ru;
* And the last one is used to produce EPrints-compatible XML output.


### Using

You should have python3 installed on your computer. Utils were tested on Linux OS (debian) only.

The typical usecase is presented bellow.
```
$ time python grnti-download.py > grnti-$(date +%Y-%m-%d).txt

real    66m12.275s
user    16m23.076s
sys     0m2.908s

$ python grnti-plain2xml.py grnti-$(date +%Y-%m-%d).txt > grnti-$(date +%Y-%m-%d).xml 
```
And that is all.


For the purpose of verification I dump it here:
```
$ wc -l grnti-$(date +%Y-%m-%d).*
   8028 grnti-2015-10-26.txt
 104394 grnti-2015-10-26.xml
 112422 total

$ ls -l grnti-$(date +%Y-%m-%d).*
-rw-r--r-- 1 user user  707758 Oct 26 17:33 grnti-2015-10-26.txt
-rw-r--r-- 1 user user 2420290 Oct 26 18:05 grnti-2015-10-26.xml

$ sha1sum grnti-$(date +%Y-%m-%d).*
f0250b68c39eb45204dc165f6970fb4781127014  grnti-2015-10-26.txt
d57b049a56fb7eed5136e2cf12287dabc453d55c  grnti-2015-10-26.xml
```

### Keywords
ГРНТИ, рубрикатор, машинно-читаемый вид, machine-readable view,  XML, EPrints



