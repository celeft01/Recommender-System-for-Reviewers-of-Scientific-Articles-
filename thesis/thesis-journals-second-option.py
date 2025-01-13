#EVERYTHING TOGETHER(ME BOOKTITLES)

#import modules
import time
timeAtStart=time.time()


# import matplotlib.pyplot as plt
# import numpy as np
from scipy.cluster.vq import whiten, kmeans2
import pandas as pd
from copy import deepcopy
from pandas.io.pytables import *
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
import h5py
import bs4 as bs
import requests
import h5py
from sklearn.feature_extraction.text import TfidfVectorizer
import json
import sys
from lxml import etree
from copy import deepcopy








df1=pd.read_parquet('myfile2.parquet', engine='fastparquet')
df3=pd.read_parquet('myfile3.parquet', engine='fastparquet')




nstr=""
knstr=""
aname63=[]
allKeys=[]
k1=""
k2=""

firstS=False
secondS=False

for i in range (1, len(sys.argv)):

    # print(sys.argv[i])

    if(sys.argv[i]=='/' and firstS==False):
        nstr = nstr[:-1]
        aname63.append(nstr)
        firstS=True
        continue
    elif(sys.argv[i]=='/' and firstS==True):
        knstr=knstr[:-1]
        allKeys.append(knstr)
        secondS=True

    if(firstS==False):
        if(sys.argv[i]==','):
            nstr = nstr[:-1]
            aname63.append(nstr)
            nstr=""
            continue
        else:
            partName=sys.argv[i]
            partName=partName[0][0].upper()+partName[1:len(partName)].lower()
            nstr=nstr+partName+" "

    elif(firstS==True and secondS==False):
        # partk1=sys.argv[i].lower()
        # k1=k1+partk1+" "
        if(sys.argv[i]==','):
            knstr = knstr[:-1]
            allKeys.append(knstr)
            knstr=""
            continue
        else:
            partKey=sys.argv[i].lower()
            knstr=knstr+partKey+" "

    # elif(firstS==True and secondS==True):
    #     partk2=sys.argv[i].lower()
    #     k2=k2+partk2+" "

knstr = knstr[:-1]
nstr = nstr[:-1]
k1= k1[:-1]
k2 = k2[:-1]
k1=k1.lower()
k2=k2.lower()




# aname63=['Anna Philippou','Dimitrios Kouzapas']
# k1='reversible'
# k2='process'
















# aname36="Dimitrios Kouzapas"
# k1="session"
# k2="types"

# aname63=["Anna Philippou", "Dimitrios Kouzapas"]
# k1="reversible process"
# k2="petri nets"







freslist=[]


resList=[]







author_test=df1[['author']].copy()
author_test.drop_duplicates(keep='first', inplace=True)
author_test.reset_index(inplace=True, drop=True)





dftest1=df1[['journal']].copy()
dftest1.drop_duplicates(keep='first', inplace=True)
dftest1.sort_values(by=['journal'], ascending=True, inplace=True)
third_lst=[0]*len(dftest1)
dftest1['ratings']=third_lst
dftest1.reset_index(inplace=True, drop=True)






def create_matrix(data, author_col, booktitle_col, rating_col):
        

        # create a sparse matrix of using the (rating, (rows, cols)) format
        rows = data[author_col].cat.codes
        cols = data[booktitle_col].cat.codes
        rating = data[rating_col]
        ratings = csr_matrix((rating, (rows, cols)))
        return ratings

df1['author'] = df1['author'].astype('category')
df1['journal'] = df1['journal'].astype('category')


pinakas=create_matrix(df1, 'author', 'journal', 'ratings')






pinakas_test=pd.DataFrame()


