class Tabela(list):

    def __init__(self, *args):
        super(Tabela, self).__init__(*args)


    def reconhece(self, estado, linha, token):
        """ Insere na tabela de símbolos um estado reconhecido

            :param estado: Estado reconhecido
            :param linha: Linha onde o estado foi reconhecido
        """
   
        self.append((estado, linha, token))
