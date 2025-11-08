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

    image_l = tk.PhotoImage(file='img_autori/logg.png')
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
    global image, image1, image2, image4, image5
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

    mm = get_exhibit()
    element_count = mm.count()

    for i in range(0, element_count):
        global image, image1, image2, image4, image5
        kub1 = tk.Label(root, width=30, height=10, background="#d2d1c0",
                        relief='groove', border=1,
                        borderwidth=1)
        if i % 2 == 0:
            kub1.place(x=x_pos, y=y_pos)
        else:
            kub1.place(x=x_pos + 230, y=y_pos)

            y_pos += 170

        if i == 0:
            image1 = tk.PhotoImage(file='img_exposition/1.png')
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
            image = tk.PhotoImage(file='img_exposition/3.png')
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
            image2 = tk.PhotoImage(file='img_exposition/4.png')
            image2 = image2.subsample(3)
            image_label = tk.Label(kub1, image=image2, background="#d2d1c0")
            image_label.place(x=30, y=30)
            text1 = tk.Label(kub1, text=f'{mm[i].title}',
                             wraplength=100, font=('', 11),
                             background="#d2d1c0")
            text1.place(x=55, y=100)
            kub1.bind('<Button-1>', lambda _: tradighi_isskustv())
            image_label.bind('<Button-1>',
                             lambda _: tradighi_isskustv())
            text1.bind('<Button-1>', lambda _: tradighi_isskustv())
        elif i == 3:
            image5 = tk.PhotoImage(file='img_exposition/5.png')
            image5 = image5.subsample(9)
            image_label = tk.Label(kub1, image=image5, background="#d2d1c0")
            image_label.place(x=40, y=5)
            text1 = tk.Label(kub1, text=f'{mm[i].title}',
                             wraplength=100, font=('', 11),
                             background="#d2d1c0")
            text1.place(x=63, y=100)
            kub1.bind('<Button-1>', lambda _: arheolog_bydushev())
            image_label.bind('<Button-1>',
                             lambda _: arheolog_bydushev())
            text1.bind('<Button-1>', lambda _: arheolog_bydushev())

        elif i == 4:
            image4 = tk.PhotoImage(file='img_exposition/pustota.png')
            image4 = image4.subsample(8)
            image_label = tk.Label(kub1, image=image4, background="#d2d1c0")
            image_label.place(x=60, y=10)
            text1 = tk.Label(kub1, text=f'{mm[i].title}',
                             wraplength=100, font=('', 11),
                             background="#d2d1c0")
            text1.place(x=55, y=100)

    def greate_exposition():
        lab = tk.Toplevel()
        lab.config(background="#d2d1c0")
        lab.geometry('300x300')
        lab.resizable(False, False)
        lab.title('Создание экспозиции')
        lab.iconbitmap('museum_3584.ico')

        title = tk.Label(lab,
                         text='Название:',
                         background='#d2d1c0',
                         font=('', 12))
        title.place(x=20, y=10)

        title_ent = tk.Entry(lab)
        title_ent.place(x=140, y=10)

        description = tk.Label(lab,
                               text='Описание:',
                               background='#d2d1c0',
                               font=('', 12))
        description.place(x=20, y=35)

        description_ent = tk.Entry(lab)
        description_ent.place(x=140, y=35)

        start_date = tk.Label(lab,
                              text='Дата начала:',
                              background='#d2d1c0',
                              font=('', 12))
        start_date.place(x=20, y=60)

        start_date_ent = tk.Entry(lab)
        start_date_ent.place(x=140, y=60)

        end_date = tk.Label(lab,
                            text='Дата конца:',
                            background='#d2d1c0',
                            font=('', 12))
        end_date.place(x=20, y=85)

        end_date_ent = tk.Entry(lab)
        end_date_ent.place(x=140, y=85)

        location = tk.Label(lab,
                            text='Место:',
                            background='#d2d1c0',
                            font=('', 12))
        location.place(x=20, y=110)

        location_ent = tk.Entry(lab)
        location_ent.place(x=140, y=110)

        created_at = tk.Label(lab,
                              text='Дата создания:',
                              background='#d2d1c0',
                              font=('', 12))
        created_at.place(x=20, y=135)

        created_at_ent = tk.Entry(lab)
        created_at_ent.insert(0, "2025-10-23 12:12:12")
        created_at_ent.place(x=140, y=135)

        def create_table():
            title = title_ent.get()
            description = description_ent.get()
            start_date = start_date_ent.get()
            end_date = end_date_ent.get()
            location = location_ent.get()
            created_at = created_at_ent.get()

            _ = Exposition.create(
                title=title,
                description=description,
                start_date=start_date,
                end_date=end_date,
                location=location,
                created_at=created_at
            )
            messagebox.showinfo("Успех", f"Экспозиция {title} создана")
            lab.destroy()

        knopka = tk.Button(lab,
                           text='Создать',
                           background='#d2d1c0',
                           command=create_table)
        knopka.place(x=115, y=190)

    def redact_exposition():
        lab = tk.Toplevel()
        lab.config(background="#d2d1c0")
        lab.geometry('300x400')
        lab.resizable(False, False)
        lab.title('Редактирование экспозиции')
        lab.iconbitmap('museum_3584.ico')

        id_label = tk.Label(lab,
                            text='ID экспозиции:',
                            background='#d2d1c0',
                            font=('', 12))
        id_label.place(x=20, y=10)

        id_ent = tk.Entry(lab)
        id_ent.place(x=140, y=10)

        title = tk.Label(lab,
                         text='Название:',
                         background='#d2d1c0',
                         font=('', 12))
        title.place(x=20, y=40)

        title_ent = tk.Entry(lab)
        title_ent.place(x=140, y=40)

        description = tk.Label(lab,
                               text='Описание:',
                               background='#d2d1c0',
                               font=('', 12))
        description.place(x=20, y=70)

        description_ent = tk.Entry(lab)
        description_ent.place(x=140, y=70)

        start_date = tk.Label(lab,
                              text='Дата начала:',
                              background='#d2d1c0',
                              font=('', 12))
        start_date.place(x=20, y=100)

        start_date_ent = tk.Entry(lab)
        start_date_ent.place(x=140, y=100)

        end_date = tk.Label(lab,
                            text='Дата конца:',
                            background='#d2d1c0',
                            font=('', 12))
        end_date.place(x=20, y=130)

        end_date_ent = tk.Entry(lab)
        end_date_ent.place(x=140, y=130)

        location = tk.Label(lab,
                            text='Место:',
                            background='#d2d1c0',
                            font=('', 12))
        location.place(x=20, y=160)

        location_ent = tk.Entry(lab)
        location_ent.place(x=140, y=160)

        created_at = tk.Label(lab,
                              text='Дата создания:',
                              background='#d2d1c0',
                              font=('', 12))
        created_at.place(x=20, y=190)

        created_at_ent = tk.Entry(lab)
        created_at_ent.place(x=140, y=190)

        def update_table():
            exp_id = id_ent.get()
            title = title_ent.get()
            description = description_ent.get()
            start_date = start_date_ent.get()
            end_date = end_date_ent.get()
            location = location_ent.get()
            created_at = created_at_ent.get()

            try:
                exposition = Exposition.get(Exposition.id == exp_id)
                exposition.title = title
                exposition.description = description
                exposition.start_date = start_date
                exposition.end_date = end_date
                exposition.location = location
                exposition.created_at = created_at
                exposition.save()

                messagebox.showinfo("Успех", f"Экспозиция {title} обновлена")
                lab.destroy()
            except Exposition.DoesNotExist:
                messagebox.showerror("Ошибка",
                                     f"Экспозиция с ID {exp_id} не найдена")

        update_button = tk.Button(lab,
                                  text='Обновить',
                                  background='#d2d1c0',
                                  command=update_table)
        update_button.place(x=115, y=250)

    def delite_exposition():
        lab = tk.Toplevel()
        lab.config(background="#d2d1c0")
        lab.geometry('300x150')
        lab.resizable(False, False)
        lab.title('Удаление экспозиции')
        lab.iconbitmap('museum_3584.ico')

        id_label = tk.Label(lab,
                            text='ID экспозиции:',
                            background='#d2d1c0',
                            font=('', 12))
        id_label.place(x=20, y=40)

        id_ent = tk.Entry(lab)
        id_ent.place(x=140, y=40)

        def delete_table():
            exp_id = id_ent.get()

            try:
                exposition = Exposition.get(Exposition.id == exp_id)
                exposition.delete_instance()

                messagebox.showinfo("Успех", f"Экспозиция {exp_id} удалена")
                lab.destroy()
            except Exposition.DoesNotExist:
                messagebox.showerror("Ошибка",
                                     f"Экспозиция с ID {exp_id} не найдена")

        delete_button = tk.Button(lab,
                                  text='Удалить',
                                  background='#d2d1c0',
                                  command=delete_table)
        delete_button.place(x=115, y=80)

    greate_button = tk.Button(root,
                              text='Создать',
                              background='#d2d1c0',
                              command=greate_exposition)
    greate_button.place(x=100, y=450)

    redact_button = tk.Button(root,
                              text='Редактировать',
                              background='#d2d1c0',
                              command=redact_exposition)
    redact_button.place(x=200, y=450)

    delite_button = tk.Button(root,
                              text='Удалить',
                              background='#d2d1c0',
                              command=delite_exposition)
    delite_button.place(x=340, y=450)


