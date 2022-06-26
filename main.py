from tkinter import *
import datetime
from tkinter.messagebox import *
from tkinter.ttk import *
import winsound

window = Tk()
window.title("Alarm clock by sammiie.com")
window.config(padx=20, pady=50, bg='#29454f')
window.geometry("450x300")


def alarm():
    if period.get() == "AM":
        x = int(hour_entry.get())
        y = int(minute_entry.get())
    if period.get() == "PM":
        x = int(hour_entry.get())+12
        y = int(minute_entry.get())
    showinfo("notification", "alarm has been set")
    while True:
        if x == datetime.datetime.now().hour and y == datetime.datetime.now().minute:
            for j in range(0,100):
                winsound.Beep(1000, 100)
            break

# **************************************** USER INTERFACE DESIGN ****************************************************************


hour_label = Label(window, text = "HOURS:")
minute_label = Label(window, text= "MINUTES:")

hour_label.grid(row=0, column=0)
minute_label.grid(row=0, column=2, padx=10)

hour_entry = Entry(window)
minute_entry = Entry(window)

hour_entry.grid(row=0, column=1, padx=10)
minute_entry.grid(row=0, column=3)

period_label = Label(window,text="AM OR PM:")
period_label.place(relx=0.25,rely=0.31)
period = Combobox(window, values=["AM", "PM"])
period.place(relx=0.42, rely=0.3)

set_btn = Button(window, text="Set Alarm", command=alarm)
set_btn.place(relx=0.4, rely=0.5)


mainloop()
