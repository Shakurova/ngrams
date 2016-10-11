# -*- coding: utf-8 -*-

import os

import russian.ru_lines_selector as ru_lines_selector
import russian.ru_ngrams as ru_ngrams
import russian.ru_comparation_with_0 as ru_comparation_with_0

TRANSLIT = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
			'е': 'e', 'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'j',
			'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o',
			'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
			'ф': 'f', 'х': 'h', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh',
			'щ': 'sch', 'ь': '', 'ы': 'y', 'ъ': '', 'э': 'e',
			'ю': 'yu', 'я': 'ya'}


def main(adj_root1, adj_root2, osnova1, osnova2, googlefile1, googlefile2, MST):

	if os.path.exists('./russian/results/'):
		pass
	else:
		os.mkdir('./russian/results/')

	# Папка с промежуточными файлами
	if os.path.exists('./russian/results_middle/'):
		pass
	else:
		os.mkdir('./russian/results_middle/')

	print(u'\nЗапуск функции ru_lines_selector для первого прилагательного...')
	adj_root_tr1 = ''.join([TRANSLIT[i] for i in list(adj_root1)])
	ru_lines_selector.write_in_file(googlefile1, adj_root_tr1, osnova1)
	print(u'\nЗапуск функции ru_lines_selector для второго прилагательного...')
	adj_root_tr2 = ''.join([TRANSLIT[i] for i in list(adj_root2)])
	ru_lines_selector.write_in_file(googlefile2, adj_root_tr2, osnova2)

	print(u'\nЗапуск MyStem для первого прилагательного...')
	result_lines_selector1 = './russian/results_middle/' + adj_root_tr1 + '_result_lines_selector.tsv'
	mystem_result1 = './russian/results_middle/' + adj_root_tr1 + '_gind_mystem.tsv'
	print('\nЗапуск в командной строке ./mystem -gind --format json ' + result_lines_selector1 + ' ' + mystem_result1 + '...')
	os.system(MST + ' -gind --format json ' + result_lines_selector1 + ' ' + mystem_result1)  # ../mystem в предыдущей папке # ./mystem в той же папке
	print(u'\nЗапуск MyStem для второго прилагательного...')
	result_lines_selector2 = './russian/results_middle/' + adj_root_tr2 + '_result_lines_selector.tsv'
	mystem_result2 = './russian/results_middle/' + adj_root_tr2 + '_gind_mystem.tsv'
	print('\nЗапуск в командной строке ./mystem -gind --format json ' + result_lines_selector2 + ' ' + mystem_result2 + '...')
	os.system(MST + ' -gind --format json ' + result_lines_selector2 + ' ' + mystem_result2)  # ../mystem в предыдущей папке # ./mystem в той же папке

	print(u'\nЗапуск функции ru_ngrams для первого прилагательного...')
	ru_ngrams.write_in_file_final(result_lines_selector1, mystem_result1, adj_root_tr1, adj_root1)
	print(u'\nЗапуск функции ru_ngrams для второго прилагательного...')
	ru_ngrams.write_in_file_final(result_lines_selector2, mystem_result2, adj_root_tr2, adj_root2)

	transl = adj_root_tr1[:2] + '_' + adj_root_tr2[:2]
	file1 = './russian/results/' + adj_root_tr1 + '_result_ngrams.tsv'
	file2 = './russian/results/' + adj_root_tr2 + '_result_ngrams.tsv'
	ru_comparation_with_0.write_down_result(file1, file2, transl, adj_root1, adj_root2, adj_root_tr1, adj_root_tr2)
