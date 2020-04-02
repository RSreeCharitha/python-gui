import json
import difflib as df
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def getWord():
    w = e.get().lower()
    if w in data:
        showData(w)
    elif len(df.get_close_matches(w, data.keys()))>0:
        match = df.get_close_matches(w, data.keys())[0]
        mb = messagebox.askyesno('What did you mean?', 'Did you mean {} ? '.format(match))
        if mb == True:
            showData(match)
        else:
            messagebox.showinfo('Not Found','Error: Word not found')
            e.delete(0, tk.END)
    else:
        messagebox.showinfo('Not Found','Error: Word not found')
        e.delete(0, tk.END)

def showData(w):
    defn = data[w]
    t.delete(1.0,tk.END)
    t.insert(tk.INSERT,defn)
    e.delete(0, tk.END)

data= json.load(open('data.json'))
root = tk.Tk()
root.title('Dictionary')
root.geometry('400x280+500+300')

l = ttk.Label(root, text='Enter word:')
t = tk.Text(root,height=10, width=30, wrap=tk.WORD)
e = ttk.Entry(root, width=20)
b = ttk.Button(root, text="Submit", command=getWord)

l.pack(padx=3, pady=3)
e.pack(padx=3, pady=3)
b.pack(padx=3, pady=3)
t.pack(padx=3, pady=3)

root.mainloop()
