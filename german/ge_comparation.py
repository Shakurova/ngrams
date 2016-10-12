# -*- coding: utf-8 -*-

import re
import codecs

import pymorphy2
from yandex_translate import YandexTranslate

morph = pymorphy2.MorphAnalyzer()


def common(file1, file2):
	"""
	Получает на вход два файла в формате существительное частотность.
	Возвращает массив, состоящий из общих существительных.
	"""
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
	return result


def write_down_result(file1, file2, adj_root_tr, adj_root1, adj_root2):
	"""
	Запись в файл result_lines_selector.tsv строк в формате
	" прилагательное существительное число вхождений" (отсортированно)
	"""

	result = common(file1, file2)

	f1 = codecs.open(file1, 'r', 'utf-8')
	f2 = codecs.open(file2, 'r', 'utf-8')
	dict1 = {line.split()[0]: line.split()[1] for line in f1}
	dict2 = {line.split()[0]: line.split()[1] for line in f2}
	f1.close()
	f2.close()

	with codecs.open('./german/results/' + adj_root_tr + '_result_0_comparation.csv', 'w', 'utf-8') as w:
		w.write('noun' + ',' + str(adj_root1) + ',' + str(adj_root2) + '\r\n')
		for noun in result:
			w.write(noun + ',' + str(dict1[noun]) + ',' + str(dict2[noun]) + '\r\n')


def common_tr(file1, file2):
	"""
	Получает на вход два файла в формате существительное частотность.
	Возвращает массив, состоящий из общих существительных. С переводом.
	"""
	result = []
	result_arr1 = []
	result_arr2 = []
	f1 = codecs.open(file1, 'r', 'utf-8')
	f2 = codecs.open(file2, 'r', 'utf-8')
	arr1 = [line.split()[0] for line in f1]
	arr2 = [line.split()[0] for line in f2]
	for elem in arr1:
		if elem in arr2:
			result.append(elem)  # в result лежит немецкое существительное, которое встретилось с обеими прил
		else:
			result_arr1.append(elem)  # в result_arr1 лежит немецкое существительное, которое встретилось только с первым прил
	for elem2 in arr2:
		if elem2 not in arr1:
			result_arr2.append(elem2)  # в result_arr2 лежит немецкое существительное, которое встретилось только со вторым прил
	f1.close()
	f2.close()
	return result, result_arr1, result_arr2


def write_down_result_tr(file1, file2, adj_root_tr, adj_root1, adj_root2, api_key):
	"""
	Запись в файл result_lines_selector.tsv строк в формате
	" прилагательное существительное число вхождений" (отсортированно). С переводом.
	"""

	translate = YandexTranslate(api_key)

	result, result_arr1, result_arr2 = common_tr(file1, file2)

	f1 = codecs.open(file1, 'r', 'utf-8')
	f2 = codecs.open(file2, 'r', 'utf-8')
	dict1 = {line.split()[0]: line.split()[1] for line in f1}  # сущ и частотность
	dict2 = {line.split()[0]: line.split()[1] for line in f2}  # сущ и частотность
	f1.close()
	f2.close()

	trans = {}
	for noun in result:
		nounblob = translate.translate(noun, 'de-ru')['text'][0].lower()  # делаем перевод
		nounblob = morph.parse(nounblob)[0].normal_form  # делаем нормализацию
		trans[noun] = nounblob
	for noun1 in result_arr1:
		nounblob1 = translate.translate(noun1, 'de-ru')['text'][0].lower()  # делаем перевод
		nounblob1 = morph.parse(nounblob1)[0].normal_form  # делаем перевод
		trans[noun1] = nounblob1
	for noun2 in result_arr2:
		nounblob2 = translate.translate(noun2, 'de-ru')['text'][0].lower()  # делаем перевод
		nounblob2 = morph.parse(nounblob2)[0].normal_form  # делаем перевод
		trans[noun2] = nounblob2

	# Запись в файл result_lines_selector.tsv строк в формате " прилагательное существительное число вхождений" (отсортированно)
	w = codecs.open('./german/results/' + adj_root_tr + '_result_0_translate_comparation.csv', 'w', 'utf-8')
	w.write('noun' + ',' + str(adj_root1) + ',' + str(adj_root2) + ',' + 'translation' + '\r\n')
	for noun in result:
		nounblob = trans[noun]
		w.write(noun + ',' + str(dict1[noun]) + ',' + str(dict2[noun]) + ',' + nounblob + '\r\n')
	for noun in result_arr1:
		nounblob = trans[noun]
		w.write(noun + ',' + str(dict1[noun]) + ',' + "0" + ',' + nounblob + '\r\n')
	for noun in result_arr2:
		nounblob = trans[noun]
		w.write(noun + ',' + "10" + ',' + str(dict2[noun]) + ',' + nounblob + '\r\n')
	w.close()
