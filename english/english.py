# -*- coding: utf-8 -*-

import os

import english.eng_lines_selector as eng_lines_selector
import english.eng_ngrams as eng_ngrams
import english.eng_comparation as eng_comparation


def main(adj_root1, adj_root2, googlefile1, googlefile2, translate):
	if os.path.exists('./english/results/'):
		pass
	else:
		os.mkdir('./english/results/')
	if os.path.exists('./english/results_middle/'):
		pass
	else:
		os.mkdir('./english/results_middle/')
	print(u'\nЗапуск функции eng_lines_selector для первого прилагательного...')
	eng_lines_selector.write_in_file(googlefile1, adj_root1)
	print(u'\nЗапуск функции eng_lines_selector для второго прилагательного...')
	eng_lines_selector.write_in_file(googlefile2, adj_root2)

	result_lines_selector1 = './english/results/' + adj_root1 + '_result_lines_selector.tsv'
	result_lines_selector2 = './english/results/' + adj_root2 + '_result_lines_selector.tsv'

	print(u'\nЗапуск функции eng_ngrams для первого прилагательного...')
	eng_ngrams.write_in_file_final(result_lines_selector1, adj_root1)
	print(u'\nЗапуск функции eng_ngrams для второго прилагательного...')
	eng_ngrams.write_in_file_final(result_lines_selector2, adj_root2)

	transl = adj_root1[:2] + '_' + adj_root2[:2]

	file1 = './english/results/' + adj_root1 + '_result_ngrams.tsv'
	file2 = './english/results/' + adj_root2 + '_result_ngrams.tsv'

	if translate == 'да':
		api_key = input('Введите свой API ключ (например, trnsl.1.1.20161012T130742Z.65cdcdc3ed0fb1e1.5c685da1cf0b0b1d0e73e5ff51990b947daa569e: ')
		eng_comparation.write_down_result_tr(file1, file2, transl, adj_root1, adj_root2, api_key)
	elif translate == 'нет':
		eng_comparation.write_down_result(file1, file2, transl, adj_root1, adj_root2)
