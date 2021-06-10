from tkinter import *
from tkinter import filedialog

root=Tk()

root.title("Image Viewer")
root.iconbitmap("C:/Users/Shiven Prakash/Desktop/PICS/Icon1.ico") 

count = 0

def OpenFile():
	global count
	count=count+1
	global image1
	global label1
	if count > 1:
		label1.grid_forget()
	root.filename=filedialog.askopenfilename(initialdir="C:/Users/Shiven Prakash/Desktop/Elecronics and Python/Python Softwares with Tkinter",title = "Select File",filetypes = (("PngImage","*.png"),("JpgImage","*.jpg"),("AllFiles","*.*")))
	image1=PhotoImage(file=root.filename)
	label1=Label(image=image1)
	label1.grid(row=1,column=1)

OF = Button(root,text="Open Image",command=OpenFile)
OF.grid(row=2,column=1)

be=Button(root,text="Quit",padx=20,pady=16,command=root.quit)
be.grid(row=2,column=2)

root.mainloop()