import tkinter as Tk
from tkinter import *
from tkinter import messagebox

window = Tk()
window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel()) #puts in the middle of the screen on top
window.withdraw() #makes the window invisible

if messagebox.askyesno('Question', 'Do you have brown eyes?') == True: #text to display
  print("Yes")
else:
  print("No")
    
window.deiconify()
window.destroy()
window.quit() #quits window
