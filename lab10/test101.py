import tkinter as tk

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)

def death(event):
    print(event.keycode)


root.bind("<Left>", death)

root.mainloop()