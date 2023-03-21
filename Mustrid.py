from tkinter import *
from tkinter import font # vajalik teksti fondi muutmiseks

raam = Tk()
raam.title("Tahvel")
tahvel = Canvas(raam, width=600, height=600, background="white")

#Harjutus. Muster
k=7
x0=0
y0=0
x1=550
y1=550

for i in range(k):
    x0+=35
    y0+=35
    x1-=35
    y1-=35
    tahvel.create_rectangle(x0,y0,x1,y1,width=1, outline="blue", fill="red")
    tahvel.create_oval(x0,y0,x1,y1,width=1, outline="blue", fill="yellow")


#Muster
x0=0
y0=0
x1=90
y1=90

for i in range(1):
    x0+=90
    y0+=90
    x1-=90
    y1-=90
    tahvel.create_rectangle(x0,y0,x1,y1,width=1, fill="white")

x0=0
y0=0
x1=90+180
y1=90
for i in range(1):
    x0+=90
    y0+=90
    x1-=90
    y1-=90
    tahvel.create_rectangle(x0,y0,x1,y1,width=1, fill="black")

    

tahvel.grid()
raam.mainloop()
