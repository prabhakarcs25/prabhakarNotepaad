from tkinter import *
from tkinter import filedialog, messagebox, colorchooser


class MyNotepad:
    current_file = "no-file"

    def change_backcolor(self):
        c = colorchooser.askcolor()
        self.txt_area.configure(background=c[1])

    def change_forecolor(self):
        c = colorchooser.askcolor()
        self.txt_area.configure(foreground=c[1])

    def exit_file(self):
        s = self.txt_area.get(1.0, END)
        if not s.strip():
            quit()
        else:
            result = messagebox.askyesnocancel(
                "save dialog box", "Do You Want To Save This File Yes,No,Cancel")
            if result == True:
                self.saveas_file()

            elif result == False:
                self.clear()

    def clear(self):
        self.txt_area.delete(1.0, END)

    def new_file(self):
        s = self.txt_area.get(1.0, END)
        if not s.strip():
            pass
        else:
            result = messagebox.askyesnocancel(
                "save dialog box", "Do You Want To Save This File Yes,No,Cancel")
            if result == True:
                self.saveas_file()

            elif result == False:
                self.clear()

    def saveas_file(self):
        f = filedialog.asksaveasfile(mode="w", defaultextension="*.txt")
        data = self.txt_area.get(1.0, END)
        f.write(data)
        self.current_file = f.name
        f.close()

    def save_file(self):
        if self.current_file == "no-file":
            self.saveas_file()
        else:
            f = open(self.current_file, mode="w")
            f.write(self.txt_area.get(1.0, END))
            f.close()

    def open_file(self, event=""):
        result = filedialog.askopenfiles(initialdir="E:\ALL", title="Open File dialog",
                                         filetypes=(("Text File", "*.txt"), ("All File", "*.*")))
       # print(result)
        for data in result:
            self.txt_area.insert(INSERT, data)
        self.current_file = result.name

    def copy_file(self):
        self.txt_area.clipboard_clear()
        self.txt_area.clipboard_append(self.txt_area.selection_get())

    def paste_file(self):
        self.txt_area.insert((INSERT, self.txt_area.clipboard_get()))

    def cut_file(self):
        self.copy_file()
        self.txt_area.delete('sel', 'first', 'sel.last')

    def del_file(self):
        self.copy_file()
        self.txt_area.delete('sel', 'first', 'sel.last')

    def __init__(self, master):
        self.master = master
        master.title("My Note Pad")

        master.wm_iconbitmap("notepad.ico")
        master.bind("<control-o>,self.open_file")
        master.bind("<control-O>,self.open_file")
        self.txt_area = Text(master, padx=5, pady=5, wrap=WORD,
                             selectbackground="green", bd=2, insertwidth=7, undo=True)
        self.txt_area.pack(fill=BOTH, expand=1)
        self.main_menu = Menu()
        self.master.config(menu=self.main_menu)

        self.file_menu = Menu(self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label="FILE", menu=self.file_menu)
        self.file_menu.add_command(
            label="New", accelerator="ctrl+n", command=self.new_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(
            label="Open", accelerator="ctrl+o", command=self.open_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(
            label="Save", accelerator="ctrl+s", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(
            label="Save As", accelerator="ctrl+d", command=self.saveas_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(
            label="Exit", accelerator="ctrl+x", command=self.exit_file)

######################################################################################################

        self.edit_menu = Menu(self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label="EDIT", menu=self.edit_menu)
        self.edit_menu.add_command(
            label="undo", command=self.txt_area.edit_undo)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(
            label="Redu", command=self.txt_area.edit_redo)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="cut", command=self.cut_file)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="copy", command=self.copy_file)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="paste", command=self.paste_file)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="delete", command=self.del_file)

        ##############################################################################################

        self.color_menu = Menu(self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label="COLOR", menu=self.color_menu)
        self.color_menu.add_command(
            label="Background color", command=self.change_backcolor)

        self.color_menu.add_command(
            label="Fore ground Color", command=self.change_forecolor)


root = Tk()

b = MyNotepad(root)
root.mainloop()
