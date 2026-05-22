import tkinter as ttk
f=ttk.Tk()
f.title("WishApp")
f.geometry('400x200')
def shows():
    a=t1.get()
    res.config(text="Hello "+ a +", Wish You Happy Birthday !")

#lable & Text Fild 
ttk.Label(f,text="Enter Your Firend Name :",font=("verdana",10,"bold")).place(x=10,y=10)
t1=ttk.Entry(f,width=30,font=("vendana",10,"bold"))
t1.place(x=10,y=35)

#wishButton
ttk.Button(f,text="BirthdayWish",font=("verdana",10,"bold"),width=15,bg="red",fg="white",command=shows).place(x=30,y=80)

#result
res=ttk.Label(f,font=("verdana",10,"bold"),fg="darkorange")
res.place(x=25,y=120)

f.mainloop()


# import tkinter as tk
# from tkinter import ttk

# # Window
# f = tk.Tk()
# f.title("🎂 Wish App")
# f.geometry("400x250")
# f.configure(bg="#ffe6f0")

# # Make responsive
# f.columnconfigure(0, weight=1)
# f.columnconfigure(1, weight=1)

# # Function
# def shows():
#     name = t1.get()
#     res.config(text=f"🎉 Hello {name},\nWish You Happy Birthday! 🎂")

# # Title
# title = tk.Label(f, text="Birthday Wisher 🎈", 
#                  font=("Verdana", 16, "bold"), 
#                  bg="#ffe6f0", fg="#cc0066")
# title.grid(row=0, column=0, columnspan=2, pady=10)

# # Label
# ttk.Label(f, text="Enter Friend Name:").grid(row=1, column=0, padx=10, pady=5, sticky="w")

# # Entry
# t1 = ttk.Entry(f, width=25)
# t1.grid(row=1, column=1, padx=10, pady=5)

# # Button
# btn = tk.Button(f, text="🎁 Send Wish", 
#                 font=("Verdana", 10, "bold"),
#                 bg="#ff4d6d", fg="white",
#                 activebackground="#ff1a4d",
#                 command=shows)
# btn.grid(row=2, column=0, columnspan=2, pady=15)

# # Result
# res = tk.Label(f, text="", 
#                font=("Verdana", 11, "bold"),
#                bg="#ffe6f0", fg="#ff6600", justify="center")
# res.grid(row=3, column=0, columnspan=2, pady=10)

# # Run
# f.mainloop()