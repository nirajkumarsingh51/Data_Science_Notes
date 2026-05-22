import tkinter as tkk
import tkinter.ttk as tk1

windows = tkk.Tk()
windows.geometry('300x400')
windows.title("Employee Details")
#ename
tkk.Label(windows,text="Employee Name",font=("verdana",8,"bold")).place(x=10,y=15)
ename=tkk.Entry(windows)
ename.place(x=120,y=20)
#post
tkk.Label(windows,text="Post",font=("verdana",8,"bold")).place(x=10,y=50)
#checkbox
c1 = tkk.Checkbutton(windows,text="Analyst")
c1.place(x=20,y=70)

c2 = tkk.Checkbutton(windows,text="Manager")
c2.place(x=100,y=70)

c3 = tkk.Checkbutton(windows,text="Cleark")
c3.place(x=180,y=70)

#gender
tkk.Label(windows,text="Gender",font=("verdana",8,"bold")).place(x=10,y=105)

#radio
var=tkk.StringVar()
var.set("Male")
#
r1=tkk.Radiobutton(windows,text="Male",variable=var,value="Male")
r1.place(x=20,y=125)
r2=tkk.Radiobutton(windows,text="Female",variable=var,value="Femail")
r2.place(x=100,y=125)
r3=tkk.Radiobutton(windows,text="Others",variable=var,value="Other")
r3.place(x=180,y=125)

#state combobox
tkk.Label(windows,text="State",font=("verdana",8,"bold")).place(x=10,y=160)
# stval=["Bihar","Jh","Mp","RJ"]
stval = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar",
        "Chhattisgarh", "Goa", "Gujarat", "Haryana",
        "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala",
        "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya",
        "Mizoram", "Nagaland", "Odisha", "Punjab",
        "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana",
        "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal" ]
st=tk1.Combobox(windows,width=30,values=stval)
st.place(x=80,y=160)

#Text Area 
tkk.Label(windows,text="Address",font=("verdana",8,"bold")).place(x=10,y=200)
ta=tkk.Text(windows,width=30,height=7)
ta.place(x=10,y=230)

#button
tkk.Button(windows,text="Submit",width=8,font=("verdana",8,"bold")).place(x=40,y=350)
tkk.Button(windows,text="Reset",width=8,font=("verdana",8,"bold")).place(x=120,y=350)
windows.mainloop()
