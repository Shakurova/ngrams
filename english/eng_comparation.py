# -*- coding: utf-8 -*-

import codecs


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
	return (result)


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

	with codecs.open('./english/results/' + adj_root_tr + '_result_0_comparation.csv', 'w', 'utf-8') as w:
		w.write('noun' + ',' + str(adj_root1) + ',' + str(adj_root2) + '\r\n')
		for noun in result:
			w.write(noun + ',' + str(dict1[noun]) + ',' + str(dict2[noun]) + '\r\n')
