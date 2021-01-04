from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=200)
window.config(padx=50, pady=50)

# Entry
input = Entry(width=10)
input.insert(END, string="0")
print(input.get())
input.grid(column=1, row=0)

# Label 1
miles_lable = Label(text="Miles", font=("Arial", 16))
miles_lable.grid(column=2, row=0)

# Label 2
is_equal_label = Label(text="is equal to", font=("Arial", 16))
is_equal_label.grid(column=0, row=1)

# Label 3
km_label = Label(text="0", font=("Arial", 16))
km_label.grid(column=1, row=1)

# Label 4
km_text_label = Label(text="Km", font=("Arial", 16))
km_text_label.grid(column=2, row=1)


# converter function
# def button_clicked():
#     print("button clicked!")
#     # my_label.config(text="Button got clicked")
#     user_input = input_text.get()
#     my_label.config(text=user_input)
def converter():
    miles_to_km = float(input.get()) * 1.6
    km_label.config(text=miles_to_km)

# calculate button
button = Button(text="Calculate", command=converter)
button.grid(column=1, row=2)

window.mainloop()
