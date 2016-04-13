# -*- coding: utf-8 -*-

import codecs, re, sys, time

# pip install -U textblob-de
# python -m textblob.download_corpora

from textblob_de import TextBlobDE as TextBlob
from textblob_de.lemmatizers import PatternParserLemmatizer
lmtzr = PatternParserLemmatizer()
#lmtzr.lemmatize("Das ist ein hässliches Auto.")
#[('das', 'DT'), ('sein', 'VB'), ('ein', 'DT'), ('hässlich', 'JJ'), ('Auto', 'NN')]


adj_root = u'feucht'#Заменить
result_lines_selector = adj_root + '_result_lines_selector.tsv'

def create_result_dict(result_lines_selector):
	''' Получает на вход файл в формате существительное прилагательное  частотность. 
	Проверяет согласованность прилагательного и существительного.
	Возвращает словарь с лемматизированным существительным и частотностью. '''
	result_lines_selector = codecs.open(result_lines_selector, 'r', 'utf-8')
	result_dict = {}
	for line in result_lines_selector:
		splited_line = line.split('\t') #делит строку на пару прил сущ и частотность
		adj_noun = splited_line[0]
		freq = splited_line[1]
		if lmtzr.lemmatize(adj_noun)[0][0] == 'feucht': #or lmtzr.lemmatize(adj_noun)[0][0] == 'naß'#проверяется лемма прилагательного
			if lmtzr.lemmatize(adj_noun)[1][0] not in result_dict: 
				result_dict[lmtzr.lemmatize(adj_noun)[1][0]] = int(splited_line[1])
			else:
				result_dict[lmtzr.lemmatize(adj_noun)[1][0]] += int(splited_line[1])
	result_lines_selector.close()
	return (result_dict)

result_dict = create_result_dict(result_lines_selector)	

#Финальная запись в файл		
result = codecs.open(adj_root + '_result_ngrams.tsv', 'w', 'utf-8')
for i in sorted(result_dict, key=result_dict.get, reverse=True):
	result.write(i +'\t'+ str(result_dict[i]) + '\r\n')
result.close()
