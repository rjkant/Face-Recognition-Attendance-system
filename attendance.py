from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np
import os
import csv
from tkinter import filedialog


mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x800+0+0")
        self.root.title("Face Recognition System")

        ####### variables ###########
        self.var_atten_id=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

        #First Image
        img1=Image.open("C:/Users/Rajnikant/Desktop/Face Recognition system/Images/1.jpg")
        img1=img1.resize((675,180),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=675,height=180)

        #second Image
        img2=Image.open("C:/Users/Rajnikant/Desktop/Face Recognition system/Images/2.jpg")
        img2=img2.resize((675,180),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=675,y=0,width=675,height=180)

        main_frame=Frame(self.root,bd=2,bg="light blue")
        main_frame.place(x=5,y=210,width=1450,height=490)

        title_lbl=Label(self.root,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",30,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=180,width=1450,height=40)


        #left side frame
        Left_frame=LabelFrame(main_frame,bd=4,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",15,"bold"))
        Left_frame.place(x=5,y=10,width=665,height=480)

        left_inside_frame=Frame(Left_frame,bd=2,bg="light blue",relief=RIDGE)
        left_inside_frame.place(x=5,y=10,width=655,height=480)

        ##### Label and Entry ####

        # Attendance Id
        AttendanceId_label=Label(left_inside_frame,text="AttendanceId:",font=("times new roman",14,"bold"),bg="light blue")
        AttendanceId_label.grid(row=0,column=0,padx=8,pady=15,sticky=W)

        AttendanceId_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_id,width=17,font=("times new roman",14,"bold"))
        AttendanceId_entry.grid(row=0,column=1,padx=5,pady=15,sticky=W)

        # Name
        Name_label=Label(left_inside_frame,text="Name:",font=("times new roman",14,"bold"),bg="light blue")
        Name_label.grid(row=0,column=2,padx=10,pady=15,sticky=W)

        Name_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_name,width=17,font=("times new roman",14,"bold"))
        Name_entry.grid(row=0,column=3,padx=5,pady=15,sticky=W)

        # Department
        Department_label=Label(left_inside_frame,text="Department:",font=("times new roman",14,"bold"),bg="light blue")
        Department_label.grid(row=1,column=0,padx=10,pady=8,sticky=W)

        Department_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_dep,width=17,font=("times new roman",14,"bold"))
        Department_entry.grid(row=1,column=1,padx=5,pady=8,sticky=W)

        # Time
        Time_label=Label(left_inside_frame,text="Time:",font=("times new roman",14,"bold"),bg="light blue")
        Time_label.grid(row=1,column=2,padx=10,pady=8,sticky=W)

        Time_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_time,width=17,font=("times new roman",14,"bold"))
        Time_entry.grid(row=1,column=3,padx=5,pady=8,sticky=W)

        # Date
        Date_label=Label(left_inside_frame,text="Date:",font=("times new roman",14,"bold"),bg="light blue")
        Date_label.grid(row=2,column=0,padx=10,pady=8,sticky=W)

        Date_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_date,width=17,font=("times new roman",14,"bold"))
        Date_entry.grid(row=2,column=1,padx=5,pady=8,sticky=W)

        # Attendance Status
        Atten_label=Label(left_inside_frame,text="Attendence Status:",font=("times new roman",14,"bold"),bg="light blue")
        Atten_label.grid(row=3,column=0,padx=5,sticky=W)

        sem_combo=ttk.Combobox(left_inside_frame,textvariable=self.var_atten_attendance,font=("times new roman",14,"bold"),width=14,state="readonly")
        sem_combo["values"]=("Status","present","Absent")
        sem_combo.current(0)
        sem_combo.grid(row=3,column=1,pady=10,sticky=W)

        # Button Frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="light blue")
        btn_frame.place(x=0,y=300,width=655,height=45)

        import_btn=Button(btn_frame,text="Import csv",width=14,command=self.importCsv,cursor="hand2",font=("times new roman",14,"bold"),bg="blue",fg="white")
        import_btn.grid(row=0,column=0)

        export_btn=Button(btn_frame,text="Export csv",width=14,command=self.exportCsv,cursor="hand2",font=("times new roman",14,"bold"),bg="blue",fg="white")
        export_btn.grid(row=0,column=1)

        update_btn=Button(btn_frame,text="Update",width=14,cursor="hand2",font=("times new roman",14,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",width=14,command=self.reset_data,cursor="hand2",font=("times new roman",14,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)








        # Right side Frame
        right_inside_frame=LabelFrame(main_frame,bd=4,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",15,"bold"))
        right_inside_frame.place(x=675,y=10,width=655,height=475)

        table_frame=Frame(right_inside_frame,bd=2,relief=RIDGE,bg="light blue")
        table_frame.place(x=12,y=8,width=630,height=440)

        ########## Scroll Bar Table ########
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("AttendanceId","Name","Department","Time","Date","Attendance Status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("AttendanceId",text="AttendanceId")
        self.AttendanceReportTable.heading("Name",text="Name")
        self.AttendanceReportTable.heading("Department",text="Department")
        self.AttendanceReportTable.heading("Time",text="Time")
        self.AttendanceReportTable.heading("Date",text="Date")
        self.AttendanceReportTable.heading("Attendance Status",text="Attendance Status")

        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("AttendanceId",width=100)
        self.AttendanceReportTable.column("Name",width=100)
        self.AttendanceReportTable.column("Department",width=100)
        self.AttendanceReportTable.column("Time",width=100)
        self.AttendanceReportTable.column("Date",width=100)
        self.AttendanceReportTable.column("Attendance Status",width=100)


        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    ########## Fetch Data #################

    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    ####### Import CSV #########3
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    ########## Export CSV ###########
    def exportCsv(self):
        try:
            if(len(mydata)) <1:
                messagebox.showerror("NO Data","No data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your Data Exported to "+os.path.basename(fln)+" successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_name.set(rows[1])
        self.var_atten_dep.set(rows[2])
        self.var_atten_time.set(rows[3])
        self.var_atten_date.set(rows[4])
        self.var_atten_attendance.set(rows[5])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")




if __name__== "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()