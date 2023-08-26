from tkinter import *
import os
from mysql import connector
from time import sleep
# Criando a janela de login

class LoginUser:
        
    try:
        connect = connector.connect(
            host='localhost',
            database='db_users',
            user='root',
            password='root'
        )

        if connect.is_connected():
            cursor = connect.cursor()

    except:
        print('NÃO FOI FEITA A CONEXÃO COM O BANCO DE DADOS')
        exit()

    def __init__(self):
        self.button_get_infos()
        self.main_login_window.mainloop()
        
    #Capturando as informações de entrada do usuário
    def passw_getter(self):
        
        passw_get = self.entry_passw_info.get()
        login_get = self.entry_user_info.get()

        get_users_registed = f'''SELECT login_user, password_user FROM db_users.tb_users_registed'''
        self.cursor.execute(get_users_registed)
        results_users = self.cursor.fetchall()
        
        for lines_get in results_users:
            if (lines_get[0], lines_get[1]) == (login_get, passw_get):
                self.alert_login()
                sleep(1)
                self.entry_passw_info.delete(0, END)
                self.entry_user_info.delete(0, END)
                break
            else:
                ...


    def alert_login(self):
        sucess_login = Label(self.main_login_window, text='Login Efetuado Com Sucesso...', bg='#faf8f7')
        sucess_login.place(x=150, y=28)


    #Configurações da janela de login
    CAMINHO_ARQUIVO = os.path.dirname(__file__)

    main_login_window = Tk()
    main_login_window.title('Sistema de Cadastro de Usuários')
    main_login_window.geometry('450x350')
    main_login_window.config(bg='#faf8f7')
    main_login_window.iconphoto(False, PhotoImage(file=CAMINHO_ARQUIVO+r"\icons\login.png"))
    main_login_window.resizable(width=False, height=False)
    
    #Configurações de imagem da tela de login
    img_user = PhotoImage(file=CAMINHO_ARQUIVO+r"\icons\user.png")
    label_user = Label(main_login_window, image=img_user, bg='#faf8f7')
    label_user.place(x=190, y=50)

    #Criando os Labels de Texto
    login_user = Label(main_login_window, width=10, height=1, text='Login', font=('Arial 8 bold'), fg='black', bg='#faf8f7')
    login_user.place(x=70, y=125)

    login_passw = Label(main_login_window, width=10, height=1, text='Senha', font=('Arial 8 bold'), fg='black', bg='#faf8f7')
    login_passw.place(x=70, y=180)

    #Criando as entradas de informação do usuário
    entry_user_info = Entry(main_login_window, width=35, font=('Arial 11'), bg='gray', fg='white')
    entry_user_info.place(x=90, y=150)

    entry_passw_info = Entry(main_login_window, width=35, font=('Arial 11'), bg='gray', fg='white', show='*')
    entry_passw_info.place(x=90, y=204)

    #Chamando a o Button para inicialização
    def button_get_infos(self):
        #Criando Botão de entrada de dados do usuário para o sistema
        send_button = Button(self.main_login_window, command=self.passw_getter, width=34, height=2, text='Entrar', font=('Arial 10'), overrelief='groove', bg='blue', fg='white')
        send_button.place(x=91.5, y=260)

LoginUser()

