import tkinter as ttk
f=ttk.Tk()
f.title("Count App")
f.geometry('400x250')
def shows(p):
    v=t1.get("1.0","end-1c").strip()
    if p==1:
        res.config(text="Total word are:"+str(v.count(" ")+v.count("\n")+1))
    elif p==2:
        res.config(text="Total lines are:"+str(v.count(".")))
    else:
        res.config(text="Total lines are:"+str(v.count("."))) 
#lable & Text Fild 
t1 = ttk.Text(f, width=45, height=8)
t1.place(x=10,y=35)

#button
ttk.Button(f,text="Word",font=("verdana",10,"bold"),width=8,bg="green",fg="white",command=lambda:shows(1)).place(x=50,y=180)
ttk.Button(f,text="characters",font=("verdana",10,"bold"),width=9,bg="red",fg="white",command=lambda:shows(2)).place(x=150,y=180)
ttk.Button(f,text="Sentence",font=("verdana",10,"bold"),width=8,bg="black",fg="white",command=lambda:shows(3)).place(x=250,y=180)

res=ttk.Label(f,font=("verdana",12,"bold"))
res.place(x=20,y=225)
f.mainloop()
