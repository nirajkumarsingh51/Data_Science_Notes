import tkinter as t
f=t.Tk()
f.title("Login Window")
f.geometry('300x300')
def disp(p):
    if p==1:
        res.config(text="Your user name is :"+str(t1.get()) +"\n Your password is :"+str(t1.get()),bg="blue",fg="white")
    else:
        t1.delete(0,t.END)
        t2.delete(0,t.END)
        res.config(text="",bg="white")

#login
t.Label(f,text="User Name",font=("verdana",10,"bold")).place(x=10,y=10)
t1=t.Entry(f,width=25,font=("verdana",10,"bold"))
t1.place(x=10,y=35)

#password
t.Label(f,text="Password",font=("verdana",10,"bold")).place(x=10,y=75)
t2=t.Entry(f,width=25,font=("verdana",10,"bold"))
t2.place(x=10,y=100)

#button
t.Button(f,text="Login",font=("verdana",10,"bold"),width=8,bg="green",fg="white",command=lambda:disp(1)).place(x=40,y=150)
t.Button(f,text="Reset",font=("verdana",10,"bold"),width=8,bg="red",fg="white",command=lambda:disp(2)).place(x=150,y=150)

#loginmassage
res=t.Label(f,font=("arial",12,"bold"))
res.place(x=20,y=200)
f.mainloop()
