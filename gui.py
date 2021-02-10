import tkinter as tk
from quote import generate_quote

# create the gui and set the title
window = tk.Tk()
window.title('Quote Generator')

# get a initial quote and set it to the
quote = generate_quote()


# when the button is clicked, update the quote that is displayed
def update_quote():
    new_quote = generate_quote()
    label.config(text=new_quote)


# create the button and the label
btn = tk.Button(window, text='Quote', command=update_quote)
label = tk.Label(
    text=quote,
    fg="white",
    bg="black"
)

# set the window geometry
window.geometry('1100x100+10+10')

# pack the button and the label
label.pack()
btn.pack()


window.mainloop()
