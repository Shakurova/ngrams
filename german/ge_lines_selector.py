# -*- coding: utf-8 -*-

import codecs
import re
import sys

trash = ['«', '»', '_NOUN_', ',', '.', '!', ')', '*', '"', ':', '-', '--', ';', '...', '?',  '(']

ss = re.compile('ß')

def lines_selector(googlefile, adj_root):
	"""
	Получает на вход название файла, содержащего биграммы из google ngrams, год, количество вхождений,
	число книг в этот год. Возвращает массив, состоящий из строк,
	содержащих корень заданного прилагательного и теги _ADJ и _NOUN.
	"""
	print('\nЗапуск функции lines_selector...')
	ss = re.compile('ß')
	arr = []
	count_line = 0  # Количество обработанных строк
	with codecs.open(googlefile, 'r', 'utf-8') as f:
		# arr = [ss.sub('ss', line) for line in f if adj_root in ss.sub('ss', line) if 'ADJ' in line if 'NOUN' in line]
		for line in f:
			# if u'nass' in line or u'naß' in line:  # Заменить !!!!!!
			if adj_root in line or ss.sub('ss', adj_root) in line:  # Заменить !!!!!!
				if 'ADJ' in line:
					if 'NOUN' in line:
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
		if line.split()[1].split('_')[0].isalpha() and line.split()[1].split('_')[0] not in trash:
			splited_line = line.split()
			pair_adj_noun = splited_line[0].split('_')[0] + ' ' + splited_line[1].split('_')[0]
			if splited_line[0].split('_')[1] == 'ADJ': # проверка порядка слов
				if pair_adj_noun not in dictionary:
					dictionary[pair_adj_noun] = int(splited_line[3])
				else:
					dictionary[pair_adj_noun] += int(splited_line[3])
	return (dictionary)

# # Запись в файл prepfile.tsv строк, содержащих нужное прилагательное
# prepfile = codecs.open(adj_root + '_prepfile.tsv', 'w', 'utf-8')
# for aa in arr:
#   prepfile.write(aa)
# prepfile.close()


def write_in_file(googlefile, adj_root):
	"""
	Запись в файл result_lines_selector.tsv строк в формате " прилагательное
	существительное число вхождений" (отсортированно)
	"""
	print('\nЗапись функции write_in_file...')
	arr = lines_selector(googlefile, adj_root)
	dictionary = frequency(arr)
	with codecs.open('./german/results_middle/' + adj_root + '_result_lines_selector.tsv', 'w', 'utf-8') as w:
		for i in sorted(dictionary, key=dictionary.get, reverse=True):
			w.write(i + '\t' + str(dictionary[i]) + '\r\n')
