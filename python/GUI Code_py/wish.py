# import tkinter as tk
# from tkinter import ttk
# from PIL import Image, ImageTk
# import pyttsx3

# # Voice engine
# engine = pyttsx3.init()

# # Window
# f = tk.Tk()
# f.title("🎂 Wish App")
# f.geometry("500x350")

# # Dark mode colors
# bg_color = "#1e1e2f"
# fg_color = "#ffffff"

# # Background Image
# img = Image.open("birthday.jpg")  # <-- add your image path
# img = img.resize((500, 350))
# bg = ImageTk.PhotoImage(img)

# bg_label = tk.Label(f, image=bg)
# bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# # Function: Animated Text + Voice
# def shows():
#     name = t1.get()
#     message = f"Hello {name}, Wish You Happy Birthday!"
#     animate_text(message, 0)
    
#     # Voice
#     engine.say(message)
#     engine.runAndWait()

# # Animation function
# def animate_text(msg, i):
#     if i <= len(msg):
#         res.config(text=msg[:i])
#         f.after(50, animate_text, msg, i+1)

# # Title
# title = tk.Label(f, text="🎉 Birthday Wisher 🎂",
#                  font=("Verdana", 18, "bold"),
#                  bg=bg_color, fg="#ff4d6d")
# title.place(relx=0.5, y=20, anchor="center")

# # Entry
# t1 = ttk.Entry(f, width=30)
# t1.place(relx=0.5, y=100, anchor="center")

# # Button
# btn = tk.Button(f, text="🎁 Send Wish",
#                 font=("Verdana", 11, "bold"),
#                 bg="#ff4d6d", fg="white",
#                 command=shows)
# btn.place(relx=0.5, y=150, anchor="center")

# # Result Label
# res = tk.Label(f, text="",
#                font=("Verdana", 12, "bold"),
#                bg=bg_color, fg="#00ffcc",
#                wraplength=400, justify="center")
# res.place(relx=0.5, y=230, anchor="center")

# f.mainloop()

import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import pyttsx3
import random

# Voice engine
engine = pyttsx3.init()

# Window
f = tk.Tk()
f.title("🎂 Birthday Wisher Pro")
f.geometry("520x380")
f.resizable(False, False)

# Colors
bg_color = "#1e1e2f"
fg_color = "#ffffff"

# Background Image
img = Image.open("birthday.jpg")
img = img.resize((520, 380))
bg = ImageTk.PhotoImage(img)

bg_label = tk.Label(f, image=bg)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# 🎉 Random Wishes List
wishes = [
    "Wish you a day full of happiness and a year full of joy!",
    "May all your dreams come true. Happy Birthday!",
    "Keep shining and smiling always!",
    "Have a fantastic birthday filled with surprises!",
    "May your life be filled with success and happiness!"
]

# Voice Toggle
voice_on = tk.BooleanVar(value=True)

# Function
def shows():
    name = t1.get().strip()
    
    if name == "":
        messagebox.showwarning("Input Error", "Please enter a name!")
        return
    
    msg = random.choice(wishes)
    message = f"🎉 Hello {name}! 🎂\n{msg}"
    
    animate_text(message, 0)
    
    # Voice
    if voice_on.get():
        engine.say(f"Hello {name}, {msg}")
        engine.runAndWait()

# Animation
def animate_text(msg, i):
    if i <= len(msg):
        res.config(text=msg[:i])
        f.after(40, animate_text, msg, i+1)

# Hover Effects
def on_enter(e):
    btn.config(bg="#ff1e56")

def on_leave(e):
    btn.config(bg="#ff4d6d")

# Title
title = tk.Label(f, text="🎉 Birthday Wisher 🎂",
                 font=("Verdana", 20, "bold"),
                 bg=bg_color, fg="#ff4d6d")
title.place(relx=0.5, y=20, anchor="center")

# Entry
t1 = ttk.Entry(f, width=30, font=("Verdana", 11))
t1.place(relx=0.5, y=110, anchor="center")

# Button
btn = tk.Button(f, text="🎁 Send Wish",
                font=("Verdana", 12, "bold"),
                bg="#ff4d6d", fg="white",
                activebackground="#ff1e56",
                command=shows)
btn.place(relx=0.5, y=160, anchor="center")

btn.bind("<Enter>", on_enter)
btn.bind("<Leave>", on_leave)

# Voice Checkbox
voice_chk = tk.Checkbutton(f, text="🔊 Voice",
                           variable=voice_on,
                           bg=bg_color, fg="white",
                           selectcolor=bg_color,
                           font=("Verdana", 10))
voice_chk.place(relx=0.5, y=200, anchor="center")

# Result Label
res = tk.Label(f, text="",
               font=("Verdana", 12, "bold"),
               bg=bg_color, fg="#00ffcc",
               wraplength=420, justify="center")
res.place(relx=0.5, y=280, anchor="center")

f.mainloop()