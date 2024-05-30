import tkinter as tk

window = tk.Tk()
window.geometry("900x600")
window.title("三目並べ")

frame = tk.Frame(window,bd=1, relief="solid")
frame.place(x=100, y=70)

record = ""
def list():
    global record
    record = []
    for n in range(9):
        record.append("")
list()

result = ""

def gudge(num, symbol):
    global record
    global result
    record[num] = symbol
    
    if (record[0] == record[1] == record[2] == symbol)or\
        (record[3] == record[4] == record[5] == symbol)or\
        (record[6] == record[7] == record[8] == symbol):
            result = tk.Label(window, text=symbol+"の勝利!", font=("MS Gothic", 50))
            return result.place(x=580, y=150)
    
    if (record[0] == record[3] == record[6] == symbol)or\
        (record[1] == record[4] == record[7] == symbol)or\
        (record[2] == record[5] == record[8] == symbol):
            result = tk.Label(window, text=symbol+"の勝利!", font=("MS Gothic", 50))
            return result.place(x=580, y=150)
    
    if (record[0] == record[4] == record[8] == symbol)or\
        (record[2] == record[4] == record[6] == symbol):
            result = tk.Label(window, text=symbol+"の勝利!", font=("MS Gothic", 50))
            return result.place(x=580, y=150)
    return

eventlabel = []
ox = ""
t = 0

def clk(event):
    global result
    global eventlabel
    global ox
    global t

    if result == "":
        if t%2 == 0:
            ox = "〇"
        else:
            ox = "×"
        
        event.widget.configure(relief="solid", bd=1)
        eventlabel.append(tk.Label(event.widget, text=ox, font=("MS Gothic", 100)))
        eventlabel[t].place(width=150, height=150)
        
        gudge(event.widget.num, ox)
        
        if t == 8:
            if result == "":
                result = tk.Label(window, text="引き分け!", font=("MS Gothic", 50))
                return result.place(x=580, y=150)
        t += 1

i = 0
for r in range(3):
    for c in range(3):
        square = tk.Frame(frame, width=150, heigh=150,bd=1, relief="solid")
        square.grid(row=r, column=c)
        square.bind("<Button>", clk)
        square.num = i
        i += 1

def retry():
     global i
     global t
     global eventlabel
     global result
     list()
     i = 0
     for l in eventlabel:
          l.place_forget()
     eventlabel = []
     t = 0
     if result != "":
        result.place_forget()
        result = ""

retry_btn = tk.Button(window, text="Retry", width=5, height=1, relief="raised", font=("MS Gothic", 50), bg="yellow", activebackground="gold", command=retry)
retry_btn.place(x=630, y=350)

window.mainloop()
