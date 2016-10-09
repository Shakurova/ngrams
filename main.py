# -*- coding: utf-8 -*-

import os

import russian.russian
import german.german
import english.english

# languages = {'русский': 'russian',
# 			'английский': 'english',
# 			'немецкий': 'german'}


def main():
	language = input("Выбериите язык (русский, английский или немецкий):  ")
	if language in ['русский', 'russian']:
		adj_root1 = input("Введите первое прилагательное(например, холодный):  ")
		adj_root2 = input("Введите второе прилагательное:  ")
		osnova1 = input("Введите основу первого прилагательного(например, холодн):  ")
		osnova2 = input("Введите основу второго прилагательного:  ")
		googlefile1 = input("Введите путь к файлу с биграммами по первому прилагательному(например, ./russian/data/googlebooks-rus-all-2gram-20120701-ho):  ")
		googlefile2 = input("Введите путь к файлу с биграммами по второму прилагательному:  ")
		mst = input("Введите путь к программе(например, ./mystem): ")
		russian.russian.main(adj_root1, adj_root2, osnova1, osnova2, googlefile1, googlefile2, mst)
	elif language in ['немецкий', 'german']:
		adj_root1 = input("Введите первое прилагательное(например, feucht):  ")
		adj_root2 = input("Введите второе прилагательное:  ")
		googlefile1 = input("Введите путь к файлу с биграммами по первому прилагательному (например, ./german/data/googlebooks-ger-all-2gram-20120701-fe):  ")
		googlefile2 = input("Введите путь к файлу с биграммами по второму прилагательному:  ")
		trtg = input("Введите путь к программе treetagger(например, /Users/elenashakurova/Desktop/ttg/): ")
		german.german.main(adj_root1, adj_root2, googlefile1, googlefile2, trtg)
	elif language in ['английский', 'english']:
		adj_root1 = input("Введите первое прилагательное(например, wet):  ")
		adj_root2 = input("Введите второе прилагательное:  ")
		googlefile1 = input("Введите путь к файлу с биграммами по первому прилагательному (например, ./englishhe/data/googlebooks-eng-all-2gram-20120701-we):  ")
		googlefile2 = input("Введите путь к файлу с биграммами по второму прилагательному:  ")
		english.english.main(adj_root1, adj_root2, googlefile1, googlefile2)
	else:
		print('Вы ввели неправильный язык')
	graphic = input('Построить график? (да/нет): ')
	if graphic == 'да':
		adj1 = 'ledyanoj'
		adj2 = 'holodnyj'
		os.system('/usr/local/bin/Rscript ./russian/graphics_normal_ideorg.R ' + adj1 + ' ' + adj2 + ' ' + 'ho_le_result_0_comparation.csv')
	else:
		pass
main()
