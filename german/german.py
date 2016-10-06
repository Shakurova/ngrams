# -*- coding: utf-8 -*-

import os

import ge_config
import ge_lines_selector
import ge_ngrams
import ge_comparation
# from tkinter import *
# from tkinter import ttk
# from tkinter.filedialog import askopenfilename


trash = ['«', '»', '_NOUN_', ',', '.', '!', ')', '*', '"', ':', '-', '--', ';', '...', '?',  '(']
languages = {'русский': 'russian',
			'английский': 'english',
			'немецкий': 'german'}


print(u'\nЗапуск функции ge_lines_selector для первого прилагательного...')
adj_root1 = ge_config.adj_root1
ge_lines_selector.write_in_file(ge_config.googlefile1, adj_root1)
print(u'\nЗапуск функции ge_lines_selector для второго прилагательного...')
adj_root2 = ge_config.adj_root2
ge_lines_selector.write_in_file(ge_config.googlefile2, adj_root2)

result_lines_selector1 = './results/' + adj_root1 + '_result_lines_selector.tsv'
result_lines_selector2 = './results/' + adj_root2 + '_result_lines_selector.tsv'

print(u'\nЗапуск функции ge_ngrams для первого прилагательного...')
ge_ngrams.write_in_file_final(result_lines_selector1, adj_root1)
print(u'\nЗапуск функции ge_ngrams для второго прилагательного...')
ge_ngrams.write_in_file_final(result_lines_selector2, adj_root2)

transl = adj_root1[:2] + '_' + adj_root2[:2]

file1 = './results/' + adj_root1 + '_gind_f_result_ngrams.tsv'
file2 = './results/' + adj_root2 + '_gind_f_result_ngrams.tsv'
ge_comparation.write_down_result(file1, file2, transl, adj_root1, adj_root2)
