from tkinter import *

root = Tk()
root.title("Grade Calculator")
root.geometry("400x400")

def Calculation():
    english = int(englishentry.get())
    analytical = int(analyticalentry.get())
    gk = int(gkentry.get())
    
    total = english + analytical + gk
    average = total / 3
    
    total_label.config(text=f"Total: {total}")
    avg_label.config(text=f"Average: {average:.2f}")
    
    if average > 50:
        grade = "PASS"
    else:
        grade = "FAIL"
        
    grade_label.config(text=f"Grade: {grade}", fg="blue")

# Labels for subjects
Label(root, text="English:", font="arial 10").place(x=50, y=20)
Label(root, text="Analytical skill:", font="arial 10").place(x=50, y=70)
Label(root, text="GK:", font="arial 10").place(x=50, y=120)

# Entries for subjects
englishvalue = StringVar()
analyticalvalue = StringVar()
gkvalue = StringVar()

englishentry = Entry(root, textvariable=englishvalue, font="arial 15", width=15)
analyticalentry = Entry(root, textvariable=analyticalvalue, font="arial 15", width=15)
gkentry = Entry(root, textvariable=gkvalue, font="arial 15", width=15)

englishentry.place(x=200, y=20)
analyticalentry.place(x=200, y=70)
gkentry.place(x=200, y=120)

# Labels to display results
total_label = Label(root, text="Total:", font="arial 10")
avg_label = Label(root, text="Average:", font="arial 10")
grade_label = Label(root, text="Grade:", font="arial 10")

total_label.place(x=50, y=170)
avg_label.place(x=50, y=210)
grade_label.place(x=50, y=250)

# Buttons for calculation and exit
Button(root, text="Calculate", font="arial 15", bg="white", bd=10, width=8, command=Calculation).place(x=50, y=300)
Button(root, text="Exit", font="arial 15", bg="white", bd=10, width=8, command=root.quit).place(x=200, y=300)

root.mainloop()