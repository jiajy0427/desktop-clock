from tkinter import *
import time, datetime
from time import gmtime, strftime
import tkinter as tk

root = Tk()

# Window Attributes
root.overrideredirect(1)
#root.wm_attributes("-transparentcolor", "gray99")
root.attributes("-transparentcolor", "black")
root.config(bg="black")

running = True

# close window
def close(event):
    global running
    running = False

root.bind('<Escape>', close)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = 200
window_height = 150

x = (screen_width //2) -(window_width // 2)
y = (screen_height // 8) - (window_height // 2)

root.geometry(f"{window_width}x{window_height}+{x}+{y}")

#timeframe = Frame(root, width=200, height=100, bg="gray99")
#timeframe.grid(row=0,column=0)
#timeframe.pack(pady=10)

#label = tk.Label(root, text="Hello, Tkinter!", fg="black", bg="gray99", font=("Ink Free", 50))  # Add a label
#label.pack()

#root.mainloop()

tkintertime = StringVar()
timelabel = tk.Label(root, textvariable=tkintertime, fg="white", bg="black", font=("Ink Free", 50))
timelabel.place(y=screen_height/2 - 300, x=screen_width/2, anchor="center")
timelabel.pack()

tkinterdate = StringVar()
datelabel = Label(root, textvariable=tkinterdate, fg="white", bg="black", font=("Ink Free", 15))
datelabel.place(y=screen_height/2 - 250, x=screen_width/2, anchor="center")
datelabel.pack()

while running:
    tkintertime.set(value=strftime("%H:%M"))
    tkinterdate.set(value=strftime("%A, %e %B"))
    root.update_idletasks()
    root.update()
    time.sleep(1)
