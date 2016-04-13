# -*- coding: utf-8 -*-

import codecs, re, sys, time

#mystem input output -nwi

translit = { u'а':u'a', u'б':u'b', u'в':u'v', u'г':u'g', u'д':u'd',
					u'е':u'e', u'ж':u'zh', u'з':u'z', u'и':u'i', u'й':u'j',
					u'к':u'k', u'л':u'l', u'м':u'm', u'н':u'n', u'о':u'o',
					u'п':u'p', u'р':u'r', u'с':u's', u'т':u't', u'у':u'u',
					u'ф':u'f', u'х':u'h', u'ц':u'ts', u'ч':u'ch', u'ш':u'sh',
					u'щ':u'sch', u'ь':u'', u'ы':u'y', u'ъ':u'', u'э':u'e',
					u'ю':u'yu', u'я':u'ya' }

adj_root = u'влажный'#Заменить
adj_root_tr = ''.join([translit[i] for i in list(adj_root)])

result_lines_selector = adj_root_tr + '_result_lines_selector.tsv'
mystem_result = adj_root_tr + '_mystem_result.tsv'
				
def create_dictionary_gram(mystem_result):
	''' Получает на вход файл с разбором из Mystem.
	Возвращает словарь dictionary_gram в формате прил сущ	[[прил инф, {разборы прил}], [сущ инф, {разборы сущ}]] и начальную форму сущ.  '''
	mystem_result = codecs.open(mystem_result, 'r', 'utf-8')
	arr = [] #массив строк из файла с разбором Mystem
	dictionary_gram = {} #словарь с разборами прил и сущ
	arr = [line.rstrip('\n') for line in mystem_result]
	#for line in mystem_result:
		#arr.append(line.rstrip('\n')) #убирает символ переноса строки
	for l in range (0, len(arr)-2, 2):
		arradj = []
		arrnoun = []
		line1 = arr[l] #строка с прил
		line2 = arr[l+1] #строка с сущ
		keydict = line1.split('{')[0] + ' ' + line2.split('{')[0] #пара прил сущ
		adjgram = line1.split('{')[1].split('=A=')
		for i in adjgram[1:]:
			i = ','.join(i[:-1].split(',')[:2]) #оставляет у разбора прил только показатель падежа и числа
			arradj.append(i) #окончительный словарь с разборами  сущ
		noungram = line2.split('{')[1].split('|')
		noungram[-1] = noungram[-1][:-1] #убирает '}' из последнего разбора сущ
		nouninf = noungram[0].split('=S,')[0] #начальная форма сущ
		for i in noungram:
			if 'S' in list(line2):
				if 'мн' in i.split('=')[1].split(','):
					arrnoun.append(str(i.split('=')[2]) + ',мн')
				elif 'ед' in i.split('=')[1].split(','):
					arrnoun.append(str(i.split('=')[2]) + ',ед')
				else:
					arrnoun.append(i.split('=')[2]) #окончительный словарь с разборами сущ
		if adjgram[0] == adj_root and 'S' in list(line2): #только нужное прилагательное и порядок прил сущ
			dictionary_gram[keydict] = [[adjgram[0], set(arradj)], [noungram[0].split('=S,')[0], set(arrnoun)]]
	mystem_result.close()
	return (dictionary_gram, nouninf) #словарь и начальная форма существительного

dictionary_gram, nouninf  = create_dictionary_gram(mystem_result)

#Промежуточная запись в файл словаря dictionary_gram
output = codecs.open(adj_root_tr + '_dictionary_mystem.tsv', 'w', 'utf-8')
for i in dictionary_gram:
	output.write(i +'\t'+ str(dictionary_gram[i]) + '\r\n')
output.close()

def agreement(pair): 
	''' Получает на вход пару прилагательное существительное.
	Возвращает True, если согласуется и False, если нет. '''
	if pair in dictionary_gram:
		for i in dictionary_gram[pair][1][1]:
			if i in dictionary_gram[pair][0][1]:
				return (True)
				pass
			else:
				return (False)

def create_result_dict(result_lines_selector):
	''' Получает на вход файл в формате существительное прилагательное  частотность. 
	Проверяет согласованность прилагательного и существительного.
	Возвращает словарь с лемматизированным существительным и частотностью. '''
	result_lines_selector = codecs.open(result_lines_selector, 'r', 'utf-8')
	result_dict = {}
	for line in result_lines_selector:
		splited_line = line.split('\t') #делит строку на пару прил сущ и частотность
		pair = splited_line[0]
		if agreement(pair):
			if dictionary_gram[pair][1][0] not in result_dict: 
				result_dict[dictionary_gram[pair][1][0]] = int(splited_line[1])
			else:
				result_dict[dictionary_gram[pair][1][0]] += int(splited_line[1])
		else:
			continue
	result_lines_selector.close()
	return (result_dict)

result_dict = create_result_dict(result_lines_selector)	

#финальная запись в файл		
result = codecs.open(adj_root_tr + '_new_new_result_ngrams.tsv', 'w', 'utf-8')
for i in sorted(result_dict, key=result_dict.get, reverse=True):
	result.write(i +'\t'+ str(result_dict[i]) + '\r\n')
result.close()

#Проблемы с частотностью из-за лемматизации и чего-нибудь еще (например, лапка)
#Отбросить биграммы, где второе слово - явно какой-то мусор
#в словаре разборов оставлять только те, где сущ
#if __name__ == '__main__':
    #main()
#запуск функции main