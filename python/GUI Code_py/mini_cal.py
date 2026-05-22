import tkinter as ttk
f=ttk.Tk()
f.title("Mini Calculator")
f.geometry('400x300')
def shows(p):
    a=float(t1.get())
    b=float(t2.get())
    if p==1:
        r=a+b
    elif p==2:
        r=a-b
    elif p==3:
        r=a*b
    else:
        r=a/b
    res.config(text="Your result is : "+str(r))

#lable & Text Fild 
ttk.Label(f,text="Enter First No.",font=("verdana",10,"bold")).place(x=10,y=10)
t1=ttk.Entry(f,width=30,font=("vendana",10,"bold"))
t1.place(x=10,y=35)

ttk.Label(f,text="Enter Second No.",font=("verdana",10,"bold")).place(x=10,y=75)
t2=ttk.Entry(f,width=30,font=("vendana",10,"bold"))
t2.place(x=10,y=100)

#button
ttk.Button(f,text="ADD",font=("verdana",10,"bold"),width=6,bg="red",fg="white",command=lambda:shows(1)).place(x=10,y=150)
ttk.Button(f,text="Sub",font=("verdana",10,"bold"),width=6,bg="green",fg="white",command=lambda:shows(2)).place(x=80,y=150)
ttk.Button(f,text="Mult",font=("verdana",10,"bold"),width=6,bg="black",fg="white",command=lambda:shows(3)).place(x=150,y=150)
ttk.Button(f,text="Div",font=("verdana",10,"bold"),width=6,bg="blue",fg="white",command=lambda:shows(4)).place(x=220,y=150)

#result
res=ttk.Label(f,font=("verdana",15,"bold"),fg="blue")
res.place(x=25,y=200)

f.mainloop()