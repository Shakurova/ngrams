# # -*- coding: utf-8 -*-

import codecs
import sys

TRASH = [u'«', u'»', u'_NOUN_', u',', u'.', u'!', u')', u'*', u'"', u':', u'-', u'--', u';', u'...', u'?',  u'(']


def lines_selector(googlefile1, osnova1):
	"""
	Получает на вход название файла, содержащего биграммы из google ngrams, год, количество вхождений, число книг в этот год.
	Возвращает массив, состоящий из строк, содержащих корень заданного прилагательного и теги _ADJ и _NOUN.
	"""
	print('\nЗапуск функции lines_selector...')
	arr = []
	count_line = 0  # Счетчик количества обработанных строк
	with codecs.open(googlefile1, 'r', 'utf-8') as f:
		# arr = [line for line in f if osnova1 in line if u'ADJ' in line if u'NOUN' in line]
		for line in f:
			if osnova1 in line:
				if u'ADJ' in line:
					if u'NOUN' in line:
						# sys.stdout.write(line) # Строки, содержащие корень нужного прилагательного
						arr.append(line)
						count_line += 1
						if count_line % 2000 == 0:
							sys.stdout.write(str(count_line) + '\r\n')
	return (arr)


def frequency(arr):
	"""
	Получает на вход массив строк, содержащих нужное прилагательное.
	Проверяет порядок слов (прилагательное существительное).
	Создает словарь dictionary, где ключи - существительное прилагательное, а значения - частотность.
	"""
	print('\nЗапуск функции frequency...')
	dictionary = {}
	for line in arr:
		if line.split()[1].split('_')[0].isalpha() and line.split()[1].split('_')[0] not in TRASH:
			splited_line = line.split()
			pair_adj_noun = splited_line[0].split('_')[0] + ' ' + splited_line[1].split('_')[0]
			if splited_line[0].split('_')[1] == 'ADJ':  # Проверка порядка слов
				if pair_adj_noun not in dictionary:
					dictionary[pair_adj_noun] = int(splited_line[3])
				else:
					dictionary[pair_adj_noun] += int(splited_line[3])
	return (dictionary)


def write_in_file(googlefile1, adj_root_tr, osnova1):
	"""
	Запись в файл result_lines_selector.tsv строк в формате " прилагательное
	существительное число вхождений" (отсортированно)
	"""
	print('\nЗапись функции write_in_file...')
	arr = lines_selector(googlefile1, osnova1)
	dictionary = frequency(arr)
	w = codecs.open('./russian/results_middle/' + adj_root_tr + '_result_lines_selector.tsv', 'w', 'utf-8')
	for i in sorted(dictionary, key=dictionary.get, reverse=True):
		w.write(i + '\t' + str(dictionary[i]) + '\r\n')
	w.close()
