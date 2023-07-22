from tkinter import *

root=Tk()
#these to function will return the height and width of the screen rispectively
screenHeigth=root.winfo_screenheight()
screenWidth=root.winfo_screenwidth()
#pass the screen width and height to the root.geomatry()
root.geometry(f"{screenWidth}x{screenHeigth}")#width x heigth

root.minsize(100,100)#set the min width of the screeen if we will try to expand the width it willnot go more then the resolution given to this function

# root.maxsize(root.winfo_screenwidth(),root.winfo_screenheight())#set the max width of the screeen if we will try to expand the width it willnot go more then the resolution given to this function

body=Frame(background="gray",height=screenHeigth,width=screenWidth)
body.pack()

monogramPhoto=PhotoImage(file="py.png")
monogramLable=Label(body,image=monogramPhoto,height=screenHeigth,width=screenWidth)
monogramLable.pack()

nameLable=Label(body,text="Enter your name:",fg="black",bg="gray")
nameLable.pack()

NameTextbox=Text(body,height=2,width=20)
NameTextbox.pack()
submitButton=Button(body,text="Submit",activebackground="black",activeforeground="white")
submitButton.pack()

root.mainloop()