# -*- coding: utf-8 -*-

import codecs, re, sys, time

googlefile = u'googlebooks-rus-all-2gram-20120701-mo' #Заменить
adj_root = u'мокр'#Заменить
arr = []
dictionary = {}
translit = { u'а':u'a', u'б':u'b', u'в':u'v', u'г':u'g', u'д':u'd',
					u'е':u'e', u'ж':u'zh', u'з':u'z', u'и':u'i', u'й':u'j',
					u'к':u'k', u'л':u'l', u'м':u'm', u'н':u'n', u'о':u'o',
					u'п':u'p', u'р':u'r', u'с':u's', u'т':u't', u'у':u'u',
					u'ф':u'f', u'х':u'h', u'ц':u'ts', u'ч':u'ch', u'ш':u'sh',
					u'щ':u'sch', u'ь':u'', u'ы':u'y', u'ъ':u'', u'э':u'e',
					u'ю':u'yu', u'я':u'ya' }
					
trash = [u'«', u'»', u'_NOUN_', u',', u'.', u'!', u')', u'*', u'"', u':', u'-', u'--', u';', u'...', u'?',  u'(']

def lines_selector(googlefile):
	''' Получает на вход название файла, содержащего биграммы из google ngrams, год, количество вхождений, число книг в этот год.
	Возвращает массив, состоящий из строк, содержащих корень заданного прилагательного и теги _ADJ и _NOUN. '''
	count_line = 0 # Количество обработанных строк
	f = codecs.open(googlefile, 'r', 'utf-8')
	for line in f:
		if u'мокр' in line:#Заменить
			if u'ADJ' in line:
				if u'NOUN' in line:
					#sys.stdout.write(line) # Строки, содержащие корень нужного прилагательного
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

##Запись в файл result_lines_selector.tsv строк в формате " прилагательное существительное число вхождений" (отсортированно)
w = codecs.open(translit[adj_root[0]] + '_result_lines_selector.tsv', 'w', 'utf-8')
for i in sorted(dictionary, key=dictionary.get, reverse=True):
	w.write(i +'\t'+ str(dictionary[i]) + '\r\n')
w.close()