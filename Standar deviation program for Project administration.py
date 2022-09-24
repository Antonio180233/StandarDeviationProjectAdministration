#!/usr/bin/env python
# coding: utf-8

# In[30]:


lista_O = [2,2,2,2,1,2,2,2,2,2,2,2,1,1,1,2,2,5,11,5,10,1,15,5,5,5,3,2,6,6]
lista_P = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,7,11,5,11,2,21,6,5,5,5,5,7,7]
med_O = sum(listaO)/len(listaO)
med_P = sum(listaP)/len(listaP)

desv_O = []
desv_P = []

for i in listaO:
    x = (i - med_O)**2
    desv_O.append(x)
for j in listaP:
    y = (j - med_P)**2
    desv_P.append(y)
    
O = (sum(desv_O)/len(lista_O))**(1/2)
P = (sum(desv_P)/len(lista_P))**(1/2)

SD = (P-O)/6
print("La desviación estándar con confianza del 68% es de", SD*.68)
print("La desviación estándar con confianza del 95% es de", SD*.95)
print("La desviación estándar con confianza del 99% es de", SD*.99)


# In[ ]:




