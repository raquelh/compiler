import pandas as pd
import sys
import numpy as np

class percorre(object):


    def percorrefita(self):
        for i in self.fita:
           percorreParse(i)

    def percorreParse(self, i):
       for k in self.parse.loc[0,:]:
           if k == i:
               print(k, i)
               print(k.index())

