
#Este algoritmo é baseado em se passar sempre o menor valor do vetor para a primeira posição 
# (ou o maior dependendo da ordem requerida),
# depois o segundo menor valor para a segunda posição e assim sucessivamente, até os últimos dois elementos. 

import numpy as np
import time 
import pandas as pd
import matplotlib.pyplot as plt

def selectionSort(alist):
  for fillslot in range(len(alist)-1, 0, -1):
    positionOfMax = 0
    for location in range(1, fillslot+1):
      if alist[location] > alist[positionOfMax]:
        positionOfMax = location
    
    temp = alist[fillslot]
    alist[fillslot] = alist[positionOfMax]
    alist[positionOfMax] = temp


alist = np.random.randint(100000, size = 100000)
print(alist)
print('-----------------------------')

selectionSort(alist)
print(alist)