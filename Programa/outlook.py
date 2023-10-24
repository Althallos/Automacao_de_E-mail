#       Integração Python com Outlook

#   Funciona para qualquer E-mail: Corporativo, Gmail, Outlook, Hotmail, etc.
import win32com.client as win32

# Criar a Integração com o Outlook
outlook = win32.Dispatch('outlook.application')

# Criar um E-mail
email = outlook.CreateItem(0)

# Configurar as Informações do seu E-mail
email.To = 'destinatário'
email.Subject = 'assunto'
email.Body = 'Texto do E-mail'
# Ou mail.HTMLBody = "<p>Corpo do E-mail em HTML</p>"

# Enviando E-mail com Anexo(s)
#anexo = "Caminho do arquivo"
#email.Attachments.Add(anexo)

email.Send()