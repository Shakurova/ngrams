# -*- coding: utf-8 -*-

import codecs
from nltk.stem.wordnet import WordNetLemmatizer

lmtzr = WordNetLemmatizer()


def create_result_dict(result_lines_selector):
	"""
	Получает на вход файл в формате существительное прилагательное  частотность.
	Проверяет согласованность прилагательного и существительного.
	Возвращает словарь с лемматизированным существительным и частотностью.
	"""
	print('\nЗапуск функции create_result_dict...')
	result_lines_selector = codecs.open(result_lines_selector, 'r', 'utf-8')
	result_dict = {}
	for line in result_lines_selector:
		splited_line = line.split()                     # делит строку на пару прил+сущ и частотность
		adj = splited_line[0]
		noun = splited_line[1]
		freq = splited_line[2]                          # частотность
		if lmtzr.lemmatize(noun) not in result_dict:    # лемматизация существительного
			result_dict[lmtzr.lemmatize(noun)] = int(freq)
		else:
			result_dict[lmtzr.lemmatize(noun)] += int(freq)
	result_lines_selector.close()
	return (result_dict)


def write_in_file_final(result_lines_selector, adj_root):
	"""
	Запись в файл.
	"""
	print('\nЗапуск функции write_in_file_final...')
	result_dict = create_result_dict(result_lines_selector)
	with codecs.open('./english/results/' + adj_root + '_result_ngrams.tsv', 'w', 'utf-8') as result:
		for i in sorted(result_dict, key=result_dict.get, reverse=True):
			result.write(i + '\t' + str(result_dict[i]) + '\r\n')