def vistavka_sovremen_isskus():
    global images_list
    if 'images_list' not in globals():
        images_list = []

    for widget in root.winfo_children():
        if widget != root:
            widget.destroy()

    root.config(background="#d2d1c0")
    shapka = tk.Label(root, background="#b0ae8e", width=47, height=3,
                      text='ВЫСТАВКА - СОВРЕМЕННОЕ ИССКУСТВО', font=('', 15))
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

        if ima == "img_sovremen/one.png":
            image_nado = image_nado.subsample(8)
            images_list.append(image_nado)
            image_lab = tk.Label(pole_kub, image=image_nado,
                                 background="#d2d1c0")
            image_lab.place(x=20, y=10)

        elif ima == "img_sovremen/two.png":
            image_nado = image_nado.subsample(9)
            images_list.append(image_nado)
            image_lab = tk.Label(pole_kub, image=image_nado,
                                 background="#d2d1c0")
            image_lab.place(x=10, y=13)
        elif ima == "img_sovremen/leto.png":
            image_nado = image_nado.subsample(7)
            images_list.append(image_nado)
            image_lab = tk.Label(pole_kub, image=image_nado,
                                 background="#d2d1c0")
            image_lab.place(x=10, y=13)
        elif ima == "img_sovremen/zima.png":
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
                      text='ВЫСТАВКА - КЛАССИЧЕСКАЯ СКУЛЬПТУРА',
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

        if ima == "img_classik/trona.png":
            image_nado = image_nado.subsample(7)
            images_list.append(image_nado)
            image_lab = tk.Label(pole_kub, image=image_nado,
                                 background="#d2d1c0")
            image_lab.place(x=40, y=10)

        elif ima == "img_classik/vozch.png":
            image_nado = image_nado.subsample(6)
            images_list.append(image_nado)
            image_lab = tk.Label(pole_kub, image=image_nado,
                                 background="#d2d1c0")
            image_lab.place(x=10, y=26)
        elif ima == "img_classik/sisk.png":
            image_nado = image_nado.subsample(7)
            images_list.append(image_nado)
            image_lab = tk.Label(pole_kub, image=image_nado,
                                 background="#d2d1c0")
            image_lab.place(x=30, y=8)
        elif ima == "img_classik/pismo.png":
            image_nado = image_nado.subsample(8)
            images_list.append(image_nado)
            image_lab = tk.Label(pole_kub, image=image_nado,
                                 background="#d2d1c0")
            image_lab.place(x=30, y=10)

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


