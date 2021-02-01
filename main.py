from tkinter import*
from tkinter import ttk
from tkinter import messagebox

Main_screen=Tk()
Main_screen.title("LOGIN FORM")

username="Fatihialem"
password="Fatih_07"

lbl_username=Label(Main_screen,text="Username",bg="yellow")
lbl_username.place(relx=0.1,rely=0.2,relwidth=0.2)
entry_username=Entry(Main_screen)
entry_username.place(relx=0.38,rely=0.2,relwidth=0.4)

lbl_password=Label(Main_screen,text="Password",bg="yellow")
lbl_password.place(relx=0.1,rely=0.4,relwidth=0.2)
entry_password=Entry(Main_screen,show="*")
entry_password.place(relx=0.38,rely=0.4,relwidth=0.4)

def username_password_control():
    if entry_username.get()==username and entry_password.get()==password:
        x = 0.04
        y = 0.18
        width = 0.2
        height = 0.05

        Main_screen.destroy()
        Screen = Tk()
        Screen.title("UNIVERSITY STUDENT REGISTRATION")

        lbl_title = Label(Screen, text="STUDENT INFORMATIONS", bg="gray", fg="white")
        lbl_title.place(relx=x + 0.035, rely=y - 0.13, relwidth=width + 0.05, relheight=height + 0.03)
        # Screen Title and Form Title

        lbl_student_id = Label(Screen, text="Student No")
        lbl_student_id.place(relx=x, rely=y)
        entry_student_id = Entry(Screen)
        entry_student_id.place(relx=x + 0.12, rely=y, relwidth=width, relheight=height)
        # Student ID  Information

        lbl_name = Label(Screen, text="Name")
        lbl_name.place(relx=x, rely=y + 0.08)
        entry_name = Entry(Screen)
        entry_name.place(relx=x + 0.12, rely=y + 0.08, relwidth=width, relheight=height)
        # Name Information

        lbl_surname = Label(Screen, text="Surname")
        lbl_surname.place(relx=x, rely=y + 0.16)
        entry_surname = Entry(Screen)
        entry_surname.place(relx=x + 0.12, rely=y + 0.16, relwidth=width, relheight=height)
        # Surname Information

        lbl_age = Label(Screen, text="Age")
        lbl_age.place(relx=x, rely=y + 0.24)
        entry_age = Entry(Screen)
        entry_age.place(relx=x + 0.17, rely=y + 0.24, relwidth=width - 0.1, relheight=height)
        lbl_department = Label(Screen, text="Department")
        # Age Information

        lbl_department.place(relx=x, rely=y + 0.32)
        cmb_departments = ttk.Combobox(Screen, values=["Computer Engineer", "Software Enginner", "Machine Engineer",
                                                       "Civil Enginner", "Medicine", "Dentist", "Architecture"])
        cmb_departments.place(relx=x + 0.12, rely=y + 0.32, relwidth=width, relheight=height)
        # Department Information

        get_sexuality = StringVar()
        lbl_male_female = Label(Screen, text="Male-Female")
        lbl_male_female.place(relx=x, rely=y + 0.4)
        radiobtn_male = Radiobutton(Screen, text="Male", value="Male", variable=get_sexuality)
        radiobtn_male.place(relx=x + 0.12, rely=y + 0.4, relwidth=0.1)
        radiobtn_female = Radiobutton(Screen, text="Female", value="Female", variable=get_sexuality)
        radiobtn_female.place(relx=x + 0.2, rely=y + 0.4, relwidth=0.1)
        # Male-Female Information

        lbl_languages = Label(Screen, text="Languages")
        lbl_languages.place(relx=x + 0.13, rely=y + 0.48)
        # Language label
        get_english = StringVar()
        checkbtn_languages = Checkbutton(Screen, text="English", onvalue="English", variable=get_english)
        checkbtn_languages.place(relx=x + 0.01, rely=y + 0.54)
        # English Checkbutton
        get_german = StringVar()
        checkbtn_languages = Checkbutton(Screen, text="German", onvalue="German", variable=get_german)
        checkbtn_languages.place(relx=x + 0.1, rely=y + 0.54)
        # German Checkbutton
        get_french = StringVar()
        checkbtn_languages = Checkbutton(Screen, text="French", onvalue="French", variable=get_french)
        checkbtn_languages.place(relx=x + 0.18, rely=y + 0.54)
        # French Checkbutton
        get_italian = StringVar()
        checkbtn_languages = Checkbutton(Screen, text="Italian", onvalue="Italian", variable=get_italian)
        checkbtn_languages.place(relx=0.3, rely=y + 0.54)
        # Italian Checkbutton

        lbl_students = Label(Screen, text="STUDENTS", width=20, bg="gray", fg="white")
        lbl_students.place(relx=x + 0.58, rely=y - 0.13, relwidth=width - 0.04, relheight=height)
        listbox_students = Listbox(Screen, borderwidth=5)
        listbox_students.place(relx=x + 0.41, rely=y - 0.06, relwidth=width + 0.3, relheight=height + 0.65)

        # Students Listbox and Label

        def insert():
            if len(entry_student_id.get()) == 0 or len(entry_name.get().strip()) == 0 or len(
                    entry_surname.get().strip()) == 0 or len(entry_age.get().strip()) == 0 or len(
                cmb_departments.get()) == 0:
                messagebox.showwarning("Missing Data",
                                       "Please Review Student ID, Name, Surname, Age or Department Data/Datas ( Age Must not Be 'Empty' )")
            else:
                try:
                    if int(entry_age.get().strip()) < 0 or int(entry_age.get().strip()) > 80:
                        messagebox.showwarning("Wrong Age Data",
                                               "Please Review The Age Data ( Age Should Be 'Between 0 and 80' )")
                    else:
                        languages = ""
                        if not len(get_english.get()) == 1:
                            languages = get_english.get() + ", "
                        if not len(get_german.get()) == 1:
                            languages = languages + get_german.get() + ", "
                        if not len(get_french.get()) == 1:
                            languages = languages + get_french.get() + ", "
                        if not len(get_italian.get()) == 1:
                            languages = languages + get_italian.get() + ", "
                        if not len(languages) == 0:
                            languages = languages[:-2]
                            listbox_students.insert(0,
                                                    entry_student_id.get() + " - " + entry_name.get() + " " + entry_surname.get() + " - " + entry_age.get() + " - " + get_sexuality.get() + " - " + cmb_departments.get() + " - " + languages)
                            messagebox.showinfo("Was İnserted Successfully", "The Student Registration was inserted")
                            entry_student_id.focus()
                        else:
                            listbox_students.insert(0,
                                                    entry_student_id.get() + " - " + entry_name.get() + " " + entry_surname.get() + " - " + entry_age.get() + " - " + get_sexuality.get() + " - " + cmb_departments.get())
                            messagebox.showinfo("Was İnserted Successfully", "The Student Registration was inserted")
                            entry_student_id.focus()
                except:
                    messagebox.showwarning("Wrong Age Data", "Please Review The Age Data ( Age Should Be 'Numeric' )")

        # Insert Registration

        def delete():
            try:
                listbox_students.delete(int(entry_deleted_regist.get().strip()) - 1)
            except:
                messagebox.showwarning("Wrong Registration No", "Please Review The Deteled Registration No")

        # Delete Registration

        btn_insert = Button(Screen, text="INSERT", bg="gray", fg="white", command=insert)
        btn_insert.place(relx=x + 0.08, rely=y + 0.67, relwidth=width - 0.04)
        # İnsert Button

        lbl_deleted_regist = Label(Screen, text="Deleted Registration No")
        lbl_deleted_regist.place(relx=x + 0.43, rely=y + 0.67)
        entry_deleted_regist = Entry(Screen, borderwidth=5)
        entry_deleted_regist.place(relx=x + 0.58, rely=y + 0.67, relwidth=width - 0.1)
        # Deleted Registration Information

        btn_delete = Button(Screen, text="DELETE", bg="gray", fg="white", command=delete)
        btn_delete.place(relx=x + 0.7, rely=y + 0.665, relwidth=width - 0.04)
        # Delete Button

        Screen.mainloop()
    else:
        messagebox.showwarning("Wrong Username or Password","Please Review The Username or Password")

btn_submit=Button(Main_screen,text="LOGIN",bg="gray",command=username_password_control)
btn_submit.place(relx=0.33,rely=0.6,relwidth=0.24,relheight=0.11)

Main_screen.mainloop()