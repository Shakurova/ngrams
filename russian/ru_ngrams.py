# -*- coding: utf-8 -*-

import codecs
import json

# mystem -gind --format json --fixlist _result_lines_selector.tsv _gind_fix_mystem.tsv d СНЯТИЕ ОМОНИМИИ -nwi

translit = { u'а':u'a', u'б':u'b', u'в':u'v', u'г':u'g', u'д':u'd',
					u'е':u'e', u'ж':u'zh', u'з':u'z', u'и':u'i', u'й':u'j',
					u'к':u'k', u'л':u'l', u'м':u'm', u'н':u'n', u'о':u'o',
					u'п':u'p', u'р':u'r', u'с':u's', u'т':u't', u'у':u'u',
					u'ф':u'f', u'х':u'h', u'ц':u'ts', u'ч':u'ch', u'ш':u'sh',
					u'щ':u'sch', u'ь':u'', u'ы':u'y', u'ъ':u'', u'э':u'e',
					u'ю':u'yu', u'я':u'ya' }

adj_root = u'золотой'  # Заменить
adj_root_tr = ''.join([translit[i] for i in list(adj_root)])

result_lines_selector = './results/' + adj_root_tr + '_result_lines_selector.tsv'
mystem_result = './results/' + adj_root_tr + '_gind_fix_mystem.tsv'


def create_dictionary_gram(mystem_result):
	"""
	Получает на вход файл с разбором из Mystem. Возвращает словарь dictionary_gram
	в формате прил сущ	[[прил инф, {разборы прил}], [сущ инф, {разборы сущ}]] и начальную форму сущ.
	"""
	mystem_result = codecs.open(mystem_result, 'r', 'utf-8')
	arr = [] # Массив строк из файла с разбором Mystem
	dictionary_gram = {} # Словарь с разборами прил и сущ
	arr = [line.rstrip('\n') for line in mystem_result]
	for l in range (0, len(arr)-2, 2):
		adjgram = []
		ngram = []
		noungram = []
		line1 = json.loads(arr[l])  # строка с прил
		line2 = json.loads(arr[l+1])  # строка с сущ
		# if line2['text']=='мудрецов':
			# print (str(line1) + ' ' + str(line2))
		if line1['analysis']!=[] and line2['analysis']!=[]:
			keydict = line1['text'] + ' ' + line2['text']  # пара прил сущ
			adjinf = line1['analysis'][0]['lex']
			nouninf = line2['analysis'][0]['lex']
			for i in line1['analysis']:
				if i['gr'][:1] == 'A':
					arradj = i['gr'].split('=')[1].strip(u'()').split(u'|')
				# else:
					# break
			# for i in line2[u'analysis']:
				# if i['gr'][:1] == 'S':
					# arrnoun = i['gr'].split('=')[1].strip(u'()').split(u'|')
			for i in arradj:
				if i[:5] == 'устар':
					i = ','.join(i.split(',')[1:3]) # если устар,вин,ед,полн,муж,од
				else:
					i = ','.join(i.split(',')[:2])  # Оставляет у разбора прил только показатель падежа и числа
				adjgram.append(i)  # Окончительный словарь с разборами  прил
			for i in line2['analysis']:
				if i['gr'][:1] == 'S':
					arrnoun =i['gr'].split('=')[1].strip(u'()').split(u'|')
					if 'мн' in i['gr'].split('=')[0].split(','):
						for a in arrnoun:
							ngram.append(str(a) + ',мн')
					elif 'ед' in i['gr'].split('=')[0].split(','):
						for a in arrnoun:
							ngram.append(str(a) + ',ед')
					else:
						for a in arrnoun:
							ngram.append(a)  # Промежуточный словарь с разборами сущ
			for i in ngram:
				if i[:5] == 'устар':
					i = ','.join(i.split(',')[1:3])  # Если устар,вин,ед,полн,муж,од
				else:
					i = ','.join(i.split(',')[:2])  # Оставляет у разбора прил только показатель падежа и числа
				noungram.append(i)  # Окончительный словарь с разборами  сущ
			# print (noungram)
			if adjinf == adj_root:  # Проверить начальную форму!!!
				dictionary_gram[keydict] = [[adjinf, set(adjgram)], [nouninf, set(noungram)]]  # Начальная форма
	mystem_result.close()
	return (dictionary_gram)  #, nouninfсловарь и начальная форма существительного

dictionary_gram  = create_dictionary_gram(mystem_result) #, nouninf

# Промежуточная запись в файл словаря dictionary_gram
output = codecs.open('./results/' + adj_root_tr + '_gind_f_dictionary_mystem.tsv', 'w', 'utf-8')
for i in dictionary_gram:
	output.write(i +'\t'+ str(dictionary_gram[i]) + '\r\n')
output.close()


def agreement(pair):
	"""
	Получает на вход пару прилагательное существительное.
	Возвращает True, если согласуется и False, если нет.
	"""
	if pair in dictionary_gram:
		for i in dictionary_gram[pair][1][1]:
			if i in dictionary_gram[pair][0][1]:
				return (True)
				break  # ЭТО НОВОЕ, ЧТО ИСПРАВИЛА + убрала False
			else:
				# print (pair)
				continue


def create_result_dict(result_lines_selector):
	"""
	Получает на вход файл в формате существительное прилагательное  частотность.
	Проверяет согласованность прилагательного и существительного.
	Возвращает словарь с лемматизированным существительным и частотностью.
	"""
	result_lines_selector = codecs.open(result_lines_selector, 'r', 'utf-8')
	result_dict = {}
	for line in result_lines_selector:
		splited_line = line.split('\t')  # Делит строку на пару прил сущ и частотность
		pair = splited_line[0]
		if agreement(pair):
		# if pair in dictionary_gram:
			if dictionary_gram[pair][1][0] not in result_dict:
				result_dict[dictionary_gram[pair][1][0]] = int(splited_line[1])
			else:
				result_dict[dictionary_gram[pair][1][0]] += int(splited_line[1])
		else:
			if pair in dictionary_gram:
				print (pair)
			continue
		# else:
			# continue
	result_lines_selector.close()
	return (result_dict)

result_dict = create_result_dict(result_lines_selector)

# Финальная запись в файл
result = codecs.open('./results/' + adj_root_tr + '_gind_f_result_ngrams.tsv', 'w', 'utf-8')
for i in sorted(result_dict, key=result_dict.get, reverse=True):
	result.write(i +'\t'+ str(result_dict[i]) + '\r\n')
result.close()

###ПРОБЛЕМЫ###
# 1. с частотностью из-за лемматизации и чего-нибудь еще (например, лапка). Частотность все время разная
# 2. в словаре разборов оставлять только те, где сущ
