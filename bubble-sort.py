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
        plt.bar( i , alist )
        plt.show()
  

alist = np.random.randint(10, size = 1000)
print('----------------------------------------------------------')

array = [1,9,0,7,2,5,8,4]
bubleSort(array)
print(array)
  
