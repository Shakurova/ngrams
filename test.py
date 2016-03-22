# -*- coding: utf-8 -*-
import re, codecs, sys, time

arr_word = []
dictionary = {}
count_line = 0 # How many lines have already been processed
testfile = u'test.tsv'

def frequency():
    count_line = 0
    with codecs.open(testfile, 'r', 'utf-8') as f:
        for line in f:
            splited_line = line.split()
            #sys.stdout.write(splited_line[0] + " " + splited_line[1] + " " + splited_line[3] + "\r\n")
            aa = splited_line[1].split('_')[0]
            if aa not in dictionary:
                dictionary[aa] = int(splited_line[3])
                #sys.stdout.write(splited_line[1] + " " + str(dictionary[splited_line[1]]) + "\r\n")
            else:
                dictionary[aa] += int(splited_line[3])
                #sys.stdout.write(splited_line[1] + " " + str(dictionary[splited_line[1]]) + "\r\n")
                #if aa[0] != u'' and splited_line[0][1] == u'ADJ':
                #sys.stdout.write(aa + "\r\n")
##            count_line += 1
##            if count_line % 2000 == 0:
##                print (count_line)
##            #sys.stdout.write(splited_line[1]+ "\r\n")
##            if splited_line[1] not in dictionary:
##                dictionary[splited_line[1]] = 1
##                #sys.stdout.write(splited_line[1] + " " + str(dictionary[splited_line[1]]) + "\r\n")
##            else:
##                dictionary[splited_line[1]] += 1
##                #sys.stdout.write(splited_line[1] + " " + str(dictionary[splited_line[1]]) + "\r\n")
    return (dictionary)

frequency()


##Запись в файл ngrams_result.tsv в формате существительное + число вхождений
w = codecs.open(u'test_result.tsv', 'w', 'utf-8')
for i in sorted(dictionary, key=dictionary.get, reverse=True):
    w.write(i +'\t'+ str(dictionary[i]) + "\r\n")
w.close()
