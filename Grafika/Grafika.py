from tkinter import *
k=0
aken=Tk()
aken.geometry("600x300")
aken.title("Welcome")
lbl4=Label(aken, fg="green",bg="lightblue",text="Ruutvõrrandi lahendamine",font="Arial 20" ,justify=CENTER)
ent=Entry(aken, fg="blue", bg="lightblue", width=4, font="Arial 20")
ent1=Entry(aken, fg="blue", bg="lightblue", width=4, font="Arial 20")
ent2=Entry(aken, fg="blue", bg="lightblue", width=4, font="Arial 20")
btn=Button(aken, fg="black", bg="green",text="Lahendus", width=10, font="Arial 20")
lbl=Label(aken, fg="green",text="x**2",font="Arial 20" ,justify=CENTER)
lbl2=Label(aken, fg="green",text="x+",font="Arial 20" ,justify=CENTER)
lbl3=Label(aken, fg="green",text="=0",font="Arial 20" ,justify=CENTER)
lbl5=Label(aken, fg="green",bg="yellow",text="LAHENDUS",font="Arial 20" ,justify=CENTER)

ent.bind("<Return>") #Enter
lbl4.pack()
ent.pack(side=LEFT)
lbl.pack(side=LEFT)
ent1.pack(side=LEFT)
lbl2.pack(side=LEFT)
ent2.pack(side=LEFT)
lbl3.pack(side=LEFT)
btn.pack(side=LEFT)
lbl5.pack(side=BOTTOM)
aken.mainloop()




