import tkinter
from tkinter import messagebox


def popUp(title="Some Title", message="Some Message"):
    '''Creates a pop up box, with args `title` and `message`, goes away when pressed OK button'''
    root = tkinter.Tk()
    root.withdraw()
    messagebox.showinfo(title, message)