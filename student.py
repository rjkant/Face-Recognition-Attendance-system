from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np
import os



class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x800+0+0")
        self.root.title("Face Recognition System")

        ######### Variables #########
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_phone=StringVar()
        self.var_email=StringVar()

        #First Image
        img1=Image.open("C:/Users/Rajnikant/Desktop/Face Recognition system/Images/1.jpg")
        img1=img1.resize((475,120),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=475,height=120)

        #second Image
        img2=Image.open("C:/Users/Rajnikant/Desktop/Face Recognition system/Images/2.jpg")
        img2=img2.resize((450,120),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=475,y=0,width=450,height=120)

        #Third Image
        img3=Image.open("C:/Users/Rajnikant/Desktop/Face Recognition system/Images/3.jpg")
        img3=img3.resize((475,120),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=925,y=0,width=475,height=120)

        #Background Image
        img4=Image.open("C:/Users/Rajnikant/Desktop/Face Recognition system/Images/bg.jpg")
        img4=img4.resize((1400,600),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=120,width=1400,height=600)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",25,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1400,height=40)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=5,y=40,width=1345,height=600)

        #left side frame
        Left_frame=LabelFrame(main_frame,bd=4,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",16,"bold"))
        Left_frame.place(x=10,y=10,width=665,height=600)

        img_left=Image.open("C:/Users/Rajnikant/Desktop/Face Recognition system/Images/3.jpg")
        img_left=img_left.resize((660,100),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=660,height=100)

        # current course information
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",14,"bold"))
        current_course_frame.place(x=5,y=100,width=660,height=120)

        # Department 
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",14,"bold"),bg="white")
        dep_label.grid(row=0,column=0)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",14,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Department","computer science","IT","Civil","Electrical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=10,sticky=W)

        # Course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",14,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",14,"bold"),width=17,state="readonly")
        course_combo["values"]=("Select Course","SE","BE","DE","CE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        # Year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",14,"bold"),bg="white")
        year_label.grid(row=1,column=0)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",14,"bold"),width=17,state="readonly")
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10)

        # Semester
        sem_label=Label(current_course_frame,text="Semester",font=("times new roman",14,"bold"),bg="white")
        sem_label.grid(row=1,column=2,padx=10,sticky=W)

        sem_combo=ttk.Combobox(current_course_frame,textvariable=self.var_sem,font=("times new roman",14,"bold"),width=17,state="readonly")
        sem_combo["values"]=("Semester","1","2")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


        # Class student Information
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",16,"bold"))
        class_student_frame.place(x=5,y=220,width=660,height=270)

        # student Id
        stu_id_label=Label(class_student_frame,text="Student Id:",font=("times new roman",14,"bold"),bg="white")
        stu_id_label.grid(row=0,column=0,padx=10,pady=4,sticky=W)

        student_id_entry=ttk.Entry(class_student_frame,textvariable=self.var_id,width=15,font=("times new roman",14,"bold"))
        student_id_entry.grid(row=0,column=1,padx=5,sticky=W)

        # student Name
        stu_name_label=Label(class_student_frame,text="Student Name:",font=("times new roman",14,"bold"),bg="white")
        stu_name_label.grid(row=0,column=2,padx=10,sticky=W)

        student_name_entry=ttk.Entry(class_student_frame,textvariable=self.var_name,width=15,font=("times new roman",14,"bold"))
        student_name_entry.grid(row=0,column=3,padx=5,sticky=W)

        # Gender
        Gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",14,"bold"),bg="white")
        Gender_label.grid(row=1,column=0,padx=10,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",14,"bold"),width=14,state="readonly")
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=1,column=1,sticky=W)

        # Date of Birth
        dob_label=Label(class_student_frame,text="DOB:",font=("times new roman",14,"bold"),bg="white")
        dob_label.grid(row=1,column=2,padx=10,pady=10,sticky=W)

        student_name_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=15,font=("times new roman",14,"bold"))
        student_name_entry.grid(row=1,column=3,padx=5,sticky=W)

        # Email
        email_label=Label(class_student_frame,text="Email:",font=("times new roman",14,"bold"),bg="white")
        email_label.grid(row=2,column=0,padx=10,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=15,font=("times new roman",14,"bold"))
        email_entry.grid(row=2,column=1,padx=5,sticky=W)

        # Phone Number
        phone_label=Label(class_student_frame,text="Phone Number",font=("times new roman",14,"bold"),bg="white")
        phone_label.grid(row=2,column=2,padx=10,pady=4,sticky=W)

        phone_name_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=15,font=("times new roman",14,"bold"))
        phone_name_entry.grid(row=2,column=3,padx=5,sticky=W)


        # Radio Button
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take photo Sample",value="yes")
        radiobtn1.grid(row=4,column=0)

        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No photo Sample",value="No")
        radiobtn2.grid(row=4,column=1)

        # Button Frame 1
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=150,width=660,height=40)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=14,cursor="hand2",font=("times new roman",14,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=14,cursor="hand2",font=("times new roman",14,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=14,cursor="hand2",font=("times new roman",14,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=14,cursor="hand2",font=("times new roman",14,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        # Button Frame 2
        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=190,width=660,height=40)

        take_photo_btn=Button(btn_frame1,text="Take photo Sample",command=self.generate_dataset,width=29,cursor="hand2",font=("times new roman",14,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=1,column=0)

        update_photo_btn=Button(btn_frame1,text="Update photo Sample",width=29,cursor="hand2",font=("times new roman",14,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=1,column=1)





        # Right side Frame
        Right_frame=LabelFrame(main_frame,bd=4,bg="white",relief=RIDGE,text="Student Data",font=("times new roman",15,"bold"))
        Right_frame.place(x=665,y=10,width=665,height=600)

        img_right=Image.open("C:/Users/Rajnikant/Desktop/Face Recognition system/Images/6.jpg")
        img_right=img_right.resize((660,100),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=660,height=100)


        ##### Search Frame ######
        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",14,"bold"))
        search_frame.place(x=5,y=100,width=660,height=70)

        search_label=Label(search_frame,text="Search By:",font=("times new roman",12,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),width=12,state="readonly")
        search_combo["values"]=("Select","RollNo","phoneNo","Name","ID")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10)

        search_entry=ttk.Entry(search_frame,width=12,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=5,sticky=W)

        search_btn=Button(search_frame,text="Search",width=12,cursor="hand2",font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=10)

        showall_btn=Button(search_frame,text="Show All",width=12,cursor="hand2",font=("times new roman",12,"bold"),bg="blue",fg="white")
        showall_btn.grid(row=0,column=4)

        ###### Table Frame ######
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=170,width=660,height=330)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","ID","Name","Gender","DOB","Email","Phone","Photo"),xscrollcommand=scroll_x,yscrollcommand=scroll_y)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("ID",text="Student Id")
        self.student_table.heading("Name",text="Student Name")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Email",text="Email Id")
        self.student_table.heading("Phone",text="Phone NO.")
        self.student_table.heading("Photo",text="Photo")
        
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=80)
        self.student_table.column("course",width=80)
        self.student_table.column("year",width=80)
        self.student_table.column("sem",width=80)
        self.student_table.column("ID",width=80)
        self.student_table.column("Name",width=80)
        self.student_table.column("Gender",width=80)
        self.student_table.column("DOB",width=80)
        self.student_table.column("Email",width=80)
        self.student_table.column("Phone",width=80)
        self.student_table.column("Photo",width=80)


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    ######### Function For backend #############
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("error","All field are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(username="root",password="Rajni@123",host="localhost",database="face_recognizer")
                my_cursor=conn.cursor()
                insert_item=("""INSERT INTO student(Department,course,Year,semester,Student_Id,student_Name,gender,DOB,Email,Phone,photo) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""")
                data=(self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_sem.get(),self.var_id.get(),self.var_name.get(),self.var_gender.get(),self.var_dob.get(),
                    self.var_email.get(),self.var_phone.get(),self.var_radio1.get())
                my_cursor.execute(insert_item,data)
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","student details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due T0:{str(es)}",parent=self.root)
    
    ############# Fetch Data #######################
    def fetch_data(self):
        conn=mysql.connector.connect(username="root",password="Rajni@123",host="localhost",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    ############### Get Cursor ##############
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_sem.set(data[3])
        self.var_id.set(data[4])
        self.var_name.set(data[5])
        self.var_gender.set(data[6])
        self.var_dob.set(data[7])
        self.var_email.set(data[8])
        self.var_phone.set(data[9])
        self.var_radio1.set(data[10])


    ######### Update Function ###############
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("error","All field are required",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("update","Do you want to update the student details",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(username="root",password="Rajni@123",host="localhost",database="face_recognizer")
                    my_cursor=conn.cursor()
                    update_item=("""update student set Department=%s,course=%s,Year=%s,semester=%s,student_Name=%s,gender=%s,DOB=%s,Email=%s,Phone=%s,photo=%s where student_Id=%s""")
                    data=(self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_sem.get(),self.var_name.get(),self.var_gender.get(),self.var_dob.get(),
                    self.var_email.get(),self.var_phone.get(),self.var_radio1.get(),self.var_id.get())
                    
                    my_cursor.execute(update_item,data)
                
                else:
                    if not update:
                        return 

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","student details successfully updated",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
            
    
    ############# Delete function ##############
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("delete","Are you sure?")
                if delete>0:
                    conn=mysql.connector.connect(username="root",password="Rajni@123",host="localhost",database="face_recognizer")
                    my_cursor=conn.cursor()
                    delete_item=("""delete from student where student_id=%s""")
                    data=(self.var_id.get(),)
                    my_cursor.execute(delete_item,data)

                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("delete","successfully deleted",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    ################ Reset function #############
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Semester")
        self.var_id.set("")
        self.var_name.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_radio1.set("")

    ######### Generate dataset or take photo sample ############
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("error","All field are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(username="root",password="Rajni@123",host="localhost",database="face_recognizer")
                my_cursor=conn.cursor()
                update_item=("""update student set Department=%s,course=%s,Year=%s,semester=%s,student_Name=%s,gender=%s,DOB=%s,Email=%s,Phone=%s,photo=%s where student_Id=%s""")
                data=(self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_sem.get(),self.var_name.get(),self.var_gender.get(),self.var_dob.get(),
                self.var_email.get(),self.var_phone.get(),self.var_radio1.get(),self.var_id.get())
                my_cursor.execute(update_item,data)
                id=self.var_id.get()
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                
                
                face_classifier=cv2.CascadeClassifier("C:/Users/Rajnikant/Desktop/Face Recognition system/haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    for (x,y,w,h) in faces:
                        face_crop=img[y:y+h,x:x+w]
                        return face_crop
                cam=cv2.VideoCapture(0)
                img_id=0
                while(True):
                    ret,my_frame=cam.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(600,600))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_path="C:/Users/Rajnikant/Desktop/Face Recognition system/Data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(255,0,0))          
                        cv2.imshow('frame',face)
                    if cv2.waitKey(100) & 0xFF == ord('q'):
                        break
                # break if the sample number is more than 60
                    elif img_id>100:
                        break
                cam.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating dataset completed")
                
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)


                

        







        



if __name__== "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()