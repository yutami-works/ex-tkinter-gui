import tkinter as tk

# 曜日のリストと現在の表示を表す番号
day_of_week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
current_dow = 0

## 曜日を前に進めるコールバック関数
def forward():
    global current_dow # グローバルの変数を使用
    current_dow += 1
    if current_dow == 7:
        current_dow = 0
    # ラベルのテキストを書き換える
    l_dow["text"] = day_of_week[current_dow]

## 曜日を後ろに戻すコールバック関数
def backward():
    global current_dow
    current_dow -= 1
    if current_dow == -1:
        current_dow = 6
    l_dow["text"] = day_of_week[current_dow]

# tkinterを終了させるコールバック関数
def fin():
    root.destroy()

# ウィンドウとウィジェットの生成とウィジェットの配置
root = tk.Tk()
root.title("DoW switch")
f = tk.Frame(root)
f.grid()

# ラベル
l_dow = tk.Label(f, text=day_of_week[current_dow])
l_dow.grid(row=0, column=0, columnspan=3)

# ボタンとイベント
b_backward = tk.Button(f, text="<-", command=backward)
b_forward = tk.Button(f, text="->", command=forward)
b_exit = tk.Button(f, text="EXIT", command=fin)
b_backward.grid(row=1, column=0)
b_forward.grid(row=1, column=1)
b_exit.grid(row=1, column=2)

# GUIのスタート
print("tkinter_started")
root.mainloop()

# GUI終了の確認
print("tkinter stopped")