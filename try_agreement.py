# -*- coding: utf-8 -*-

import codecs, re, sys, time
from pymystem3 import Mystem
mystem = Mystem()

dictionary = {u"влажные руки":1, u"влажный кошка":24, u"влажные руки":5, u"влажной трава":34,  u"влажные руки":23, u"влажная тряпка":5, u"влажной рыба":4, u"влажная тряпка":8, u"влажными реки":54}	  


def agreement(pair_adj_noun):
	''' Получает на вход пару прилагательное существительное . 
	Проверяет согласование прилагательного и существительного, выдает True, если согласовано, и False, если нет. 
	Используется в frequency. '''
	a, n = pair_adj_noun.split()
	hyp_adj, hyp_noun = hypothesis_adj_noun(a, n)
	for gram in hyp_noun:
		if gram in hyp_adj:
			return (True)
		else:
			return (False)
		
#Нужно учитывать род?
#Обработать файл mystem'ом и здесь смотреть уже обработанный файл
#mystem input output -ni
def hypothesis_adj_noun(a, n):
	''' Получает на вход прилагательное и существительное.
	Возвращает все возможные варианты разбора для прилагательного и для существительного. 
	Используется в agreement. '''
	adj_gram = mystem.analyze(a)[0]['analysis'][0][u'gr'].split(u'=')[1]   #(пр,ед,полн,жен|дат,ед,полн,жен|род,ед,полн,жен|твор,ед,полн,жен)
	noun_gram = mystem.analyze(n)[0]['analysis'][0][u'gr'].split(u'=')[1]   #твор
	hyp_adj = [hyp.split(',')[:2] for hyp in adj_gram.strip('()').split('|')] # [['пр', 'ед', 'полн', 'жен'], ['дат', 'ед', 'полн', 'жен'], ['род', 'ед', 'полн', 'жен'], ['твор', 'ед', 'полн', 'жен']]
	hyp_noun = [hyp.split(',') for hyp in noun_gram.strip('()').split('|')] # [['твор']]
	# sys.stdout.write(str(a) + ' ' + str(adj_gram) + '\r\n')
	# sys.stdout.write(str(n) + ' ' + str(noun_gram) + '\r\n')
	# sys.stdout.write(str(a) + ' ' + str(hyp_adj) + '\r\n')
	# sys.stdout.write(str(n) + ' ' + str(hyp_noun) + '\r\n' + '\r\n')
	return (hyp_adj, hyp_noun)

dict_new = {}

for pair in dictionary:
	a, n = pair.split()
	if agreement(pair):
		a = mystem.lemmatize(a)[0]
		print (a)
		n = mystem.lemmatize(n)[0]
		print (n)
		an = str(a) + ' ' + str(n) #' '.join(arr), arr = a, n
		print (an)
		if an not in dict_new:
			dict_new[an] = int(dictionary[pair])
			#sys.stdout.write(splited_line[1] + " " + str(dictionary[splited_line[1]]) + "\r\n")
		else:
			dict_new[an] += int(dictionary[pair])
		print (str(an) + ' ' + str(dict_new[an]))