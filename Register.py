from tkinter import *
import os

class CreateAccount:

    CAMINHO_ARQUIVO = os.path.dirname(__file__)

    create_account_window = Tk()
    create_account_window.title('Sistema de Cadastro de Usuários')
    create_account_window.geometry('450x350')
    create_account_window.config(bg='#faf8f7')
    create_account_window.iconphoto(False, PhotoImage(file=CAMINHO_ARQUIVO+r"\icons\login.png"))
    create_account_window.resizable(width=False, height=False)

    def __init__(self):
        self.center(self.create_account_window)
        self.create_account_window.mainloop()

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

    