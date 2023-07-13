from tkinter import *
from tkinter import messagebox


class Layout:
    def __init__(self):
        self.clicked = None
        self.dropdown = None
        self.window = Tk()
        self.window_execute()

    def admin_functions(self):
        self.clicked = StringVar()
        self.clicked.set(functions[0])
        self.dropdown = OptionMenu(self.window, self.clicked, *functions)
        self.dropdown.pack()

        button = Button(self.window, text="Select", command=self.open_selected_function)
        button.pack()

    def open_selected_function(self):
        selected_option = self.clicked.get()

        if selected_option == "Add the item":
            self.open_add_item_window()
        elif selected_option == "Search the item":
            self.open_search_item_window()
        elif selected_option == "Remove the item":
            self.open_remove_item_window()

    def open_add_item_window(self):
        messagebox.showinfo("Add Item", "Add Item window is opened.")

    def open_search_item_window(self):
        messagebox.showinfo("Search Item", "Search Item window is opened.")

    def open_remove_item_window(self):
        messagebox.showinfo("Remove Item", "Remove Item window is opened.")

    def window_execute(self):
        self.window.title("Admin Side")
        self.window.geometry("500x500")
        self.admin_functions()
        self.window.mainloop()


functions = ["Add the item", "Search the item", "Remove the item"]
main = Layout()
