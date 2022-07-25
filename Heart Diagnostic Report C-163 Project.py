# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 19:08:14 2022

@author: Swasti
"""

from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Heart Diagnostic Report")
root.geometry("600x600")
root.configure(background="salmon")

question1_radioButton = StringVar(value = "0")

Question1 = Label(root, text = "Do you experience shortness of breath during routine activities?")
Question1.pack()
Question1_r1 = Radiobutton(root, text = "yes", variable = question1_radioButton, value = "yes", bg = "salmon")
Question1_r1.pack()
Question1_r2 = Radiobutton(root, text = "no", variable = question1_radioButton, value = "no", bg = "salmon")
Question1_r2.pack()

question2_radioButton = StringVar(value = "0")

Question2 = Label(root, text = "Do you hae swelling in the feet/ankles/legs (shoes feel tighter) or abdomen?")
Question2.pack()
Question2_r1 = Radiobutton(root, text = "yes", variable = question2_radioButton, value = "yes", bg = "salmon")
Question2_r1.pack()
Question2_r2 = Radiobutton(root, text = "no", variable = question2_radioButton, value = "no", bg = "salmon")
Question2_r2.pack()

question3_radioButton = StringVar(value = "0")

Question3 = Label(root, text = "Do you feel any of these symptoms - confusion, disorientation or loss of memory?")
Question3.pack()
Question3_r1 = Radiobutton(root, text = "yes", variable = question3_radioButton, value = "yes", bg = "salmon")
Question3_r1.pack()
Question3_r2 = Radiobutton(root, text = "no", variable = question3_radioButton, value = "no", bg = "salmon")
Question3_r2.pack()

question4_radioButton = StringVar(value = "0")

Question4 = Label(root, text = "Do you experience shortness of breath during rest/lying down?")
Question4.pack()
Question4_r1 = Radiobutton(root, text = "yes", variable = question4_radioButton, value = "yes", bg = "salmon")
Question4_r1.pack()
Question4_r2 = Radiobutton(root, text = "no", variable = question4_radioButton, value = "no", bg = "salmon")
Question4_r2.pack()

question5_radioButton = StringVar(value = "0")

Question5 = Label(root, text = "Do you experience persistent wheezing/coughing that produces white or pink blood tinged mucus?")
Question5.pack()
Question5_r1 = Radiobutton(root, text = "yes", variable = question5_radioButton, value = "yes", bg = "salmon")
Question5_r1.pack()
Question5_r2 = Radiobutton(root, text = "no", variable = question5_radioButton, value = "no", bg = "salmon")
Question5_r2.pack()

def fever_score():
    score = 0
    if question1_radioButton.get() == "yes" : 
        score = score+10
        print(score)
        
    if question2_radioButton.get() == "yes" :
        score = score+10
        print(score)
        
    if question3_radioButton.get() == "yes" :
        score = score+10
        print(score)
        
    if question4_radioButton.get() == "yes" :
        score = score+10
        print(score)
        
    if question5_radioButton.get() == "yes" :
        score = score+10
        print(score)
        
    if score <=10:
        messagebox.showinfo("Report", "You don't need to visit a doctor.")
        
    elif score >10 and score <=30:
        messagebox.showinfo("Report", "You might perhaps have to visit a doctor.")
        
    else : 
        messagebox.showinfo("Report", "I strongly advise you to visit a doctor.")
        
btn = Button(root, text = "Click Me", command = fever_score)
btn.pack()

root.mainloop()