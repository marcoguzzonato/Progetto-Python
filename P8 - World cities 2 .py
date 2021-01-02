#!/usr/bin/env python
# coding: utf-8

# Il giro al mondo in 80 giorni: 

# Problema del percorso minimo in un grafo.
# 
# 3 città piu vicine
# 
# Pesi: 
#     2 ore
#     4 ore
#     8 ore
#     
#     2 ore se è un altra nazione
#     2 ore se ha + di 200k abitanti. 
#     
# Calcolare il tempo minimo del viaggio. 
# 
# librerie per gestire grafi e reti, capire algoritmo e implemetarlo, altre librerie... 

# In[55]:


import numpy as np
import pandas as pd
import math as m
from collections import defaultdict
import heapq
import itertools


# In[8]:


file = 'italiancities.xlsx'
cities = pd.read_excel(file, index_col = 'id')


# In[9]:


cities.head(4)


# In[10]:


cities.dtypes


# In[11]:


cities.index[1:4]


# In[12]:


cities.city_ascii[:2]


# In[21]:


def dist2punti2(k, o):
    Rt=6378.388
    lat_A=(m.pi*k[0])/180
    lat_B=(m.pi*o[0])/180
    lon_A=(m.pi*k[1])/180
    lon_B=(m.pi*o[1])/180
    dl=abs(lon_A-lon_B)
    p = m.acos((m.sin(lat_B)*m.sin(lat_A))+(m.cos(lat_B)*m.cos(lat_A)*m.cos(dl)))
    if(lon_A>0 and lon_B>0): 
        if(lon_B > lon_A): 
            p=p
        else:
            p=2*m.pi-p
    if(lon_A<0 and lon_B<0): 
        if(lon_B > lon_A): 
            p=p
        else:
            p=2*m.pi-p
    if(lon_A>0 and lon_B<0):
        if((lon_A+abs(lon_B))<m.pi): 
            p=2*m.pi-p
        else:
            p=p
    if(lon_A<0 and lon_B>0):
        if((lon_B+abs(lon_A))<m.pi): 
            p=p
        else:
            p=2*m.pi-p
    return(p*Rt)


# In[22]:


lat = [c for c in cities.lat]
lng = [c for c in cities.lng]
cit = [c for c in cities.city_ascii] #nodes
id_cit = [c for c in cities.index] #per creare table con indici unici


# In[23]:


dict_coordinates= {i:[j, k] for i, j, k in zip(cit, lat, lng)}


# In[24]:


dict_coordinates['Rome'] 


# In[25]:


dict_coordinates.keys()


# In[26]:


dict_coordinates.values()


# In[29]:


Z = [_ for _ in dict_coordinates.keys()]


for a, k in  dict_coordinates.items():
    for b, o in  dict_coordinates.items():
        if a == b:
            pass
        else:
            dist2punti2(k, o)
            print (a, '-', b, ':', dist2punti2(k, o))

#print(Z)


# In[30]:


I = defaultdict(lambda: defaultdict(lambda: 0))
for a, k in  dict_coordinates.items():
    for b, o in  dict_coordinates.items():
        if a == b:
            pass
        else:
            I[a][b] = dist2punti2(k, o)
I = pd.DataFrame(I).T
I.fillna(0, inplace=True)


# In[31]:


I.head() #da leggere da riga a colonna  ??


# In[35]:


I[:1][:]


# In[58]:


three_closest = defaultdict(lambda: defaultdict(lambda: 0))
for a, k in  dict_coordinates.items():
    for b, o in  dict_coordinates.items():
        if a == b:
            pass
        else:
            dist2punti2(k, o)
            three_closest[a][b] = dist2punti2(k, o)


# In[59]:


three_closest


# In[60]:


ordered_by_distance = {k:dict(sorted(v.items(), key=lambda item: item[1])) for k,v in sorted(three_closest.items())}


# In[61]:


ordered_by_distance


# In[57]:


for q, w in ordered_by_distance.items():
     for t, y in (itertools.islice(ordered_by_distance.items(), 3)):
             print(q, t)


# In[43]:


for index, row in I.head(n=1).iterrows():
    print('From: ',index, 'To:\\n',row)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[44]:


closest_cities = I.apply(lambda x: heapq.nsmallest(4, x), axis=1)


# In[45]:


closest_cities = I.apply(lambda x: heapq.nsmallest(4, x), axis=1)


# In[46]:


closest_cities_df = pd.DataFrame(closest_cities.values.tolist())


# In[47]:


closest_cities_df 


# In[56]:


Y = np.argmin(I, axis=1, shape(1, -1), out=None)


# In[ ]:





# In[49]:


# Initialize dictionary 
test_dict = {'gfg' : 1, 'is' : 4, 'best' : 6, 'for' : 7, 'geeks' : 3 } 
  
# Initialize K 
K = 2
  
# printing original dictionary 
print("The original dictionary is : " + str(test_dict)) 
  
# Smallest K values in Dictionary 
# Using nsmallest 
res = nsmallest(K, test_dict, key = test_dict.get) 
  
# printing result 
print("The minimum K value pairs are " + str(res)) 


# In[50]:


c = 3
for c, p in 
close = nsmallest(3, test_dict, key = test_dict.get)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[32]:


cities = [_ for _ in cit]
M = pd.DataFrame(np.zeros((len(cit), len(cit))), index= cities, columns= cities)


# In[215]:


dict_distances


# In[43]:


M.loc['Rome']['Rome']


# In[44]:


M['Rome']['Rome']


# In[45]:


M.iloc[0][0] = 2

