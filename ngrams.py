# -*- coding: utf-8 -*-
import codecs, re, sys, time

googlefile = u'googlebooks-rus-all-2gram-20120701-vl' #Заменить
dictionary = {}

#Проверять, что сначала ADJ, потом NOUN
#Проверять согласование
#Засекать время
#Сделать для разных языков

def preprocessing(googlefile):
	count_line = 0
	prepfile = codecs.open('prepfile.tsv', 'w', 'utf-8')
	with codecs.open(googlefile, 'r', 'utf-8') as f:
		for line in f:
			if u"влажн" in line and u"ADJ" in line and u"NOUN" in line:
				#sys.stdout.write(line) # All lines that contain u"влажный"
				prepfile.write(line)
				count_line += 1
				if count_line % 2000 == 0:
					sys.stdout.write(count_line)
	prepfile.close()
	return (prepfile)

def frequency(testfile):
	count_line = 0
	with codecs.open(testfile, 'r', 'utf-8') as f:
		for line in f:
			splited_line = line.split()
            #sys.stdout.write(splited_line[0] + " " + splited_line[1] + " " + splited_line[3] + "\r\n")
			aa = splited_line[1].split('_')[0]
			if splited_line[0].split('_')[1] == "ADJ":
				if aa not in dictionary:
					dictionary[aa] = int(splited_line[3])
					#sys.stdout.write(splited_line[1] + " " + str(dictionary[splited_line[1]]) + "\r\n")
				else:
					dictionary[aa] += int(splited_line[3])
    #return(dictionary)

#prepfile = preprocessing(googlefile)
prepfile = u'prepfile.tsv'
frequency(prepfile)

##Запись в файл ngrams_result.tsv в формате существительное + число вхождений
w = codecs.open(u'test_result.tsv', 'w', 'utf-8')
for i in sorted(dictionary, key=dictionary.get, reverse=True):
	w.write(i +'\t'+ str(dictionary[i]) + "\r\n")
w.close()




##Описание работы программы

##preprocessing
##Сначала создается файл из строк, содержащих основу нужного прилагательного и теги Adj Noun (порядок пока не учитывается)

##frequency
##Строки делятся по пробелу, а потом по подчеркиванию. Получается массив splited_line = мокрая, Adj, вата, Noun, 1994, 45
##Создается словарь dictionary. если слово есть в словаре, прибавляется число вхождений, если нет - присваивается
