import tkinter as tk

def key_down(event):
    global key
    key = event.keysys
    
def key_up(event):
    global key
    key = " "

def main_proc():
    global cx, cy
    if key == "Up":
        cy -= 20
    if key == "Down":
        cy += 20
    if key == "Left":
        cx -= 20
    if key == "Right":
        cx += 20
    canv.coords("tori", cx, cy)
    root.after(100, main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん") # 練習1

    # 練習2
    canv = tk.Canvas(root, width=1500, height=900, bg="black")
    canv.pack()

    # 練習3
    tori = tk.PhotoImage(file="fig/5.png") 
    cx, cy = 300, 400
    canv.create_image(cx, cy, image=tori, tag="tori")

    # 練習4
    key = "" # 現在押されているキーを表す

    # 練習5,6
    root.bind("<KeyPress>", key_down) # 練習5
    root.bind("<KeyRelease>", key_up) # 練習6

    # 練習7
    main_proc()
    
    root.mainloop()


