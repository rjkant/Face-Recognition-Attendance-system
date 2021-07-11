from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np
import os



class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x800+0+0")
        self.root.title("Face Recognition System")

        
        #Background Image
        
        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",30,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1500,height=40)

        img_top=Image.open("C:/Users/Rajnikant/Desktop/Face Recognition system/Images/9.png")
        img_top=img_top.resize((1400,560),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        bg_img=Label(self.root,image=self.photoimg_top)
        bg_img.place(x=0,y=40,width=1400,height=560)

        btn=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="red",fg="white")
        btn.place(x=0,y=600,width=1400,height=40)


    def train_classifier(self):
        data_dir=("C:/Users/Rajnikant/Desktop/Face Recognition system/Data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]  #list comprehension

        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L') #Gray scale image
            imagenp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imagenp)
            ids.append(id)
            cv2.imshow("Training",imagenp)
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break

        ids=np.array(ids)

        ######### Train the classifier ########
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)            
        clf.write("C:/Users/Rajnikant/Desktop/Face Recognition system/classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed",parent=self.root)

        




if __name__== "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()