#       Integração Python com Gmail

import yagmail
usuario = yagmail.SMTP(user='usuario@gmail.com', password='senha')
usuario.send(to='destinatario', subject='assunto', contents='conteúdo do E-mail')

# Para enviar para várias pessoas, insira uma lista de destinatarios

# Enviando E-mail com Anexo(s)
usuario.send(to='destinatario', subject='assunto', contents='conteúdo do E-mail', attachments='arquivo')

# Para enviar uma cópia oculta de um e-mail a um ou mais destinatários, você pode utilizar o parâmetro bcc ao enviar o e-mail com o Yagmail.


#       Personalizando o texto do E-mail

#   Com Python Normal

# Primeira Forma: -> Lista de frases
corpo_email = [
    'mensagem 1',
    'mensagem 2',
    'mensagem 3'
]
corpo_email = '\n'.join(corpo_email)

# Segunda Forma: -> String de várias linhas
corpo_email = """
mensagem 1
mensagem 2
mensagem 3
"""
usuario.send(to='destinatario', subject='assunto', contents= corpo_email)

#   Com HTML
corpo_email2 = """
<p><b>mensagem 1</b></p><p>mensagem 2</p><p>mensagem 3</p>
"""
usuario.send(to='destinatario', subject='assunto', contents= corpo_email2)