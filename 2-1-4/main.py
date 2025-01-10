import tkinter as tk
import tkinter.font as tkFont

# main window
root = tk.Tk()
root.wm_geometry("300x200")

# create empty frame
frame_login = tk.Frame(root)
frame_auth = tk.Frame(root)

# activate the grid in our new frame
frame_login.grid(row=0, column=0, sticky="news")
frame_auth.grid(row=0, column=0, sticky="news")

def login():
    frame_auth.tkraise()

# widgets for frame_login
normal_font = tkFont.Font(family="Arial", size=12, weight=tkFont.BOLD)
lbl_username = tk.Label(frame_login, text='Username:', font=normal_font, fg="red")
lbl_username.pack(padx=50)

# Text box for username
ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack()

lbl_password = tk.Label(frame_login, text='Password:', font=normal_font, fg="red")
lbl_password.pack(padx=50)

ent_password = tk.Entry(frame_login, bd=3)
ent_password.pack()

button_login = tk.Button(frame_login, text='Login', font=normal_font, fg="red", command=login)
button_login.pack(pady=10)

# Auth frame label
lbl_authorized = tk.Label(frame_auth, text='Authorization Screen', font='Times 14')
lbl_authorized.pack(padx=50)

frame_login.tkraise()

root.mainloop()
