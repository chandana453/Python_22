from tkinter import *

def clicked():
    miles = float(input.get())
    km = miles *1.609
    output.config(text=km)



window = Tk()
window.title("my first GUI program")
window.minsize(width=500, height=500)
window.config(padx=20,pady=20 )

equal_label = Label(text="is equal to")
equal_label.grid(column=0,row=1)

input = Entry()
input.grid(column=1,row=0)

miles_label=Label(text="MILES")
miles_label.grid(column=2,row=0)

km_label = Label(text="KMS")
km_label.grid(column=2,row=1)

output = Label(text="0")
output.grid(column=1,row=1)

button = Button(text="calculate", command=clicked)
button.grid(column=1,row=3)






window.mainloop()