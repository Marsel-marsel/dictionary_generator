# dictionary_generator
Generates dictionary of Moscow mobile numbers. Includes MTS, Megafon, Beeline, Tele2 subscribers.
Script fetchs phone number patterns from indexmain.ru_collected.txt and generates dictionary phone_num_dict.txt. Each phone number presents twice with 7 and 8 country codes. Python 2 compatible.
Generated dictionary phone_num_dict.txt contains 82620000 unique numbers. File size: 1.9GB.

Performance:
python2 rus_mobile_number_generator.py  87.97s user 1.30s system 98% cpu 1:30.36 total
