from tkinter import *
from tkinter import messagebox  

# Create the main window
root = Tk()
root.geometry("400x250")  # Set window size
root.title("hw")  # Set window title
root.config(bg='sky blue')
def show_and_hide():
    if entry2['show'] == '*':
        entry2['show'] = ''
    else:
        entry2['show'] = '*'
def mainloop():
    file1 = open("C:\\Users\\atharv\\3D Objects\\pm.txt","a")
    L = ['Username : '+ entry1.get() + '  ,  ' + "Password : "+ entry2.get() + "\n"]
    file1.writelines(L)
    file1.close()  
    messagebox.showinfo("Good News",message="Your information has been successfully got saved in pm.txt")
    entry1.delete(0,END)
    entry2.delete(0,END)
checkBox_showPassword = Checkbutton(root,text='show',bg='pink',fg='black',
                                    command=show_and_hide)
label1 = Label(root,
              text="PASSWORD MANAGER",
              bg = 'pink',
              font = ('arial',15,'bold')
              )

label1.place(x=125,y=5)
# Create the label widget with all options
label2 = Label(root,
              text="Enter the Username or Email :",
              bg = 'sky blue',
              font = ('arial',10,'bold'))
label2.place(x=0,y=50)
entry1 = Entry(root,font= ('arial',10,'bold'),bg ='pink')
entry1.place(x=0,y=75)


label3 = Label(root,
              text="Enter the Password :",
              bg = 'sky blue',
              font = ('arial',10,'bold'),)
label3.place(x=0,y=130)
entry2 = Entry(root,font= ('arial',10,'bold'),bg ='pink',show='*')
entry2.place(x=0,y=154)
checkBox_showPassword.place(x=160,y=150)
butt = Button(root,text='Save Information',font=('arial',10,'bold'),bg='pink',fg='black',command=mainloop)
butt.place(x=125,y=200)
root.mainloop()