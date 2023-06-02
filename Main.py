import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv
import tkinter as tk
from tkinter import font

#Main Page
def load_frame1():
    clear_widgets(frame2)
    frame1.tkraise()
    frame1.pack_propagate(False)
    tk.Label(frame1, text="Vokabel-App", bg="grey", fg="black", font=("TkMeanuFont", 14)).pack()
    # button
    tk.Button(frame1, text="Vocab Decks", font=("Times New Roman", 20), bg="grey", fg="white", cursor="hand1",
              activebackground="#badee2", activeforeground="black", command=lambda: load_frame2()).grid(pady=250)

#Vocab Adding
def load_frame2():
    clear_widgets(frame1)
    frame2.tkraise()
    frame2.grid_propagate(False)
    tk.Label(frame2, text="Add a new Word", bg="grey", fg="black", font=("TkMeanuFont", 14)).grid(row=1, column=10,
                                                                                                  pady=0)
    # button
    tk.Button(frame2, text="Go Back", font=("TkHeadingFont", 10), bg="grey", fg="white", cursor="hand1",
              activebackground="#badee2", activeforeground="black", command=lambda: load_frame1()).grid(row=0, column=0,
                                                                                                        pady=2)
    vocab = tk.Entry(frame2)
    vocab.grid(row=3, column=3, pady=5)
    vocab_placeholder = tk.Label(frame2, text="front side", fg="grey", bg="white", font=("Times New Roman", 10))
    vocab_placeholder.grid(row=3, column=3, pady=1)
    vocab_placeholder.bind("<Button-1>", lambda e: vocab.focus())
    answer = tk.Entry(frame2)
    answer.grid(row=4, column=3, pady=5)
    answer_placeholder = tk.Label(frame2, text="back side", fg="grey", bg="white", font=("Times New Roman", 10))
    answer_placeholder.grid(row=4, column=3, pady=1)
    answer_placeholder.bind("<Button-1>", lambda f: answer.focus())
    tk.Button(frame2, text="Add", font=("Times New Roman", 20), bg="grey", fg="white", cursor="hand1",
              activebackground="#badee2", activeforeground="black",
              command=lambda: [submitVocab(vocab.get(), answer.get()),answer.delete(0,tk.END),vocab.delete(0,tk.END)]).grid(row=5, column=4, pady=3)

def writingformat(front, back):
    return str(front+";"+back+"\n")

def load_frame3():
    clear_widgets(frame1)
    clear_widgets(frame2)
    frame3.tkraise()
    frame3.grid_propagate(False)
    frame3.pack_propagate(False)


def clear_widgets(frame):
    for widget in frame.winfo_children():
        widget.destroy()


def submitVocab(vocab, answer):
    front = vocab
    back = answer
    if (len(front) != 0 and len(back) != 0):
        print(front, " ", back, " has been added")

        vocabs[0].append(front)
        vocabs[1].append(back)
        # string = str(front,";",back,"\n")
        with open("vocabs.txt", "a") as f:
            f.write(writingformat(front, back))
        f.close()


root = tk.Tk()
root.title("App")

vocabs = [[], []]

# root.eval("tk::PlaceWindow . center")
x = root.winfo_screenwidth() // 2
y = int(root.winfo_screenheight() * 0.1)
root.geometry("500x600+" + str(x) + "+" + str(y))

frame1 = tk.Frame(root, width=500, height=600, bg="grey")
frame2 = tk.Frame(root, width=500, height=600, bg="grey")
frame3 = tk.Frame(root, width=500, height=600, bg="grey")

for frame in (frame1, frame2, frame3):
    frame.grid(row=0, column=0)

load_frame1()

# run the app
root.mainloop()