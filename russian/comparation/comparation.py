# -*- coding: utf-8 -*-

import codecs, re, sys, time

file1 = 'C:/Users/Елена/Desktop/Курсач/py3_version/russian/results/syroj_gind_f_result_ngrams.tsv' #Заменить
file2 = 'C:/Users/Елена/Desktop/Курсач/py3_version/russian/results/vlazhnyj_gind_f_result_ngrams.tsv' #Заменить

adj1 = u'syroj'#Заменить
adj2 = u'vlazhnyj'#Заменить

adj_root_tr = 'sy_vl'#Заменить

					

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
w = codecs.open(adj_root_tr + '_result_comparation.csv', 'w', 'utf-8')
w.write('noun' + ',' + str(adj1) + ',' + str(adj2) + '\r\n') #+ ',' + 'прил1 // прил2' 
for noun in result:
	w.write(noun + ',' + str(dict1[noun]) + ',' + str(dict2[noun]) + '\r\n')# + ',' + str(int(dict1[noun])//int(dict2[noun]))
w.close()