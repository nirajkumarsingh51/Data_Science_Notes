import tkinter as ttk
windows = ttk.Tk()
windows.title("Student Regerestation Form")
windows.geometry('400x500')

#Heading
ttk.Label(windows,text="Student Regerestation Form",font=("verdana",15,"bold")).place(x=15,y=20)
#studentDetails
ttk.Label(windows,text="Name of Student",font=("verdana",10,"bold")).place(x=20,y=45)
t1=ttk.Entry(windows,width=20,font=("Verdana",10,"bold"))
t1.place(x=160,y=50)

ttk.Label(windows,text="Father's Name",font=("verdana",10,"bold")).place(x=20,y=75)
t1=ttk.Entry(windows,width=20,font=("Verdana",10,"bold"))
t1.place(x=160,y=75)

windows.mainloop()
