from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
import os
from time import strftime
from datetime import datetime
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x800+0+0")
        self.root.title("Face Recognition System")

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

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDENCE SYSTEM",font=("times new roman",27,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1400,height=40)

        ######### Time ################
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
        
        lbl=Label(title_lbl,font=('times new roman',14,'bold'),bg='white',fg='blue')
        lbl.place(x=0,y=0,width=110,height=50)
        time()

        #student Button
        img5=Image.open("C:/Users/Rajnikant/Desktop/Face Recognition system/Images/student.jpg")
        img5=img5.resize((170,130),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,command=self.student_details,image=self.photoimg5,cursor="hand2")
        b1.place(x=170,y=100,width=170,height=130)

        b1_1=Button(bg_img,command=self.student_details,text="Student Details",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=170,y=235,width=170,height=30)

        # Detect face button
        img6=Image.open("C:/Users/Rajnikant/Desktop/Face Recognition system/Images/6.jpg")
        img6=img6.resize((170,130),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,command=self.face_data,cursor="hand2")
        b1.place(x=430,y=100,width=170,height=130)

        b1_1=Button(bg_img,text="Face Detector",command=self.face_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=430,y=235,width=170,height=30)

        # Attendance Button
        img9=Image.open("C:/Users/Rajnikant/Desktop/Face Recognition system/Images/attendance.jpg")
        img9=img9.resize((170,130),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,command=self.attedance_data,cursor="hand2")
        b1.place(x=680,y=100,width=170,height=130)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attedance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=680,y=235,width=170,height=30)

        #Help Button
        img11=Image.open("C:/Users/Rajnikant/Desktop/Face Recognition system/Images/help.jpg")
        img11=img11.resize((170,130),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,command=self.help_btn,cursor="hand2")
        b1.place(x=930,y=100,width=170,height=130)

        b1_1=Button(bg_img,text="Help",cursor="hand2",command=self.help_btn,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=930,y=235,width=170,height=30)
        


        # Train data Button 
        img7=Image.open("C:/Users/Rajnikant/Desktop/Face Recognition system/Images/5.jpg")
        img7=img7.resize((170,130),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,command=self.train_data,cursor="hand2")
        b1.place(x=170,y=320,width=170,height=130)

        b1_1=Button(bg_img,text="Train data",command=self.train_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=170,y=455,width=170,height=30)

        # Photos Button
        img8=Image.open("C:/Users/Rajnikant/Desktop/Face Recognition system/Images/photo.jpg")
        img58=img8.resize((170,130),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,command=self.open_img,cursor="hand2")
        b1.place(x=430,y=320,width=170,height=130)

        b1_1=Button(bg_img,text="Photos",command=self.open_img,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=430,y=455,width=170,height=30)


        

        # Developer Button
        img10=Image.open("C:/Users/Rajnikant/Desktop/Face Recognition system/Images/developer.png")
        img10=img10.resize((170,130),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,command=self.dev_btn,cursor="hand2")
        b1.place(x=680,y=320,width=170,height=130)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.dev_btn,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=680,y=455,width=170,height=30)

        
        #Exit Button
        img12=Image.open("C:/Users/Rajnikant/Desktop/Face Recognition system/Images/exit.jpg")
        img12=img12.resize((170,130),Image.ANTIALIAS)
        self.photoimg12=ImageTk.PhotoImage(img12)

        b1=Button(bg_img,image=self.photoimg12,command=self.iExit,cursor="hand2")
        b1.place(x=930,y=320,width=170,height=130)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=930,y=455,width=170,height=30)

    def open_img(self):
        os.startfile("C:/Users/Rajnikant/Desktop/Face Recognition system/Data")

    ####### Student details ########
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
    
    def attedance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    
    def dev_btn(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_btn(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)
    
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure to exit?",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return 

    

if __name__== "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()