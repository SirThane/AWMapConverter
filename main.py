import tkinter as tk
import awmap
from tkinter import filedialog


class GUI:
    def __init__(self):
        self.awmap = None
        self.root = tk.Tk()

        self.menubar = tk.Menu(self.root)

        self.file_menu = tk.Menu(self.menubar)
        self.menubar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open from AWS File", command=self.open_from_aws)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.quit)

        self.root.config(menu=self.menubar)

        self.root.mainloop()

    def open_from_aws(self):
        try:
            with tk.filedialog.askopenfile(mode="rb", filetypes=[("AWS Map Editor Files", "*.aws")]) as in_file:
                self.awmap = awmap.AWMap(in_file.read(), "AWS")
        except AttributeError:
            pass

    def quit(self):
        self.root.quit()


if __name__ == "__main__":
    window = GUI()
