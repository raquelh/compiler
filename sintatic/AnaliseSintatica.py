import pandas as pd

parse = pd.read_csv('tabelaParse.csv')

print(parse.columns.values)

acao = parse
saltos = parse

print(acao.columns.values[:-5])
print(saltos.columns.values[-5:])