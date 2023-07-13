from tkinter import *

functions = ["Add the item", "Search the item", "Remove the item"]


class Addition(Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("ADD")
        self.geometry("300x300")


class Searching(Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Search ")
        self.geometry("300x300")


class Removing(Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Removal")
        self.geometry("300x300")


class Layout:
    def __init__(self):
        self.canvas = None
        self.file = None
        self.button = None
        self.clicked = None
        self.dropdown = None
        self.window = Tk()
        self.window_execute()

    def admin_functions(self):
        self.clicked = StringVar()
        self.clicked.set(functions[0])
        self.dropdown = OptionMenu(self.canvas, self.clicked, *functions)
        self.dropdown.place(x=190, y=500)
        
        self.button = Button(self.window, text="Select", command=self.open_selected_function)
        self.button.place(x=210, y=540)

    def open_selected_function(self):
        selected_option = self.clicked.get()

        match selected_option:
            case "Add the item":
                Addition(self.window)
            case"Search the item":
                Searching(self.window)
            case"Remove the item":
                Removing(self.window)

    def window_execute(self):
        self.window.title("Admin Side")
        self.window.geometry("500x600")
        self.file = PhotoImage(file="ICON.png")
        image_label = Label(self.window, image=self.file)
        image_label.pack()
        self.admin_functions()
        self.window.mainloop()


main = Layout()
