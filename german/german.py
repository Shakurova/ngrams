# -*- coding: utf-8 -*-

import os

# import german.ge_config as ge_config
import german.ge_lines_selector as ge_lines_selector
import german.ge_ngrams as ge_ngrams
import german.ge_comparation as ge_comparation
# from tkinter import *
# from tkinter import ttk
# from tkinter.filedialog import askopenfilename


def main(adj_root1, adj_root2, googlefile1, googlefile2):
	if os.path.exists('./german/results/'):
		pass
	else:
		os.mkdir('./german/results/')
	if os.path.exists('./german/results_middle/'):
		pass
	else:
		os.mkdir('./german/results_middle/')
	print(u'\nЗапуск функции ge_lines_selector для первого прилагательного...')
	# adj_root1 = ge_config.adj_root1
	ge_lines_selector.write_in_file(googlefile1, adj_root1)
	print(u'\nЗапуск функции ge_lines_selector для второго прилагательного...')
	# adj_root2 = ge_config.adj_root2
	ge_lines_selector.write_in_file(googlefile2, adj_root2)

	result_lines_selector1 = './german/results_middle/' + adj_root1 + '_result_lines_selector.tsv'
	result_lines_selector2 = './german/results_middle/' + adj_root2 + '_result_lines_selector.tsv'

	print(u'\nЗапуск функции ge_ngrams для первого прилагательного...')
	ge_ngrams.write_in_file_final(result_lines_selector1, adj_root1)
	print(u'\nЗапуск функции ge_ngrams для второго прилагательного...')
	ge_ngrams.write_in_file_final(result_lines_selector2, adj_root2)

	transl = adj_root1[:2] + '_' + adj_root2[:2]

	file1 = './german/results/' + adj_root1 + '_result_ngrams.tsv'
	file2 = './german/results/' + adj_root2 + '_result_ngrams.tsv'
	ge_comparation.write_down_result(file1, file2, transl, adj_root1, adj_root2)