from tkinter import *
from PIL import ImageTk, Image
import customtkinter
import os
import tkinter

root_tk = tkinter.Tk()

root_tk.geometry("530x380")
root_tk.title("FitTracker")

root_tk.configure(bg='#3c3c3c')
customtkinter.set_appearance_mode("Dark")

img0 = ImageTk.PhotoImage(Image.open("FitTracker/default.jpg"))
img1 = ImageTk.PhotoImage(Image.open("FitTracker/armCurl.jpg"))
img2 = ImageTk.PhotoImage(Image.open("FitTracker/pushUp.jpg"))
img3 = ImageTk.PhotoImage(Image.open("FitTracker/dynamicChest.jpg"))
img4 = ImageTk.PhotoImage(Image.open("FitTracker/sitUp.png"))
img5 = ImageTk.PhotoImage(Image.open("FitTracker/legRaise.jpg"))
img6 = ImageTk.PhotoImage(Image.open("FitTracker/plank.jpg"))
img7 = ImageTk.PhotoImage(Image.open("FitTracker/squat.jpg"))
img8 = ImageTk.PhotoImage(Image.open("FitTracker/calfRaise.jpg"))
img9 = ImageTk.PhotoImage(Image.open("FitTracker/lunge.jpg"))
img10 = ImageTk.PhotoImage(Image.open("FitTracker/FIT.jpg"))
img11 = ImageTk.PhotoImage(Image.open("FitTracker/Instruction.png"))
img12 = ImageTk.PhotoImage(Image.open("FitTracker/aboutUs.jpg"))

imgList = [img0, img1, img2, img3, img4, img5, img6, img7, img8, img9, img10, img11, img12]



# functions, events
def imgShow(imgNum):
    global imgList
    global imgLabel
    imgLabel.place_forget()
    imgLabel = Label(iframe, borderwidth=0, image=imgList[imgNum])
    imgLabel.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

def open(filename):
    os.system('python '+ filename)
    print(filename)

def exercises():
    new_tk = Toplevel()
    new_tk.geometry("570x300")
    new_tk.configure(bg='#3c3c3c')

    # declaration ng items sa exercise window
    elabel = Label(new_tk, text="Exercises", font= ('Eras Bold ITC', 30, 'bold'), bg='#3c3c3c', fg='#1c94cf')
    btnback = customtkinter.CTkButton(master=new_tk, corner_radius=10, fg_color='#aa0000', hover_color='#ff3333', text="Back", command=lambda: [new_tk.withdraw(), root_tk.deiconify()])
    nframe = customtkinter.CTkFrame(master=new_tk, width=520, height=220, corner_radius=35, fg_color='#202020')

    # arms buttons
    alabel = Label(nframe, text="Arms", font= ('Eras Bold ITC', 16, 'bold'), bg='#202020', fg='#FFFFFF')
    btnacurl = customtkinter.CTkButton(master=nframe, width=140, height=40, corner_radius=10, text="Arm Curl", command=lambda: open("arm-curl.py"))
    btnpushup = customtkinter.CTkButton(master=nframe, width=140, height=40, corner_radius=10, text="Push-Ups", command=lambda: open("push-ups.py"))
    btndchest = customtkinter.CTkButton(master=nframe, width=140, height=40, corner_radius=10, text="Dynamic-Chest", command=lambda: open("dynamic-chest-workout.py"))
   
    # core buttons
    clabel = Label(nframe, text="Core", font= ('Eras Bold ITC', 16, 'bold'), bg='#202020', fg='#FFFFFF')
    btnsitup = customtkinter.CTkButton(master=nframe, width=140, height=40, corner_radius=10, text="Sit-Ups", command=lambda: open("sit-ups.py"))
    btnlraise = customtkinter.CTkButton(master=nframe, width=140, height=40, corner_radius=10, text="Leg Raise", command=lambda: open("leg-raise.py"))
    btnplank = customtkinter.CTkButton(master=nframe, width=140, height=40, corner_radius=10, text="Planking", command=lambda: open("planking.py"))

    # legs buttons
    llabel = Label(nframe, text="Legs", font= ('Eras Bold ITC', 16, 'bold'), bg='#202020', fg='#FFFFFF')
    btnsquat = customtkinter.CTkButton(master=nframe, width=140, height=40, corner_radius=10, text="Squats", command=lambda: open("squat.py"))
    btncalf = customtkinter.CTkButton(master=nframe, width=140, height=40, corner_radius=10, text="Calf-Raises", command=lambda: open("calf-raises.py"))
    btnlunge = customtkinter.CTkButton(master=nframe, width=140, height=40, corner_radius=10, text="Lunge", command=lambda: open("lunges.py"))


    # ***********************************************- placement ng items sa exercise window -***********************************************
    elabel.place(relx=0.39, rely=0.1, anchor= tkinter.E)
    btnback.place(relx=0.73, rely=0.1, anchor=tkinter.W)
    nframe.place(relx=0.5, rely=0.2, anchor=tkinter.N)

    # arms label, exercises
    alabel.place(relx=0.18, rely=0.15, anchor=tkinter.E)
    btnacurl.place(relx=0.32, rely=0.35, anchor=tkinter.E)
    btnpushup.place(relx=0.32, rely=0.55, anchor=tkinter.E)
    btndchest.place(relx=0.32, rely=0.75, anchor=tkinter.E)

    # core label, exercises
    clabel.place(relx=0.42, rely=0.15, anchor=tkinter.CENTER)
    btnsitup.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)
    btnlraise.place(relx=0.5, rely=0.55, anchor=tkinter.CENTER)
    btnplank.place(relx=0.5, rely=0.75, anchor=tkinter.CENTER)

    # legs label, exercises
    llabel.place(relx=0.68, rely=0.15, anchor=tkinter.W)
    btnsquat.place(relx=0.68, rely=0.35, anchor=tkinter.W)
    btncalf.place(relx=0.68, rely=0.55, anchor=tkinter.W)
    btnlunge.place(relx=0.68, rely=0.75, anchor=tkinter.W)

    root_tk.withdraw()


