# import turtle
# import colorsys
# t = turtle. Turtle()
# s = turtle. Screen() .bgcolor('black')
# t.speed(0)
# n = 70
# h = 0
# for i in range (360):
#     c = colorsys.hsv_to_rgb(h, 1, 0.8)
#     h+= 1/n
#     t.color(c)
#     t.left(1)
#     t.fd(1)
#     for j in range (2):
#           t.left(2)
#           t.circle(100)

# from turtle import *
# import colorsys
# trace=(3)
# h=0.7
# bgcolor('black')
# pensize(2)
# for i in range(190):
#     c=colorsys.hsv_to_rgb(h,1,1)
#     color(c)
#     h+=0.004
#     circle(190-i,90)
#     lt(90)
#     lt(20)
#     circle(190-i,90)
#     lt(18)



import tkinter as tk

root = tk.Tk()
root.title("Niraj Portfolio App")
root.geometry("900x600")
root.configure(bg="#0f172a")

# ====== SIDEBAR ======
sidebar = tk.Frame(root, bg="#020617", width=200)
sidebar.pack(side="left", fill="y")

# ====== MAIN AREA ======
main_area = tk.Frame(root, bg="#0f172a")
main_area.pack(side="right", expand=True, fill="both")

# function to clear frame
def clear_frame():
    for widget in main_area.winfo_children():
        widget.destroy()

# ====== PAGES ======

def home():
    clear_frame()
    tk.Label(main_area, text="👋 Welcome", font=("Arial", 24, "bold"), fg="cyan", bg="#0f172a").pack(pady=20)

    tk.Label(main_area, text="""
NIRAJ KUMAR SINGH
BCA Student | AWS & Web Developer

📍 Patna, Bihar
📧 nirajsingh9570460932@gmail.com
📞 +91 9153942168
""", font=("Arial", 14), fg="white", bg="#0f172a").pack()

def skills():
    clear_frame()
    tk.Label(main_area, text="💻 Skills", font=("Arial", 22, "bold"), fg="cyan", bg="#0f172a").pack(pady=20)

    tk.Label(main_area, text="""
• AWS (IAM, EC2, S3)
• HTML, CSS, JavaScript
• Java, C
• MySQL
• Git & GitHub
""", font=("Arial", 13), fg="white", bg="#0f172a").pack()

def projects():
    clear_frame()
    tk.Label(main_area, text="🚀 Projects", font=("Arial", 22, "bold"), fg="cyan", bg="#0f172a").pack(pady=20)

    tk.Label(main_area, text="""
🔹 Restaurant Management System
🔹 SEO Writing Assistant (AI Tool)
🔹 Java Attendance Tracker (AWS Deploy)
""", font=("Arial", 13), fg="white", bg="#0f172a").pack()

def contact():
    clear_frame()
    tk.Label(main_area, text="📞 Contact", font=("Arial", 22, "bold"), fg="cyan", bg="#0f172a").pack(pady=20)

    tk.Label(main_area, text="""
📧 Email: nirajsingh9570460932@gmail.com
📞 Phone: +91 9153942168
🔗 LinkedIn / GitHub
""", font=("Arial", 13), fg="white", bg="#0f172a").pack()

# ====== BUTTON STYLE ======
def nav_button(text, command):
    return tk.Button(sidebar, text=text, command=command,
                     font=("Arial", 12, "bold"),
                     fg="white", bg="#020617",
                     activebackground="#1e293b",
                     relief="flat", pady=10)

# ====== NAVIGATION BUTTONS ======
nav_button("🏠 Home", home).pack(fill="x")
nav_button("💻 Skills", skills).pack(fill="x")
nav_button("🚀 Projects", projects).pack(fill="x")
nav_button("📞 Contact", contact).pack(fill="x")

# default page
home()

root.mainloop()