def tradighi_isskustv():
    global images_list
    if 'images_list' not in globals():
        images_list = []

    for widget in root.winfo_children():
        if widget != root:
            widget.destroy()

    root.config(background="#d2d1c0")
    shapka = tk.Label(root, background="#b0ae8e", width=47, height=3,
                      text='ВЫСТАВКА - ТРАДИЦИОННОЕ ИССКУСТВО',
                      font=('', 15))
    shapka.place(x=0, y=0)

    def get_exponat():
        exponat = Exhibit.select().where(
            Exhibit.exposishi == 'Традиционное искусство')
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

        if ima == "img_tradi/kazach.png":
            image_nado = image_nado.subsample(6)
            images_list.append(image_nado)
            image_lab = tk.Label(pole_kub, image=image_nado,
                                 background="#d2d1c0")
            image_lab.place(x=10, y=10)

        elif ima == "img_tradi/ngtort.png":
            image_nado = image_nado.subsample(7)
            images_list.append(image_nado)
            image_lab = tk.Label(pole_kub, image=image_nado,
                                 background="#d2d1c0")
            image_lab.place(x=10, y=10)
        elif ima == "img_tradi/rino.png":
            image_nado = image_nado.subsample(15)
            images_list.append(image_nado)
            image_lab = tk.Label(pole_kub, image=image_nado,
                                 background="#d2d1c0")
            image_lab.place(x=20, y=8)
        elif ima == "img_tradi/tixive.png":
            image_nado = image_nado.subsample(8)
            images_list.append(image_nado)
            image_lab = tk.Label(pole_kub, image=image_nado,
                                 background="#d2d1c0")
            image_lab.place(x=30, y=10)

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
                   author_id=i.aftor.id: Autor(author_id, 'tradighi'))

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


def arheolog_bydushev():
    global images_list
    if 'images_list' not in globals():
        images_list = []

    for widget in root.winfo_children():
        if widget != root:
            widget.destroy()

    root.config(background="#d2d1c0")
    shapka = tk.Label(root, background="#b0ae8e", width=47, height=3,
                      text='ВЫСТАВКА - АРХЕОЛОГИЯ БУДУЩЕГО',
                      font=('', 15))
    shapka.place(x=0, y=0)

    def get_exponat():
        exponat = Exhibit.select().where(
            Exhibit.exposishi == 'Археология будущего')
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

        image_nado = image_nado.subsample(8)
        images_list.append(image_nado)
        image_lab = tk.Label(pole_kub, image=image_nado,
                             background="#d2d1c0")
        image_lab.place(x=30, y=10)

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
                   author_id=i.aftor.id: Autor(author_id, 'arheol'))

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
        elif previous_exhibition == 'tradighi':
            tradighi_isskustv()
        elif previous_exhibition == 'arheol':
            arheolog_bydushev()
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

# tradighi_isskustv()

# arheolog_bydushev()

root.mainloop()
