# -*- coding: utf-8 -*-

import os

import ru_config
import ru_lines_selector
import ru_ngrams
import ru_comparation_with_0
# from tkinter import *
# from tkinter import ttk
# from tkinter.filedialog import askopenfilename


trash = ['«', '»', '_NOUN_', ',', '.', '!', ')', '*', '"', ':', '-', '--', ';', '...', '?',  '(']
translit = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
			'е': 'e', 'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'j',
			'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o',
			'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
			'ф': 'f', 'х': 'h', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh',
			'щ': 'sch', 'ь': '', 'ы': 'y', 'ъ': '', 'э': 'e',
			'ю': 'yu', 'я': 'ya'}
languages = {'русский': 'russian',
			'английский': 'english',
			'немецкий': 'german'}


print(u'\nЗапуск функции ru_lines_selector для первого прилагательного...')
adj_root1 = ru_config.adj_root1
adj_root_tr1 = ''.join([translit[i] for i in list(adj_root1)])
ru_lines_selector.write_in_file(ru_config.googlefile1, adj_root_tr1, ru_config.osnova1)
print(u'\nЗапуск функции ru_lines_selector для второго прилагательного...')
adj_root2 = ru_config.adj_root2
adj_root_tr2 = ''.join([translit[i] for i in list(adj_root2)])
ru_lines_selector.write_in_file(ru_config.googlefile2, adj_root_tr2, ru_config.osnova2)

print(u'\nЗапуск MyStem для первого прилагательного...')
result_lines_selector1 = './results/' + adj_root_tr1 + '_result_lines_selector.tsv'
mystem_result1 = './results/' + adj_root_tr1 + '_gind_fix_mystem.tsv'
print('\nЗапуск в командной строке ./mystem -gind --format json ' + result_lines_selector1 + ' ' + mystem_result1 + '...')
os.system('../mystem -gind --format json ' + result_lines_selector1 + ' ' + mystem_result1)
print(u'\nЗапуск MyStem для второго прилагательного...')
result_lines_selector2 = './results/' + adj_root_tr2 + '_result_lines_selector.tsv'
mystem_result2 = './results/' + adj_root_tr2 + '_gind_fix_mystem.tsv'
print('\nЗапуск в командной строке ./mystem -gind --format json ' + result_lines_selector2 + ' ' + mystem_result2 + '...')
os.system('../mystem -gind --format json ' + result_lines_selector2 + ' ' + mystem_result2)


print(u'\nЗапуск функции ru_ngrams для первого прилагательного...')
ru_ngrams.write_in_file_final(result_lines_selector1, mystem_result1, adj_root_tr1, adj_root1)
print(u'\nЗапуск функции ru_ngrams для второго прилагательного...')
ru_ngrams.write_in_file_final(result_lines_selector2, mystem_result2, adj_root_tr2, adj_root2)

transl = adj_root_tr1[:2] + '_' + adj_root_tr2[:2]
file1 = './results/' + adj_root_tr1 + '_gind_f_result_ngrams.tsv'
file2 = './results/' + adj_root_tr2 + '_gind_f_result_ngrams.tsv'
ru_comparation_with_0.write_down_result(file1, file2, transl, adj_root1, adj_root2)

# TO-DO
# для всех raw input проделать все действия, описанные выше (чтобы если человек хотел сделать выборку
# только по одному, он бы делал по одному, а если компарэйшн, то тоже пожалуйста)
# language = input("Выбериите язык: русский, английский или немецкий-  ")

# root = Tkinter.Tk()
# root = Tkinter.Tk()
# filename = askopenfilename(parent=root)
# print(filename)
# сделать сдесь разархивацию

# name = askopenfilename(filetypes=(("Text File", "*.txt"), ("All Files", "*.*")),
# 						title="Choose a file.")
# print(name)
#