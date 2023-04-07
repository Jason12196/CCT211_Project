import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import datetime
import random

def hotel_management_system():
    root = tk.Tk()
    root.geometry("1024x600")
    root.minsize(1024, 600)
    root.maxsize(1024, 600)
    root.configure(bg='white')
    root.title("Hotel Management System")

    def employee_login_page():
        frame1 = tk.Frame(root, height=400, width=1024, bg='white')

        # Staff info frame
        staff_info = tk.Frame(frame1, bg='white', height=350, width=1024)

        # Manager name card
        manager = Image.open("manager.png")
        manager_photo = ImageTk.PhotoImage(manager.resize((100,100), Image.LANCZOS))
        manager_info_label = tk.Label(staff_info, image=manager_photo, bg='white')
        manager_info_label.image = manager_photo
        manager_info_label.pack()
        manager_info_label.place(x=200, y=0)

        manager_info_text = tk.Frame(staff_info, bg='white', height=122, width=300)
        tk.Label(manager_info_text, text="Manager", font=('Arial bold', 17), bg='white').place(x=20, y=0)
        tk.Label(manager_info_text, text="Mr. John Wick", font=('Arial', 10), fg='Grey', bg='white').place(x=20, y=30)
        tk.Label(manager_info_text, text="Extension: 001", font=('Arial', 10), fg='Grey', bg='white').place(x=20, y=50)
        tk.Label(manager_info_text, text="Email: johnwick@fuji.ca", font=('Arial', 10), fg='Grey', bg='white').place(x=20, y=70)
        manager_info_text.pack()
        manager_info_text.place(x=300, y=1)


        # Front desk name card
        front_desk = Image.open("front_desk.png")
        front_desk_photo = ImageTk.PhotoImage(front_desk.resize((100, 100), Image.LANCZOS))
        front_desk_info_label = tk.Label(staff_info, image=front_desk_photo, bg='white')
        front_desk_info_label.image = front_desk_photo
        front_desk_info_label.pack()
        front_desk_info_label.place(x=200, y=152)

        front_desk_info_text = tk.Frame(staff_info, bg='white', height=122, width=300)
        tk.Label(front_desk_info_text, text="Front Desk", font=('Arial bold', 17), bg='white').place(x=20, y=0)
        tk.Label(front_desk_info_text, text="Ms. Jane Doe", font=('Arial', 10), fg='Grey', bg='white').place(x=20, y=30)
        tk.Label(front_desk_info_text, text="Extension: 002", font=('Arial', 10), fg='Grey', bg='white').place(x=20, y=50)
        tk.Label(front_desk_info_text, text="Email: janedoe@fuji.ca", font=('Arial', 10), fg='Grey', bg='white').place(x=20, y=70)
        front_desk_info_text.pack()
        front_desk_info_text.place(x=300, y=152)

        staff_info.pack()
        staff_info.place(x=0, y=0)

        # Login frame
        login_frame = tk.Frame(frame1, bg='white', height=350, width=512)
        login_frame.place(x=450, y=0)
        login_frame.pack_propagate(False)

        tk.Label(login_frame, text="Login", font='msserif 28 bold', bg='white').place(x=70, y=0)
        tk.Label(login_frame, text="Username", font='msserif 15 bold', bg='white').place(x=70, y=50)
        tk.Label(login_frame, text="Password", font='msserif 15 bold', bg='white').place(x=70, y=100)

        username_entry = tk.Entry(login_frame, width=30, borderwidth=0, highlightthickness=0, bg='#E8ECFF')
        username_entry.place(x=70, y=80)

        password_entry = tk.Entry(login_frame, width=30, borderwidth=0, highlightthickness=0, bg='#E8ECFF', show="*")
        password_entry.place(x=70, y=130)


        frame1.pack_propagate(False)
        frame1.tkraise()
        frame1.place(x=0, y=200)

    employee_login_page()

    root.mainloop()
hotel_management_system()