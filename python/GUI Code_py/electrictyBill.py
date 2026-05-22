import tkinter as t
eb=t.Tk()
eb.title("Electricty Bill")
eb.geometry('500x500')
eb.resizable(False,False)
def getval(event):
    a=float(cr.get()) - float(pr.get())
    tu.insert(0,a)
    tu.config(state="disabled")

def disp():
    if var.get()=="Commercial":
        rate=9
    else:
        rate=4
    v=float(tu.get()) 
    print(rate)
    res.config(text="Your total bill amount is : " + str(v*rate))

#lable
t.Label(eb,text="Current Reading",font=("verdana",12,"bold")).place(x=10,y=10)
cr=t.Entry(eb,width=25,font=("verdana",12,"bold"))
cr.place(x=200,y=10)

t.Label(eb,text="Previous Reading",font=("verdana",12,"bold")).place(x=10,y=50)
pr=t.Entry(eb,width=25,font=("verdana",12,"bold"))
pr.place(x=200,y=50)

t.Label(eb,text="Total Unit Consumed",font=("verdana",12,"bold")).place(x=120,y=90)
tu=t.Entry(eb,width=25,font=("verdana",12,"bold"))
tu.place(x=100,y=130)

# RadioButton variable
var=t.StringVar()
var.set("Residential")

#Radiobutton
r1=t.Radiobutton(eb,text="Commercial (9/unit)",variable=var,value="Commercial")
r1.place(x=100,y=200)
r2=t.Radiobutton(eb,text="Residential(4/unit)",variable=var,value="Residential")
r2.place(x=250,y=200)

# Button
t.Button(eb,text="Calculate",font=("verdana",10,"bold"),width=8,bg="green",fg="white",command=disp).place(x=200,y=300)

#bill
res=t.Label(eb,font=("verdana",12,"bold"))
res.place(x=10,y=400)
pr.bind("<FocusOut>", getval)

# t4=ttk.Entry(windows,width=25,font=("verdana",12,"bold"))
# t4.place(x=200,y=400)

eb.mainloop()