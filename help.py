from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np
import os



class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x800+0+0")
        self.root.title("Face Recognition System")

        img=Image.open("C:/Users/Rajnikant/Desktop/Face Recognition system/Images/developer1.png")
        img=img.resize((1400,760),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1400,height=760)

        title_lbl=Label(bg_img,text="HELP DESK",font=("times new roman",30,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1400,height=40)

        help_label=Label(bg_img,text="Email:rajnikant7549@gmail.com",font=("times new roman",14,"bold"),bg="red")
        help_label.place(x=550,y=220)



if __name__== "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()