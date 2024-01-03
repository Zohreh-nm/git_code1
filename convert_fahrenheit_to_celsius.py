import tkinter as tk 
from tkinter import ttk
window = tk.Tk()

fahrenheit_val = tk.StringVar()

show_result_lbl = tk.Label(
    window,
    text = 'result will be shown here!'
)

def convert_fahrenheit_celsius(*args):
    
    fahrenheit_degree = fahrenheit_val.get()
    try:
        fahrenheit_value = float(fahrenheit_degree)
        show_result_lbl['text'] = (fahrenheit_value -32)*5/9
    except ValueError:
        if fahrenheit_degree != '':
            show_result_lbl['text'] = 'You should enter a number!'
        else:
            show_result_lbl['text'] = 'Your input is empty!'
            
window.bind('<Return>', convert_fahrenheit_celsius)
            
    

fahrenheit_lbl = tk.Label(
    window,
    text ='Fahrenheit:'
)

fahrenheit_entry = ttk.Entry(
    window,
    width = 50,
    textvariable = fahrenheit_val,
)

celsius_lbl = tk.Label(
    window,
    text = 'Celsius:',
)

calc_button = ttk.Button(
    window,
    text = 'Calc',
    command = convert_fahrenheit_celsius,
)


fahrenheit_lbl.grid(row = 0, column = 0, padx = 10, pady = 10)
fahrenheit_entry.grid(row = 0, column = 1)
celsius_lbl.grid(row =1, column = 0, padx = 10, pady = 10)
show_result_lbl.grid(row = 1, column = 1, padx = 10, pady = 10)
calc_button.grid(row = 0, column = 2, padx = 10, pady = 10)



window.mainloop()