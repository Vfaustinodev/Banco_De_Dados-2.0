import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *



class ConsultingDates:

    def __init__(self):
          self.body_of_program()
          self.center(self.root)
          self.root.mainloop()

    def body_of_program(self):
        self.root = tk.Tk()

        b1 = ttk.Button(self.root, text="Button 1", bootstyle=SUCCESS)
        b1.pack(side=LEFT, padx=5, pady=10)

        b2 = ttk.Button(self.root, text="Button 2", bootstyle=(INFO, OUTLINE))
        b2.pack(side=LEFT, padx=5, pady=10)

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

if __name__ == '__main__':
      ConsultingDates()