from tkinter import *
from tkinter import font
import datetime

def finish(*args):
    global win
    win.destroy()
def clock_time():
    ctime=datetime.datetime.now()
    ctime=ctime.strftime('%H:%M:%S')
    txt.set(ctime)

    win.after(1000,clock_time)

def toggle_fullscreen(self,event=None):
    win.state=not win.state
    win.attributes("-fullscreen",win.state)
    return "break"

win=Tk()
win.geometry('850x200')
win.title('digital clock')
win.resizable(False,False)
win.configure(background='black')

win.bind('<Escape>',toggle_fullscreen)
# win.bind('<F11>',toggle_fullscreen)

fnt=font.Font(family='Helvetica', size=120,weight='bold')
txt=StringVar()
# txt.set('hh:mn:ss pm')

lbl=Label(win,textvariable=txt,font=fnt,foreground='white',background='black')
lbl.place(relx=0.5,rely=0.5,anchor=CENTER)
win.after(1000,clock_time)
win.mainloop()

