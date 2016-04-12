# -*- coding: utf-8 -*-

import codecs, re, sys, time

# pip install -U textblob-de
# python -m textblob.download_corpora

from textblob_de import TextBlobDE as TextBlob
from textblob_de.lemmatizers import PatternParserLemmatizer
lmtzr = PatternParserLemmatizer()
#lmtzr.lemmatize("Das ist ein hässliches Auto.")
#[('das', 'DT'), ('sein', 'VB'), ('ein', 'DT'), ('hässlich', 'JJ'), ('Auto', 'NN')]
#lmtzr.lemmatize("hässliches")[0][0]
#'hässlich'

adj_root = u'humid'#Заменить
result_lines_selector = 'h_result_lines_selector.tsv' #заменить

def create_result_dict(result_lines_selector):
	''' Получает на вход файл в формате существительное прилагательное  частотность. 
	Проверяет согласованность прилагательного и существительного.
	Возвращает словарь с лемматизированным существительным и частотностью. '''
	result_lines_selector = codecs.open(result_lines_selector, 'r', 'utf-8')
	result_dict = {}
	for line in result_lines_selector:
		splited_line = line.split() #делит строку на пару прил сущ и частотность
		adj = splited_line[0]
		noun = splited_line[1]
		freq = splited_line[2]
		if lmtzr.lemmatize(noun) not in result_dict: 
			result_dict[lmtzr.lemmatize(noun)] = int(splited_line[2])
		else:
			result_dict[lmtzr.lemmatize(noun)] += int(splited_line[2])
	result_lines_selector.close()
	return (result_dict)

#проверять лемму прилагательного
result_dict = create_result_dict(result_lines_selector)	

#Финальная запись в файл		
result = codecs.open(adj_root[0] + '_result_dict_output.tsv', 'w', 'utf-8')
for i in sorted(result_dict, key=result_dict.get, reverse=True):
	result.write(i +'\t'+ str(result_dict[i]) + '\r\n')
result.close()