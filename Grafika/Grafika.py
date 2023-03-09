from tkinter import *
k=0
def klikker(event):
    global k
    k+=1
    if k>=1 and a.get() and b.get() and c.get():
        a_val = a.get()
        b_val = b.get()
        c_val = c.get()
        try:
            a_float = float(a_val)
        except ValueError:
            a_float = 0.0
        try:
            b_float = float(b_val)
        except ValueError:
            b_float = 0.0
        try:
            c_float = float(c_val)
        except ValueError:
            c_float = 0.0
        D = b_float**2 - 4 * a_float * c_float
        if D<=-1:
            lbl5.configure(text=f"juur on väiksem kui null D:{D}") 
        else:
            x1= (-b_float+D**(1/2))/(2*a_float)
            x2= (-b_float-D**(1/2))/(2*a_float)
            lbl5.configure(text=f"D: {D}\n x1: {x1}\n x2: {x2}")
aken = Tk()
aken.geometry("600x300")
aken.title("Welcome")
lbl4 = Label(aken, fg="green", bg="lightblue", text="Ruutvõrrandi lahendamine", font="Arial 20", justify=CENTER)
a = Entry(aken, fg="blue", bg="lightblue", width=4, font="Arial 20")
b = Entry(aken, fg="blue", bg="lightblue", width=4, font="Arial 20")
c = Entry(aken, fg="blue", bg="lightblue", width=4, font="Arial 20")
btn = Button(aken, fg="black", bg="green", text="Lahendus", width=10, font="Arial 20")
lbl = Label(aken, fg="green", text="x**2", font="Arial 20", justify=CENTER)
lbl2 = Label(aken, fg="green", text="x+", font="Arial 20", justify=CENTER)
lbl3 = Label(aken, fg="green", text="=0", font="Arial 20", justify=CENTER)
lbl5 = Label(aken, fg="green", bg="yellow", width=30, height=3, text="LAHENDUS", font="Arial 15")
btn.bind("<Button-1>", klikker) #Enter
lbl5.pack(side=BOTTOM)
lbl4.pack()
a.pack(side=LEFT)
lbl.pack(side=LEFT)
b.pack(side=LEFT)
lbl2.pack(side=LEFT)
c.pack(side=LEFT)
lbl3.pack(side=LEFT)
btn.pack(side=LEFT)
aken.mainloop()
