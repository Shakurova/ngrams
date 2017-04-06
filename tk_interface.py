# -*- coding: utf-8 -*-

import os
import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename

TRANSLIT = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
            'е': 'e', 'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'j',
            'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o',
            'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
            'ф': 'f', 'х': 'h', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh',
            'щ': 'sch', 'ь': '', 'ы': 'y', 'ъ': '', 'э': 'e',
            'ю': 'yu', 'я': 'ya'}




def built_graphic(language, adj_root1, adj_root2, draw):
    graphic = draw
    if graphic == 1:
        transl = adj_root1[:2] + '_' + adj_root2[:2]
        if language in ['german', 'english']:
            print(transl + '_result_0_comparation.csv')
            os.system('/usr/local/bin/Rscript ./russian/graphics_normal_ideorg.R ' + adj_root1 + ' ' + adj_root2 + ' ' + './' + language + '/results/' + transl + '_result_0_comparation.csv')
            print('Программа завершила свою работу!')
        if language in ['russian']:
            adj_root_tr1 = ''.join([TRANSLIT[i] for i in list(adj_root1)])
            adj_root_tr2 = ''.join([TRANSLIT[i] for i in list(adj_root2)])
            transl = adj_root_tr1[:2] + '_' + adj_root_tr2[:2]
            print('./' + language + '/' + transl + '_result_0_comparation.csv')
            os.system('/usr/local/bin/Rscript ./russian/graphics_normal_ideorg.R ' + adj_root_tr1 + ' ' + adj_root_tr2 + ' ' + './' + language + '/results/' + transl + '_result_0_comparation.csv')
            print('Программа завершила свою работу!')
    elif graphic == 0:
        print('Программа завершила свою работу!')
    else:
        print('Нет такого варианта ответа. Программа завершила свою работу!')
        pass

global d
d = {}

class TkFileDialogExample1:

  def __init__(self, master):
    # tkinter.Frame.__init__(self, root)

    self.master = master
    self.frame = Frame(self.master)
    ######

    lab2 = Label(self.frame, text="Выберите язык", font="Arial 18")
    lab2.pack()

    self.lang = IntVar()
    rbutton1 = Radiobutton(self.frame, text='русский', variable=self.lang, value='1')
    rbutton2 = Radiobutton(self.frame, text='английский', variable=self.lang, value='2')
    rbutton3 = Radiobutton(self.frame, text='немецкий', variable=self.lang, value='3')
    rbutton1.pack()
    rbutton2.pack()
    rbutton3.pack()

    #####

    self.button_final = Button(self.frame, text="Дальше!", command=self.new_window)
    self.button_final.pack()

    self.frame.pack()

  def new_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = TkFileDialogExampl2(self.newWindow, self.lang.get())