for nam in range(len(aname63)):

    aname36=aname63[nam]

    

    #print(pinakas)











    #FOR BOOKTITLES

    user_input=aname36


    pinakas_test = pinakas_test.append(df1[df1['author']==user_input].copy())
    # print(pinakas_test)



    #Checking if input has entries
    if(pinakas_test.empty):
        print(json.dumps('No entries from this author'))
        exit()
        

    #print(pinakas_test)




    # author_test=df1[['author']].copy()
    # author_test.drop_duplicates(keep='first', inplace=True)
    # author_test.reset_index(inplace=True, drop=True)





    # dftest1=df1[['booktitle']].copy()
    # dftest1.drop_duplicates(keep='first', inplace=True)
    # dftest1.sort_values(by=['booktitle'], ascending=True, inplace=True)
    # third_lst=[0]*len(dftest1)
    # dftest1['ratings']=third_lst
    # dftest1.reset_index(inplace=True, drop=True)



for i in range (0, len(dftest1)):
    for j in range(0, len(pinakas_test)):
        if(pinakas_test.iloc[j,1]==dftest1.iloc[i,0]):
            #dftest1.iloc[i,1]=pinakas_test.iloc[j,2]
            dftest1.iloc[i,1]=dftest1.iloc[i,1]+pinakas_test.iloc[j,2]
        
                        
                    


query_item=dftest1['ratings'].copy().values.reshape(1,-1)



                        



model_knn = NearestNeighbors(metric = 'cosine', algorithm = 'brute')
model_knn.fit(pinakas)
distances, indices = model_knn.kneighbors(query_item, n_neighbors = 200)#out 10 for testing
    
    

for i in range(0, len(distances.flatten())):
    #if i == 0:
        #print('Recommendations for {0}:\n'.format(author_test.iloc[indices.flatten()[i],0]))
    #else:
        #print('{0}: {1}, with distance of {2}:'.format(i, author_test.iloc[indices.flatten()[i],0], distances.flatten()[i]))
    if (i!=0 and (author_test.iloc[indices.flatten()[i],0] not in resList) and (author_test.iloc[indices.flatten()[i],0] not in aname63)):
        resList.append(author_test.iloc[indices.flatten()[i],0])

            




#finding co-authors

def findCo(name):
    
    URL = 'https://dblp.uni-trier.de/search/author?xauthor='+str(name)
    URL2='https://dblp.uni-trier.de/pid/'
    URL3='.xml?view=coauthor'

    # parsing
    url_link = requests.get(URL)
    file = bs.BeautifulSoup(url_link.text, features="xml")#,'lxml')

    


    auth_pid=str(file.find('author')['pid'])

    coauthors=[]

    finalURL=URL2+auth_pid+URL3
    url_link2=requests.get(finalURL)
    file2=bs.BeautifulSoup(url_link2.text, features="xml")#,'lxml')
    

    for i in file2.find_all('author'):
        coauthors.append(i.text)
        
    return coauthors

coList=[]
for nam in range(len(aname63)):    
    coList=coList + findCo(aname63[nam])
coList = list(dict.fromkeys(coList))#delete duplicates




#FOR BOOKTITLE




for j in resList:
    # for i in coList:

        # if(not(any(char.isdigit() for char in j) and any(char.isdigit() for char in i))):
        #     wordi=''.join([c for c in i if not i.isdigit()])
        #     wordj=''.join([c for c in j if not i.isdigit()])
        #     if(wordi==wordj):
        #         resList.remove(j)



    if(j in coList):
        resList.remove(j)
    

            










#NEW TF-IDF ALGORITHM


# freslist.append(resList)




def keywordAlg(aName):
    name=aName
    



    titlesdf = df3[df3['author']==name].copy()
    # print(titlesdf)
    titles=titlesdf["title"].tolist()
    # print(titles)
    for i in range(len(titles)):
        if(titles[i] is not None):
            titles[i]=titles[i]
        else:
            titles.pop(i)





    

    
        
    # keyword1=k1
    # keyword2=k2
    # KW1=0
    # KW2=0
    titlesLower=[]
    totalScore=[]
    # keyw1=[]
    # keyw2=[]

    for i in range(0, len(allKeys)):
        keyword1=allKeys[i]
        KW1=0
        keyw1=[]
        for j in range (0,len(titles)):


        
            if(titles[j].lower().count(keyword1)>0 and(titles[j].lower() not in titlesLower)):
                titlesLower.append(titles[j].lower())
                KW1=KW1+1
                keyw1.append(titles[j])

        keyw1.insert(0, keyword1)
        keyw1.insert(0, KW1)
        totalScore.append(keyw1)
                
    
    
    
    
        
    # for i in range (0,len(titles)):


    #     #this option also counts the substrings
    #     if(titles[i].count(keyword1)>0):
    #         KW1=KW1+1
    #         keyw1.append(titles[i])
    #     if(titles[i].count(keyword2)>0):
    #         KW2=KW2+1
    #         keyw2.append(titles[i])



        


    # keyw1.insert(0, KW1)
    # keyw2.insert(0, KW2)
    
    # totalScore.append(keyw1)
    # totalScore.append(keyw2)

    return totalScore



