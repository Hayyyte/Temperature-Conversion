import tkinter as tk
from tkinter import ttk

def convert():
    temperature = entryInt.get()
    if is_celsius.get():
        converted_temp = (temperature * 9/5) + 32  
        output_label.config(text=f"Output: {temperature}°C = {converted_temp:.2f}°F")
    else:
        converted_temp = (temperature - 32) * 5/9  
        output_label.config(text=f"Output: {temperature}°F = {converted_temp:.2f}°C")

def toggle_unit():
    is_celsius.set(not is_celsius.get())
    if is_celsius.get():
        unit_label.config(text="Unit: Celsius")
    else:
        unit_label.config(text="Unit: Fahrenheit")

window = tk.Tk()
window.title("Temperature Converter")
window.geometry("300x200")

title_label = ttk.Label(window, text="Temperature Converter", font=("Arial", 20))
title_label.pack(pady=10)

input_frame = ttk.Frame(window)
entryInt = tk.DoubleVar()
entry = ttk.Entry(input_frame, textvariable=entryInt)
button = ttk.Button(input_frame, text="Convert", command=convert)
entry.pack(side="left")
button.pack(side="left")
input_frame.pack(pady=10)

toggle_button = ttk.Button(window, text="Toggle Unit", command=toggle_unit)
toggle_button.pack(pady=5)

unit_label = ttk.Label(window, text="Unit: Celsius")
unit_label.pack()

output_label = ttk.Label(window, text="")
output_label.pack()

is_celsius = tk.BooleanVar(value=True)  

window.mainloop()
