from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np
import os



class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x800+0+0")
        self.root.title("Face Recognition System")

        img=Image.open("C:/Users/Rajnikant/Desktop/Face Recognition system/Images/developer1.png")
        img=img.resize((1400,760),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1400,height=760)

        title_lbl=Label(bg_img,text="DEVELOPER",font=("times new roman",30,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1400,height=40)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=900,y=40,width=450,height=600)

        img1=Image.open("C:/Users/Rajnikant/Desktop/Face Recognition system/Images/7.jpg")
        img1=img1.resize((200,200),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(main_frame,image=self.photoimg1)
        f_lbl.place(x=250,y=0,width=200,height=200)

        # Developer Info
        dev_label=Label(main_frame,text="hello i am Rajnikant",font=("times new roman",14,"bold"),bg="white")
        dev_label.place(x=0,y=5)

        dev_label=Label(main_frame,text="I am a full stack developer",font=("times new roman",14,"bold"),bg="white")
        dev_label.place(x=0,y=30)







if __name__== "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()