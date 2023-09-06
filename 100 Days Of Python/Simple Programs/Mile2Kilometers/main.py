from tkinter import *

window = Tk()

window.title("Miles 2 Kilometers Converter")
window.config(padx=20,pady=20)

firstLabel = Label(text="is equal to")
firstLabel.grid(column=0, row=1)

kmLabel = Label(text="Km")
kmLabel.grid(column=2, row=1)

milesLabel = Label(text="Miles")
milesLabel.grid(row=0, column=2)

textBox = Entry()
textBox.grid(row=0, column=1)

numbyy = 0

converted = Label(text=numbyy)
converted.grid(row=1, column=1)


def buttCommand():
    converted.config(text=(float(textBox.get())*1.689))


button = Button(text="calculate", command=buttCommand)
button.grid(row=3,column=1)
window.mainloop()
