import tkinter as tk
from connect import Authorization, Exposition, Exhibit, Authors
from tkinter import messagebox

root = tk.Tk()
root.geometry("500x500")
root.title('МУЗЕЙ')
root.resizable(False, False)
root.config(background='#8c8269')
root.iconbitmap('museum_3584.ico')

current_window = None


def Autorizashion():
    global image_l, current_window
    if current_window:
        current_window.destroy()

    current_window = tk.Label(root, bg="#504a3b",
                              width=50, height=25)
    current_window.place(x=76, y=64)

    text_avtorization = tk.Label(current_window,
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

    pole_login = tk.Label(current_window,
                          text='ВАШ ЛОГИН:',
                          background='#504a3b',
                          fg='white',
                          font=('', 12))
    pole_login.place(x=30, y=80)

    entry_login = tk.Entry(current_window,
                           width=20,
                           background='#504a3b',
                           fg='white',
                           font=('', 10, 'bold'))
    entry_login.place(x=170, y=80)

    pole_password = tk.Label(current_window,
                             text='ВАШ ПАРОЛЬ:',
                             background='#504a3b',
                             fg='white',
                             font=('', 12))
    pole_password.place(x=30, y=120)

    entry_paswo = tk.Entry(current_window,
                           width=20,
                           background='#504a3b',
                           fg='white',
                           font=('', 10, 'bold'),
                           show='*')
    entry_paswo.place(x=170, y=120)

    def voiti():
        login = entry_login.get()
        password = entry_paswo.get()

        def get_zap():
            zap = Authorization.select()
            return zap

        vse_bd = get_zap()

        status = 0

        for i in vse_bd:
            if login == i.login and password == i.password:
                status = 1
                current_window.destroy()
                glavnui()
                break
            else:
                status = 0

        if status == 0:
            messagebox.showwarning("Ошибка", "Неверный логин или пароль")
        else:
            messagebox.showinfo("Успех", "Добро пожаловать!")

    button_entrance = tk.Button(current_window,
                                width=20,
                                background="#3f3a2d",
                                text='ВОЙТИ',
                                font=('', 12, 'bold'),
                                fg='white',
                                command=voiti)
    button_entrance.place(x=75, y=290)

    button_requstration = tk.Label(current_window,
                                   text='РЕГИСТРАЦИЯ',
                                   background='#504a3b',
                                   fg="#332f24",
                                   font=('', 12, 'bold'))
    button_requstration.place(x=120, y=330)
    button_requstration.bind('<Button-1>', lambda _: Requstrat())

    image_l = tk.PhotoImage(file='logg.png')
    image_l = image_l.subsample(5)
    image_label = tk.Label(current_window,
                           image=image_l,
                           background='#504a3b')
    image_label.place(x=55, y=160)


def Requstrat():
    global image_l, current_window
    if current_window:
        current_window.destroy()

    current_window = tk.Label(root, bg="#504a3b",
                              width=50, height=25)
    current_window.place(x=76, y=64)

    text_avtorization = tk.Label(current_window,
                                 text='РЕГИСТРАЦИЯ',
                                 bg="#504a3b",
                                 fg='white',
                                 width=35,
                                 height=3,
                                 font=('', 12, 'bold'),
                                 border=1,
                                 borderwidth=1,
                                 relief='groove')
    text_avtorization.place(y=0, x=0)

    pole_login = tk.Label(current_window,
                          text='ВВЕДИ ЛОГИН:',
                          background='#504a3b',
                          fg='white',
                          font=('', 12))
    pole_login.place(x=30, y=80)

    entry_login = tk.Entry(current_window,
                           width=20,
                           background='#504a3b',
                           fg='white',
                           font=('', 10, 'bold'))
    entry_login.place(x=170, y=80)

    pole_password = tk.Label(current_window,
                             text='ВВЕДИ ПАРОЛЬ:',
                             background='#504a3b',
                             fg='white',
                             font=('', 12))
    pole_password.place(x=30, y=120)

    entry_paswo = tk.Entry(current_window,
                           width=20,
                           background='#504a3b',
                           fg='white',
                           font=('', 10, 'bold'),
                           show='*')
    entry_paswo.place(x=170, y=120)

    def voitu():
        login = entry_login.get()
        password = entry_paswo.get()
        _ = Authorization.create(
            login=login,
            password=password
        )
        current_window.destroy()
        glavnui()
        messagebox.showinfo("Успех", "Вы успешно зарегистрировались!")

    button_entrance = tk.Button(current_window,
                                width=20,
                                background="#3f3a2d",
                                text='ВОЙТИ',
                                font=('', 12, 'bold'),
                                fg='white',
                                command=voitu)
    button_entrance.place(x=75, y=290)

    button_requstration = tk.Label(current_window,
                                   text='АВТОРИЗАЦИЯ',
                                   background='#504a3b',
                                   fg="#332f24",
                                   font=('', 12, 'bold'))
    button_requstration.place(x=120, y=330)
    button_requstration.bind('<Button-1>', lambda _: Autorizashion())

    image_l = tk.PhotoImage(file='logg.png')
    image_l = image_l.subsample(5)
    image_label = tk.Label(current_window,
                           image=image_l,
                           background='#504a3b')
    image_label.place(x=55, y=160)


def glavnui():
    global image, image1, image2
    ''' выбор экпозиции'''
    for widget in root.winfo_children():
        widget.destroy()

    root.config(background="#d2d1c0")
    shapka = tk.Label(root, background="#b0ae8e", width=47, height=3,
                      text='ЭКСПОЗИЦИИ', font=('', 15))
    shapka.place(x=0, y=0)

    x_pos = 30

    y_pos = 100

    def get_exhibit():
        exbi = Exposition.select()
        return exbi

    element_count = get_exhibit().count()

    for i in range(0, element_count):
        global image, image1, image2
        kub1 = tk.Label(root, width=30, height=10, background="#d2d1c0",
                        relief='groove', border=1,
                        borderwidth=1)
        if i % 2 == 0:
            kub1.place(x=x_pos, y=y_pos)
        else:
            kub1.place(x=x_pos + 230, y=y_pos)

            y_pos += 170

        if i == 0:
            image1 = tk.PhotoImage(file='1.png')
            image1 = image1.subsample(14)
            image_label = tk.Label(kub1, image=image1, background="#d2d1c0")
            image_label.place(x=34, y=0)
            text1 = tk.Label(kub1, text='Современное исскуство',
                             wraplength=100, font=('', 11),
                             background="#d2d1c0")
            text1.place(x=55, y=100)
            kub1.bind('<Button-1>', lambda _: vistavka_sovremen_isskus())
            image_label.bind('<Button-1>',
                             lambda _: vistavka_sovremen_isskus())
            text1.bind('<Button-1>', lambda _: vistavka_sovremen_isskus())

        elif i == 1:
            image = tk.PhotoImage(file='3.png')
            image = image.subsample(40)
            image_label = tk.Label(kub1, image=image, background="#d2d1c0")
            image_label.place(x=49, y=0)
            text1 = tk.Label(kub1, text='Классическая  скульптура',
                             wraplength=100, font=('', 11),
                             background="#d2d1c0")
            text1.place(x=55, y=100)
            kub1.bind('<Button-1>', lambda _: klassik_isskustv())
            image_label.bind('<Button-1>',
                             lambda _: klassik_isskustv())
            text1.bind('<Button-1>', lambda _: klassik_isskustv())
        elif i == 2:
            image2 = tk.PhotoImage(file='4.png')
            image2 = image2.subsample(3)
            image_label = tk.Label(kub1, image=image2, background="#d2d1c0")
            image_label.place(x=30, y=30)
            text1 = tk.Label(kub1, text='Традиционное исскуство',
                             wraplength=100, font=('', 11),
                             background="#d2d1c0")
            text1.place(x=55, y=100)


def vistavka_sovremen_isskus():
    global images_list
    if 'images_list' not in globals():
        images_list = []

    for widget in root.winfo_children():
        if widget != root:
            widget.destroy()

    root.config(background="#d2d1c0")
    shapka = tk.Label(root, background="#b0ae8e", width=47, height=3,
                      text='ВЫСТАВСКА - СОВРЕМЕННОЕ ИССКУСТВО', font=('', 15))
    shapka.place(x=0, y=0)

    def get_exponat():
        exponat = Exhibit.select().where(
            Exhibit.exposishi == 'Современное искусство')
        return exponat

    expon = get_exponat()

    main_frame = tk.Frame(root, background="#d2d1c0")
    main_frame.place(x=0, y=60, width=500, height=400)

    canvas = tk.Canvas(main_frame, bg="#d2d1c0", highlightthickness=0)
    scrollbar = tk.Scrollbar(main_frame, orient="vertical",
                             command=canvas.yview)
    content_frame = tk.Frame(canvas, background="#d2d1c0")

    canvas.create_window((0, 0), window=content_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)

    y_pos = 100
    for i in expon:
        pole_kub = tk.Frame(content_frame, width=440, height=160,
                            background="#d2d1c0",
                            relief='groove', borderwidth=2)
        pole_kub.pack(pady=10, padx=20)
        pole_kub.pack_propagate(False)

        ima = f"{i.image}"
        image_nado = tk.PhotoImage(file=ima)

        if ima == "one.png":
            image_nado = image_nado.subsample(8)
            images_list.append(image_nado)
            image_lab = tk.Label(pole_kub, image=image_nado,
                                 background="#d2d1c0")
            image_lab.place(x=20, y=10)

        elif ima == "two.png":
            image_nado = image_nado.subsample(9)
            images_list.append(image_nado)
            image_lab = tk.Label(pole_kub, image=image_nado,
                                 background="#d2d1c0")
            image_lab.place(x=10, y=13)
        elif ima == "leto.png":
            image_nado = image_nado.subsample(7)
            images_list.append(image_nado)
            image_lab = tk.Label(pole_kub, image=image_nado,
                                 background="#d2d1c0")
            image_lab.place(x=10, y=13)
        elif ima == "zima.png":
            image_nado = image_nado.subsample(5)
            images_list.append(image_nado)
            image_lab = tk.Label(pole_kub, image=image_nado,
                                 background="#d2d1c0")
            image_lab.place(x=10, y=13)

        text = tk.Label(pole_kub, text=f"{i.title}",
                        background="#d2d1c0",
                        font=('', 12))
        text.place(x=220, y=8)
        opisanie = tk.Label(pole_kub, text=f"{i.description}",
                            background="#d2d1c0",
                            font=('', 10))
        opisanie.place(x=220, y=30)
        materials = tk.Label(pole_kub, text=f"{i.material}",
                             background="#d2d1c0",
                             font=('', 10))
        materials.place(x=220, y=48)
        razmer = tk.Label(pole_kub, text=f"Размер: {i.dimensions}",
                          background="#d2d1c0",
                          font=('', 10))
        razmer.place(x=220, y=66)
        eyar_creation = tk.Label(pole_kub,
                                 text=f"Год создания: {i.creation_year}",
                                 background="#d2d1c0",
                                 font=('', 10))

        autor = tk.Label(pole_kub,
                         text=f"Автор: {i.aftor.first_name}",
                         background="#d2d1c0",
                         font=('', 10),
                         cursor='hand2')
        autor.place(x=220, y=100)
        autor.bind('<Button-1>', lambda _,
                   author_id=i.aftor.id: Autor(author_id, 'sovremen'))

        eyar_creation.place(x=220, y=84)
        price = tk.Label(pole_kub, text=f"Цена: {i.value} р",
                         background="#d2d1c0",
                         font=('', 13))
        price.place(x=290, y=125)

        y_pos += 180

    content_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    def on_mousewheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    canvas.bind("<MouseWheel>", on_mousewheel)

    back_button = tk.Button(root, text="Назад", command=glavnui,
                            background="#b0ae8e", font=('', 10))
    back_button.place(x=10, y=465)


def klassik_isskustv():
    global images_list
    if 'images_list' not in globals():
        images_list = []

    for widget in root.winfo_children():
        if widget != root:
            widget.destroy()

    root.config(background="#d2d1c0")
    shapka = tk.Label(root, background="#b0ae8e", width=47, height=3,
                      text='ВЫСТАВСКА - КЛАССИЧЕСКАЯ СКУЛЬПТУРА',
                      font=('', 15))
    shapka.place(x=0, y=0)

    def get_exponat():
        exponat = Exhibit.select().where(
            Exhibit.exposishi == 'Классическая скульптура')
        return exponat

    expon = get_exponat()

    main_frame = tk.Frame(root, background="#d2d1c0")
    main_frame.place(x=0, y=60, width=500, height=400)

    canvas = tk.Canvas(main_frame, bg="#d2d1c0", highlightthickness=0)
    scrollbar = tk.Scrollbar(main_frame, orient="vertical",
                             command=canvas.yview)
    content_frame = tk.Frame(canvas, background="#d2d1c0")

    canvas.create_window((0, 0), window=content_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)

    y_pos = 100
    for i in expon:
        pole_kub = tk.Frame(content_frame, width=440, height=160,
                            background="#d2d1c0",
                            relief='groove', borderwidth=2)
        pole_kub.pack(pady=10, padx=20)
        pole_kub.pack_propagate(False)

        ima = f"{i.image}"
        image_nado = tk.PhotoImage(file=ima)

        if ima == "trona.png":
            image_nado = image_nado.subsample(7)
            images_list.append(image_nado)
            image_lab = tk.Label(pole_kub, image=image_nado,
                                 background="#d2d1c0")
            image_lab.place(x=40, y=10)

        elif ima == "vozch.png":
            image_nado = image_nado.subsample(6)
            images_list.append(image_nado)
            image_lab = tk.Label(pole_kub, image=image_nado,
                                 background="#d2d1c0")
            image_lab.place(x=10, y=26)
        elif ima == "sisk.png":
            image_nado = image_nado.subsample(7)
            images_list.append(image_nado)
            image_lab = tk.Label(pole_kub, image=image_nado,
                                 background="#d2d1c0")
            image_lab.place(x=30, y=8)

        text = tk.Label(pole_kub, text=f"{i.title}",
                        background="#d2d1c0",
                        font=('', 12))
        text.place(x=220, y=8)
        opisanie = tk.Label(pole_kub, text=f"{i.description}",
                            background="#d2d1c0",
                            font=('', 10))
        opisanie.place(x=220, y=30)
        materials = tk.Label(pole_kub, text=f"{i.material}",
                             background="#d2d1c0",
                             font=('', 10))
        materials.place(x=220, y=48)
        razmer = tk.Label(pole_kub, text=f"Размер: {i.dimensions}",
                          background="#d2d1c0",
                          font=('', 10))
        razmer.place(x=220, y=66)
        eyar_creation = tk.Label(pole_kub,
                                 text=f"Год создания: {i.creation_year}",
                                 background="#d2d1c0",
                                 font=('', 10))

        autor = tk.Label(pole_kub,
                         text=f"Автор: {i.aftor.first_name}",
                         background="#d2d1c0",
                         font=('', 10),
                         cursor='hand2')
        autor.place(x=220, y=100)
        autor.bind('<Button-1>', lambda _,
                   author_id=i.aftor.id: Autor(author_id, 'klassik'))

        eyar_creation.place(x=220, y=84)
        price = tk.Label(pole_kub, text=f"Цена: {i.value} р",
                         background="#d2d1c0",
                         font=('', 13))
        price.place(x=290, y=125)

        y_pos += 180

    content_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    def on_mousewheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    canvas.bind("<MouseWheel>", on_mousewheel)

    back_button = tk.Button(root, text="Назад", command=glavnui,
                            background="#b0ae8e", font=('', 10))
    back_button.place(x=10, y=465)


def Autor(author_id, previous_exhibition=None):
    for widget in root.winfo_children():
        widget.destroy()

    author = Authors.get(Authors.id == author_id)

    shapka = tk.Label(root, background="#b0ae8e", width=47, height=3,
                      text=f'Автор: {author.first_name} {author.last_name}',
                      font=('', 15))
    shapka.place(x=0, y=0)

    main_frame = tk.Frame(root, background="#d2d1c0")
    main_frame.place(x=0, y=60, width=500, height=400)

    info_frame = tk.Frame(main_frame, background="#d2d1c0")
    info_frame.pack(pady=20, padx=20, fill="both", expand=True)

    name_label = tk.Label(info_frame,
                          text=f"{author.first_name} {author.last_name}",
                          background="#d2d1c0",
                          font=('', 16, 'bold'))
    name_label.pack(pady=10)

    if author.biography:
        bio_label = tk.Label(info_frame,
                             text=f"Биография: {author.biography}",
                             background="#d2d1c0",
                             font=('', 10),
                             wraplength=400,
                             justify="left")
        bio_label.pack(pady=5)

    if author.birth_date:
        years_label = tk.Label(info_frame,
                               text=f"Годы жизни: {author.birth_date}",
                               background="#d2d1c0",
                               font=('', 10))
        years_label.pack(pady=5)

    works_label = tk.Label(info_frame,
                           text="Другие работы автора:",
                           background="#d2d1c0",
                           font=('', 12, 'bold'))
    works_label.pack(pady=10)

    other_works = Exhibit.select().where(Exhibit.aftor == author).limit(5)

    for work in other_works:
        work_label = tk.Label(info_frame,
                              text=f"• {work.title} ({work.creation_year})",
                              background="#d2d1c0",
                              font=('', 9))
        work_label.pack(pady=2)

    def back_command():
        if previous_exhibition == 'sovremen':
            vistavka_sovremen_isskus()
        elif previous_exhibition == 'klassik':
            klassik_isskustv()
        else:
            glavnui()

    back_button = tk.Button(root, text="Назад",
                            command=back_command,
                            background="#b0ae8e", font=('', 10))
    back_button.place(x=10, y=465)

    home_button = tk.Button(root, text="На главную",
                            command=glavnui,
                            background="#b0ae8e", font=('', 10))
    home_button.place(x=400, y=465)


Autorizashion()

# glavnui()

# vistavka_sovremen_isskus()

# klassik_isskustv()

root.mainloop()
