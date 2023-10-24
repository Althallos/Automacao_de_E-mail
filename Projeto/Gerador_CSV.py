import pandas as pd
from pathlib import Path

#       Gerador de Arquivos CSV

#   OBS: Caso de erro de arquivo Insira o caminho do arquivo

# Criando a pasta Relatorios
pasta_relatorio = Path(r'Projeto/Relatorios').mkdir()

# Cria o CSV Gerentes_E-mail.csv

lista = {'Gerente':['Maria', 'Lira', 'Guilherme', 'Pedro', 'Júlia', 'Larrisa', 'Sabrina'],
         'E-mail':['user+1@gmail.com', 'user+2@gmail.com', 'user+3@gmail.com', 'user+4@gmail.com', 'user+5@gmail.com', 'user+6@gmail.com', 'user+7@gmail.com'],
         'Relatório':['Financeiro', 'Logística', 'Manuntenção', 'Marketing', 'Operações', 'Produtos', 'Vendas']}
arquivo = pd.DataFrame(lista)
arquivo.to_csv(r'Projeto/Gerentes_E-mail.csv', index=False)

relatorio_csv = pd.DataFrame()
# Cria arquivos CSV para cada relatório
for relatorio in arquivo["Relatório"]:
    relatorio_csv.to_csv(r'Projeto/Relatorios/{}.csv'.format(relatorio))