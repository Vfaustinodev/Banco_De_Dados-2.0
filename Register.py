from tkinter.ttk import *
import customtkinter
from datetime import datetime
from tkinter import *
from tkinter import messagebox
import sqlite3
import os, re
from time import sleep
import smtplib, email.message, random, string
from PIL import ImageTk, Image

class ValidateEntry:

    def validating_age_entry(self, age):
        num_age = '150'
        if age == '': return True

        try:
            value = int(age)
            value = str(age)
        except ValueError:
            return False
        return len(value) <= len(num_age) and int(value) <= 150
    
    def validating_cpf_entry(self, cpf):
        num = '9' * 11
        if cpf == '': return True

        try:
            value = int(cpf)
            value = str(cpf)
        except ValueError:
            return False
        
        return len(value) <= len(num)
    
    def limited_name_entry(self, name):
        num = '9' * 60
        if name == '': return True

        try:
            value = str(name)
        except ValueError:
            return False
        
        return len(value) <= len(num)

class CreateAccount(ValidateEntry):

    #Variaveis de flexibilidade
    CODE_GERATED = '******'
    rec_year_actual = datetime.now()
    ACTUAL_YEAR = rec_year_actual.year
    PATH_FILE = os.path.dirname(__file__)
    
    #Conexão com o Banco de Dados
    try:
        connected = sqlite3.connect(PATH_FILE+'/users_registed.db')
        cursor = connected.cursor()

    except:
        exit()

    #Função construtora sendo utilizada para alinhamento de funções e chamado de eventos dentro da janela.
    def __init__(self):

        self.validate_entry_age()
        self.create_gender()
        self.button_register()
        self.labels_infos()
        self.entry_infos()
        self.center(self.create_account_window)
        self.create_account_window.mainloop()

    # Método que faz a leitura do arquivo onde contém todos os paises do mundo e envia para uma lista que vai ser lida pelo ComboBox.
    country_add = []
    with open(PATH_FILE + './files/country.txt', 'r', encoding='utf8') as country_entry:

        for indice in country_entry.readlines():
            formatin_country = indice.strip('\n')
            country_add.append(formatin_country)

    #Escolhendo o estilo da janela.
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('dark-blue')

    #Criando a janela utilizando customtkinter.
    create_account_window = customtkinter.CTk()
    create_account_window.title('Sistema de Cadastro de Usuários')
    create_account_window.geometry('650x600')
    create_account_window.config(bg='#faf8f7')
    create_account_window.iconbitmap(PATH_FILE+'/icons/register.ico')
    create_account_window.resizable(width=False, height=False)

    # Adicionando os paises ao Combobox
    combo_country = Combobox(create_account_window)
    combo_country['values'] = country_add
    combo_country.current(30)
    combo_country.place(x=261, y=184)

    #Função responsável em fazer com que a janela do aplicativo inicie sempre no centro da tela.
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

    #Função responsável por sinalizar onde o usuário vai digitar determinada informação.
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
        self.label_gender.place(x=103, y=465)

        self.label_email_verify = Label(self.create_account_window, width=13, height=1, text='Código Recebido', bg='#faf8f7')
        self.label_email_verify.place(x=153, y=318)

        self.label_email_verify_code = Label(self.create_account_window, width=8, height=1, text='', bg='#faf8f7', font=('Arial 9'))
        self.label_email_verify_code.place(x=90, y=340)

        self.label_name = Label(self.create_account_window, width=12, height=1, text='Nome completo', bg='#faf8f7', font=('Arial 9'))
        self.label_name.place(x=156, y=365)

        self.label_phone_number = Label(self.create_account_window, width=15, height=1, text='Número de telefone', bg='#faf8f7', font=('Arial 9'))
        self.label_phone_number.place(x=156, y=415)

        self.label_passw_confirm = Label(self.create_account_window, width=15, height=1, text='', bg='#faf8f7', font=('Arial 9'))
        self.label_passw_confirm.place(x=240, y=75)

    #Função responsável por receber as informações digitadas pelo usuário.
    def entry_infos(self):
        
        self.entry_login = Entry(self.create_account_window, width=40, font=('Arial 11'), bg='#faf8f7', relief='raised')
        self.entry_login.place(x=155, y=50)

        text_password = StringVar()
        text_password.trace("w", lambda name, index, mode, text_password=text_password: self.callback_pass(text_password))
        self.entry_password = Entry(self.create_account_window, textvariable=text_password, width=40, font=('Arial 11'), bg='#faf8f7', relief='raised', show='*')
        self.entry_password.place(x=155, y=100)
        #text_password.trace("w", lambda name, index, mode, text_password=self.pass_entry: self.callback(text_password))

        self.entry_age = Entry(self.create_account_window, validate='key', validatecommand= self.validate_age, width=15, font=('Arial 11'), bg='#faf8f7', relief='raised')
        self.entry_age.place(x=155, y=150)

        self.entry_cpf = Entry(self.create_account_window, validate='key', validatecommand=self.validated_cpf, width=40, font=('Arial 11'), bg='#faf8f7', relief='raised')
        self.entry_cpf.place(x=155, y=240)

        self.entry_email = Entry(self.create_account_window, width=40, font=('Arial 11'), relief='raised', bg='#faf8f7')
        self.entry_email.place(x=155, y=290)

        self.entry_email_code = Entry(self.create_account_window, width=15, font=('Arial 11'), relief='raised', bg='#faf8f7')
        self.entry_email_code.place(x=155, y=340)

        self.entry_name = Entry(self.create_account_window, validate='key', validatecommand=self.validated_name, width=40, font=('Arial 11'), relief='raised', bg='#faf8f7')
        self.entry_name.place(x=155, y=390)

        self.entry_phone_number = Entry(self.create_account_window, width=40, font=('Arial 11'), relief='raised', bg='#faf8f7')
        self.entry_phone_number.place(x=155, y=440)

    def show_pass(self):

        self.entry_password['show'] = ''

    def button_register(self):
        
        #Criando botão de registro
        button_register = customtkinter.CTkButton(master=self.create_account_window, command=self.recept_informations, width=150, height=30, text='Criar conta', cursor='hand2', corner_radius=0)
        button_register.place(x=153, y=530)

        button_valid_cpf = customtkinter.CTkButton(master=self.create_account_window, command=self.cpf_validating, width=50, height=25, text='Verificar', cursor='hand2', corner_radius=0)
        button_valid_cpf.place(x=490, y=238)

        button_valid_nick = customtkinter.CTkButton(master=self.create_account_window, command=self.verify_nickname, width=50, height=25, text='Verificar', cursor='hand2', corner_radius=0)
        button_valid_nick.place(x=490, y=49)

        button_send_email = customtkinter.CTkButton(master=self.create_account_window, command=self.send_email, width=50, height=25, text='Enviar', cursor='hand2', corner_radius=20, bg_color='#faf8f7')
        button_send_email.place(x=490, y=288)

        button_show_pass = customtkinter.CTkButton(master=self.create_account_window, command=self.show_pass, width=50, height=25, text='Mostrar', cursor='hand2', corner_radius=20, bg_color='#faf8f7')
        button_show_pass.place(x=490, y=100)

        button_valid_email = customtkinter.CTkButton(master=self.create_account_window, command=self.verify_email, width=50, height=25, text='Confirmar', cursor='hand2', bg_color='#faf8f7', corner_radius=20)
        button_valid_email.place(x=285, y=337)

    #Função responsavél por receber e validar duas funções, função de Label e função de envio de dados ao Banco.
    def recept_informations(self):

        self.validating_all_dates()
        
        if self.counting_steps == 4:
            #Enviando os dados para o banco
            self.sending_dates()

            msg_sucess = f'Cadastro realizado com sucesso\nSeja Bem Vindo! {self.entry_login.get()}'
            messagebox.showinfo('Mensagem de boas vindas!', msg_sucess)
            #Timer para ver alterações
            sleep(1)
            self.label_confirmation['text'] = ''
            #Limpando as entradas, para facilitar a criação de uma nova conta.
            self.entry_login.delete(0, END)
            self.entry_password.delete(0, END)
            self.entry_age.delete(0, END)
            self.combo_country.current(30)
            self.entry_cpf.delete(0, END)
            self.entry_email.delete(0, END)
            self.entry_email_code.delete(0, END)
            self.entry_name.delete(0, END)
            self.entry_phone_number.delete(0, END)
            self.label_email_verify_code['text'] = ''
            self.label_passw_confirm['text'] = ''
            self.label_confirmation_user['text'] = ''
            
        else:
            pass

    def obtain_gender(self):
        rec_gender = self.selection_gender.get()
        return rec_gender
    # Criando as opções de gêneros
    def create_gender(self):

        self.selection_gender = StringVar()

        gender_male = customtkinter.CTkRadioButton(self.create_account_window, command=self.obtain_gender, text='Masculino', value='Masculino', cursor='hand2', variable=self.selection_gender, border_width_checked=6, border_width_unchecked=4, bg_color='#faf8f7', text_color='#000000', border_color='#000000', corner_radius=6, hover_color='#f54316', radiobutton_width=22, radiobutton_height=20)
        gender_male.place(x=155, y=490)

        gender_female = customtkinter.CTkRadioButton(self.create_account_window, command=self.obtain_gender, text='Feminino', value='Feminino', cursor='hand2', variable=self.selection_gender, border_width_checked=6, border_width_unchecked=4, bg_color='#faf8f7', text_color='#000000', border_color='#000000', corner_radius=6, hover_color='#f54316', radiobutton_width=22, radiobutton_height=20)
        gender_female.place(x=265, y=490)

        gender_others = customtkinter.CTkRadioButton(self.create_account_window, command=self.obtain_gender, text='Outros', value='Outros', cursor='hand2', variable=self.selection_gender, border_width_checked=6, border_width_unchecked=4, bg_color='#faf8f7', text_color='#000000', border_color='#000000', corner_radius=6, hover_color='#f54316', radiobutton_width=22, radiobutton_height=20)
        gender_others.place(x=375, y=490)

    def validate_cpf(self, cpf):
        
        cpf_formating = f"{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}"
        
        if not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf_formating):
            return False
        
        numbers = [int(digit) for digit in cpf_formating if digit.isdigit()]
        
        if len(numbers) != 11 or len(set(numbers)) == 1:
            return False
        
        # Validação do segundo dígito verificador:
        sum_of_products = sum(a*b for a, b in zip(numbers[0:9], range(10, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if numbers[9] != expected_digit:
            return False

        # Validação do segundo dígito verificador:
        sum_of_products = sum(a*b for a, b in zip(numbers[0:10], range(11, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if numbers[10] != expected_digit:
            return False
        
        return True

    def cpf_validating(self):

        rec_entry_cpf = self.entry_cpf.get()

        if self.validate_cpf(rec_entry_cpf) == True:
            self.label_verify()
            return True
        
        else:
            self.label_verify()
            self.label_confirmation['text'] = 'ERROR!'
            self.label_confirmation['fg'] = 'red'
            self.label_confirmation['width'] = 6
            self.label_confirmation.place(x=100, y=241)
            
    def label_verify(self):

        self.label_confirmation = Label(self.create_account_window, width=6, height=1, text='OK!', fg='green', bg='#faf8f7')
        self.label_confirmation.place(x=100, y=241)
            
    def sending_dates(self):
        #Capturando a data exata de registro.
        rec_date = datetime.now()
        DAY = rec_date.day
        MONTH = rec_date.month
        YEAR = rec_date.year
        CAPTURE_DATE = f'{DAY:02}/{MONTH:02}/{YEAR}'
        
        #Capturando o horário exato em que o registrado é feito.
        rec_hours = datetime.now()
        HOURS = rec_hours.hour
        MINUTES = rec_hours.minute
        SECONDS = rec_hours.second
        CAPTURE_HOUR = f'{HOURS:02}:{MINUTES:02}:{SECONDS:02}'

        #Capturando os dados de entrada dos metódos de entrada.
        rec_entry_login = self.entry_login.get()
        rec_entry_passw = self.entry_password.get()
        rec_entry_age = self.entry_age.get()
        rec_combo_country = self.combo_country.get()
        rec_entry_cpf = self.entry_cpf.get()
        rec_entry_email = self.entry_email.get()
        rec_year_birthday = self.ACTUAL_YEAR - int(rec_entry_age)
        intercept_gender = f'{self.obtain_gender()}'

        formating_cpf = f"{rec_entry_cpf[0:3]}.{rec_entry_cpf[3:6]}.{rec_entry_cpf[6:9]}-{rec_entry_cpf[9:11]}"

        #Enviando as informações obtidas na entrada para o banco de dados.
        self.cursor.execute(f'''INSERT INTO tb_users_registed
        (name_registed, phone_number, login_user, password_user, age, country, year_of_birthday, cpf_user, email_user, registed_hour, gender_user, registed_date) 
        VALUES ('{self.entry_name.get()}', '{self.entry_phone_number.get()}', '{str(rec_entry_login)}', '{str(rec_entry_passw)}', '{int(rec_entry_age)}', '{str(rec_combo_country)}',
        '{int(rec_year_birthday)}', '{str(formating_cpf)}', '{str(rec_entry_email)}', '{str(CAPTURE_HOUR)}', '{str(intercept_gender)}', '{str(CAPTURE_DATE)}')
        ''')
        #Confirmando o envio dos dados ao Banco de Dados.
        self.connected.commit()

    def verify_nickname(self):

        rec_entry_nick = self.entry_login.get()
        rec_nicks_only = '''SELECT login_user FROM tb_users_registed'''
        self.cursor.execute(rec_nicks_only)
        lines_obtained = self.cursor.fetchall()

        for lines_nicks in lines_obtained:

            if lines_nicks[0] == rec_entry_nick or rec_entry_nick == '':

                self.label_verify_user()
                self.label_confirmation_user['text'] = 'USUÁRIO INDISPONÍVEL!'
                self.label_confirmation_user['fg'] = 'red'
                return False
                
        self.label_verify_user()
        return True
             
    def label_verify_user(self):

        self.label_confirmation_user = Label(self.create_account_window, width=22, height=1, text='USUÁRIO DISPONÍVEL!', fg='green', bg='#faf8f7', font=('Times 8'))
        self.label_confirmation_user.place(x=255, y=26)

    def verify_email(self):
        
        rec_entry_email_code = self.entry_email_code.get()

        if rec_entry_email_code.upper() == self.CODE_GERATED:
            self.label_email_verify_code['text'] = 'OKAY!'
            self.label_email_verify_code['fg'] = 'green'
            return True
        else:
            self.label_email_verify_code['text'] = 'ERROR!'
            self.label_email_verify_code['fg'] = 'red'
            return False

    def code_generator(self):
        
        self.CODE_GERATED = ''
        count_pass = 3
        for index in range(count_pass):

            self.code_gerating_letter = random.choice(string.ascii_uppercase)
            self.code_gerating_number = random.randint(0,9)

            self.CODE_GERATED += self.code_gerating_letter
            self.CODE_GERATED += str(self.code_gerating_number)
    
    def send_email(self):

        self.code_generator()

        rec_entry_email = self.entry_email.get()

        body_email = f"""
        <h1>Ola! {self.entry_login.get()}<br/><br/> Vamos validar o seu e-mail de Cadastro no Sistema<br/></h1>
        <h1><br/>CODIGO: {self.CODE_GERATED}<br/></h1>
        """

        msg = email.message.Message()
        msg['Subject'] = "Código de Verificação"
        msg['From'] = 'sistemadecadastropy@gmail.com'
        msg['To'] = f'{rec_entry_email}'
        password = 'ninndxersjybahct' 
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(body_email)

        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()
        # Login Credentials for sending the mail
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))

    def validating_all_dates(self):

        self.counting_steps = 0

        #Validando CPF
        if self.cpf_validating() == True:
            self.counting_steps += 1
        else:
            self.entry_cpf.delete(0, END)

        #Validando NickName
        if self.verify_nickname() == True:
            self.counting_steps += 1
        else:
            self.entry_login.delete(0, END)

        #Validando o Código enviado para o E-mail
        if self.verify_email() == True:
            self.counting_steps += 1
        else:
            self.entry_email_code.delete(0, END)
        
        #Validando o Código enviado para o E-mail
        if self.password_response == True:
            self.counting_steps += 1
        else:
            self.entry_password.delete(0, END)

    def validate_entry_age(self):
        
        self.validate_age = (self.create_account_window.register(self.validating_age_entry), '%P')
        self.validated_cpf = (self.create_account_window.register(self.validating_cpf_entry), '%P')
        self.validated_name = (self.create_account_window.register(self.limited_name_entry), '%P')

    #Função responsável por validar a senha em tempo real
    def callback_pass(self, pass_entry):

        self.pass_entry = pass_entry
        validation_of_pass = re.compile(r'^(((?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%<^&*?])[a-zA-Z0-9!@#$%<^&*?]{8,})|([a-zA-Z]+([- .,_][a-zA-Z]+){4,}))$')
        
        if validation_of_pass.match(self.pass_entry.get()):
            self.label_passw_confirm['text'] = 'SENHA FORTE!'
            self.label_passw_confirm['fg'] = 'green'
            self.password_response = True
        else:
            self.label_passw_confirm['text'] = 'SENHA FRACA!'
            self.label_passw_confirm['fg'] = 'red'
            self.password_response = False

if __name__ == '__main__':
    CreateAccount()