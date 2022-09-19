import tkinter as tk


window = tk.Tk()
window.title("Hello wold")
window.geometry("300x300")

canvas=tk.Canvas(width=300,height=300,background="white")
canvas.pack()

canvas.create_polygon(35,20,85,20,110,63,85,106,35,106,10,63,fill="black")





tk.mainloop()