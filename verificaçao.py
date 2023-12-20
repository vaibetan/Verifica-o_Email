#Aqui vamos fazer um sistema de login com verificaçao de email
import customtkinter as Ctk
import random
from email.message import EmailMessage
import ssl
import smtplib
import email.message


lista = []

def codigo():
    save_2 = Codigo_usuario.get()
    lista.append(save_2)
    if save_2 == unificado:
        Texto_Verficaçao.destroy()
        Texto_Verficaçao_2.destroy()
        Codigo_usuario.destroy()
        Botao_verificaçao.destroy()
        Parabens.place(x=100, y= 40)

def enviar_email():  
    save_1 = lista[0]
    global unificado
    
    corpo_email = f"""
    seu codigo é:
    {unificado}
    """

    msg = email.message.Message()
    msg['Subject'] = "Assunto"
    msg['From'] = 'treinerpython@gmail.com'
    msg['To'] = save_1
    password = 'uxo b hdwk en y v ycbq' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    


def Entrar():
    E = Email_usuario.get()
    S = Senha_usuario.get()
    lista.append(E)
    Texto_Login.destroy()
    Texto_Senha.destroy()
    Texto_Email.destroy()
    Email_usuario.destroy()
    Senha_usuario.destroy()
    Lembre_de_mim.destroy()
    Botao.destroy()
    Texto_Verficaçao.place(x=190, y=0)
    Texto_Verficaçao_2.place(x=50, y=40)
    Codigo_usuario.place(x=180, y= 40)
    Botao_verificaçao.place(x=180, y= 80)
    enviar_email()

afb = ['A', 'B', 'C', 'D', 'E', 'F']
num = ['1', '2' , '3', '4', '5', '6', '7', '8' ,'9' ,'10']
tudo_1 = afb + num

lista = []

str_aleatoria = random.sample(tudo_1, 5)
separador = ''
unificado = separador.join(list(str_aleatoria))

#criaçao da jenela 
root = Ctk.CTk()
root.title('Login')
root.geometry('500x300')


Texto_Login = Ctk.CTkLabel(root, text='Crie seu login', font=('circular', 17, 'bold'))
Texto_Login.place(x=190, y=0)

Texto_Email = Ctk.CTkLabel(root, text='Email:', font=('circular', 17, 'bold'))
Texto_Email.place(x=130, y=40)

Email_usuario = Ctk.CTkEntry(root, placeholder_text=('Seu email aqui'), width=210)
Email_usuario.place(x=180, y= 40)

Texto_Senha = Ctk.CTkLabel(root, text='Senha:', font=('circular', 17, 'bold'))
Texto_Senha.place(x=123, y=80)

Senha_usuario = Ctk.CTkEntry(root, placeholder_text=('Sua Senha aqui'), width=210, show='*')
Senha_usuario.place(x=180, y= 80)

Lembre_de_mim = Ctk.CTkCheckBox(root, text="Lembre de mim", height=5)
Lembre_de_mim.place(x=128, y= 120)

Botao = Ctk.CTkButton(root, text="confirmar", command= Entrar )
Botao.place(x=190, y= 150)

Texto_Verficaçao = Ctk.CTkLabel(root, text='verifique seu email', font=('circular', 17, 'bold') )

Texto_Verficaçao_2 = Ctk.CTkLabel(root, text='digite o codigo:', font=('circular', 17, 'bold') )

Codigo_usuario = Ctk.CTkEntry(root, placeholder_text=('codigo'), width=210)

Botao_verificaçao = Ctk.CTkButton(root, text="confirmar", command=codigo)

Parabens = Ctk.CTkLabel(root, text='login feito com sucesso!', font=('circular', 27, 'bold') )



root.mainloop()

