# -*- coding: utf-8 -*-

import codecs
import re
import treetaggerwrapper

tagger = treetaggerwrapper.TreeTagger(TAGLANG='de', TAGDIR='/Users/elenashakurova/Desktop/ttg/')

ss = re.compile('ß')


def create_result_dict(result_lines_selector, adj_root):
	"""
	Получает на вход файл в формате существительное прилагательное  частотность.
	Проверяет согласованность прилагательного и существительного.
	Возвращает словарь с лемматизированным существительным и частотностью.
	"""
	print('\nЗапуск функции create_result_dict...')
	result_lines_selector = codecs.open(result_lines_selector, 'r', 'utf-8')
	result_dict = {}
	for line in result_lines_selector:
		splited_line = line.split('\t')             # делит строку на пару прил сущ и частотность
		adj_noun = splited_line[0]
		freq = splited_line[1]
		tags = tagger.tag_text(adj_noun)
		tags2 = treetaggerwrapper.make_tags(tags)
		# tags2 = tagger.tag(adj_noun)
		# print(tags2)
		if tags2[0][2].split("|")[0] == adj_root or ss.sub('ss', adj_root):   # проверяется лемма прилагательного
			if tags2[1][2].split("|")[0] not in result_dict:
				result_dict[tags2[1][2].split("|")[0]] = int(splited_line[1])
			else:
				result_dict[tags2[1][2].split("|")[0]] += int(splited_line[1])
	result_lines_selector.close()
	return (result_dict)


def write_in_file_final(result_lines_selector, adj_root):
	"""
	Запись в файл.
	"""
	print('\nЗапуск функции write_in_file_final...')
	result_dict = create_result_dict(result_lines_selector, adj_root)
	with codecs.open('./german/results/' + adj_root + '_result_ngrams.tsv', 'w', 'utf-8') as result:
		for i in sorted(result_dict, key=result_dict.get, reverse=True):
			result.write(i + '\t' + str(result_dict[i]) + '\r\n')
