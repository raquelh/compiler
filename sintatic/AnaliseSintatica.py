import pandas as pd
import sys
import numpy as np
#from percorre import percorre
#from Tabela import Tabela

'''class AnaliseSintatica(object):
    """ Classe de Implementação da etapa de Análise Sintática
    """

    tabela = Tabela()
    fita = np.array(self.tabela)
    fita = fita[:,0]
    


    fita = ['129' '112' '69' '127' '69' '76' '130' '114' '69' '133' '73' '131' '69'
    '112' '58' '69' '127' '69' '76' '128' '124' '69' '132' '69' '127' '69'
    '76']
    parse = pd.read_csv('tableParse.csv')

    index = percorre()
    def __init__(self, *args):
        super(AnaliseSintatica, self).__init__(*args)
        self.fita = fita
        self.parse = parse
        self.index = index

    if __name__ == '__main__':
        self.index.percorrefita()
        #main()  '''
    

    #print(parse.shape)
    #print(parse.loc[0,:].shape)
    #index = percorre()
    #print(parse.columns.values)
    #print(parse)
    #acao = parse
    #saltos = parse

    #print(acao.columns.values[:-5])
    #print(saltos.columns.values[-5:])
    
    #percorrefita()


def reduz():
    n_prod = np.genfromtxt('numeroProd.txt', dtype = 'str', delimiter='-')
    print(n_prod)

pilha = [0]
fita = ['129', '112',  '69', '127', '69', '76', '130', '114', '69', '133', '73', '131', '69',
    '112', '58', '69', '127', '69', '76', '128', '124', '69', '132', '69', '127', '69',
    '76']
parse = pd.read_csv('tableParse.csv')
state = 1