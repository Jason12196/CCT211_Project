import tkinter as tk
from PIL import Image, ImageTk



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
             "\n We attract millions of tourists each year with exciting entertainment and residence services. " \
             "\n Try to book a reservation with the button above!" \
             "\nOur amenities include:" \
             "\n- Spacious rooms with scenic views" \
             "\n- Fitness center and spa with facilities" \
             "\n- Indoor and outdoor pools" \
             "\n- 24-hour concierge and room service" \
             "\nBook your stay with us today and experience the luxury and comfort that Fuji Number One has to offer!"

intro = tk.Label(home_page, text=intro_text, font=('Arial', 9), bg='#191825', fg='#E8ECFF', justify='center')
intro.place(relx=0.5, rely=0.7, anchor='center')

enter_button = tk.Button(home_page, text="Enter", font=('Arial', 12), bg='#E8ECFF', fg='#191825', width=10, height=2, command=home_page.destroy, borderwidth=0,
               highlightthickness=0)
enter_button.place(relx=0.5, rely=0.9, anchor='center')

home_page.mainloop()