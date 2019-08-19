import pandas as pd
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

import django
django.setup()

from autocomp.models import Word_TB
#read data from tsv file
f_path="/home/wasim/Documents/FullThrottle/library/input/word_search.tsv"
df=pd.read_csv(f_path,sep="\t")

#Convert to Dictionary
words_dict={}
count=1
for index,row in df.iterrows():
	words_dict[row["the"]]=row["23135851162"]
	try:
		#print(row["the"]+"->")
		print(count)
		count+=1
		w_tb=Word_TB.objects.get_or_create(word=row["the"],frequency=row["23135851162"])[0]
		#w_tb.save()
	except:
		print("error")



#def add_name(nm,fr):
#for i in words_dict.keys():
	

	#add_name(i,words_dict[i])


