#Buble sort é o algoritmo mais simples, porém menos eficiente.

#Cada elemento ds posição i será comparado com o elemento da posição i + 1
  # caso esse elemento (i) for maior que i + 1 eles trocam de lugar.

import numpy as np
import time 
import pandas as pd
import matplotlib.pyplot as plt

def bubleSort(alist):
  for passnum in range(len(alist)-1,0,-1):
    for i in range(passnum):
      
      if alist[i] > alist[i+1]:
        temp = alist[i]
        alist[i] = alist[i+1]
        alist[i+1] = temp
  

alist = np.random.randint(10, size = 100)
print(alist)
print('----------------------------------------------------------')
bubleSort(alist)
print(alist)
  
