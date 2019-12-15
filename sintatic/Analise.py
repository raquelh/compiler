import pandas as pd
import sys
import numpy as np

def percorrefita(fita, parse, pilha, state):
        for i in fita:
            percorreParse(parse, i, state, pilha)

def quebra(prod, pilha, parse, i):
    print(prod)
    if prod.count('s'):
        #empilha
        state = prod.split('s')
        state = int(state[1])
        pilha.append(i)
        pilha.append(state)
        #return state
    elif prod.count('r'):
        state = prod.split('r')
        state = int(state[1])
        reduz(state, pilha, parse)
        pilha.append(i)
        #return state
    else:
        #print(prod)
        print(prod)
        state = int(prod)

def percorreState(estadoPilha, i, pilha, parse):
    quebra(estadoPilha, pilha, parse,i)
    #pilha.append(i)
    #pilha.append(state)


    '''state, emp = quebra(parse.iloc[state, aux])
    pilha.append(i)
    pilha.append(state)'''
    

#precisa rever a função 
def percorreParse(parse, i, state, pilha):
    m = 0
    for k in parse.loc[0,:]:
        if k == i:
            #print(k, i)
            aux = m
            break
        m += 1
    print(pilha)
    print('jesus', i, pilha[-1], aux)
    percorreState(parse.iloc[pilha[-1]+1, aux], i, pilha, parse)
    

    #print(aux+1)
    #print(state, aux)

    #state, emp = quebra(parse.iloc[state, aux])
    #print(state, aux)
    
    #print(pilha)

def salto(parse, aux, regra):
    return int(parse.loc[aux+1, regra])
    #print('regra que salta', parse.loc[aux+1, regra])


def reduz(state, pilha, parse):
    n_prod = np.genfromtxt('numeroProd.txt', dtype = 'str', delimiter='-')
    #print('n_prod', n_prod[state,2])
    #print('pilha ant', pilha)
    for i in range(int(n_prod[state,2])*2):
        del(pilha[-1])
    aux = pilha[-1]
    pilha.append(n_prod[state,1])
    #return salto(parse, aux, n_prod[state, 1])
    pilha.append(salto(parse, aux, n_prod[state, 1]))
    
    #print(n_prod)
    #print('depois', pilha)

pilha = [0]
fita = ['129', '112',  '69', '127', '69', '76', '130', '114', '69', '133', '73', '131', '69',
    '112', '58', '69', '127', '69', '76', '128', '124', '69', '132', '69', '127', '69',
    '76']
parse = pd.read_csv('tableParse.csv')
state = 1
print(parse)
#reduz()
percorrefita(fita, parse, pilha, state)
print(pilha)