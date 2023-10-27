import pandas as pd
from pathlib import Path
import yagmail

relatorios = Path(r'Projeto\Relatorios')
gerentes = pd.read_csv(r'Projeto\Gerentes_E-mail.csv')

usuario = yagmail.SMTP(user='usuario@gmail.com', password='senha')

nome, email, setor = gerentes['Gerente'], gerentes['E-mail'], gerentes['Relatório']

#   Enviando o Relatório para cada setor correspondente
for i, arquivo in enumerate(relatorios.iterdir()):
    nome_arquivo = arquivo.name
    for relatorio in setor:
        if relatorio == nome_arquivo[:-4]:
            usuario.send(to=f'{email[i]}', subject=f'Relatório do arquivo: {relatorio}', contents=f'{nome[i]}, o Anexo do arquvio {relatorio}', attachments=f'{arquivo}')
