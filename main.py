# -*- coding: utf-8 -*-

import os

TRANSLIT = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
			'е': 'e', 'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'j',
			'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o',
			'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
			'ф': 'f', 'х': 'h', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh',
			'щ': 'sch', 'ь': '', 'ы': 'y', 'ъ': '', 'э': 'e',
			'ю': 'yu', 'я': 'ya'}


def built_graphic(language, adj_root1, adj_root2):
	graphic = input('Построить график? (да/нет): ')
	if graphic == 'да':
		transl = adj_root1[:2] + '_' + adj_root2[:2]
		if language in ['немецкий', 'german', 'english', 'английский']:
			print(transl + '_result_0_comparation.csv')
			os.system('/usr/local/bin/Rscript ./russian/graphics_normal_ideorg.R ' + adj_root1 + ' ' + adj_root2 + ' ' + './' + language + '/results/' + transl + '_result_0_comparation.csv')
			print('Программа завершила свою работу!')
		if language in ['русский', 'russian']:
			adj_root_tr1 = ''.join([TRANSLIT[i] for i in list(adj_root1)])
			adj_root_tr2 = ''.join([TRANSLIT[i] for i in list(adj_root2)])
			transl = adj_root_tr1[:2] + '_' + adj_root_tr2[:2]
			print('./' + language + '/' + transl + '_result_0_comparation.csv')
			os.system('/usr/local/bin/Rscript ./russian/graphics_normal_ideorg.R ' + adj_root_tr1 + ' ' + adj_root_tr2 + ' ' + './' + language + '/results/' + transl + '_result_0_comparation.csv')
			print('Программа завершила свою работу!')
	elif graphic == 'нет':
		print('Программа завершила свою работу!')
	else:
		print('Нет такого варианта ответа. Программа завершила свою работу!')
		pass


def main():
	language = input("Выбериите язык (русский, английский или немецкий):  ")
	if language in ['русский', 'russian']:
		language = 'russian'
		adj_root1 = input("Введите первое прилагательное(например, холодный):  ")
		adj_root2 = input("Введите второе прилагательное:  ")
		what_to_do = input("Обработать данные? (Напишите 1)\nПостроить график? (Напишите 2)\nВведите число: ")
		if what_to_do == '1':
			import russian.russian
			osnova1 = input("Введите основу первого прилагательного(например, холодн):  ")
			osnova2 = input("Введите основу второго прилагательного:  ")
			googlefile1 = input("Введите путь к файлу с биграммами по первому прилагательному(например, ./russian/data/googlebooks-rus-all-2gram-20120701-ho):  ")
			googlefile2 = input("Введите путь к файлу с биграммами по второму прилагательному:  ")
			MST = input("Введите путь к программе(например, ./mystem): ")
			russian.russian.main(adj_root1, adj_root2, osnova1, osnova2, googlefile1, googlefile2, MST)
			built_graphic(language, adj_root1, adj_root2)
		elif what_to_do == '2':
			built_graphic(language, adj_root1, adj_root2)
		else:
			print('Вы неправильно ввели число')
	elif language in ['немецкий', 'german']:
		language = 'german'
		import german.german
		adj_root1 = input("Введите первое прилагательное(например, feucht):  ")
		adj_root2 = input("Введите второе прилагательное:  ")
		what_to_do = input("Обработать данные? (Напишите 1)\nПостроить график? (Напишите 2)\nВведите число: ")
		if what_to_do == '1':
			googlefile1 = input("Введите путь к файлу с биграммами по первому прилагательному (например, ./german/data/googlebooks-ger-all-2gram-20120701-fe):  ")
			googlefile2 = input("Введите путь к файлу с биграммами по второму прилагательному:  ")
			TRTG = input("Введите путь к программе treetagger(например, /Users/elenashakurova/Desktop/ttg/): ")
			translate = input("Сделать перевод? (да/нет):  ")
			german.german.main(adj_root1, adj_root2, googlefile1, googlefile2, TRTG, translate)
			built_graphic(language, adj_root1, adj_root2)
		elif what_to_do == '2':
			built_graphic(language, adj_root1, adj_root2)
		else:
			print('Вы неправильно ввели число')
	elif language in ['английский', 'english']:
		language = 'english'
		import english.english
		adj_root1 = input("Введите первое прилагательное(например, humid):  ")
		adj_root2 = input("Введите второе прилагательное:  ")
		what_to_do = input("Обработать данные? (Напишите 1)\nПостроить график? (Напишите 2)\nВведите число: ")
		if what_to_do == '1':
			googlefile1 = input("Введите путь к файлу с биграммами по первому прилагательному (например, ./english/data/googlebooks-eng-all-2gram-20120701-hu):  ")
			googlefile2 = input("Введите путь к файлу с биграммами по второму прилагательному:  ")
			translate = input("Сделать перевод? (да/нет):  ")
			english.english.main(adj_root1, adj_root2, googlefile1, googlefile2, translate)
			built_graphic(language, adj_root1, adj_root2)
		elif what_to_do == '2':
			built_graphic(language, adj_root1, adj_root2)
		else:
			print('Вы неправильно ввели число')
	else:
		print('Вы ввели неправильный язык')
main()


# может надо только сравнить?

# ЗАВТРА - ДОБАВИТЬ ВОЗМОЖНОСТЬ СЕМАНТИЧЕСКИХ ГРУПП (+ ВОПРОС В МЕЙН) И ДОДЕЛАТЬ ПРЕЗЕНТАЦИЮ
# Добавить нормальный вывод корреляций
# В предыдущий версии можно было рисовать цветом слова только какой-то одной категории, или выводить только одну категорию
