# -*- coding: utf-8 -*-

import os

import ru_config
import ru_lines_selector
import ru_ngrams


translit = {u'а': u'a', u'б':u'b', u'в':u'v', u'г':u'g', u'д':u'd',
			 u'е': u'e', u'ж':u'zh', u'з':u'z', u'и':u'i', u'й':u'j',
			u'к':u'k', u'л':u'l', u'м':u'm', u'н':u'n', u'о':u'o',
			u'п':u'p', u'р':u'r', u'с':u's', u'т':u't', u'у':u'u',
			u'ф':u'f', u'х':u'h', u'ц':u'ts', u'ч':u'ch', u'ш':u'sh',
			u'щ':u'sch', u'ь':u'', u'ы':u'y', u'ъ':u'', u'э':u'e',
			u'ю':u'yu', u'я':u'ya' }
trash = [u'«', u'»', u'_NOUN_', u',', u'.', u'!', u')', u'*', u'"', u':', u'-', u'--', u';', u'...', u'?',  u'(']


print(u'ru_lines_selector для первого прилагательного')
adj_root1 = ru_config.adj_root1
adj_root_tr1 = ''.join([translit[i] for i in list(adj_root1)])
ru_lines_selector.write_in_file(ru_config.googlefile1, adj_root_tr1, ru_config.osnova1)
print(u'ru_lines_selector для второго прилагательного')
adj_root2 = ru_config.adj_root2
adj_root_tr2 = ''.join([translit[i] for i in list(adj_root2)])
ru_lines_selector.write_in_file(ru_config.googlefile2, adj_root_tr2, ru_config.osnova2)


print(u'MyStem для первого прилагательного')
result_lines_selector1 = './results/' + adj_root_tr1 + '_result_lines_selector.tsv'
mystem_result1 = './results/' + adj_root_tr1 + '_gind_fix_mystem.tsv'
print('./mystem -gind --format json ' + result_lines_selector1 + ' ' + mystem_result1)
os.system('./mystem -gind --format json ' + result_lines_selector1 + ' ' + mystem_result1)
print(u'MyStem для второго прилагательного')
result_lines_selector2 = './results/' + adj_root_tr2 + '_result_lines_selector.tsv'
mystem_result2 = './results/' + adj_root_tr2 + '_gind_fix_mystem.tsv'
print('./mystem -gind --format json ' + result_lines_selector2 + ' ' + mystem_result2)
os.system('./mystem -gind --format json ' + result_lines_selector2 + ' ' + mystem_result2)


print(u'ru_ngrams для первого прилагательного')
ru_ngrams.write_in_file_final(result_lines_selector1, mystem_result1, adj_root_tr1, adj_root1)
print(u'ru_ngrams для второго прилагательного')
ru_ngrams.write_in_file_final(result_lines_selector2, mystem_result2, adj_root_tr2, adj_root2)


# типа для всех raw input проделать все действия, описанные выше (чтобы если человек хотел сделать выборку
#  только по одному, он бы делал по одному6 а если компарэйшн, то тоже пожалуйста)