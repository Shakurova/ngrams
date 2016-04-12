# -*- coding: utf-8 -*-

import codecs, re, sys, time

googlefile = u'googlebooks-ger-all-2gram-20120701-na' #Заменить
adj_root = u'nass'#Заменить
arr = []
dictionary = {}

					
trash = [u'«', u'»', u'_NOUN_', u',', u'.', u'!', u')', u'*', u'"', u':', u'-', u'--', u';', u'...', u'?',  u'(']

def lines_selector(googlefile):
	''' Получает на вход название файла, содержащего биграммы из google ngrams, год, количество вхождений, число книг в этот год.
	Возвращает массив, состоящий из строк, содержащих корень заданного прилагательного и теги _ADJ и _NOUN. '''
	count_line = 0 # Количество обработанных строк
	f = codecs.open(googlefile, 'r', 'utf8')#, 'utf-8'
	for line in f:
		#line = line.encode('utf-8')#???
		if u'nass' in line or u'naß' in line: #Заменить
			if u'ADJ' in line:
				if u'NOUN' in line:
					sys.stdout.write(line) # Строки, содержащие корень нужного прилагательного
					arr.append(line)
					count_line += 1
					if count_line % 2000 == 0:
						sys.stdout.write(str(count_line) + '\r\n')
	f.close()
	return (arr)

def frequency(arr):
	''' Получает на вход массив строк, содержащих нужное прилагательное.
	Проверяет порядок слов (прилагательное существительное). 
	Создает словарь dictionary, где ключи - существительное прилагательное, а значения - частотность'''
	for line in arr:
		if line.split()[1].split('_')[0].isalpha() and line.split()[1].split('_')[0] not in trash:
			splited_line = line.split()
			pair_adj_noun = splited_line[0].split('_')[0] + ' ' + splited_line[1].split('_')[0]
			if splited_line[0].split('_')[1] == 'ADJ': #проверка порядка слов
				if pair_adj_noun not in dictionary: 
					dictionary[pair_adj_noun] = int(splited_line[3])
				else:
					dictionary[pair_adj_noun] += int(splited_line[3])
	return (dictionary)
	
arr = lines_selector(googlefile)
dictionary = frequency(arr)	

#УДАЛИТЬ ПОТОМ
#запись в файл prepfile.tsv строк, содержащих нужное прилагательное
prepfile = codecs.open('na_nprepfile.tsv', 'w', 'utf-8')	
for aa in arr:
		prepfile.write(aa)
prepfile.close()



##Запись в файл result_lines_selector.tsv строк в формате " прилагательное существительное число вхождений" (отсортированно)
w = codecs.open(adj_root[0] + '_nresult_lines_selector.tsv', 'w', 'utf-8')
for i in sorted(dictionary, key=dictionary.get, reverse=True):
	w.write(i +'\t'+ str(dictionary[i]) + '\r\n')
w.close()