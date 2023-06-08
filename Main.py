import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv
import tkinter as tk
import glob
from tkinter import font




#Constructor
txtfiles = glob.glob("*.txt")#

currentFile = txtfiles[0]

#Main Page
def load_frame1():
    clear_widgets(frame2)
    clear_widgets(frame3)
    frame1.tkraise()
    frame1.pack_propagate(False)
    tk.Label(frame1, text="Vokabel-App", bg="grey", fg="black", font=("TkMeanuFont", 14)).pack()
    # button
    tk.Button(frame1, text="Vocab Decks", font=("Times New Roman", 20), bg="grey", fg="white", cursor="hand1",
              activebackground="#badee2", activeforeground="black", command=lambda: load_frame3()).grid(pady=250)

#Vocab Adding Page
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

#Decks List
def load_frame3():
    clear_widgets(frame1)
    clear_widgets(frame2)
    clear_widgets(frame3)
    frame3.tkraise()
    frame3.grid_propagate(False)
    frame3.pack_propagate(False)
    tk.Label(frame3, text="Choose a Deck", bg="grey", fg="black", font=("TkMeanuFont", 10)).pack()
    for deck in txtfiles:
        tk.Button(frame3, text= ""+deck+"", font=("Times New Roman", 20), bg="grey", fg="white", cursor="hand1",
              activebackground="#badee2", activeforeground="black",command=lambda: [load_frame2(), editCurrentfile(deck)]).pack()
    tk.Button(frame3,text = "Add a new Deck",font=("Times New Roman", 10), bg="grey", fg="white", cursor="hand1",
              activebackground="#badee2", activeforeground="black",command=lambda: [newDeck(),load_frame3()]).pack()


def newDeck():

    s = newDeckHilfsmethode()
    f = open(s,"w")
    f.close()
    txtfiles.append(s)
    global Liste
    Liste = ""

def newDeckHilfsmethode():

    if ( "newDeck.txt" in txtfiles):
        print ("newDeck.txt" in txtfiles)
        return "newDeck"+ str(1)


    if ("newDeck" +str(1)+".txt" in txtfiles):
        if ("newDeck" + str(2) + ".txt" in txtfiles):
            if ("newDeck" + str(3) + ".txt" in txtfiles):
                if ("newDeck" + str(4) + ".txt" in txtfiles):
                    if ("newDeck" + str(5) + ".txt" in txtfiles):
                        if ("newDeck" + str(6) + ".txt" in txtfiles):
                            raise Exception("Too many Docs with the same name")
                        return "newDeck" + str(5 + 1) + ".txt"
                    return "newDeck" + str(4 + 1) + ".txt"
                return "newDeck" + str(3 + 1) + ".txt"
            return "newDeck" + str(2 + 1) + ".txt"
        return "newDeck"+str(1+1)+".txt"
    return "newDeck.txt"

def editCurrentfile(deck):
    currentFile = txtfiles[txtfiles.index(deck)]


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
        with open(currentFile, "a") as f:
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