authorScores2=[]
#testList=['Dimitrios Kouzapas','Anna Philippou', 'Antonis Antonopoulos', 'Amrita Suresh', 'Irek Ulidowski']

for i in range (0,len(resList)):
    authorScores2.append(keywordAlg(resList[i]))
    # authorScores.append(keywordAlg(resList[i]))
    


authorScores=[]
for i in range(len(authorScores2)):
    ksum=0
    for j in range (len(authorScores2[i])):
        ksum=ksum+authorScores2[i][j][0]
    authorScores.append(ksum)

authorScoresCopy=authorScores.copy()

# combTable=zip(authorScores,resList)
combTable=zip(authorScores,resList)
ScombTable=sorted(combTable, reverse=True)
sortedNames=[name for score,name in ScombTable]
sortedScores=[score for score,name in ScombTable]


sortedNames=sortedNames[:100]
sortedScores=sortedScores[:100]




combTable=zip(authorScoresCopy,authorScores2)
ScombTable=sorted(combTable, reverse=True)
sortedScores2=[name for score,name in ScombTable]
sortedScoresCopy=[score for score,name in ScombTable]

SortedScores2=sortedScores2[:100]





#checking for possible* coauthors
pco=[False]*len(sortedNames)


for j in range(len(sortedNames)):
    for i in range(len(coList)):
        if((sortedNames[j] in coList[i]) or (coList[i] in sortedNames[j])):
            pco[j]=True











#prostheto apotelesmata algorithmou(keyword score kai koina sinedria)

author_entries=[]#o pinakas aftos tha periexi ta koina tou kathe author me afton pou psaxnoume

pinakas_test_list=[]


for i in range(len(aname63)):
    pintest=df1[df1['author']==aname63[i]].copy()
    pinakas_test_list=pinakas_test_list + pintest.loc[:, "journal"].values.tolist()

pinakas_test_list = list(dict.fromkeys(pinakas_test_list))#delete duplicates




for i in range(len(sortedNames)):
    author_entries.append(((df1[df1['author']==sortedNames[i]].copy()).loc[:,["journal", "ratings"]]).values.tolist())


    # print("before removing: "+str(author_entries[i])+"\n")


    itemstoremove=[]

    for j in range(len(author_entries[i])):
        if(not(author_entries[i][j][0] in pinakas_test_list)):
            itemstoremove.append(author_entries[i][j])


    
    for k in range(len(itemstoremove)):
        author_entries[i].remove(itemstoremove[k])

    # print("after removing: "+str(author_entries[i])+"\n\n\n\n\n")













timeAtEnd=time.time()-timeAtStart



freslist.append(sortedNames)
freslist.append(sortedScores)
freslist.append(sortedScores2)
freslist.append(author_entries)
freslist.append(pco)
freslist.append(timeAtEnd)




print(json.dumps(freslist))

# final_result=""

# for i in range(len(freslist[0])):
#     for j in range(len(freslist)):
#         if(j==0):
#             if(pco[i]==True):
#                 final_result=final_result+"Name: "+str(freslist[j][i])+" (possible coauthor) | "
#             else:
#                 final_result=final_result+"Name: "+str(freslist[j][i])+" | "
#         elif(j==2):
#             final_result=final_result+"Number of common confernces: "+str(len(freslist[j][i]))
#         else:
#             final_result=final_result+"Keywords score: "+str(freslist[j][i])+" | "
#     final_result=final_result+"<br>"




# print(json.dumps(final_result))

