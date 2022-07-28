from tkinter import*
from PIL import Image,ImageTk#pip inistall pillow
class Register:
    def _init_(Self,root):
        self,root=root
        self.root.title("Regiseration Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        #==Bg  Image===
        self.bg=ImageTk.PhotoImage(file="image/1.jpg")
        bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)


         #==LEFT  Image===
        self.left=ImageTk.PhotoImage(file="image/4.png")
        left=Label(self.root,image=self.left).place(x=80,y=100,width=400,height=500)


        #===Register Frame==
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)

        title=Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)


        f_name=Label(frame1,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
        txt_fname=Entry(frame1,font=("times new roman",15)bg="lightgray").place(x=50,y=130,width=250)

        l_name=Label(frame1,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=100)
        txt_lname=Entry(frame1,font=("times new roman",15)bg="lightgray").place(x=370,y=130,width=250)

        root=Tk()
        obj=Register(root)
        root.mainloop()