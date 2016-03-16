# -*- coding: utf-8 -*-
import re, codecs, sys, time


googlefile = u'googlebooks-rus-all-2gram-20120701-vl'
arr_word = []
dictionary = {} # 
count_line = 0 # How many lines have already been processed
size = 1097621 # КБ
##print sum(1 for l in open(googlefile, "r")) #26274744 - lines



##def cleaning():
##    with codecs.open(googlefile, 'r', 'utf-8') as f:
##        for line in f:
##            re.sub("[^а-яА-ЯёЁ ]", "", line)

##cleaning()


    

def frequency():
    count_line = 0
    #t1 = time.time()
    with codecs.open(googlefile, 'r', 'utf-8') as f:
        for line in f:
            if u"влажный" in line or u"ВЛАЖНЫЙ" in line:
                #sys.stdout.write(line) # All lines that contain u"влажный"
                splited_line = re.split("\s|\t", line)
                count_line += 1
                if count_line == 2000:
                     print count_line
                     #print(time.time() - t1)
                     count_line = 0
                #sys.stdout.write(splited_line[1]+ "\r\n")
                c = 0
                if splited_line[1] not in dictionary:
                    dictionary[splited_line[1]] = 1
                    #sys.stdout.write(splited_line[1] + " " + str(dictionary[splited_line[1]]) + "\r\n")
                else:
                    c = dictionary[splited_line[1]]
                    c += 1   
                    dictionary[splited_line[1]] = c
                    #sys.stdout.write(splited_line[1] + " " + str(dictionary[splited_line[1]]) + "\r\n")
      

frequency()


dictionary.sort()
most = 0
for word in dictionary:
    while most < 30:
        sys.stdout.write(word + " " + str(dictionary[word]) + "\r\n")
        most += 1 
    
# Нужно ли вообще записывать словарь в файл? Наверное да ...
##w = codecs.open(u'ngrams_result.txt', 'w', 'utf-8')
##for d in dictionary:
##    w.write(d + "\r\n")
##w.close()

##1. Можно ли сделать очистку текста от всего что не кирилица не с помощью регулярных выражений? Как это сделать быстрее?
##2. прикинуть, какому объёму в мегабайтах соответствует какое количество строк в файле с биграммами, чтобы уметь предсказывать время работы программы.
##3. 2000 строк обрабатываются примерно за 20 секунд, всего  26274744 строк, значит весь файл будет обрабатываться 72 часа (если я правильно посчитала).
## Как можно ускорить работу программы?
