#!/usr/bin/env python
# coding: utf-8

# In[17]:


import numpy as np

with open('benzene.xyz') as b:
    
    for line in b:
    
        raw = list(b)
                    
        del(raw[0])
        

    for i in range(len(raw)):
        
        raw[i] = str(raw[i]).split('     ')
        
        
        for j in range(1,4):
            
            raw[i][j] = float(raw[i][j])
            #print(raw[i][j])
            
#print(raw)

for k in range(0, (len(raw))):
    
    for l in range(1, len(raw)):
        
        if k == l:
            
            continue
            
        else:
            
            x = raw[l][1] - raw[k][1]
            y = raw[l][2] - raw[k][2]
            z = raw[l][3] - raw[k][3]
        
            dist = round(np.sqrt((x*x)+(y*y)+(z*z)), 3)
        
            print('The distance between atom', k, 'and atom', l, 'is', dist)


# In[ ]:




