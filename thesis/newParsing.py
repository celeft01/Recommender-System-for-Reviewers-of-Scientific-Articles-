#import modules
import matplotlib.pyplot as plt
import numpy as np
from scipy.cluster.vq import whiten, kmeans2
import pandas as pd
from lxml import etree
from copy import deepcopy
from pandas.io.pytables import *
import gc
import h5py
import time

# #parsing xml file using lxml(because there are DTD in the xml) for individual booktitles and journals


# parser = etree.XMLParser(dtd_validation=True)
# tree1=etree.parse('dblp_mini_1.xml', parser)
# tree2=etree.parse('dblp_mini_2.xml', parser)
# root1=tree1.getroot()
# root2=tree2.getroot()




# def tr_xml2(xml_doc):
#     attr=xml_doc.attrib
              
        
#     for xml in xml_doc.findall('inproceedings'):
#         dict=deepcopy(attr)
#         s1=""
#         s2=""
#         s3=""
        
#         s4=""
        
#         for x in xml.findall('author'):
            
#             s1=x.text
#             author_list.append(s1)
#             s2=""
#             s3=""
#             s4=""
            
            
#             for y in xml.findall('booktitle'):
#                 s2=y.text
#             for z in xml.findall('journal'):
#                 s3=z.text
#             for t in xml.findall('title'):
#                 s4=t.text
#             booktitle_list.append(s2)
#             journal_list.append(s3)
#             title_list.append(s4)
            
        
        
#     for xml in xml_doc.findall('article'):
#         dict=deepcopy(attr)
#         s1=""
#         s2=""
#         s3=""
#         s4=""
        
#         for x in xml.findall('author'):
#             s1=x.text
#             author_list.append(s1)
#             s2=""
#             s3=""
#             s4=""
            
#             for y in xml.findall('booktitle'):
#                 s2=y.text
#             for z in xml.findall('journal'):
#                 s3=z.text
#             for t in xml.findall('title'):
#                 s4=t.text
#             booktitle_list.append(s2)
#             journal_list.append(s3)
#             title_list.append(s4)
    
        
        

# author_list=[]
# booktitle_list=[]
# journal_list=[]
# title_list=[]

     
        
# tr_xml2(root1)

# tr_xml2(root2)






# dict1 = {'author': author_list, 'booktitle': booktitle_list}
# dict2 = {'author': author_list, 'journal': journal_list}
# dict3={'author': author_list, 'title': title_list}
    
# df1 = pd.DataFrame(dict1)
# df2 = pd.DataFrame(dict2)
# df3= pd.DataFrame(dict3)

# ratings1=[1 for i in range(len(df1))]
# ratings2=[1 for i in range(len(df2))]
# df1['ratings']=ratings1
# df2['ratings']=ratings2






# #df2

# df1.drop(df1[df1['booktitle'] == ''].index, inplace = True)
# df1.reset_index(inplace=True, drop=True)

# df2.drop(df2[df2['journal'] == ''].index, inplace = True)
# df2.reset_index(inplace=True, drop=True)

# df3.drop(df3[df3['title'] == ''].index, inplace = True)
# df3.reset_index(inplace=True, drop=True)






# df1.sort_values(['author', 'booktitle'], inplace=True)
# df1.reset_index(inplace=True, drop=True)
# check_table=df1.duplicated()

# count=1
# for x in range(0, len(check_table)):
#     if(x==len(check_table)-1):
#         if(check_table[x]==False):
#             df1.at[x,'ratings']=count
#         elif(check_table[x]==True):
#              df1.at[x, 'ratings']=count+1
#     elif(check_table[x]==False and count>1):
#         df1.at[x-1,'ratings']=count
#         count=1
#     elif(check_table[x]==True):
#         count=count+1
# #print(check_table)
# #print(df321)
# df1.drop_duplicates(keep='last', subset=["author", "booktitle"], inplace=True)
# df1.reset_index(inplace=True, drop=True)



# df2.sort_values(['author', 'journal'], inplace=True)
# df2.reset_index(inplace=True, drop=True)
# check_table2=df2.duplicated()

# count=1
# for x in range(0, len(check_table2)):
#     if(x==len(check_table2)-1):
#         if(check_table2[x]==False):
#             df2.at[x,'ratings']=count
#         elif(check_table2[x]==True):
#              df2.at[x, 'ratings']=count+1
#     elif(check_table2[x]==False and count>1):
#         df2.at[x-1,'ratings']=count
#         count=1
#     elif(check_table2[x]==True):
#         count=count+1
# #print(check_table)
# #print(df321)
# df2.drop_duplicates(keep='last', subset=["author", "journal"], inplace=True)
# df2.reset_index(inplace=True, drop=True)



# df3.sort_values(['author', 'title'], inplace=True)
# df3.reset_index(inplace=True, drop=True)
# df3.drop_duplicates(keep='last', subset=["author", "title"], inplace=True)
# df3.reset_index(inplace=True, drop=True)
# #lst=[check_table, ratings1]
# #del lst
# #gc.collect()


# df1.to_parquet('myfile1.parquet', engine='fastparquet')
# print(df1)

# df2.to_parquet('myfile2.parquet', engine='fastparquet')
# print(df2)


# df3.to_parquet('myfile3.parquet', engine='fastparquet')
# print(df3)


















#parsing xml file using lxml(because there are DTD in the xml) for combined booktitles and journals without titles(because already created)


parser = etree.XMLParser(dtd_validation=True)
tree1=etree.parse('dblp_mini_1.xml', parser)
tree2=etree.parse('dblp_mini_2.xml', parser)
root1=tree1.getroot()
root2=tree2.getroot()




def tr_xml2(xml_doc):
    attr=xml_doc.attrib
              
        
    for xml in xml_doc.findall('inproceedings'):
        dict=deepcopy(attr)
        s1=""
        s2=""
        s3=""
        for x in xml.findall('author'):
            
            s1=x.text
            author_list.append(s1)
            s2=""
            s3=""
            
            for y in xml.findall('booktitle'):
                s2=y.text
            for z in xml.findall('journal'):
                s3=z.text
            booktitle_list.append(s2)
            journal_list.append(s3)
            
        
        
    for xml in xml_doc.findall('article'):
        dict=deepcopy(attr)
        s1=""
        s2=""
        s3=""
        
        for x in xml.findall('author'):
            s1=x.text
            author_list.append(s1)
            s2=""
            s3=""
            
            for y in xml.findall('booktitle'):
                s2=y.text
            for z in xml.findall('journal'):
                s3=z.text
            booktitle_list.append(s2)
            journal_list.append(s3)
    
        
        

author_list=[]
booktitle_list=[]
journal_list=[]
     
        
tr_xml2(root1)

tr_xml2(root2)






dict1 = {'author': author_list, 'booktitle-journal': booktitle_list}
dict2 = {'author': author_list, 'booktitle-journal': journal_list}
    
df1 = pd.DataFrame(dict1)
df2 = pd.DataFrame(dict2)
ratings1=[1 for i in range(len(df1))]
ratings2=[1 for i in range(len(df2))]
df1['ratings']=ratings1
df2['ratings']=ratings2






#df2

df1.drop(df1[df1['booktitle-journal'] == ''].index, inplace = True)
df1.reset_index(inplace=True, drop=True)

df2.drop(df2[df2['booktitle-journal'] == ''].index, inplace = True)
df2.reset_index(inplace=True, drop=True)






df1.sort_values(['author', 'booktitle-journal'], inplace=True)
df1.reset_index(inplace=True, drop=True)
check_table=df1.duplicated()

count=1
for x in range(0, len(check_table)):
    if(x==len(check_table)-1):
        if(check_table[x]==False):
            df1.at[x,'ratings']=count
        elif(check_table[x]==True):
             df1.at[x, 'ratings']=count+1
    elif(check_table[x]==False and count>1):
        df1.at[x-1,'ratings']=count
        count=1
    elif(check_table[x]==True):
        count=count+1
#print(check_table)
#print(df321)
df1.drop_duplicates(keep='last', subset=["author", "booktitle-journal"], inplace=True)
df1.reset_index(inplace=True, drop=True)



df2.sort_values(['author', 'booktitle-journal'], inplace=True)
df2.reset_index(inplace=True, drop=True)
check_table2=df2.duplicated()

count=1
for x in range(0, len(check_table2)):
    if(x==len(check_table2)-1):
        if(check_table2[x]==False):
            df2.at[x,'ratings']=count
        elif(check_table2[x]==True):
             df2.at[x, 'ratings']=count+1
    elif(check_table2[x]==False and count>1):
        df2.at[x-1,'ratings']=count
        count=1
    elif(check_table2[x]==True):
        count=count+1
#print(check_table)
#print(df321)
df2.drop_duplicates(keep='last', subset=["author", "booktitle-journal"], inplace=True)
df2.reset_index(inplace=True, drop=True)



#lst=[check_table, ratings1]
#del lst
#gc.collect()



# print(df1)
# print(df2)

combined = [df1, df2]
  
dfAll = pd.concat(combined)
dfAll.reset_index(inplace=True, drop=True)


# dfAll.to_hdf('storeAll.h5', 'table', append=True)
dfAll.to_parquet('myfileAll.parquet', engine='fastparquet')


