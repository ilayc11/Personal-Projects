import tkinter

window = tkinter.Tk()

window.title("Miles 2 Kilometers")
window.minsize(width=500,height=300)

my_label=tkinter.Label(text="My Label",font=("Ariel",24,"bold"))
my_label.pack(side="left",expand=True)



window.mainloop()
