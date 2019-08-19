# libraries
import pandas as pd
from functools import lru_cache
from collections import OrderedDict
import re
import json
import pickle
#from autocomp.library import trie

#Implementation of trie data structure
class Node:
    auto_comp=[]
    def __init__(self):
        self.m_children_nodes={}
        self.m_total_word_so_far=""
        self.m_curr_letter=""
        self.m_word=""
        self.m_curr_index=0
        
        
    def add_word(self, word, word_so_far = "",curr_index= -1):
        self.m_word=word
        self.m_curr_index=curr_index
        if self.m_curr_index >=0:
            self.m_curr_letter=self.m_word[self.m_curr_index]
            self.m_total_word_so_far=word_so_far + self.m_word[self.m_curr_index]
        if self.m_curr_index+1 < len(self.m_word):     #next up letter within word
            if self.m_word[self.m_curr_index+1] not in self.m_children_nodes:
                self.m_children_nodes[self.m_word[self.m_curr_index+1]]=Node()
                self.m_children_nodes[self.m_word[self.m_curr_index+1]].add_word(self.m_word,self.m_total_word_so_far,self.m_curr_index+1)
            else:
                self.m_children_nodes[self.m_word[self.m_curr_index+1]].add_word(self.m_word,self.m_total_word_so_far,self.m_curr_index+1)
    def auto_complete_word(self,str):
        if len(str) > 0 and str[0] in self.m_children_nodes:
            self.m_children_nodes[str[0]].auto_complete_word(str[1:])
        if len(str)==0:
            print("auto completed word:")
            self.print_tree()
        #print(self.auto_comp)
    def print_tree(self):
        #auto_words=[]
        if self:
            if len(self.m_children_nodes)==0:
                self.auto_comp.append(self.m_total_word_so_far)
            else:
                for i in self.m_children_nodes:
                    self.m_children_nodes[i].print_tree()
    def clear_list(self):
        self.auto_comp.clear()
def load():    
    #reading data
    f_path="/home/wasim/Documents/FullThrottle/library/input/word_search.tsv"
    df=pd.read_csv(f_path,sep="\t")
    words=df["the"].tolist()
    #Converting to Dictionary
    words_dict={}
    for index,row in df.iterrows():
        words_dict[row["the"]]=row["23135851162"]
    #preprocessing of data
    l=[]
    for i in words:
        if type(i) == float:
            continue
        else:
            l.append(i)
    root=Node()
    for word in l:
        root.add_word(word)
    return root,words_dict,l
obj,dic,l=load()
