import tkinter as tk
from tkinter.tix import MAX
import maze_maker as mm # 練習8
import random

# 練習5
def key_down(event):
    global key
    key = event.keysym

def count_up():
    global tmr
    tmr = tmr+1
    label["text"] = tmr
    root.after(1000, count_up)


# 練習6
def key_up(event):
    global key
    key = ""

def main_proc():
    global cx, cy, mx, my
    if key == "Up":
        my -= 1
    if key == "Down":
        my += 1
    if key == "Left":
        mx -= 1
    if key == "Right":
        mx += 1
    if maze_list[my][mx] == 0:
        cx, cy =mx*100+50, my*100+50
    else:
        if key == "Up":
            my += 1
        if key == "Down":
            my -= 1
        if key == "Left":
            mx += 1
        if key == "Right":
            mx -= 1
    canv.coords("tori", cx, cy)
    root.after(100, main_proc)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん") # 練習1
    root1 = tk.Tk()
    label = tk.Label(root1,font=("", 80))
    label.pack()

    # 練習2
    canv = tk.Canvas(root, width=1500, height=900, bg="black")
    canv.pack()

    # 練習9,10
    maze_list = mm.make_maze(15,9)
    # print(maze_list)
    mm.show_maze(canv, maze_list)

    # 練習3
    tori = tk.PhotoImage(file="fig/5.png") 
    mx, my = 1, 1
    cx, cy = 300+50, 400+50
    canv.create_image(cx, cy, image=tori, tag="tori")

    # 練習4
    key = "" # 現在押されているキーを表す

    # 練習5,6
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)    

    # 練習7
    main_proc()

    root.mainloop()

    #root.after(1000, count_up)
    root.bind("<KeyPress>", key_down)
   


