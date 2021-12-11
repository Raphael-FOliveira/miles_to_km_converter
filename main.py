import tkinter as tk


def miles_to_km():
    miles = float(user_input.get())
    result_km = round(miles * 1.60934, 2)
    result.config(text=f"{result_km}")


screen = tk.Tk()
screen.minsize()
screen.title("M to Km converter")
screen.config(padx=30, pady=30)

user_input = tk.Entry(width=7)
user_input.grid(row=0, column=1)

label = tk.Label(text="Miles")
label.grid(row=0, column=2)

is_equal = tk.Label(text="is equal to")
is_equal.grid(row=1, column=0)

result = tk.Label(text="0")
result.grid(row=1, column=1)

km_label = tk.Label(text="Km")
km_label.grid(row=1, column=2)

button = tk.Button(text="Convert!", command=miles_to_km)
button.grid(row=2, column=1)

screen.mainloop()
