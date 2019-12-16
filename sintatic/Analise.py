import pandas as pd
import sys
import numpy as np
# from lex.AnaliseLexica import AnaliseLexica

def percorrefita(fita, parse, pilha, state):
        for i in fita:
            percorreParse(parse, i, state, pilha)

def quebra(prod, pilha, parse, i, aux):
    if prod.count('s'):
        #empilha
        state = prod.split('s')
        state = int(state[1])
        pilha.append(i)
        pilha.append(state)
    #reduz
    elif prod.count('r'):
        state = prod.split('r')
        state = int(state[1])
        reduz(state, pilha, parse)
        percorreState(parse.iloc[pilha[-1]+1, aux], i, pilha, parse, aux)

    elif prod == 'acc':
        print('linguagem aceita')
        for k in range(2):
            del(pilha[-1])
    elif prod == 0:
        print()
    else:
        print('Erro sintatico por conta de ', prod)

def percorreState(estadoPilha, i, pilha, parse, aux):
    quebra(estadoPilha, pilha, parse,i, aux)

def percorreParse(parse, i, state, pilha):
    m = int(0)
    for k in parse.loc[0,:]:
        if k == i:
            aux = m
            break
        m += 1
    print(pilha)
    percorreState(parse.iloc[pilha[-1]+1, aux], i, pilha, parse, aux)


def salto(parse, aux, regra):
    return int(parse.loc[aux+1, regra])


def reduz(state, pilha, parse):
    n_prod = np.genfromtxt('sintatic/numeroProd.txt', dtype = 'str', delimiter='-')
    for i in range(int(n_prod[state,2])*2):
        del(pilha[-1])
    aux = pilha[-1]
    pilha.append(n_prod[state,1])
    pilha.append(salto(parse, aux, n_prod[state, 1]))

