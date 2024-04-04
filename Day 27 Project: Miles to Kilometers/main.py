from tkinter import *


# Calculate function.
def calculate():
    output.config(text=float(entry.get()) * 1.609)


# Window setup.
window = Tk()
window.title("Miles to Kilometers")
window.minsize(width=70, height=70)
window.config(padx=20, pady=20)

# Input entry.
entry = Entry(width=5)
entry.grid(column=1, row=0)

# "Miles" label.
miles = Label(text="Miles")
miles.grid(column=2, row=0)

# "Is equal to" label.
is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

# Output label.
output = Label(text="0")
output.grid(column=1, row=1)

# "Km" label.
kilometers = Label(text="Km")
kilometers.grid(column=2, row=1)

# Calculate button.
calculate = Button(text="Calculate", command=calculate)
calculate.grid(column=1, row=2)

window.mainloop()
