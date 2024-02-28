from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
from PIL import Image,ImageTk
import numpy as  np,joblib
import time


w=Tk()
w.geometry('1367x740')
w.minsize(1367,740)
w.minsize(1367,740)
w.config(bg='#666666')




#-----------------------------Handlers------------

def e_surprise1(event):
    event.widget.config(borderwidth=4,relief=RAISED,bg='#ffffcc')

def e_surprise2(event):
    event.widget.config(borderwidth=1,bg='white')

def predict(event):
    l1=[]
    my_progress['value']=0
    label.config(text='Processing...')
    for i in range(5):
        my_progress['value']+=20
        my_progress.update_idletasks()
        time.sleep(.4)
    try:
        for i in range(len(l)):
            l1.append(float(l2[i].get()))
    except:
        label.config(text='')
        mb.showerror('Some error has occured','--------PROCESSING ERROR-------\n\nMay Be You Entered Wrong Values \n \tOR\n Leave Some Entries')
        my_progress['value']=0
    else:
        arr=np.array([l1])
        model=joblib.load('breast_cancer_detection.pkl')
        value=model.predict(arr)
        label.config(text='')
        if value==0.0:
            mb.showwarning('URGENT ATTENTION NEEDED!','The Patient has BREAST CANCER.')
        else:
            mb.showinfo('NO NEED TO WORRY','The Patient has no Breast Cancer')
        my_progress['value']=0

def clear(event):
    setting()

def destroy(event):
    w.destroy()

#----------------------------------------------------





def setting():
    for i in range(len(l)):
        l2[i].set('')

# def setting():
#     my_values=[17.99, 10.38, 122.8, 1001.0, 0.1184, 0.2776, 0.3001, 0.1471, 0.2419, 0.07871, 1.095, 0.9053, 8.589, 153.4, 0.006399, 0.04904, 0.05373, 0.01587, 0.03003, 0.006193, 25.38, 17.33, 184.6, 2019.0, 0.1622, 0.6656, 0.7119, 0.2654, 0.4601, 0.1189]
#     for i in range(len(l)):
#         l2[i].set(my_values[i])



image=Image.open('doctor1.jpg')
resized_image=image.resize((550,740))
photo=ImageTk.PhotoImage(resized_image)
Label(w,image=photo,bg='#666666').pack(side=LEFT)



Label(w,text='Breast Cancer Detection Application\n Using Machine Learning Model',font='lucida 20 italic',fg='white',bg='dark green').pack(fill=X)



l=['mean radius', 'mean texture', 'mean perimeter', 'mean area',
       'mean smoothness', 'mean compactness', 'mean concavity',
       'mean concave points', 'mean symmetry', 'mean fractal dimension',
       'radius error', 'texture error', 'perimeter error', 'area error',
       'smoothness error', 'compactness error', 'concavity error',
       'concave points error', 'symmetry error',
       'fractal dimension error', 'worst radius', 'worst texture',
       'worst perimeter', 'worst area', 'worst smoothness',
       'worst compactness', 'worst concavity', 'worst concave points',
       'worst symmetry', 'worst fractal dimension']



x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24,x25,x26,x27,x28,x29,x30=[StringVar() for i in range(30)]
l2=[x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24,x25,x26,x27,x28,x29,x30]
setting()


Label(w,text='Enter the value of Tumor Features',font='helvetica 12 bold',fg='white',bg='red').pack(fill=X,pady=5)
c=0
frame=Frame(w,bg='#888888')
frame.pack(fill=X)

for k in range(3):
    f1=Frame(frame,bg='#888888')
    f1.grid(row=k,column=0,padx=12,pady=12)
    for m in range(2):
        f2=Frame(f1,bg='#888888')
        f2.grid(row=0,column=m,padx=50)
        for i in range(5):
            for j in range(2):
                if j%2==0:
                    Label(f2,text=f'{l[c].title()}: ',bg='#888888',fg='white',font='lucida 9 bold').grid(row=i,column=j,pady=5)
                else:
                    e=Entry(f2,textvariable=l2[c])
                    e.grid(row=i,column=j,pady=5)
                    e.bind('<ButtonPress-1>',e_surprise1)
                    e.bind('<Leave>',e_surprise2)
                    c+=1



frame1=Frame(w,bg='#666666')
frame1.pack(pady=14)

b1=Button(frame1,text='Predict Cancer',padx=12,pady=8,font='lucida 9 bold')
b1.grid(row=0,column=0,padx=7)
b1.bind('<ButtonPress-1>',predict)

b2=Button(frame1,text='Clear All',padx=12,pady=8,font='lucida 9 bold')
b2.grid(row=0,column=1,padx=7)
b2.bind('<ButtonPress-1>',clear)

b3=Button(frame1,text='Close',padx=12,pady=8,font='lucida 9 bold')
b3.grid(row=0,column=2,padx=7)
b3.bind('<ButtonPress-1>',destroy)



my_progress=ttk.Progressbar(w,orient=HORIZONTAL,length=400,mode='determinate')
my_progress.place(x=760,y=710)

label=Label(w,text='',fg='#00ff00',bg='#666666',font='helvetica 12 italic')
label.place(x=1180,y=710)



w.mainloop()




