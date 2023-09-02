from tkinter.ttk import *
import customtkinter
from datetime import datetime
from tkinter import *
from mysql.connector import connect
import os

class CreateAccount:

    ANO_ATUAL = 2023
    CAMINHO_ARQUIVO = os.path.dirname(__file__)

    try:
        connected = connect(
            host='localhost',
            database='db_users',
            user='root',
            password='root'
        )

        if connected.is_connected():
            cursor = connected.cursor()
    except:
        exit()


    def __init__(self):

        self.create_gender()
        self.button_register()
        self.labels_infos()
        self.entry_infos()
        self.center(self.create_account_window)
        self.create_account_window.mainloop()

    country_add = []
    with open(CAMINHO_ARQUIVO + './files/country.txt', 'r', encoding='utf8') as country_entry:

        for indice in country_entry.readlines():
            formatin_country = indice.strip('\n')
            country_add.append(formatin_country)

    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('dark-blue')

    create_account_window = customtkinter.CTk()
    create_account_window.title('Sistema de Cadastro de Usuários')
    create_account_window.geometry('600x550')
    create_account_window.config(bg='#faf8f7')
    create_account_window.iconbitmap(CAMINHO_ARQUIVO+r'./icons/login.ico')
    create_account_window.resizable(width=False, height=False)

    # Adicionando os paises ao Combobox
    combo_country = Combobox(create_account_window)
    combo_country['values'] = country_add
    combo_country.current(30)
    combo_country.place(x=261, y=184)


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

    def labels_infos(self):

        self.label_login = Label(self.create_account_window, width=20, height=1, text='Nome de usuário', bg='#faf8f7')
        self.label_login.place(x=130, y=25)
        
        self.label_password = Label(self.create_account_window, width=20, height=1, text='Crie uma senha', bg='#faf8f7')
        self.label_password.place(x=124, y=75)

        self.label_age = Label(self.create_account_window, width=20, height=1, text='Digite sua idade', bg='#faf8f7')
        self.label_age.place(x=125, y=125)

        self.label_country = Label(self.create_account_window, width=15, height=1, text='Selecione o País', bg='#faf8f7')
        self.label_country.place(x=143, y=184)

        self.label_cpf = Label(self.create_account_window, width=20, height=1, text='Digite seu CPF', bg='#faf8f7')
        self.label_cpf.place(x=122, y=215)

        self.label_email = Label(self.create_account_window, width=20, height=1, text='Digite seu e-mail', bg='#faf8f7')
        self.label_email.place(x=128, y=266)

        self.label_gender = Label(self.create_account_window, width=20, height=1, text='Gênero', bg='#faf8f7')
        self.label_gender.place(x=103, y=320)

    def entry_infos(self):
        
        self.entry_login = Entry(self.create_account_window, width=40, font=('Arial 11'), bg='#faf8f7', relief='raised')
        self.entry_login.place(x=155, y=50)

        self.entry_password = Entry(self.create_account_window, width=40, font=('Arial 11'), bg='#faf8f7', relief='raised')
        self.entry_password.place(x=155, y=100)

        self.entry_age = Entry(self.create_account_window, width=40, font=('Arial 11'), bg='#faf8f7', relief='raised')
        self.entry_age.place(x=155, y=150)

        self.entry_cpf = Entry(self.create_account_window, width=40, font=('Arial 11'), bg='#faf8f7', relief='raised')
        self.entry_cpf.place(x=155, y=240)

        self.entry_email = Entry(self.create_account_window, width=40, font=('Arial 11'), relief='raised', bg='#faf8f7')
        self.entry_email.place(x=155, y=290)

    def button_register(self):

        button_register = customtkinter.CTkButton(master=self.create_account_window, command=self.recept_informations, width=150, height=30, text='Criar conta', cursor='hand2')
        button_register.place(x=152, y=400)

    def recept_informations(self):

        rec_hours = datetime.now()
        HOURS = rec_hours.hour
        MINUTES = rec_hours.minute
        SECONDS = rec_hours.second
        CAPTURE_HOUR = f'{HOURS:02}:{MINUTES:02}:{SECONDS:02}'

        rec_entry_login = self.entry_login.get()
        rec_entry_passw = self.entry_password.get()
        rec_entry_age = self.entry_age.get()
        rec_combo_country = self.combo_country.get()
        rec_entry_cpf = self.entry_cpf.get()
        rec_entry_email = self.entry_email.get()
        rec_year_birthday = self.ANO_ATUAL - int(rec_entry_age)
        intercept_gender = f'{self.obtain_gender()}'

        SENDING_INFORMATIONS = f'''INSERT INTO db_users.tb_users_registed
        (login_user, password_user, age, country, year_of_birthday, cpf_user, email_user, registed_hour, gender_user) 
        VALUE ('{str(rec_entry_login)}', '{str(rec_entry_passw)}', '{int(rec_entry_age)}', '{str(rec_combo_country)}',
        '{int(rec_year_birthday)}', '{str(rec_entry_cpf)}', '{str(rec_entry_email)}', '{str(CAPTURE_HOUR)}', '{str(intercept_gender)}')
'''
        self.cursor.execute(SENDING_INFORMATIONS)
        self.connected.commit()

        self.entry_login.delete(0, END)
        self.entry_password.delete(0, END)
        self.entry_age.delete(0, END)
        self.combo_country.current(30)
        self.entry_cpf.delete(0, END)
        self.entry_email.delete(0, END)

    def obtain_gender(self):
        rec_gender = self.selection_gender.get()
        return rec_gender

    # Gêneros opções
    def create_gender(self):

        self.selection_gender = StringVar()

        gender_male = Radiobutton(self.create_account_window, command=self.obtain_gender, text='Masculino', value='Masculino', bg='#faf8f7', cursor='hand2', variable=self.selection_gender)
        gender_male.place(x=150, y=350)

        gender_female = Radiobutton(self.create_account_window, command=self.obtain_gender, text='Feminino', value='Feminino', bg='#faf8f7', cursor='hand2', variable=self.selection_gender)
        gender_female.place(x=250, y=350)

        gender_others = Radiobutton(self.create_account_window, command=self.obtain_gender, text='Outros', value='Outros', bg='#faf8f7', cursor='hand2', variable=self.selection_gender)
        gender_others.place(x=350, y=350)


CreateAccount()
    