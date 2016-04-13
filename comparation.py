# -*- coding: utf-8 -*-

import codecs, re, sys, time

file1 = './russian/results/vlazhnyj_result_ngrams.tsv' #Заменить
file2 = './russian/results/mokryj_result_ngram.tsv' #Заменить

adj1 = u'влажный'#Заменить
adj2 = u'мокрый'#Заменить

adj_root_tr = 'mo_vl'

					

def common(file1, file2):
	''' Получает на вход два файла в формате существительное частотность.
	Возвращает массив, состоящий из общих существительных. '''
	result = []
	f1 = codecs.open(file1, 'r', 'utf-8')
	f2 = codecs.open(file2, 'r', 'utf-8')
	arr1 = [line.split()[0] for line in f1]
	arr2 = [line.split()[0] for line in f2]
	for elem in arr1:
		if elem in arr2:
			result.append(elem)
	f1.close()
	f2.close()
	return (result)

result = common(file1, file2)

f1 = codecs.open(file1, 'r', 'utf-8')
f2 = codecs.open(file2, 'r', 'utf-8')
dict1 = {line.split()[0]:line.split()[1] for line in f1}
dict2 = {line.split()[0]:line.split()[1] for line in f2}
f1.close()
f2.close()
		
##Запись в файл result_lines_selector.tsv строк в формате " прилагательное существительное число вхождений" (отсортированно)
w = codecs.open(adj_root_tr + '_result_comparation.tsv', 'w', 'utf-8')
w.write('существительное' + '\t' + str(adj1) + '\t' + str(adj2) + '\t' + 'прил1 // прил2' + '\r\n')
for noun in result:
	w.write(noun + '\t' + str(dict1[noun]) + '\t' + str(dict2[noun]) + '\t' + str(int(dict1[noun])//int(dict2[noun])) + '\r\n')
w.close()