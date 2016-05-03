# -*- coding: utf-8 -*-

import codecs, re, sys, time, json, random

file1 = 'C:/Users/Елена/Desktop/Курсач/py3_version/russian/results/syroj_gind_f_result_ngrams.tsv' #Заменить
file2 = 'C:/Users/Елена/Desktop/Курсач/py3_version/russian/results/vlazhnyj_gind_f_result_ngrams.tsv' #Заменить

adj1 = u'syroj'#Заменить
adj2 = u'vlazhnyj'#Заменить

adj_root_tr = 'sy_vl'#Заменить

ideo = 'baranov.csv'				

dic = codecs.open("C:/Users/Елена/Desktop/Курсач/py3_version/russian/one.txt", 'r', 'utf-8')
dicti= {} #словарь в формате 1:'1', где первое число обозначает более узкое понятие, второе - более широкое

for line in dic:
	one = line.split()[0]
	two = int(line.split()[1])
	three = int(line.split()[2])
	for i in range(two,three+1):
		dicti[i]=one	

def generate_color():
	'''Генератор рандомных цветов.'''
    color = '#{:02x}{:02x}{:02x}'.format(*map(lambda x: random.randint(0, 255), range(3)))
    return (color)	
	
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
		
def read_ideo(ideo):
	''' Получает на вход файл с разбором из Mystem.
	Возвращает словарь dictionary_gram в формате прил сущ	[[прил инф, {разборы прил}], [сущ инф, {разборы сущ}]] и начальную форму сущ.  '''
	ideo = codecs.open(ideo, 'r', 'utf-8')
	result_dict = {}
	for line in ideo:
		line = line.lower()
		code = line.split(";")[0].split(".")[0]
		word = line.split(";")[1].split("\r\n")[0].split(" (")[0]
		# if code not in result_dict:
			# result_dict[code] = []
			# result_dict[code].append(word)
		# else:
			# result_dict[code].append(word)	
		result_dict[word] = dicti[int(code)]	
	ideo.close()
	return (result_dict)#словарь, где ключ - слово из списка Баранова, значение - цифра, обозначающая категорию

result_dict = read_ideo(ideo)

col = {} #словарь, в котором ключ - существительное, значение - его цвет
for noun in result:
	if noun in result_dict:
		col[result_dict[noun]] = generate_color()
	else:
		col["other"] = generate_color()
		
##Запись в файл в формате существительное | частотности по двум прилагательным | цвет
w = codecs.open(adj_root_tr + '_result_comparation.csv', 'w', 'utf-8')
w.write('noun' + ',' + str(adj1) + ',' + str(adj2) + ',' + 'code' + '\r\n')
for noun in result:
	if noun in result_dict:
		w.write(noun + ',' + str(dict1[noun]) + ',' + str(dict2[noun]) + ',' + str(col[result_dict[noun]]) + '\r\n')
	else:
		w.write(noun + ',' + str(dict1[noun]) + ',' + str(dict2[noun]) + ',' + str(col["other"]) + '\r\n')
w.close()
