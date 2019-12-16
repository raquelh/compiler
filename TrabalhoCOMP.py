import sys

sys.path.append('./afd')
sys.path.append('./lex')
sys.path.append('./sintatic')

from Analisador import Analisador

analisador = Analisador()
analisador.analisar('./codigo.in') 
