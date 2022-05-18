from tkinter import *
import time


root = Tk()
root.geometry('215x195')
root.title('Clock')
root.config(bg='black')


def Clock():
    h = str(time.strftime("%H"))
    m = str(time.strftime("%M"))
    s = str(time.strftime("%S"))
    n = str(time.strftime("%p"))
    day = str(time.strftime("%A"))
    d = str(time.strftime("%d"))
    m1 = str(time.strftime("%m"))
    y = str(time.strftime("%Y"))

    if int(h) > 12 and int(m) > 0:
        lbl_noon.config(text=n)
    if int(h) > 12:
        h = str(int(h) - 12)

    lbl_hr.config(text=h)
    lbl_min.config(text=m)
    lbl_sec.config(text=s)
    lbl_date.config(text=d)
    lbl_month.config(text=m1)
    lbl_year.config(text=y)
    lbl_day.config(text=day)

    lbl_hr.after(1000, Clock)


lbl_hr = Label(root, text="12", font=("Comic Sans MS", 15, "bold"), relief=RAISED, border=3, bg='#FFD119')
lbl_hr.place(x=20, y=15, width=40, height=30)

lbl_min = Label(root, text="12", font=("Comic Sans MS", 15, "bold"), relief=RAISED, border=3, bg='#FFD119')
lbl_min.place(x=65, y=15, width=40, height=30)

lbl_sec = Label(root, text="12", font=("Comic Sans MS", 15, "bold"), relief=RAISED, border=3, bg='#FFD119')
lbl_sec.place(x=110, y=15, width=40, height=30)

lbl_noon = Label(root, text="AM", font=("Comic Sans MS", 13, "bold"), relief=RAISED, border=3, bg='#FFD119')
lbl_noon.place(x=155, y=15, width=40, height=30)

lbl = Label(root, text="Time", font=("Comic Sans MS", 10, "bold"), relief=RAISED, border=3, bg='#FF3333')
lbl.place(x=20, y=50, width=175, height=20)

lbl_date = Label(root, text="12", font=("Comic Sans MS", 15, "bold"), relief=RAISED, border=3, bg='#FFD119')
lbl_date.place(x=20, y=90, width=40, height=30)

lbl_month = Label(root, text="12", font=("Comic Sans MS", 15, "bold"), relief=RAISED, border=3, bg='#FFD119')
lbl_month.place(x=65, y=90, width=40, height=30)

lbl_year = Label(root, text="12", font=("Comic Sans MS", 15, "bold"), relief=RAISED, border=3, bg='#FFD119')
lbl_year.place(x=110, y=90, width=85, height=30)

lbl_day = Label(root, text="WEDNESDAY", font=("Comic Sans MS", 15, "bold"), relief=RAISED, border=3, bg='#FFD119')
lbl_day.place(x=20, y=125, width=175, height=30)

lbl = Label(root, text="Date and Day", font=("Comic Sans MS", 10, "bold"), relief=RAISED, border=3, bg='#FF3333')
lbl.place(x=20, y=160, width=175, height=20)




Clock()
root.mainloop()