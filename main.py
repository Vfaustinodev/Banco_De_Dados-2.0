from tkinter import *
import customtkinter
import keyboard
import os, sqlite3
from time import sleep
from PIL import ImageTk, Image

# Criando a janela de login
class LoginUser:
        
    PATH_FILE_DIR = os.path.dirname(__file__)

    try:
        connect = sqlite3.connect(PATH_FILE_DIR+'/users_registed.db')
        cursor = connect.cursor()

    except:
        print('NÃO FOI FEITA A CONEXÃO COM O BANCO DE DADOS')
        exit()

    def __init__(self):
        
        self.center(self.main_login_window)
        self.register_user()
        self.button_get_infos()
        self.main_login_window.mainloop()
        
    #Capturando as informações de entrada do usuário
    def passw_getter(self, event=None):
        
        passw_get = self.entry_passw_info.get()
        login_get = self.entry_user_info.get()

        self.cursor.execute(f'''SELECT login_user, password_user FROM tb_users_registed''')
        results_users = self.cursor.fetchall()
        
        for lines_get in results_users:
            if (lines_get[0], lines_get[1]) == (login_get, passw_get):
                sleep(1)
                self.entry_passw_info.delete(0, END)
                self.entry_user_info.delete(0, END)
                break
            else:
                ...

    def center(self, win):
        win.update_idletasks()

        width = win.winfo_width()
        frm_width = win.winfo_rootx() - win.winfo_x()
        win_width = width + 2 * frm_width

        height = win.winfo_height()
        titlebar_height = win.winfo_rooty() - win.winfo_y()
        win_height = height + titlebar_height + frm_width

        x = win.winfo_screenwidth() // 2 - win_width // 2
        y = win.winfo_screenheight() // 2 - win_height // 2

        win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

        win.deiconify()

    #Configurações da janela de login
    PATH_FILE_DIR = os.path.dirname(__file__)

    customtkinter.set_appearance_mode('system')
    customtkinter.set_default_color_theme('green')

    main_login_window = customtkinter.CTk()
    main_login_window.title('Painel de Login')
    main_login_window.geometry('600x440')
    main_login_window.iconbitmap(PATH_FILE_DIR+"/icons/login.ico")
    main_login_window.eval('tk::PlaceWindow . center')

    image_background= customtkinter.CTkImage(Image.open(PATH_FILE_DIR+"./icons/background.jpg"), size=(1366, 768))
    background_image = customtkinter.CTkLabel(master=main_login_window, image=image_background)
    background_image.pack()

    frame=customtkinter.CTkFrame(master=main_login_window, width=380, height=320, corner_radius=15, bg_color='black')
    frame.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

    label_welcome = customtkinter.CTkLabel(master=frame, text='Seja Bem Vindo(a)', font=('Century Gotic', 20))
    label_welcome.place(x=112, y=50)

    #Criando as entradas de informação do usuário
    entry_user_info = customtkinter.CTkEntry(master=frame, width=250, border_color='#82817e', placeholder_text='Usuário')
    entry_user_info.place(x=70, y=120)

    entry_passw_info = customtkinter.CTkEntry(master=frame, width=250, border_color='#82817e', show='*', placeholder_text='Senha')
    entry_passw_info.place(x=70, y=170)

    #Indo para janela de cadastro
    def window_register(self):
        
        from Register import CreateAccount
        CreateAccount()

    #Botão para se cadastrar
    def register_user(self):

        register_account = customtkinter.CTkButton(master=self.frame, command=self.window_register, width=10, height=1, font=('Century Gotic', 12), text='Criar conta', fg_color='transparent', hover_color='gray')
        register_account.place(x=255, y=209)

    #Chamando a o Button para inicialização
    def button_get_infos(self):
        #Criando Botão de entrada de dados do usuário para o sistema
        send_button = customtkinter.CTkButton(master=self.frame, command=self.passw_getter, width=200, height=38, font=('Arial', 15), corner_radius=7, text='Login', fg_color='#0f9633')
        send_button.place(x=91.5, y=240)
        self.entry_passw_info.bind('<Return>', self.passw_getter)

if __name__ == '__main__':
    LoginUser()
