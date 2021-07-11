from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import numpy as np
import os



class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x800+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",30,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1450,height=40)

        img_left=Image.open("C:/Users/Rajnikant/Desktop/Face Recognition system/Images/6.jpg")
        img_left=img_left.resize((675,675),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        bg_img=Label(self.root,image=self.photoimg_left)
        bg_img.place(x=0,y=40,width=675,height=675)

        img_right=Image.open("C:/Users/Rajnikant/Desktop/Face Recognition system/Images/19.jpg")
        img_right=img_right.resize((675,675),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        bg_img=Label(self.root,image=self.photoimg_right)
        bg_img.place(x=675,y=40,width=675,height=675)

        btn=Button(bg_img,text="FACE RECOGNITION",command=self.face_recog,cursor="hand2",font=("times new roman",15,"bold"),bg="red",fg="white")
        btn.place(x=90,y=400,width=230,height=40)
    ######### Attendance ##################
    def mark_attendance(self,i,n,d):
        with open("C:/Users/Rajnikant/Desktop/Face Recognition system/atten.csv","r+",newline="\n") as f:
            myDatalist=f.readlines()
            name_list=[]
            for line in myDatalist:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtstring=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{n},{d},{dtstring},{d1},present")

    
    ############ Face Recognition Function ##########
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_img,scaleFactor,minNeighbors)

            coord=[]
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_img[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                conn=mysql.connector.connect(username="root",password="Rajni@123",host="localhost",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select student_Name from student where Student_Id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select Department from student where Student_Id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("select Student_Id from student where Student_Id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)


                if confidence>77:
                    cv2.putText(img,f"ID:  {i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:  {n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department: {d}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i, n, d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]
            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("C:/Users/Rajnikant/Desktop/Face Recognition system/haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("C:/Users/Rajnikant/Desktop/Face Recognition system/classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while (True):
            ret,img=video_cap.read()
            img=recognize(img, clf, faceCascade)
            cv2.imshow("welcome to face recognition",img)

            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
        video_cap.release()
        cv2.destroyAllWindows()







if __name__== "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()