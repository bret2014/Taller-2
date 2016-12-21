from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()

my_image = PhotoImage(file="naruto.gif")
canvas.create_image(0,0, anchor=NW,image=my_image)
tk.mainloop()

tk=tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
canvas.create_polygon(10,10,10,60,50,35)

for x in range(0,60):
    canvas.move(1,5,0)
    tk.update()
    time.sleep(0.05)

tk.mainloop()
