from django.shortcuts import render,render_to_response
from django.http import HttpResponse
#from . import form
from autocomp.models import Word_TB
# libraries
import pandas as pd
from functools import lru_cache
from collections import OrderedDict
import re
import json
import pickle
from django.views.decorators import csrf
#from autocomp.library import trieds
#from autocomp.form import NewForm


# Create your views here.
def AutoComp(request):
	return HttpResponse("<h1>hi</h1>")

#def form_get_data(request):
#	word=request.get[word]
#	form1=form.form_page()
#	return render(request,"autocomplete/home.html",{'form':form1})
def word_search(obj,words_dict,l,input_word):
    #Input section
    root=obj
    root.clear_list()
    k=input_word
    root.auto_complete_word(k)
    auto_lst=list(root.auto_comp)

    #finidng keyword in strings
    def finding_substrings():
        if auto_lst.__len__() < 25:
            r=re.compile(k)
            match = filter(r.findall,l)
            return list(match)
        else:
            pass
    sub_str_list=finding_substrings()

    #creating final dictionary with words
    def creating_final_dict():
        f_word_dict={}
        for i in root.auto_comp:
            f_word_dict[i]=words_dict[i]
        try:
            for j in sub_str_list:
                f_word_dict[j]=words_dict[j]
        except:
            pass
        return f_word_dict
    final_dict=creating_final_dict()

    #soring the dictionary
    d_descending = OrderedDict(sorted(final_dict.items(), key=lambda kv: kv[1], reverse=True))

    #getting top 25 words
    lst=[]
    for x in list(d_descending)[0:25]:
        lst.append(x)

    #creating final List with data
    final_lst=[]
    lst=sorted(lst, key=len)
    for i in lst:
        if k == i and k not in final_lst:
            final_lst.append(k)
        else:
            final_lst.append(i)

    #arranging data in the list
    temp=[]
    for i in final_lst:
        if k not in temp:
            temp.append(k)
        elif i.startswith(k):
            temp.append(i)
        else:
            pass
    for i in final_lst:
        if i not in temp:
            temp.append(i)

    #Cnverting data into Json
    j=json.dumps(temp)
    return temp
	
def words(request):
#	words_list=Word_TB.objects.order_by('word')
#	form = NewForm()

#	if request.method == "GET":
	input_word=str(request.GET.get("word"))
	print(input_word)
	word_list=[input_word]
#word_search(trieds.obj,trieds.dic,trieds.l,input_word)
	word_dict={'words':word_list}
	return render(request,'autocomplete/word.html',context=word_dict)

def article(request):
	if request.method == "POST":
		search_text=request.POST['search_text']
	else:
		search_text= "HI"
	articles =Word_TB.objects.filter(word__contains=search_text)
	return render(request,'autocomplete/ajax_search.html',{'articles':articles})



















#	return render(request,'autocomplete/word.html',context=word_dict)
