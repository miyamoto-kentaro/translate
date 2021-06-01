# coding:utf-8
import os
import sys

import pandas
from googletrans import Translator

translator = Translator()
csv_dir =  os.path.abspath('/mnt/c/Users/kenta/Documents/2021課題/化学工学')
data=pandas.read_csv(csv_dir + '/translate.csv',encoding='utf-8')
english_list=[]
# print(data.head(1))
for i in data['japanese']:
    dst = translator.translate(i, src='ja', dest='en')
    english_list.append(dst.text)

data['english']=english_list

data.to_csv(csv_dir + '/result.csv'.format(csv_dir),encoding='utf_8_sig' ,index=False)

print('defaultencoding:', sys.getdefaultencoding())