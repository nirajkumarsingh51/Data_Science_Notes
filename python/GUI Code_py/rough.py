from tkinter import ttk # it used for level file type import
import tkinter as tk
window = tk.Tk()
window.title("First Gui S/w")
window.geometry('300x300')

#lable
enter_name_label=ttk.Label(window,text="Enter Your Name :- ")
enter_name_label.grid(row=0,column=0,sticky=tk.W)

enter_surname_label=ttk.Label(window,text="Enter Your Surname :- ")
enter_surname_label.grid(row=1,column=0,sticky=tk.W)

enter_email_label=ttk.Label(window,text="Enter Your Email :- ")
enter_email_label.grid(row=2,column=0,sticky=tk.W)

enter_gender_label=ttk.Label(window,text="Select Your Gender :- ")
enter_gender_label.grid(row=3,column=0,sticky=tk.W)


# 
name=tk.StringVar()
name_entery_box = ttk.Entry(window,width=18,textvariable=name)
name_entery_box.grid(row=0,column=1)

surname=tk.StringVar()
surname_entery_box = ttk.Entry(window,width=18,textvariable=surname)
surname_entery_box.grid(row=1,column=1)

email= tk.StringVar()
email_entery_box = ttk.Entry(window,width=18,textvariable=email)
email_entery_box.grid(row=2,column=1)

#combobox
mail_femail=tk.StringVar()
new_combo_box = ttk.Combobox(window,width=18,state="readonly",textvariable=mail_femail)
new_combo_box["values"] = ("Select","Male","femail","Others")
new_combo_box.current(0)
new_combo_box.grid(row=3,column=1)

# Radio 
new_radio_btn1 = ttk.Radiobutton(window,text="Student",value="Student")
 

window.mainloop()
