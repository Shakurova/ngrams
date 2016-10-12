# -*- coding: utf-8 -*-

import re
import os

import german.ge_lines_selector as ge_lines_selector
import german.ge_ngrams as ge_ngrams
import german.ge_comparation as ge_comparation


def main(adj_root1, adj_root2, googlefile1, googlefile2, TRTG, translate):
	ss = re.compile('ß')  # все ß заменяются на ss
	adj_root1 = ss.sub('ss', adj_root1)
	adj_root2 = ss.sub('ss', adj_root2)
	if os.path.exists('./german/results/'):
		pass
	else:
		os.mkdir('./german/results/')
	if os.path.exists('./german/results_middle/'):
		pass
	else:
		os.mkdir('./german/results_middle/')
	print(u'\nЗапуск функции ge_lines_selector для первого прилагательного...')
	ge_lines_selector.write_in_file(googlefile1, adj_root1)
	print(u'\nЗапуск функции ge_lines_selector для второго прилагательного...')
	ge_lines_selector.write_in_file(googlefile2, adj_root2)

	result_lines_selector1 = './german/results_middle/' + adj_root1 + '_result_lines_selector.tsv'
	result_lines_selector2 = './german/results_middle/' + adj_root2 + '_result_lines_selector.tsv'

	print(u'\nЗапуск функции ge_ngrams для первого прилагательного...')
	ge_ngrams.write_in_file_final(result_lines_selector1, adj_root1, TRTG)
	print(u'\nЗапуск функции ge_ngrams для второго прилагательного...')
	ge_ngrams.write_in_file_final(result_lines_selector2, adj_root2, TRTG)

	transl = adj_root1[:2] + '_' + adj_root2[:2]

	file1 = './german/results/' + adj_root1 + '_result_ngrams.tsv'
	file2 = './german/results/' + adj_root2 + '_result_ngrams.tsv'

	if translate == 'да':
		api_key = input('Введите свой API ключ (например, trnsl.1.1.20161012T130742Z.65cdcdc3ed0fb1e1.5c685da1cf0b0b1d0e73e5ff51990b947daa569e: ')
		ge_comparation.write_down_result_tr(file1, file2, transl, adj_root1, adj_root2, api_key)
	elif translate == 'нет':
		ge_comparation.write_down_result(file1, file2, transl, adj_root1, adj_root2)
