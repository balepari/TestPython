import tkinter
from PIL import ImageTk, Image

top = tkinter.Tk()
w=tkinter.Canvas(top, width=800, height=600, bg="yellow")


path="hello.jpg"
img=ImageTk.PhotoImage(Image.open(path))

image=w.create_image(50,50,image=img, anchor='nw')
a=w.create_line(0,0,200,200)

frame=tkinter.Frame(top)
frame.grid(row=0, column=0)

btn=[[0 for x in range(3)] for x in range(3)] 
for x in range(3):
	for y in range(3):
		btn[x][y] = tkinter.Button(frame)
		btn[x][y].grid(column=x, row=y)



# b=tkinter.Button(top, width=1, height=1, text="1")


# w.pack()
top.mainloop()
