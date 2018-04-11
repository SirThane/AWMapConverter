import tkinter as tk
import os
import awmap
from tkinter import filedialog, messagebox
from tkinter import scrolledtext as sc


file_formats = {
    "txt": ("Plain Text File", "*.txt"),
    "csv": ("Comma-Separated Values (CSV)", "*.csv"),
    "aws": ("AWS Map Editor File", "*.aws"),
}


class GUI:
    def __init__(self):
        self.awmap = None
        self.root = tk.Tk()
        self.root.title("Advance Wars Map Converter v0.1b")
        self.root.wm_minsize(width=400, height=400)
        # self.root.wm_maxsize(width=500, height=250)

        # Menu Bar Items

        self.menubar = tk.Menu(self.root)

        self.file_menu = tk.Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open from AWS File...", command=self.open_from_aws)
        self.file_menu.add_command(label="Open from AWBW File...", command=self.open_from_awbw)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Save to AWS File...", command=self.save_to_aws)
        self.file_menu.add_command(label="Save to AWBW File...", command=self.save_to_awbw)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.quit)

        self.help_menu = tk.Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="Help", command=self.unimplemented)

        self.root.config(menu=self.menubar)

        # All the shit in the Header

        self.map_info_frame = tk.Frame(self.root, border=5)
        self.map_info_frame.grid(row=0, column=0, sticky=tk.W)

        # Map Meta Data Frame

        self.meta_frame = tk.Frame(self.map_info_frame)
        self.meta_frame.grid(row=0, column=0, sticky=tk.W)

        self.map_title = tk.Label(self.meta_frame, text="Title: ")
        self.map_title.grid(row=0, column=0, sticky=tk.E)
        self.map_title_value = tk.StringVar(name="map_title")
        self.map_title_value.trace_add("write", self.update_title)
        self.map_title_field = tk.Entry(self.meta_frame, state=tk.DISABLED, textvariable=self.map_title_value)
        self.map_title_field.grid(row=0, column=1)

        self.map_author = tk.Label(self.meta_frame, text="Author: ")
        self.map_author.grid(row=1, column=0, sticky=tk.E)
        self.map_author_value = tk.StringVar(name="map_author")
        self.map_author_value.trace_add("write", self.update_author)
        self.map_author_field = tk.Entry(self.meta_frame, state=tk.DISABLED, textvariable=self.map_author_value)
        self.map_author_field.grid(row=1, column=1)

        self.map_desc = tk.Label(self.meta_frame, text="Description: ")
        self.map_desc.grid(row=2, column=0, sticky=tk.E)
        self.map_desc_value = tk.StringVar(name="map_desc")
        self.map_desc_value.trace_add("write", self.update_desc)
        self.map_desc_field = tk.Entry(self.meta_frame, state=tk.DISABLED, textvariable=self.map_desc_value)
        self.map_desc_field.grid(row=2, column=1)

        # Map Analytics Frame

        self.map_analytic_frame = tk.Frame(self.map_info_frame)
        self.map_analytic_frame.grid(row=0, column=1, padx=5, sticky=tk.N)

        # Map Dimensions

        self.map_dimensions_frame = tk.Frame(self.map_analytic_frame)
        self.map_dimensions_frame.grid(row=0, column=0, columnspan=2, sticky=tk.N)

        self.map_dimensions_label = tk.Label(self.map_dimensions_frame, text="Dimensions")
        self.map_dimensions_label.grid(row=0, column=0, columnspan=3)

        self.map_size_w_value = tk.StringVar(name="map_size_w")
        # self.map_size_w_value.trace_add("write", self.unimplemented)
        self.map_size_w_field = tk.Entry(self.map_dimensions_frame, state=tk.DISABLED,
                                         textvariable=self.map_size_w_value, width=3)
        self.map_size_w_field.grid(row=1, column=0)

        self.map_dimensions_x_label = tk.Label(self.map_dimensions_frame, text="x")
        self.map_dimensions_x_label.grid(row=1, column=1, padx=1)

        self.map_size_h_value = tk.StringVar(name="map_size_h")
        # self.map_size_h_value.trace_add("write", self.unimplemented)
        self.map_size_h_field = tk.Entry(self.map_dimensions_frame, state=tk.DISABLED,
                                         textvariable=self.map_size_h_value, width=3)
        self.map_size_h_field.grid(row=1, column=2)

        # Map CSV Display

        self.map_frame = tk.Frame(self.root, border=5)
        self.map_frame.grid(row=1, column=0)

        self.map_csv = sc.ScrolledText(self.map_frame, wrap='word', state=tk.DISABLED, width=50, height=8)
        self.map_csv.grid(row=0, column=0)

        # Save Buttons

        self.bottom_buttons = tk.Frame(self.root, borderwidth=2)
        self.bottom_buttons.grid(row=2, column=0, sticky=tk.S)

    # Open File Dialog Methods

    def open_from_aws(self):
        try:
            with tk.filedialog.askopenfile(mode="rb", filetypes=[file_formats["aws"]]) as in_file:
                self.awmap = awmap.AWMap().from_aws(in_file.read())
            self.init_fields()
        except AttributeError:
            pass  # TODO: Add MessageDialog with Error details.

    def open_from_awbw(self):
        try:
            with tk.filedialog.askopenfile(mode="r", filetypes=[file_formats["txt"]]) as in_file:
                try:
                    title = os.path.splitext(in_file.name)[0]
                    title = os.path.basename(title)
                except Exception as e:
                    print(e)
                    self.root.quit()
                self.awmap = awmap.AWMap().from_awbw(in_file.read(), title=title)
            self.init_fields()
        except AttributeError:
            pass

    def init_fields(self):
        self.update_title_field(self.awmap.title)
        self.update_author_field(self.awmap.author)
        self.update_desc_field(self.awmap.desc)
        self.update_map_csv(self.awmap.to_awbw)
        self.update_map_size_w(self.awmap.size_w)
        self.update_map_size_h(self.awmap.size_h)

    # Save File Dialog Buttons

    def save_to_aws(self):
        try:
            with tk.filedialog.asksaveasfile(mode="wb", defaultextension=".aws",
                                             filetypes=[file_formats["aws"]]) as out_file:
                out_file.write(self.awmap.to_aws)
        except AttributeError:
            pass  # TODO: Add MessageDialog with Error details.

    def save_to_awbw(self):
        try:
            with tk.filedialog.asksaveasfile(mode="w", defaultextension=".txt",
                                             filetypes=[file_formats["txt"]]) as out_file:
                out_file.write(self.awmap.to_awbw)
        except AttributeError:
            pass  # TODO: Add MessageDialog with Error details.

    # Map Meta Data Update Methods

    def update_title(self, *args):
        self.awmap.title = self.map_title_value.get()

    def update_title_field(self, value=None):
        self.map_title_field.config(state=tk.NORMAL)
        self.map_title_value.set(value)

    def update_author(self, *args):
        self.awmap.author = self.map_author_value.get()

    def update_author_field(self, value=None):
        self.map_author_field.config(state=tk.NORMAL)
        self.map_author_value.set(value)

    def update_desc(self, *args):
        self.awmap.desc = self.map_desc_value.get()

    def update_desc_field(self, value=None):
        self.map_desc_field.config(state=tk.NORMAL)
        self.map_desc_value.set(value)

    # Update Map Analytics Methods

    def update_map_size_w(self, w):
        self.map_size_w_field.config(state=tk.NORMAL, disabledbackground="white", disabledforeground="black")
        self.map_size_w_value.set(w)
        self.map_size_w_field.config(state=tk.DISABLED)

    def update_map_size_h(self, h):
        self.map_size_h_field.config(state=tk.NORMAL, disabledbackground="white", disabledforeground="black")
        self.map_size_h_value.set(h)
        self.map_size_h_field.config(state=tk.DISABLED)

    # Map CSV Update Methods

    def update_map_csv(self, value=None):
        self.map_csv.config(state=tk.NORMAL)
        self.map_csv.delete(1.0, tk.END)
        self.map_csv.insert(tk.INSERT, value)
        self.map_csv.config(state=tk.DISABLED)

    # Unimplemented Features

    def unimplemented(self, *args, **kwargs):
        tk.messagebox.showinfo("Unimplemented", "This feature is not yet implemented.")

    # Exit/Quit Button Method

    def quit(self):
        self.root.quit()


if __name__ == "__main__":
    window = GUI()
    window.root.mainloop()