def instructions():
    global imgLabel
    global iframe
    new1_tk = Toplevel()
    new1_tk.geometry("800x380")
    new1_tk.configure(bg='#3c3c3c')

    # declaration ng items sa instructions tab

    ilabel = Label(new1_tk, text="Instructions", font= ('Eras Bold ITC', 30, 'bold'), bg='#3c3c3c', fg='#1c94cf')
    iframe = customtkinter.CTkFrame(master=new1_tk, width=400, height=350, corner_radius=35, fg_color='#202020')
    imgLabel = Label(master=iframe, image=img0, borderwidth=0)

    btnclose = customtkinter.CTkButton(master=new1_tk, width=140, height=40, corner_radius=10, fg_color='#aa0000', hover_color='#ff3333', text="Close", command=new1_tk.destroy)
    btnacurl = customtkinter.CTkButton(master=new1_tk, width=140, height=40, corner_radius=10, text="Arm Curl", command=lambda: imgShow(1))
    
    btnpushup = customtkinter.CTkButton(master=new1_tk, width=140, height=40, corner_radius=10, text="Push-Ups", command=lambda: imgShow(2))
    btndchest = customtkinter.CTkButton(master=new1_tk, width=140, height=40, corner_radius=10, text="Dynamic-Chest", command=lambda: imgShow(3))
    
    btnsitup = customtkinter.CTkButton(master=new1_tk, width=140, height=40, corner_radius=10, text="Sit-Ups", command=lambda: imgShow(4))
    btnlraise = customtkinter.CTkButton(master=new1_tk, width=140, height=40, corner_radius=10, text="Leg Raise", command=lambda: imgShow(5))
   
    btnplank = customtkinter.CTkButton(master=new1_tk, width=140, height=40, corner_radius=10, text="Planking", command=lambda: imgShow(6))
    btnsquat = customtkinter.CTkButton(master=new1_tk, width=140, height=40, corner_radius=10, text="Squats", command=lambda: imgShow(7))
    
    btncalf = customtkinter.CTkButton(master=new1_tk, width=140, height=40, corner_radius=10, text="Calf-Raises", command=lambda: imgShow(8))
    btnlunge = customtkinter.CTkButton(master=new1_tk, width=140, height=40, corner_radius=10, text="Lunge", command=lambda: imgShow(9))

    # *************************************----- placement ng items sa instructions window -----*************************************
    ilabel.place(relx=0.35, rely=0.12, anchor= tkinter.E)
    iframe.place(relx=0.45, rely=0.5, anchor=tkinter.W)

    btnclose.place(relx=0.20, rely=0.30, anchor=tkinter.E)
    btnacurl.place(relx=0.39, rely=0.30, anchor=tkinter.E)

    btnpushup.place(relx=0.20, rely=0.43, anchor=tkinter.E)
    btndchest.place(relx=0.39, rely=0.43, anchor=tkinter.E)

    btnsitup.place(relx=0.20, rely=0.56, anchor=tkinter.E)
    btnlraise.place(relx=0.39, rely=0.56, anchor=tkinter.E)

    btnplank.place(relx=0.20, rely=0.69, anchor=tkinter.E)
    btnsquat.place(relx=0.39, rely=0.69, anchor=tkinter.E)

    btncalf.place(relx=0.20, rely=0.82, anchor=tkinter.E)
    btnlunge.place(relx=0.39, rely=0.82, anchor=tkinter.E)

    imgLabel.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

def aboutUs():
    global imgU
    aboutTab = Toplevel()
    aboutTab.geometry("500x480")
    aboutTab.configure(bg='#3c3c3c')

    imgU = Label(aboutTab, borderwidth=0, image=imgList[12])
    imgU.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

# declaration ng items sa root_tk

frame = customtkinter.CTkFrame(master=root_tk, width=200, height=200, corner_radius=35, fg_color='#202020')
imgMain = Label(root_tk, borderwidth=0, image=imgList[10])


btnExercises = customtkinter.CTkButton(master=frame, height=40, corner_radius=10, text="Exercises", command=exercises)
btnSettings = customtkinter.CTkButton(master=frame, height=40, corner_radius=10, text="About Us", command=aboutUs)
btnInstructions = customtkinter.CTkButton(master=frame, height=40, corner_radius=10, text="Instructions", command=instructions)
#btnExercises = customtkinter.CTkButton(master=frame, corner_radius=10, text="Exercises", command=lambda: open("tracker.py"))



# placement sa UI ng root_tk

frame.place(relx=0.5, rely=0.35, anchor=tkinter.N)
imgMain.place(relx=0.5, rely=0.18, anchor=tkinter.CENTER)

btnExercises.place(relx=0.5, rely=0.35, anchor=tkinter.S)
btnInstructions.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
btnSettings.place(relx=0.5, rely=0.65, anchor=tkinter.N)




root_tk.mainloop()
# messagebox. = showinfo, showwarning, showerror, askquestion, askokcancel, askyesno