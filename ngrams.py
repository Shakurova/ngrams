# -*- coding: utf-8 -*-
import re
import codecs
import gzip
##f = f = gzip.open('googlebooks-rus-all-2gram-20120701-vl.gz', 'r')
##for line in f():
##    file_content = f.read()
##f.close()
arr_word = []
dictionary = {}
with gzip.open(u'googlebooks-rus-all-2gram-20120701-vl.gz', 'rb') as f:
    for line in f:
        line = line.decode('utf8')
        second = re.findall(u'(?:влажный|ВЛАЖНЫЙ)(?:_ADJ)? ([а-яА-ЯёЁ]+)', line)
        for iss in second:
            c = 0
            if iss not in dictionary:
                dictionary[iss] =1
            else:
                c = dictionary[iss]
                c+=1   
                dictionary[iss] = 1
            ##print iss

w = codecs.open("ngrams_result.txt", u'w', u'utf-8')       
for d in dictionary:
        w.write(d + "\n")
w.close()
         
##            arr_word.append(line)
##for i in arr_word:
##    print i
##for iline in arr_word:
##    second = re.findall(u'(?:влажный|влажный)(?:_ADJ)? ([а-яА-ЯёЁ]+)(?:_NOUN)?', iline)
##    print second
##    c = 0
##    if second not in dictionary:
##        dictionary[second] =1
##    else:
##        c = dictionary[second]
##        c+=1   
##        dictionary[second] = 1
##for d in dictionary:
##    print d
    
