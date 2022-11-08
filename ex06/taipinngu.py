import tkinter as tk
from tkinter import messagebox
import sys
import random
import time
import threading

QUESTION = ["tkinter", "geometry", "widgets", "messagebox", "configure", 
            "label", "column", "rowspan", "grid", "init", "collaborator",
            "setting", "kokaton"]

class Fight_kokaton(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        master.geometry("500x400")
        master.title("こうかとんを倒せ！")

        # 問題数インデックス
        self.index = 0

        # 正解数カウント用
        self.correct_cnt = 0

        self.create_widgets()

        t = threading.Thread(target=self.timer)
        t.start()

        # Tkインスタンスに対してキーイベント処理を実装
        self.master.bind("<KeyPress>", self.type_event)

    # ウィジェットの生成と配置
    def create_widgets(self):
        self.q_label = tk.Label(self, text="お題：", font=("",20))
        self.q_label.grid(row=0, column=0)
        self.q_label2 = tk.Label(self, text=random.choice(QUESTION), width=10, anchor="nw", font=("",20))
        self.q_label2.grid(row=0, column=1)

        self.ans_label = tk.Label(self, text="解答：", font=("",20))
        self.ans_label.grid(row=1, column=0)
        self.ans_label2 = tk.Label(self, text="", width=10, anchor="nw", font=("",20))
        self.ans_label2.grid(row=1, column=1)

        self.result_label = tk.Label(self, text="", font=("",20))
        self.result_label.grid(row=2, column=0, columnspan=2)

        self.time_label = tk.Label(self, text="", font=("",20))
        self.time_label.grid(row=3, column=0, columnspan=2)

        self.flg2 = True

        self.img = tk.PhotoImage(file="fig/koukaton.png")
        self.canvas = tk.Canvas(self, width=300, height=300)
        self.canvas.create_image(150, 150, image=self.img)
        self.canvas.grid(row=4, column=0, columnspan=3)

    # キー入力時のイベント処理
    def type_event(self, event):
        if event.keysym == "Return":# 入力値がEnterの場合は答え合わせ
            if self.q_label2["text"] == self.ans_label2["text"]:
                self.result_label.configure(text="正解！", fg="red")
                self.correct_cnt += 1

            else:
                self.result_label.configure(text="残念！", fg="blue")

            # 解答欄をクリア
            self.ans_label2.configure(text="")

            # 次の問題を出題
            self.index += 1
            if self.index == 10: #len(QUESTION)
                self.q_label2.configure(text="終了！")
                if self.correct_cnt > 7:
                    messagebox.showinfo("リザルト", f"{self.correct_cnt}/10問正解！こうかとんに勝った！")
                else:
                    messagebox.showinfo("リザルト", f"{self.correct_cnt}/10問正解。こうかとんに負けちゃった…")
                sys.exit(0)
            self.q_label2.configure(text=random.choice(QUESTION))

        elif event.keysym == "BackSpace":
            text = self.ans_label2["text"]
            self.ans_label2["text"] = text[:-1]

        else:
            self.ans_label2["text"] += event.keysym # 入力値がEnter以外の場合は文字入力としてラベルに追記する

    def timer(self):
        self.second = 0
        self.flg = True
        while self.flg:
            self.second += 1
            self.time_label.configure(text=f"経過時間：{self.second}秒")
            time.sleep(1)


if __name__ == "__main__":
    root = tk.Tk()
    Fight_kokaton(master=root)
    root.mainloop()