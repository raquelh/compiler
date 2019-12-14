import pandas as pd
import sys
import numpy as np

def percorrefita(fita, parse, pilha, state):
        #state = 1
        #print(parse.loc[1,:])
        for i in fita:
            percorreParse(parse, i, state, pilha)

def quebra(prod):
    print(prod)
    if prod.count('s'):
        #empilha
        state = prod.split('s')
        state = int(state[1])
        return state, prod
    elif prod.count('r'):
        reduz = prod.split('r')
        state = int(state[1])
        return state, prod
    else:
        state = prod
        return state, prod
    #elif prod.count('r'):
        #reduz = prod.split('r')
        #função que reduz 

#precisa rever a função 
def percorreParse(parse, i, state, pilha):
    m = 0
    for k in parse.loc[0,:]:
        #print(k, i)
        if k == i:
            aux = m
            #break
            print(state)
            state, emp = quebra(parse.iloc[state, aux+1])
            #print(aux)
            #empilha
            pilha.append(i)
            pilha.append(emp)
    #print(pilha)
    percorrefita(fita, parse, pilha, state)
    #print(parse.iloc[state, aux+1])
def reduz():
    n_prod = np.genfromtxt('numeroProd.txt', dtype = 'str', delimiter='-')
    print(n_prod)

pilha = [0]
fita = ['129', '112',  '69', '127', '69', '76', '130', '114', '69', '133', '73', '131', '69',
    '112', '58', '69', '127', '69', '76', '128', '124', '69', '132', '69', '127', '69',
    '76']
parse = pd.read_csv('tableParse.csv')
print(parse)
reduz()
percorrefita(fita, parse, pilha, 1)