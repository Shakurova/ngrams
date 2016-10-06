# -*- coding: utf-8 -*-

import codecs
import random

# print('Импорт словаря НКРЯ...')
# dic = codecs.open("C:/Users/Елена/Desktop/Курсач/py3_version/russian/noungraphic/nouns.csv", 'r', 'utf-8')
# noundicti = {}  # Cловарь в формате 1:'1', где первое число обозначает более узкое понятие, второе - более широкое
#
#
# def create_noindicti():
# 	for line in dic:
# 		word = line.split(';')[1]
# 		cat = line.split(';')[4]
# 		if cat == "":
# 			continue
# 		else:
# 			noundicti[word] = cat
# 	return noundicti
#
#
# def generate_color():
# 	color = '#{:02x}{:02x}{:02x}'.format(*map(lambda x: random.randint(0, 255), range(3)))
# 	return color


def common(file1, file2):
	"""
	Получает на вход два файла в формате существительное частотность.
	Возвращает массив, состоящий из общих существительных.
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
			result.append(elem)  # и в arr1 и в arr2
		else:
			result_arr1.append(elem)  # только в arr1
	for elem2 in arr2:
		if elem2 not in arr1:
			result_arr2.append(elem2)  # только в arr2
	f1.close()
	f2.close()
	return result, result_arr1, result_arr2  # массив с общими существительными


def write_down_result(file1, file2, transl, adj_root1, adj_root2):
	result, result_arr1, result_arr2 = common(file1, file2)
	f1 = codecs.open(file1, 'r', 'utf-8')
	f2 = codecs.open(file2, 'r', 'utf-8')
	dict1 = {line.split()[0]: line.split()[1] for line in f1}
	dict2 = {line.split()[0]: line.split()[1] for line in f2}
	f1.close()
	f2.close()

	w = codecs.open('./results/' + transl + '_result_0_comparation.csv', 'w', 'utf-8')
	w.write('noun' + ',' + str(adj_root1) + ',' + str(adj_root2) + '\r\n')
	for noun in result:
		w.write(noun + ',' + str(dict1[noun]) + ',' + str(dict2[noun]) + '\r\n')  # str(noundicti[noun])
	for noun in result_arr1:
		w.write(noun + ',' + str(dict1[noun]) + ',' + "0" + '\r\n')
	for noun in result_arr2:
		w.write(noun + ',' + "0" + ',' + str(dict2[noun]) + '\r\n')
	w.close()

# col = {}   # Словарь, в котором ключ - существительное, значение - его цвет
# for noun in result:
# 	if noun in noundicti:
# 		col[noundicti[noun]] = generate_color()
# 	else:
# 		col["other"] = "black"
# for noun1 in result_arr1:
# 	if noun1 in noundicti:
# 		col[noundicti[noun1]] = generate_color()
# 	else:
# 		col["other"] = "black"
# for noun2 in result_arr2:
# 	if noun2 in noundicti:
# 		col[noundicti[noun2]] = generate_color()
# 	else:
# 		col["other"] = "black"

# Запись в файл в формате существительное | частотности по двум прилагательным | цвет



