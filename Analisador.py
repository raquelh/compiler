from lex.AnaliseLexica import AnaliseLexica
import sintatic.Analise as AnaliseSintatica
import numpy as np
import pandas as pd


class Analisador(object):
    """ Classe geral de gerenciamento das etapas de compilação

        Implementa as seguintes funcionalidades do projeto:
        + Análise léxica
    """

    lexico = AnaliseLexica()
    sintatico = AnaliseSintatica


    def __init__(self, *args):
        super(Analisador, self).__init__(*args)


    def analiselexica(self, codigo):
        """ Executa a análise léxica

            :param codigo: path do código fonte para análise
        """
        self.lexico.analise(codigo)


    def analisar(self, codigo):
        """ Método que chama os métodos das etapas de análise
            do código fonte.

            :param codigo: path do código fonte para análise
        """
        self.analiselexica(codigo)
        self.analisesintatica()

    def analisesintatica(self):
        pilha = [0]
        fita = list(np.array(self.lexico.tabela)[:,0])
        del(fita[-1])
        parse = pd.read_csv('sintatic/tableParse.csv')
        state = 1
        print(parse)
        AnaliseSintatica.percorrefita(fita, parse, pilha, state)
