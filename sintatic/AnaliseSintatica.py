import pandas as pd
import sys
import numpy as np
#from Tabela import Tabela

class AnaliseSintatica(object):
    """ Classe de Implementação da etapa de Análise Sintática
    """

    '''tabela = Tabela()
    fita = np.array(self.tabela)
    fita = fita[:,0]
    '''
    fita = ['129' '112' '69' '127' '69' '76' '130' '114' '69' '133' '73' '131' '69'
    '112' '58' '69' '127' '69' '76' '128' '124' '69' '132' '69' '127' '69'
    '76']
    parse = pd.read_csv('tableParse.csv')
    #print(parse.shape)
    print(parse.loc[0,:].shape)

    def __init__(self, *args):
        percorrefita()

    def percorrefita(self):
        for i in self.fita:
           percorreParse(i)

    def percorreParse(self, i):
       for k in self.parse.loc[0,:]:
           if k == i:
               print(k, i)

    #print(parse.columns.values)
    #print(parse)
    #acao = parse
    #saltos = parse

    #print(acao.columns.values[:-5])
    #print(saltos.columns.values[-5:])
    
    #percorrefita()