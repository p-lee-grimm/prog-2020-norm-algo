from tkinter import Tk, Frame, Menu


class Window (Frame):

    def __init__(self):
        super().__init__()
        self.Name()

    def Name (self):
        self.master.title("Работа нормального алгорифма")

        Toolbar = Menu(self.master)
        self.master.config(menu=Toolbar)

        Menulist = Menu(Toolbar)
        Menulist.add_command(label="Выход", command=self.Exit)
        Toolbar.add_cascade(label="Файл", menu=Menulist)

    def Exit(self):
        self.quit()


def main():
    root = Tk()
    root.geometry("1280x720")
    app = Window ()
    root.mainloop()


if __name__ == '__main__':
    main()