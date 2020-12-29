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

# In[28]:


import numpy as np
import pandas as pd
import math as m


# In[29]:


def dist2punti(k):
    Rt=6378.388
    lat_A=(m.pi*k[0])/180
    lat_B=(m.pi*k[2])/180
    lon_A=(m.pi*k[1])/180
    lon_B=(m.pi*k[3])/180
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


# In[30]:


file = 'italiancities.xlsx'
cities = pd.read_excel(file, index_col = 'id')


# In[31]:


cities.head(4)


# In[5]:


cities.dtypes


# In[41]:


cities.index[1:4]


# In[6]:


cities.city_ascii[:2]


# In[43]:


lat = [c for c in cities.lat]
lng = [c for c in cities.lng]
cit = [c for c in cities.city_ascii] #nodes
id_cit = [c for c in cities.index] #per creare table con indici unici


# In[44]:


dict_distances= {i:[j, k] for i, j, k in zip(cit, lat, lng)}


# In[57]:


dict_distances['Rome'] 


# In[58]:


H = dist2punti(dict_distances['Milan'] +  dict_distances ['Rome']) #prova calcolo distanza 2 città


# In[59]:


H


# In[60]:


dict_distances.keys()


# In[61]:


dict_distances.values()


# In[62]:


cities = [_ for _ in cit]
M = pd.DataFrame(np.zeros((len(cit), len(cit))), index= cities, columns= cities)


# In[63]:


M


# In[124]:


def append_dict(cit):
    o ={}
    for i, a in enumerate(cit):
        for j, b in enumerate(cit):        
            k = [(dict_distances[a] + dict_distances[b])]
            p=  [dist2punti(k)]
            for key, val in dict_distances.items():
                if key in :
                dict_distances[a] = [dict_distances[a],k] 
    return dict_distances

for key,val in to_add.items():
    if key in d:
        d[key] = [d[key],val]


# In[133]:


for i, a in enumerate(cit):
    for j, b in enumerate(cit):        
        k = [(dict_distances[a] + dict_distances[b])]


# In[137]:


k


# In[138]:


[(dict_distances['Rome'] + dict_distances['Milan'])]


# In[139]:


create_dict(cit)


# In[140]:


dict_distances


# In[ ]:





# In[ ]:





# In[ ]:





# In[17]:


def fill ():
    cities = [_ for _ in cit]
    m = pd.DataFrame(np.zeros((len(cit), len(cit))), index= cities, columns= cities)
    for i, row in enumerate(cit):
        for j, col in enumerate(cit):
            k = [dist2punti(dict_distances[(M.iloc[[i]])] + dict_distances [M.iloc[[]][[col]]])            
            m.iloc[i-1:i] [M.columns[j-1:j]] = k
        return m
                 
#dobbiamo farlo con ID, no con nome della città.


# In[22]:


def fill(M):
    for i in range(len(cit)):
        for j in range(len(cit)):
            k = [dist2punti(dict_distances[(M.iloc[[i]])] + dict_distances [M.iloc[[]][[j]]])            
            M.iloc[i-1:i] [M.columns[j-1:j]] = k
        return M


# In[19]:


def fill ():
    cities = [_ for _ in cit]
    m = pd.DataFrame(np.zeros((len(cit), len(cit))), index= cities, columns= cities)
    for i, row in enumerate(cit):
        for j, col in enumerate(cit):
            k = [dist2punti(dict_distances[(M.iloc[[i]])] + dict_distances [M.iloc[[]][[j]]])            
            m.loc[row] [M.columns[col]] = k
        return m


# In[436]:


M.loc['Rome']['Rome']


# In[437]:


M['Rome']['Rome']


# In[438]:


M.iloc[0][0] = 2


# In[339]:


#M.apply(dist2punti(dict_distances[]), axis=0)


# In[ ]:





# In[ ]:




