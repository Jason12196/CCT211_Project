import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from typing import Dict

from PIL import Image, ImageTk
import datetime
import random

# Local SQL database


rooms_info = {
    1: {'name': 'Room 1', 'type': 'Single room  ', 'price': 119, 'beds': 1, 'wifi': 'no', 'breakfast': 'yes',
        'status': 'available', 'square': 20},
    2: {'name': 'Room 2', 'type': 'Double room  ', 'price': 229, 'beds': 1, 'wifi': 'yes', 'breakfast': 'no',
        'status': 'available', 'square': 25},
    3: {'name': 'Room 3', 'type': 'Triple room  ', 'price': 269, 'beds': 2, 'wifi': 'yes', 'breakfast': 'no',
        'status': 'available', 'square': 30},
    4: {'name': 'Room 4', 'type': 'Queen room  ', 'price': 199, 'beds': 3, 'wifi': 'yes', 'breakfast': 'no',
        'status': 'available', 'square': 35},
    5: {'name': 'Room 5', 'type': 'King room  ', 'price': 219, 'beds': 2, 'wifi': 'yes', 'breakfast': 'yes',
        'status': 'available', 'square': 50},
    6: {'name': 'Room 6', 'type': 'Ocean view room  ', 'price': 519, 'beds': 2, 'wifi': 'yes', 'breakfast': 'yes',
        'status': 'available', 'square': 50},
    7: {'name': 'Room 7', 'type': 'Garden room  ', 'price': 419, 'beds': 2, 'wifi': 'yes', 'breakfast': 'yes',
        'status': 'available', 'square': 52},
    8: {'name': 'Room 8', 'type': 'Presidential suite', 'price': 1200, 'beds': 3, 'wifi': 'yes', 'breakfast': 'yes',
        'status': 'available', 'square': 78},
}

room_photos = {
    1: 'single.jpeg',
    2: 'double.jpeg',
    3: 'triple.jpeg',
    4: 'queen.jpeg',
    5: 'king.jpeg',
    6: 'ocean_view.jpeg',
    7: 'garden.jpeg',
    8: 'presidential.jpeg',
}

payment = [
    {"order_id": 238912, "room_id": 1, "customer_name": "Tom sjaio", "customer_phone": "12345678901","check_in": "2020-12-12", "check_out": "2020-12-13", "status": "paid","price": 100, "payment_method": "cash", "payment_date": "2020-12-12 12:00:00"},
    {"order_id": 238913, "room_id": 2, "customer_name": "Bisa siao", "customer_phone": "12345678901",
     "check_in": "2020-12-12", "check_out": "2020-12-13", "status": "paid",
     "price": 238, "payment_method": "cash", "payment_date": "2020-12-12 12:00:00"},
]

admin_account = {
    "admin": "admin",
}

print(payment[1]["order_id"])


home_page = tk.Tk()
home_page.geometry("1024x600")
home_page.title("Welcome")
home_page.configure(bg="#191825")
home_page.minsize(1024, 600)
home_page.maxsize(1024, 600)
home_page_background = Image.open("home_page.png")
home_page_background = home_page_background.resize((700, 300), Image.LANCZOS)
home_page_background = ImageTk.PhotoImage(home_page_background)
home_page_background_label = tk.Label(home_page, image=home_page_background)
home_page_background_label.place(x=0, y=0, relwidth=1, relheight=1)
home_page_background_label.pack()

Header1 = tk.Label(home_page, text="Fuji Number One", font=('Arial Black', 20), bg='#191825', fg='#E8ECFF')
Header1.place(relx=0.5, rely=0.58, anchor='center')

intro_text = "Fuji Number One is a high end hotel near the Niagara Falls. " \
            "\n  " \
            "\n We attract millions of tourists each year with exciting entertainment and residence services. " \
            "\n  " \
            "\n Try to book a reservation with the button above!" \
            "\n  " \
            "\nOur amenities include:" \
            "\n  " \
            "\n- Spacious rooms with scenic views" \
            "\n  " \
            "\n- Fitness center and spa with facilities" \
            "\n  " \
            "\n- Indoor and outdoor pools" \
            "\n  " \
            "\n- 24-hour concierge and room service" \
            "\n  " \
            "\nBook your stay with us today and experience the luxury and comfort that Fuji Number One has to offer!"
intro = tk.Label(home_page, text=intro_text, font=('Arial', 10), bg='#191825', fg='#E8ECFF', justify='center')
intro.place(relx=0.5, rely=0.68, anchor='center')

enter_button = tk.Button(home_page, text="Enter", font=('Arial', 12), bg='#E8ECFF', fg='#191825', width=10, height=2, command=home_page.destroy, borderwidth=0,
               highlightthickness=0)
enter_button.place(relx=0.5, rely=0.9, anchor='center')

home_page.mainloop()

def hotel_management_system():
    root = tk.Tk()
    root.geometry("1024x600")
    root.minsize(1024, 600)
    root.maxsize(1024, 600)
    root.configure(bg='white')
    root.title("Hotel Management System")

# logout button
    def logout():
        quit = messagebox.askyesno("Exit", "Are you sure you want to exist?")
        if quit:
            root.destroy()
            return

# employee login page
    def employee_login_page():
        frame1 = tk.Frame(root, height=400, width=1024, bg='white')

        # Staff info frame
        staff_info = tk.Frame(frame1, bg='white', height=350, width=1024)

        # Manager name card
        manager = Image.open("manager.png")
        manager_photo = ImageTk.PhotoImage(manager.resize((90,100), Image.LANCZOS))
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
        front_desk_photo = ImageTk.PhotoImage(front_desk.resize((90, 100), Image.LANCZOS))
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

        def login():
            if username_entry.get() in admin_account:
                if password_entry.get() == admin_account[username_entry.get()]:
                    admin_window()
                else:
                    tk.messagebox.showerror('Error', 'Wrong Password')
            else:
                tk.messagebox.showerror('Error', 'Wrong Username')

        tk.Button(login_frame, text="Login", font='msserif 10 bold', bg='white', command=login, width=10,
                  height=2).place(x=70, y=170)

        frame1.pack_propagate(False)
        frame1.tkraise()
        frame1.place(x=0, y=200)

        def admin_window():
            admin_frame = tk.Frame(root, height=400, width=1024, bg='white')
            admin_frame.place(x=0, y=200)
            admin_frame.pack_propagate(False)

            tk.Label(admin_frame, text="Hotel State", font='msserif 20', bg='white')

            smf1 = tk.Frame(admin_frame, height=150, width=130, bg='white')
            tr = tk.Label(smf1, text='Total Rooms:', fg='white', bg='cyan4', width=100, height=2, font='helvetica 15')
            tr.pack(side='top')
            smf1.pack_propagate(False)
            smf1.place(x=30, y=30)
            tk.Label(smf1, text=len(rooms_info), fg='cyan4', bg='white', font='msserif 50').pack(anchor='center')

            avr = len([i for i in rooms_info if rooms_info[i]['status'] == 'available'])

            smf2 = tk.Frame(admin_frame, height=150, width=175, bg='white')
            ar = tk.Label(smf2, text='Available Rooms:', fg='white', bg='cyan4', width=130, height=2,
                          font='helvetica 15')
            ar.pack(side='top')
            smf2.pack_propagate(False)
            smf2.place(x=170, y=30)
            tk.Label(smf2, text=avr, fg='cyan4', bg='white', font='msserif 50').pack(anchor='center')

            rer = len([i for i in rooms_info if rooms_info[i]['status'] == 'Reserved'])

            smf3 = tk.Frame(admin_frame, height=150, width=175, bg='white')
            tre = tk.Label(smf3, text='Total reservations:', fg='white', bg='cyan4', width=130, height=2,
                           font='helvetica 15')
            tre.pack(side='top')
            smf3.pack_propagate(False)
            smf3.place(x=350, y=30)
            tk.Label(smf3, text=rer, fg='cyan4', bg='white', font='msserif 50').pack(anchor='center')

            smf4 = tk.Frame(admin_frame, height=150, width=175, bg='white')
            tc = tk.Label(smf4, text='Total Customers:', fg='white', bg='cyan4', width=130, height=2,
                          font='helvetica 15')
            tc.pack(side='top')
            smf4.pack_propagate(False)
            smf4.place(x=530, y=30)
            tk.Label(smf4, text='40', fg='cyan4', bg='white', font='msserif 50').pack(anchor='center')

            smf5 = tk.Frame(admin_frame, height=150, width=175, bg='white')
            ts = tk.Label(smf5, text='Total Staff:', fg='white', bg='cyan4', width=130, height=2, font='helvetica 15')
            ts.pack(side='top')
            smf5.pack_propagate(False)
            smf5.place(x=710, y=30)
            tk.Label(smf5, text='18', fg='cyan4', bg='white', font='msserif 50').pack(anchor='center')
            redf1 = tk.Frame(admin_frame, height=8, width=1080, bg='cyan4')

            smf6 = tk.Frame(admin_frame, height=150, width=130, bg='white')
            ts = tk.Label(smf6, text='New Order:', fg='white', bg='cyan4', width=130, height=2, font='helvetica 15')
            ts.pack(side='top')
            smf6.pack_propagate(False)
            smf6.place(x=890, y=30)
            tk.Label(smf6, text='2', fg='cyan4', bg='white', font='msserif 50').pack(anchor='center')

            redf1.place(x=0, y=22)
            tk.Label(admin_frame, text='Hotel Status', font='msserif 12', bg='cyan4', fg='white').pack(anchor='center')
            redf1.pack_propagate(False)

            def view_all_orders():
                view_order_frame = tk.Frame(root, height=400, width=1024, bg='white')
                view_order_frame.place(x=0, y=200)
                view_order_frame.pack_propagate(False)
                view_order_frame.tkraise()
                tk.Label(view_order_frame, text='All Orders', font='msserif 25', fg='black', bg='white').place(x=0, y=0)

                listbox = tk.Listbox(view_order_frame, font='msserif 10', width=1024, height=20)
                listbox.place(x=0, y=50)

                listbox.insert(tk.END,
                               "Order ID" + " " * 5 + "Room ID" + " " * 4 + "Costumer Name" + " " * 8 + "Order Time" + " " * 10 + "Order Status" + " " * 4 + "Order Price" + " " * 6 + "Reserve Time")

                for i in payment:
                    listbox.insert(tk.END, str(i["order_id"]) + " " * 10 + str(i["room_id"]) + " " * 10 + str(
                        i["customer_name"].split(' ')[1]) + " " * 10 + str(i["payment_date"]) + " " * 10 + str(
                        i["status"]) + " " * 10 + str(i["price"]) + " " * 10 + str(
                        i["check_in"] + "-" + i["check_out"]))

                tk.Button(view_order_frame, text='Back', font='msserif 10 bold', bg='white', command=lambda: view_order_frame.destroy(),
                          width=15, height=2).place(x=200, y=0)

                def cancel_order():
                    cancel_order_frame = tk.Frame(root, height=400, width=1024, bg='white')
                    cancel_order_frame.place(x=0, y=200)
                    cancel_order_frame.pack_propagate(False)
                    cancel_order_frame.tkraise()
                    tk.Label(cancel_order_frame, text='Cancel Order', font='msserif 25', fg='black', bg='white').place(x=0, y=0)
                    tk.Label(cancel_order_frame, text='Order ID', font='msserif 10', fg='black', bg='white').place(x=0, y=50)
                    order_id = tk.Entry(cancel_order_frame)
                    order_id.place(x=100, y=50)
                    tk.Button(cancel_order_frame, text='back', font='msserif 10 bold', bg='white', command=lambda: cancel_order_frame.destroy(),
                          width=15, height=2).place(x=300, y=0)

                    def cancel():
                        if order_id.get() == '':
                            messagebox.showinfo("Error", "Please enter order id")
                        else:
                            for i in payment:
                                if str(i["order_id"]) == str(order_id.get()):
                                    del payment[payment.index(i)]
                                    messagebox.showinfo("Success", "Order Cancelled")
                                    break
                            else:
                                messagebox.showinfo("Error", "Order ID not found")

                    tk.Button(cancel_order_frame, text='Cancel Order', font='msserif 10 bold', bg='white', command=cancel).place(x=400, y=0)

                tk.Button(view_order_frame, text='Cancel', font='msserif 10 bold', bg='white',command=cancel_order,
                          width=15, height=2).place(x=400, y=0)
            tk.Button(admin_frame, text='View All Orders', font='msserif 10 bold', bg='white', command=view_all_orders,width=15, height=2).place(x=50, y=300)



# room reservation page
    def room_reservation_page():

        frame2 = tk.Frame(root, height=400, width=1024, bg='white')
        frame2.place(x=0, y=200)
        frame2.pack_propagate(False)
        frame2.tkraise()

    # Personal information frame
        tk.Label(frame2, text="Personal Information", font='msserif 20', bg='white').place(x=255, y=0)

    # First name
        first_name_frame = tk.Frame(frame2, height=1, width=1)
        first_name = tk.Entry(first_name_frame)
        first_name.insert(0, "First Name*")
        first_name_frame.place(x=20, y=50)
        first_name.pack(ipady=4, ipadx=15)
        def on_entry_click_first_name():
            if first_name.get() == "First Name*":
                first_name.delete(0, "end")
                first_name.insert(0, "")
                first_name.config(fg='black')
        def on_exit_click_first_name():
            if first_name.get() == "":
                first_name.insert(0, "First Name*")
                first_name.config(fg='grey')
        first_name.bind('<FocusIn>', lambda args: on_entry_click_first_name())
        first_name.bind('<FocusOut>', lambda args: on_exit_click_first_name())

    # Last name
        last_name_frame = tk.Frame(frame2, height=1, width=1)
        last_name = tk.Entry(last_name_frame)
        last_name.insert(0, "Last Name*")
        last_name_frame.place(x=235, y=50)
        last_name.pack(ipady=4, ipadx=15)
        def on_entry_click_last_name():
            if last_name.get() == "Last Name*":
                last_name.delete(0, "end")
                last_name.insert(0, "")
                last_name.config(fg='black')
        def on_exit_click_last_name():
            if last_name.get() == "":
                last_name.insert(0, "Last Name*")
                last_name.config(fg='grey')
        last_name.bind('<FocusIn>', lambda args: on_entry_click_last_name())
        last_name.bind('<FocusOut>', lambda args: on_exit_click_last_name())

    # Phone number
        phone_number_frame = tk.Frame(frame2, height=1, width=1)
        phone_number = tk.Entry(phone_number_frame)
        phone_number.insert(0, "Phone Number*")
        phone_number_frame.place(x=450, y=50)
        phone_number.pack(ipady=4, ipadx=15)
        def on_entry_click_phone_number():
            if phone_number.get() == "Phone Number*":
                phone_number.delete(0, "end")
                phone_number.insert(0, "")
                phone_number.config(fg='black')
        def on_exit_click_phone_number():
            if phone_number.get() == "":
                phone_number.insert(0, "Phone Number*")
                phone_number.config(fg='grey')
        phone_number.bind('<FocusIn>', lambda args: on_entry_click_phone_number())
        phone_number.bind('<FocusOut>', lambda args: on_exit_click_phone_number())

    # Identity information frame
        tk.Label(frame2, text="Identity Information", font='msserif 20', bg='white').place(x=255, y=100)

    # passport number
        passport_number_frame = tk.Frame(frame2, height=1, width=1)
        passport_number = tk.Entry(passport_number_frame)
        passport_number.insert(0, "Passport Number*")
        passport_number_frame.place(x=20, y=150)
        passport_number.pack(ipady=4, ipadx=15)
        def on_entry_click_passport_number():
            if passport_number.get() == "Passport Number*":
                passport_number.delete(0, "end")
                passport_number.insert(0, "")
                passport_number.config(fg='black')
        def on_exit_click_passport_number():
            if passport_number.get() == "":
                passport_number.insert(0, "Passport Number*")
                passport_number.config(fg='grey')
        passport_number.bind('<FocusIn>', lambda args: on_entry_click_passport_number())
        passport_number.bind('<FocusOut>', lambda args: on_exit_click_passport_number())

    # check in date
        check_in_date_frame = tk.Frame(frame2, height=1, width=1)
        check_in_date = tk.Entry(check_in_date_frame)
        check_in_date.insert(0, "Check In Date(yyyy-mm-dd)*")
        check_in_date_frame.place(x=235, y=150)
        check_in_date.pack(ipady=4, ipadx=15)
        def on_entry_click_check_in_date():
            if check_in_date.get() == "Check In Date(yyyy-mm-dd)*":
                check_in_date.delete(0, "end")
                check_in_date.insert(0, "")
                check_in_date.config(fg='black')
        def on_exit_click_check_in_date():
            if check_in_date.get() == "":
                check_in_date.insert(0, "Check In Date(yyyy-mm-dd)*")
                check_in_date.config(fg='grey')
        check_in_date.bind('<FocusIn>', lambda args: on_entry_click_check_in_date())
        check_in_date.bind('<FocusOut>', lambda args: on_exit_click_check_in_date())

    # check out date
        check_out_date_frame = tk.Frame(frame2, height=1, width=1)
        check_out_date = tk.Entry(check_out_date_frame)
        check_out_date.insert(0, "Check Out Date(yyyy-mm-dd)*")
        check_out_date_frame.place(x=450, y=150)
        check_out_date.pack(ipady=4, ipadx=15)
        def on_entry_click_check_out_date():
            if check_out_date.get() == "Check Out Date(yyyy-mm-dd)*":
                check_out_date.delete(0, "end")
                check_out_date.insert(0, "")
                check_out_date.config(fg='black')
        def on_exit_click_check_out_date():
            if check_out_date.get() == "":
                check_out_date.insert(0, "Check Out Date*(yyyy-mm-dd)")
                check_out_date.config(fg='grey')
        check_out_date.bind('<FocusIn>', lambda args: on_entry_click_check_out_date())
        check_out_date.bind('<FocusOut>', lambda args: on_exit_click_check_out_date())

    # Reservation information frame
        tk.Label(frame2, text="Reservation Information", font='msserif 20', bg='white').place(x=255, y=200)

        # children
        children_frame = tk.Frame(frame2, height=1, width=1)
        children = tk.Entry(children_frame)
        children.insert(0, "Number of Children*")
        children_frame.place(x=20, y=250)
        children.pack(ipady=4, ipadx=15)
        def on_entry_click_children():
            if children.get() == "Number of Children*":
                children.delete(0, "end")
                children.insert(0, "")
                children.config(fg='black')
        def on_exit_click_children():
            if children.get() == "":
                children.insert(0, "Number of Children*")
                children.config(fg='grey')
        children.bind('<FocusIn>', lambda args: on_entry_click_children())
        children.bind('<FocusOut>', lambda args: on_exit_click_children())

        # adults
        adults_frame = tk.Frame(frame2, height=1, width=1)
        adults = tk.Entry(adults_frame)
        adults.insert(0, "Number of Adults*")
        adults_frame.place(x=235, y=250)
        adults.pack(ipady=4, ipadx=15)
        def on_entry_click_adults():
            if adults.get() == "Number of Adults*":
                adults.delete(0, "end")
                adults.insert(0, "")
                adults.config(fg='black')
        def on_exit_click_adults():
            if adults.get() == "":
                adults.insert(0, "Number of Adults*")
                adults.config(fg='grey')
        adults.bind('<FocusIn>', lambda args: on_entry_click_adults())
        adults.bind('<FocusOut>', lambda args: on_exit_click_adults())

        # Days of stay
        days_of_stay_frame = tk.Frame(frame2, height=1, width=1)
        days_of_stay = tk.Entry(days_of_stay_frame)
        days_of_stay.insert(0, "Days of Stay*")
        days_of_stay_frame.place(x=450, y=250)
        days_of_stay.pack(ipady=4, ipadx=15)
        def on_entry_click_days_of_stay():
            if days_of_stay.get() == "Days of Stay*":
                days_of_stay.delete(0, "end")
                days_of_stay.insert(0, "")
                days_of_stay.config(fg='black')
        def on_exit_click_days_of_stay():
            if days_of_stay.get() == "":
                days_of_stay.insert(0, "Days of Stay*")
                days_of_stay.config(fg='grey')
        days_of_stay.bind('<FocusIn>', lambda args: on_entry_click_days_of_stay())
        days_of_stay.bind('<FocusOut>', lambda args: on_exit_click_days_of_stay())

    # Room choosen frame
        room_chosen_frame = tk.Frame(frame2, height=1, width=1)
        room_choosen = tk.Entry(room_chosen_frame)
        room_choosen.insert(0, "Enter Room Number*")
        room_chosen_frame.place(x=20, y=300)
        room_choosen.pack(ipady=4, ipadx=15)
        def on_entry_click_room_choosen():
            if room_choosen.get() == "Enter Room Number*":
                room_choosen.delete(0, "end")
                room_choosen.insert(0, "")
                room_choosen.config(fg='black')
        def on_exit_click_room_choosen():
            if room_choosen.get() == "":
                room_choosen.insert(0, "Enter Room Number*")
                room_choosen.config(fg='grey')
        room_choosen.bind('<FocusIn>', lambda args: on_entry_click_room_choosen())
        room_choosen.bind('<FocusOut>', lambda args: on_exit_click_room_choosen())

        # Payment Method
        payment_method_frame = tk.Frame(frame2, height=1, width=1)
        payment_method = ttk.Combobox(payment_method_frame, width = 22, values=("Please select payment method...", "Cash", "Credit Card", "Debit Card", "WeChat"), state="readonly")
        # Combobox shuts down Jason's MacBook, but not Windows machine
        payment_method.current(0)
        payment_method_frame.place(x=400, y=300)
        payment_method.pack(ipady=4, ipadx=15)

    # Selection filter frame
        tk.Label(frame2, text="Selection Filter", font='msserif 20', bg='white', fg='black').place(x=800, y=0)

        # Beds Filter
        beds_label = tk.Label(frame2, text="Bed(s): ", font='msserif 15', bg='white', fg='black')
        beds_label.place(x=745, y=50)

        beds = tk.IntVar()
        beds.set(0)
        #This set of RedioButtons is crashing the program, need a fix
        tk.Radiobutton(frame2, text="1", variable=beds, value=1, bg='white', fg='black').place(x=800, y=50)
        tk.Radiobutton(frame2, text="2", variable=beds, value=2, bg='white', fg='black').place(x=850, y=50)
        tk.Radiobutton(frame2, text="3", variable=beds, value=3, bg='white', fg='black').place(x=900, y=50)

        # breakfast filter
        breakfast_label = tk.Label(frame2, text="Breakfast: ", font='msserif 15', bg='white', fg='black')
        breakfast_label.place(x=725, y=75)
        breakfast = tk.IntVar()
        breakfast.set(0)
        #This set of RedioButtons is crashing the program, need a fix
        tk.Radiobutton(frame2, text="Yes", variable=breakfast, value=1, bg='white', fg='black').place(x=800, y=75)
        tk.Radiobutton(frame2, text="No", variable=breakfast, value=2, bg='white', fg='black').place(x=850, y=75)

        # Wifi filter
        wifi_label = tk.Label(frame2, text="Wifi: ", font='msserif 15', bg='white', fg='black')
        wifi_label.place(x=765, y=100)
        wifi = tk.IntVar()
        wifi.set(0)
        #This set of RedioButtons is crashing the program, need a fix
        tk.Radiobutton(frame2, text="Yes", variable=wifi, value=1, bg='white', fg='black').place(x=800, y=100)
        tk.Radiobutton(frame2, text="No", variable=wifi, value=2, bg='white', fg='black').place(x=850, y=100)

        # Room Type filter
        room_type_label = tk.Label(frame2, text="Room Type: ", font='msserif 15', bg='white', fg='black')
        room_type_label.place(x=712, y=125)
        room_type = tk.IntVar()
        room_type.set(0)
        tk.Radiobutton(frame2, text="Single", variable=room_type, value=1, bg='white', fg='black').place(x=800, y=125)
        tk.Radiobutton(frame2, text="Double", variable=room_type, value=2, bg='white', fg='black').place(x=870, y=125)
        tk.Radiobutton(frame2, text="Triple", variable=room_type, value=3, bg='white', fg='black').place(x=940, y=125)
        tk.Radiobutton(frame2, text="Queen", variable=room_type, value=4, bg='white', fg='black').place(x=800, y=150)
        tk.Radiobutton(frame2, text="King", variable=room_type, value=5, bg='white', fg='black').place(x=870, y=150)
        tk.Radiobutton(frame2, text="Ocean View", variable=room_type, value=6, bg='white', fg='black').place(x=920, y=150)
        tk.Radiobutton(frame2, text="Garden", variable=room_type, value=7, bg='white', fg='black').place(x=800, y=175)
        tk.Radiobutton(frame2, text="Presidental Suite", variable=room_type, value=8, bg='white', fg='black').place(x=870, y=175)

        # Price filter
        price_label = tk.Label(frame2, text="Price: ", font='msserif 15', bg='white', fg='black')
        price_label.place(x=700, y=200)
        # Low price tag
        low_price = tk.Entry(frame2, width=13)
        low_price.insert(0, "Lowest Acceptable")
        low_price.place(x=750, y=200)

        def on_click_low_price(event):
            low_price.delete(0, tk.END)

        low_price.bind("<Button-1>", on_click_low_price)

        def exit_low_price(event):
            if low_price.get() == "":
                low_price.insert(0, "Lowest Acceptable")

        low_price.bind("<FocusOut>", exit_low_price)

        # High price tag
        high_price = tk.Entry(frame2, width=13)
        high_price.insert(0, "Highest Acceptable")
        high_price.place(x=880, y=200)

        def on_click_high_price(event):
            high_price.delete(0, tk.END)

        high_price.bind("<Button-1>", on_click_high_price)

        def exit_high_price(event):
            if high_price.get() == "":
                high_price.insert(0, "Highest Acceptable")

        high_price.bind("<FocusOut>", exit_high_price)

        # List of rooms
        room_list = tk.Listbox(frame2, height=7, width=40, font='msserif 12', bg='white', fg='black', selectbackground='green', selectforeground='white')
        room_list.place(x=700, y=260)
        room_list.insert(tk.END, "Rooms of your search will appear here")
        
        def find_room():
            bed = beds.get()
            breakfast1 = breakfast.get()
            wifi1 = wifi.get()
            type1 = room_type.get()
            low = low_price.get()
            high = high_price.get()
            if breakfast1 == 1:
                breakfast1 = "yes"
            if breakfast1 == 2:
                breakfast1 = "no"
            if wifi1 == 1:
                wifi1 = "yes"
            if wifi1 == 2:
                wifi1 = "no"
            if type1 == 1:
                type1 = "Single room"
            if type1 == 2:
                type1 = "Double room"
            if type1 == 3:
                type1 = "Triple room"
            if type1 == 4:
                type1 = "Queen room"
            if type1 == 5:
                type1 = "King-size room"
            if type1 == 6:
                type1 = "Ocean view room"
            if type1 == 7:
                type1 = "Garden view room"
            if type1 == 8:
                type1 = "Presidential suite"
            print(bed, breakfast1, wifi1, type1, low, high)

            beds_rooms = set([i for i in rooms_info if rooms_info[i]['beds'] == bed]) if bed != 0 else set(
                [i for i in rooms_info])
            breakfast_rooms = beds_rooms if breakfast1 == 0 else set(
                [i for i in beds_rooms if rooms_info[i]['breakfast'] == breakfast1])
            wifi_rooms = breakfast_rooms if wifi1 == 0 else set(
                [i for i in breakfast_rooms if rooms_info[i]['wifi'] == wifi1])
            type_rooms = wifi_rooms if type1 == 0 else set(
                [i for i in wifi_rooms if rooms_info[i]['type'].strip() == type1])
            print(beds_rooms, breakfast_rooms, wifi_rooms, type_rooms)
            lower_price_rooms = type_rooms.copy()
            list_of_room = lower_price_rooms.copy()
            if low != 'Low Price' and low != '' and list_of_room:
                try:
                    low = int(low)
                    for i in type_rooms:
                        if rooms_info[i]["price"] < low:
                            lower_price_rooms.remove(i)
                except:
                    lower_price_rooms = type_rooms
            if high != 'High Price' and high != '' and list_of_room:
                try:
                    high = int(high)
                    for i in lower_price_rooms:
                        print(i, rooms_info[i]["price"])
                        if rooms_info[i]["price"] > high:
                            print(i)
                            list_of_room.remove(i)
                except:
                    list_of_room = list(lower_price_rooms)
            print(lower_price_rooms, list_of_room)
            room_list.delete(0, tk.END)
            if list_of_room:
                room_list.insert(tk.END, 'Room id ' + ' ' * 10 + 'Price')
                for i in list_of_room:
                    room_list.insert(tk.END, ' ' * 8 + str(i) + ' ' * 18 + str(rooms_info[i]['price']))
            else:
                room_list.insert(tk.END, 'No rooms match your filter')

        # Find Rooms button
        tk.Button(frame2, text='Find Rooms', bg='white', fg='cyan4', font='msserif 12',activebackground='green', width=10, height=1, command=find_room).place(x=820, y=230)
        
        # Book Room function
        def book_room():
            if first_name.get() == "First Name *" or last_name.get() == "Last Name *" or phone_number.get() == "Phone Number*" or \
                    passport_number.get() == "Passport Number *" or check_in_date.get() == "Check In Date(yyyy-mm-dd)*" or \
                    check_out_date.get() == "Check Out Date(yyyy-mm-dd) *" or children.get() == "Number of Children*" or \
                    adults.get() == "Number of Adults*" or days_of_stay.get() == "Days of Stay*" or \
                    room_choosen.get() == "Room Number*" or payment_method.get() == "Please select payment method...":

                messagebox.showerror("Error", "Please fill in all required information")

            elif first_name.get() == '' or last_name.get() == '' or phone_number.get() == '' or passport_number.get() == '' or \
                    check_in_date.get() == '' or check_out_date.get() == '' or children.get() == '' or adults.get() == '' or \
                    days_of_stay.get() == '' or room_choosen.get() == '' or payment_method.get() == '':

                messagebox.showerror("Error", "Please fill in all required information")

            elif room_choosen.get().isdigit() is False:
                messagebox.showerror("Error", "Please enter a valid room number")

            else:
                order_id = 238914
                room_id = int(room_choosen.get())
                checkindate = check_in_date.get()
                checkoutdate = check_out_date.get()
                today = datetime.date.today()

                today = today.strftime("%Y-%m-%d")

                if room_id not in rooms_info:
                    messagebox.showerror("Error", "Please enter a valid room number")
                elif checkindate > checkoutdate:
                    messagebox.showerror("Error", "Please enter a valid check in and check out date")
                elif checkindate == checkoutdate or checkindate < today or checkoutdate < today:
                    messagebox.showerror("Error", "Please enter a valid check in and check out date")

                else:
                    for order in payment:
                        if order["room_id"] == room_id and order["check_in"] == checkindate and order["check_out"] == checkoutdate:
                            messagebox.showerror("Error", "This room has been booked")
                            break
                    else:
                        d: dict[str, int | str] = {"order_id": order_id, "room_id": room_id, "costumer_name": str(first_name.get() + " " + last_name.get()), "costumer_phone": str(phone_number.get()),"check_in": str(checkindate),"check_out": str(checkoutdate),"price": rooms_info[room_id]["price"] * int(days_of_stay.get()),"status": "paid","payment_method": str(payment_method.get()),"payment_date": str(datetime.date.today().strftime("%Y-%m-%d")),}

                        payment.append(
                            d
                        )

                        order_root = tk.Tk()

                        order_root.title("Order Information")
                        order_root.minsize(height=400, width=400)
                        order_root.configure(bg='White')
                        tk.Label(order_root, text='Order Information', font='msserif 14 bold', bg='White').place(x=10,
                                                                                                                y=0)
                        tk.Frame(order_root, height=4, width=300, bg='cyan4').place(x=10, y=39)
                        tk.Label(order_root, text='Order ID: ' + str(order_id), font='msserif 12 bold',
                                 bg='White').place(x=10,
                                                   y=50)
                        tk.Label(order_root, text='Room ID: ' + str(room_id), font='msserif 12 bold', bg='White').place(
                            x=10,
                            y=80)
                        tk.Label(order_root, text='Costumer Name: ' + first_name.get() + " " + last_name.get(),
                                 font='msserif 12 bold', bg='White').place(x=10, y=110)
                        tk.Label(order_root, text='Check In Date: ' + checkindate, font='msserif 12 bold',
                                 bg='White').place(
                            x=10, y=140)
                        tk.Label(order_root, text='Check Out Date: ' + checkoutdate, font='msserif 12 bold',
                                 bg='White').place(
                            x=10, y=170)
                        tk.Label(order_root, text='Price: ' + str(rooms_info[room_id]["price"] * int(days_of_stay.get())),
                                 font='msserif 12 bold', bg='White').place(x=10, y=200)
                        tk.Label(order_root, text='Status: paid', font='msserif 12 bold', bg='White').place(x=10, y=230)
                        tk.Label(order_root, text='Payment Method: ' + payment_method.get(), font='msserif 12 bold',
                                 bg='White').place(x=10, y=260)
                        tk.Label(order_root, text='Payment Date: ' + datetime.date.today().strftime("%Y-%m-%d"),
                                 font='msserif 12 bold', bg='White').place(x=10, y=290)
                        tk.Button(order_root, text='OK', font='msserif 12 bold', bg='cyan4', fg='White',
                                  command=order_root.destroy).place(x=160, y=330)

                        order_root.mainloop()

        # Book Room button
        tk.Button(frame2, text='Book Room', bg='white', fg='cyan4', font='msserif 12',activebackground='green', width=10, height=1, command=book_room).place(x=300, y=350)

# room information page
    def room_information_page():
        frame3 = tk.Frame(root, height=400, width=1024, bg='white')
        frame3.place(x=0, y=200)
        frame3.pack_propagate(False)
        frame3.tkraise()

        # Room information frame
        tk.Label(frame3, font='msserif 20', bg='white').place(x=255, y=0)

        # Room picture frame
        room_picture_frame = tk.Frame(frame3, height=400, width=500, bg='white')
        room_picture_frame.place(x=212, y=0)

        # Room information display frame
        room_info_display_frame = tk.Frame(frame3, height=400, width=300, bg='white')
        room_info_display_frame.place(x=724, y=0)
        room_info_display_frame.pack_propagate(False)
        display_label_1 = tk.Label(room_info_display_frame, text="Room Information", font='msserif 14 bold', bg='white', fg='black')
        display_label_1.place(x=0, y=0)
        display_label_2 = tk.Label(room_info_display_frame, text="Selected room information will appear here", font='msserif 10', bg='white', fg='black')
        display_label_2.place(x=0, y=40)
        display_label_3 = tk.Label(room_info_display_frame, text="Room status: ", font='msserif 10', bg='white', fg='black')
        display_label_3.place(x=0, y=70)
        display_label_4 = tk.Label(room_info_display_frame, text="Room status: ", font='msserif 10', bg='white', fg='black')
        display_label_4.place(x=0, y=110)
        display_label_5 = tk.Label(room_info_display_frame, text="Room status: ", font='msserif 10', bg='white', fg='black')
        display_label_5.place(x=0, y=150)
        display_label_6 = tk.Label(room_info_display_frame, text="Room status: ", font='msserif 10', bg='white', fg='black')
        display_label_6.place(x=0, y=230)
        display_label_7 = tk.Label(room_info_display_frame, text="Room status: ", font='msserif 10', bg='white', fg='black')
        display_label_7.place(x=0, y=270)
        display_label_8 = tk.Label(room_info_display_frame, text="Room status: ", font='msserif 10', bg='white', fg='black')
        display_label_8.place(x=0, y=310)
        display_label_9 = tk.Label(room_info_display_frame, text="Room status: ", font='msserif 10', bg='white', fg='black')
        display_label_9.place(x=0, y=350)

        def room_info(room_number):
            room = rooms_info[room_number]
            display_label_2.config(text="Room Number: " + str(room_number))
            display_label_3.config(text="Room status: " + room['status'])
            display_label_4.config(text="Room price: " + str(room['price']))
            display_label_5.config(text="Bed number: " + str(room['beds']))
            display_label_6.config(text="WiFi Availability: " + room['wifi'])
            display_label_7.config(text="Breakfast Availability: " + room['breakfast'])
            display_label_8.config(text="Room square footage: " + str(room['square']))
            display_label_9.config(text="Room type: " + room['type'])

            img = Image.open(room_photos[room_number])
            room_picture = ImageTk.PhotoImage(img.resize((450, 350), Image.ANTIALIAS))
            room_picture_label = tk.Label(room_picture_frame, image=room_picture, height=350, width=450)
            room_picture_label.image = room_picture
            room_picture_label.place(x=0, y=0)

        button1 = tk.Button(frame3, text='Room 1', bg='white', fg='cyan4', font='msserif 12',width=10, height=1, command=lambda: room_info(1))
        button1.place(x=80, y=0)
        button2 = tk.Button(frame3, text='Room 2', bg='white', fg='cyan4', font='msserif 12',width=10, height=1, command=lambda: room_info(2))
        button2.place(x=80, y=40)
        button3 = tk.Button(frame3, text='Room 3', bg='white', fg='cyan4', font='msserif 12',width=10, height=1, command=lambda: room_info(3))
        button3.place(x=80, y=80)
        button4 = tk.Button(frame3, text='Room 4', bg='white', fg='cyan4', font='msserif 12',width=10, height=1, command=lambda: room_info(4))
        button4.place(x=80, y=120)
        button5 = tk.Button(frame3, text='Room 5', bg='white', fg='cyan4', font='msserif 12',width=10, height=1, command=lambda: room_info(5))
        button5.place(x=80, y=160)
        button6 = tk.Button(frame3, text='Room 6', bg='white', fg='cyan4', font='msserif 12',width=10, height=1, command=lambda: room_info(6))
        button6.place(x=80, y=200)
        button7 = tk.Button(frame3, text='Room 7', bg='white', fg='cyan4', font='msserif 12',width=10, height=1, command=lambda: room_info(7))
        button7.place(x=80, y=240)
        button8 = tk.Button(frame3, text='Room 8', bg='white', fg='cyan4', font='msserif 12',width=10, height=1, command=lambda: room_info(8))
        button8.place(x=80, y=280)