class TkFileDialogExampl2:

    def __init__(self, master, lang):
        self.master = master
        self.frame = Frame(self.master)

        print(lang)

        if lang == 2 or lang == 3:
            labtr = Label(self.frame, text="Сделать перевод? (для английского и немецкого)", font="Arial 18")
            labtr.pack()

            self.tr = IntVar()
            rbutton_yes = Radiobutton(self.frame, text='да', variable=self.tr, value='1')
            rbutton_no = Radiobutton(self.frame, text='нет', variable=self.tr, value='0')
            rbutton_yes.pack()
            rbutton_no.pack()

        ######

        lab1 = Label(self.frame, text="Введите первое прилагательное", font="Arial 18")
        lab1.pack()

        self.adj1 = Entry(self.frame, width=20, bd=3)
        self.adj1.pack()

        if lang == 1:
            lab11 = Label(self.frame, text="Введите основу первого прилагательного", font="Arial 18")
            lab11.pack()

            self.osnova1 = Entry(self.frame, width=20, bd=3)
            self.osnova1.pack()

        ######

        lab2 = Label(self.frame, text="Введите второе прилагательное", font="Arial 18")
        lab2.pack()

        self.adj2 = Entry(self.frame, width=20, bd=3)
        self.adj2.pack()

        if lang == 1:
            lab22 = Label(self.frame, text="Введите основу второго прилагательного", font="Arial 18")
            lab22.pack()

            self.osnova2 = Entry(self.frame, width=20, bd=3)
            self.osnova2.pack()

        ######

        lab4 = Label(self.frame, text="Что вы хотите сделать?", font="Arial 18")
        lab4.pack()

        self.var1 = IntVar()
        self.var2 = IntVar()
        self.check1 = Checkbutton(self.frame, text=u'Построить таблицы', variable=self.var1, onvalue=1, offvalue=0)
        self.check2 = Checkbutton(self.frame, text=u'Нарисовать график', variable=self.var2, onvalue=1, offvalue=0)
        self.check1.pack()
        self.check2.pack()

        ######

        self.returned_values = {}
        self.returned_values['first'] = None
        self.returned_values['second'] = None
        self.returned_values['mst'] = None
        self.returned_values['trtg'] = None

        self.first = Button(self.frame, text='Выберите файл с первым прилагательным', command=self.askopenfilename_first)
        self.second = Button(self.frame, text='Выберите файл со вторым прилагательным', command=self.askopenfilename_second)
        self.first.pack()
        self.second.pack()

        if lang == 1:
            self.mst = Button(self.frame, text='Введите путь к программе mystem', command=self.askopenfilename_mst)
            self.mst.pack()

        if lang == 3:
            self.trtg = Button(self.frame, text='Введите путь к программе TreeTagger', command=self.askopenfilename_trtg)
            self.trtg.pack()

        self.lang = lang

        self.button_final = Button(self.frame, text="Поехали!", command=self.Pressed)
        self.button_final.pack()

        self.frame.pack()

    def askopenfilename_first(self):
          self.returned_values['first'] = askopenfilename()

    def askopenfilename_second(self):
          self.returned_values['second'] = askopenfilename()

    def askopenfilename_mst(self):
          self.returned_values['mst'] = askopenfilename()

    def askopenfilename_trtg(self):
          self.returned_values['trtg'] = askopenfilename()


    def Pressed(self):  # function

          answers = {}
          answers['adj1'] = self.adj1.get()
          if self.lang == 1:
              answers['osnova1'] = self.osnova1.get()
          answers['adj1_path'] = self.returned_values['first']

          answers['adj2'] = self.adj2.get()
          if self.lang == 1:
              answers['osnova2'] = self.osnova2.get()
          answers['adj2_path'] = self.returned_values['second']

          answers['draw_table'] = self.var1.get()
          answers['draw_graphic'] = self.var2.get()

          answers['language'] = self.lang

          if self.lang == 2 or self.lang == 3:
              answers['translate'] = self.tr.get()

          if self.lang == 1:
              answers['mystem'] = self.returned_values['mst']

          if self.lang == 3:
            answers['TRTG'] = self.returned_values['trtg']

          for k in answers:
              print(k, answers[k])

          if answers['language'] == 1:
              language = 'russian'
              if answers['draw_table'] == 1:
                  import russian.russian
                  russian.russian.main(answers['adj1'], answers['adj2'], answers['osnova1'], answers['osnova2'], answers['adj1_path'], answers['adj2_path'], answers['mystem'])
                  built_graphic(language, answers['adj1'], answers['adj2'], answers['draw_graphic'])
              elif answers['draw_graphic'] == 1:
                  built_graphic(language, answers['adj1'], answers['adj2'], answers['draw_graphic'])

          elif answers['language'] == 2:
              language = 'english'
              import english.english
              if answers['draw_table'] == 1:
                  translate = answers['translate']
                  english.english.main(answers['adj1'], answers['adj2'], answers['adj1_path'], answers['adj2_path'], translate)
                  built_graphic(language, answers['adj1'], answers['adj2'], answers['draw_graphic'])
              elif answers['draw_graphic'] == 1:
                  built_graphic(language, answers['adj1'], answers['adj2'], answers['draw_graphic'])

          elif answers['language'] == 3:
              language = 'german'
              import german.german
              if answers['draw_table'] == 1:
                  translate = answers['translate']
                  german.german.main(answers['adj1'], answers['adj2'], answers['adj1_path'], answers['adj2_path'], TRTG, translate)
                  built_graphic(language, answers['adj1'], answers['adj2'], answers['draw_graphic'])
              elif answers['draw_graphic'] == 1:
                  built_graphic(language, answers['adj1'], answers['adj2'], answers['draw_graphic'])


if __name__=='__main__':
  root = Tk()
  TkFileDialogExample1(root)
  root.mainloop()



