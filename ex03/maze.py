import tkinter as tk
import maze_maker as mm
import random

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def count_up():
    global tmr, jid
    tmr = tmr + 1
    label1["text"] = tmr
    jid = root1.after(1000, count_up)

def main_proc():
    global mx, my
    global cx, cy
    global tori
    if key == "w":
        tori = tk.PhotoImage(file=f"fig/4.png")
        canv.create_image(cx, cy, image=tori, tag="tori")
        my -= 1
    if key == "s":
        tori = tk.PhotoImage(file=f"fig/3.png")
        canv.create_image(cx, cy, image=tori, tag="tori")
        my += 1
    if key == "a":
        tori = tk.PhotoImage(file=f"fig/1.png")
        canv.create_image(cx, cy, image=tori, tag="tori")
        mx -= 1
    if key == "d":
        tori = tk.PhotoImage(file=f"fig/6.png")
        canv.create_image(cx, cy, image=tori, tag="tori")
        mx += 1
    if maze_list[my][mx] == 0:
        cx, cy = mx*100+50, my*100+50
        if key == "w":
            tori = tk.PhotoImage(file=f"fig/4.png")
            canv.create_image(cx, cy, image=tori, tag="tori")
        if key == "s":
            tori = tk.PhotoImage(file=f"fig/3.png")
            canv.create_image(cx, cy, image=tori, tag="tori")
        if key == "a":
            tori = tk.PhotoImage(file=f"fig/1.png")
            canv.create_image(cx, cy, image=tori, tag="tori")
        if key == "d":
            tori = tk.PhotoImage(file=f"fig/6.png")
            canv.create_image(cx, cy, image=tori, tag="tori")
    else:
        if key == "w":
            my += 1
        if key == "s":
            my -= 1
        if key == "a":
            mx += 1
        if key == "d":
            mx -= 1
    canv.coords("tori", cx, cy)
    root.after(100, main_proc)


if __name__ == "__main__":
    root = tk.Tk()
    root1 = tk.Tk()
    root.title("迷えるこうかとん")
    root1.title()
    label1 = tk.Label(root1, font=("", 80))
    label1.pack()
    root1.after(1000, count_up)
    tmr = 0
    jid = None

    canv = tk.Canvas(root, width=1500, height=900, bg="black")
    canv.pack()

    #練習9,10
    maze_list = mm.make_maze(15, 9)
    # print(maze_list)
    mm.show_maze(canv, maze_list)
    
    tori = tk.PhotoImage(file=f"fig/3.png")
    mx, my = 1, 1
    cx, cy = mx*100+50, my*100+50
    canv.create_image(cx, cy, image=tori, tag="tori")

    key = "" #現在押されているキーを表す変数

    #練習5,6
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    #練習7
    main_proc()

    root.after(1000, count_up)

    root = tk.mainloop()
   


