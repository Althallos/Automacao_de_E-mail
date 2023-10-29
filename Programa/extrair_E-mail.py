#   Informação sobre a biblioteca Imap
#IMAP Server:
#https://www.systoolsgroup.com/imap/

#imap_tools:
#https://github.com/ikvk/imap_tools/blob/master/README.rst

#       Extrair Informações de um E-mail
from imap_tools import MailBox, AND

# Entrando na conta
usuario = 'E-mail'
senha = 'Senha'
meu_email = MailBox('imap.gmail.com').login(usuario, senha)

# Pegar E-mail que foram enviados por um remetente específico
lista_emails = meu_email.fetch(AND(from_='Email do Remetente', to='Destinatario'))

print(len(list(lista_emails)))      # Quantos E-mail Existem com os critérios definidos
for msg in lista_emails:
    print(msg.subject)
    print(msg.text)

# Pegar Anexo de um E-mail
lista_emails = meu_email.fetch(AND(from_='Email do Remetente'))
for email in lista_emails:
    if len(email.attachments) > 0:
        for anexo in email.attachments:
            if 'Nome do Anexo' in anexo.filename:
                informacoes_anexo = anexo.payload
                with open('Nome do Arquivo', 'wb') as arquivo:
                    arquivo.write(informacoes_anexo)
