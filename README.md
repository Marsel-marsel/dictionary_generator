#### Motivation
Using my russians friends WI-FI spots I've noticed that
many of them uses their own cell phone number as password for SSID.
Thus for WI-FI penetration testing I've decided to create script which 
is generate all possible cell phone numbers belonging to russian telecom providers. 

#### How does script work?

Firstly I've decided to generate numbers from 70000000 up to 79999999 and 
from 80000000 up to 89999999. Note that +7 (or 8 as many russian people 
write it down) is country code of Russia. But obviously this list 
has a lot of redundant entries.
So I appealed to _indexmain.ru_ which describes telecom providers codes
and ranges of numbers which can be used as cell phone number.
Thus number of entries in my list decreased dramatically.

So I use _indexmain.ru_collected.txt_'s file entries like
```+7 916 00x-xx-xx```	as pattern to generate numbers from 
```79160000000``` up to ```79160099999``` and also range from 
```89160000000``` up to ```89160099999```. So final list of numbers
contains of MTS, Megafon, Beeline, Tele2 subscribers.

#### POC
After _phone_num_dict.txt_ has been generated I've 
check it with 10 real numbers randomly fetched from 
my own phone dictionary simply using ```grep <friend's number> phone_num_dict.txt; echo $?``` 
and get 10 matches.

#### Further usage
Each entry of _phone_num_dict.txt_ could be SHA1-ed 
to create rainbow table to make brute force attack on 
WPA2 faster.

#### Performance
python2 rus_mobile_number_generator.py  87.97s user 1.30s system 98% cpu 1:30.36 total
