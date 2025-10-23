import tkinter as tk

root = tk.Tk()
root.geometry("500x500")
root.title('МУЗЕЙ')
root.resizable(False, False)
root.config(background='#8c8269')
root.iconbitmap('museum_3584.ico')


def Autorizashion():
    global image_l
    window_requs_avto = tk.Label(root, bg="#504a3b",
                                 width=50, height=25)
    window_requs_avto.place(x=76, y=64)
    text_avtorization = tk.Label(window_requs_avto,
                                 text='АВТОРИЗАЦИЯ',
                                 bg="#504a3b",
                                 fg='white',
                                 width=35,
                                 height=3,
                                 font=('', 12, 'bold'),
                                 border=1,
                                 borderwidth=1,
                                 relief='groove')
    text_avtorization.place(y=0, x=0)

    pole_login = tk.Label(window_requs_avto,
                          text='ВАШ ЛОГИН:',
                          background='#504a3b',
                          fg='white',
                          font=('', 12))
    pole_login.place(x=30, y=80)

    entry_login = tk.Entry(window_requs_avto,
                           width=20,
                           background='#504a3b',
                           fg='white',
                           font=('', 10, 'bold'))
    entry_login.place(x=170, y=80)

    pole_password = tk.Label(window_requs_avto,
                             text='ВАШ ПАРОЛЬ:',
                             background='#504a3b',
                             fg='white',
                             font=('', 12))
    pole_password.place(x=30, y=120)

    entry_paswo = tk.Entry(window_requs_avto,
                           width=20,
                           background='#504a3b',
                           fg='white',
                           font=('', 10, 'bold'))
    entry_paswo.place(x=170, y=120)

    button_entrance = tk.Button(window_requs_avto,
                                width=20,
                                background="#3f3a2d",
                                text='ВОЙТИ',
                                font=('', 12, 'bold'),
                                fg='white')
    button_entrance.place(x=75, y=290)

    button_requstration = tk.Label(window_requs_avto,
                                   text='РЕГИСТРАЦИЯ',
                                   background='#504a3b',
                                   fg="#332f24",
                                   font=('', 12, 'bold'))
    button_requstration.place(x=120, y=330)

    image_l = tk.PhotoImage(file='logg.png')
    image_l = image_l.subsample(5)
    image_label = tk.Label(window_requs_avto,
                           image=image_l,
                           background='#504a3b')
    image_label.place(x=55, y=160)


Autorizashion()

root.mainloop()