# top frame
    top_frame = tk.Frame(root, height=50, width=1024, bg='cyan4')
    label = tk.Label(top_frame, height=50, width=1080)
    label.place(x=0, y=0)
    top_frame.place(x=0, y=0)

    top_frame_title = tk.Label(top_frame, text="Hotel Management System", font='Arial 30 bold', bg='cyan4', height=50, width=1024, fg='white', anchor='center')
    top_frame_title.pack()

    top_frame.pack_propagate(False)

# Selection Menu Frame
    selection_menu_frame = tk.Frame(root, height=95, width=1024, bg='white')
    selection_menu_frame.place(x=0, y= 50 + 5)

    img1 = Image.open("rooms.png")
    Image_1 = ImageTk.PhotoImage(img1.resize((90, 65), Image.ANTIALIAS))
    selection_1 = tk.Button(selection_menu_frame, image=Image_1, bg='white', width=180, command=room_information_page)
    selection_1.image = Image_1
    selection_1.place(x=122, y=0)
    selection_1_label = tk.Label(selection_menu_frame, text='Room Information', font='msserif 13', fg='black', bg='white')
    selection_1_label.place(x= 122 + 100 - 60, y=75)

    img2 = Image.open("book_room.png")
    Image_2 = ImageTk.PhotoImage(img2.resize((70, 65), Image.ANTIALIAS))
    selection_2 = tk.Button(selection_menu_frame, image=Image_2, bg='white', width=180, command=room_reservation_page)
    selection_2.image = Image_2
    selection_2.place(x= 122 + 200, y=0)
    selection_2_label = tk.Label(selection_menu_frame, text='Book A Room', font='msserif 13', fg='black', bg='white')
    selection_2_label.place(x= 122 + 300 - 45, y=75)

    img3 = Image.open("manager.png")
    Image_3 = ImageTk.PhotoImage(img3.resize((55, 65), Image.ANTIALIAS))
    selection_3 = tk.Button(selection_menu_frame, image=Image_3, bg='white', width=180, command=employee_login_page)
    selection_3.image = Image_3
    selection_3.place(x= 122 + 400 , y=0)
    selection_3_label = tk.Label(selection_menu_frame, text='Employee System', font='msserif 13', fg='black', bg='white')
    selection_3_label.place(x= 122 + 500 - 58, y=75)

    img4 = Image.open("exit.png")
    Image_4 = ImageTk.PhotoImage(img4.resize((70, 65), Image.ANTIALIAS))
    selection_4 = tk.Button(selection_menu_frame, image=Image_4, bg='white', width=180, command=logout)
    selection_4.image = Image_4
    selection_4.place(x= 122 + 600, y=0)
    selection_4_label = tk.Label(selection_menu_frame, text='Exit', font='msserif 13', fg='black', bg='white')
    selection_4_label.place(x= 122 + 700 - 20, y=75)

    selection_menu_frame.pack_propagate(False)
    label = tk.Label(root, height=400, width=1024, bg='white')
    label.place(x=0, y= 200)

    room_reservation_page()

    root.mainloop()
hotel_management_system()