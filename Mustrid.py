
from optparse import OptionValueError
from random import *
from struct import pack
from tkinter import *
from tkinter import font # vajalik teksti fondi muutmiseks
from math import*
from turtle import color

aken = Tk()
aken.title("Tahvel")
tahvel = Canvas(aken, width=600, height=600, background="white")

#Harjutus. Muster oval
def oval():
    x0=0
    y0=0
    x1=600
    y1=600
    a=300
    r=(a**2+a**2)**(1/2)
    p=(a-r)

    for i in range(12):
        x0+=p
        y0+=p
        x1-=p
        y1-=p
        tahvel.create_rectangle(x0,y0,x1,y1,width=1, outline="blue", fill="red")
        tahvel.create_oval(x0,y0,x1,y1,width=1, outline="blue", fill="yellow")
        p=r-p
        r=r-p
        a=((r)*sqrt(2))/2




#Muster ruut
def ruut():
    for rida in range(8):
        for veerg in range(8):
            x0 = veerg * 80
            y0 = rida * 80
            x1 = x0 + 80
            y1 = y0 + 80
            if (rida + veerg) % 2 == 0:
                tahvel.create_rectangle(x0, y0, x1, y1, width=1, fill="white")
            else:
                tahvel.create_rectangle(x0, y0, x1, y1, width=1, fill="black")

#Harjutus. Muster oval 2
def oval2():
    colors= ["black","cyan","magenta","red","blue","gray","yellow","green","lightblue","pink","gold"]
    raam2=Tk()
    raam2.title("ringid")
    tahvel2=Canvas(raam2,width=600,height=600,background="white")
    x0=0
    y0=0
    x1=600
    y1=600
    p=5
    for i in range(55):
        x0+=p 
        y0+=p 
        x1-=p 
        y1-=p 
        tahvel2.create_oval(x0,y0,x1,y1,fill=choice(colors))
        tahvel2.grid()

var1=StringVar()
var2=StringVar()

c1=Checkbutton(aken,text="Ruut",variable=var2,onvalue="Teine",offvalue="--",command=ruut)
c2=Checkbutton(aken,text="Oval2",variable=var2,onvalue="Kolmas",offvalue="---",command=oval2) 

c1.grid(row=1, column=1)
c2.grid(row=2, column=1)
c1.deselect()
c2.deselect()






tahvel.grid()
aken.mainloop()
