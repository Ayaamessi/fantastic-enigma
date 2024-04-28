import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.configure(bg='lightblue') 

score = 0

question1 = tk.StringVar()
question2 = tk.StringVar()
question3 = tk.StringVar() 
question4 = tk.StringVar()
question5 = tk.StringVar()

label = tk.Label(root, text="Do you have a fever?", bg='white', fg='black')
label.place(relx=0.5, rely=0.2, anchor='center')

yes_button1 = tk.Radiobutton(root, text="Yes", variable=question1, value='yes')
no_button1 = tk.Radiobutton(root, text="No", variable=question1, value='no')
yes_button1.place(relx=0.3, rely=0.3, anchor='center')  
no_button1.place(relx=0.7, rely=0.3, anchor='center')

# Add other questions similarly 

def calculate_score():
    global score
    score = 0
    if question1.get() == 'yes':
        score += 10
    if question2.get() == 'yes':
        score += 10
    if question3.get() == 'yes':
        score += 10 
    if question4.get() == 'yes':
        score += 10
    if question5.get() == 'yes':
        score += 10

    if score <= 10:
        messagebox.showinfo('Result', 'You do not need to visit a doctor.')
    elif score > 10 and score <= 30:   
        messagebox.showinfo('Result', 'You might perhaps have to visit a doctor.')
    else:
        messagebox.showinfo('Result', 'I strongly advise you to visit a doctor.')

submit_button = tk.Button(root, text='Submit', command=calculate_score)  
submit_button.place(relx=0.5, rely=0.4)

root.mainloop()