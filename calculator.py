import tkinter as tk 
from tkinter import ttk
from tkinter import E, W, N, S


window = tk.Tk()

calc_keys =[
    {
        'text': '7',
        'command': lambda: insert_number_in_calc_result('7'),
    },
    {
        'text': '8',
        'command': lambda: insert_number_in_calc_result('8'),
    },
    {
        'text': '9',
        'command': lambda: insert_number_in_calc_result('9'),
    },
    {
        'text': '+',
        'command': lambda: insert_number_in_calc_result('+'),
    },
    {
        'text': '4',
        'command': lambda: insert_number_in_calc_result('4'),
    },
    {
        'text': '5',
        'command': lambda: insert_number_in_calc_result('5'),
    },
    {
        'text': '6',
        'command': lambda: insert_number_in_calc_result('6'),
    },
    {
        'text': '-',
        'command': lambda: insert_number_in_calc_result('-'),
    },
    {
        'text': '1',
        'command': lambda: insert_number_in_calc_result('1'),
    },
    {
        'text': '2',
        'command': lambda: insert_number_in_calc_result('2'),
    },
    {
        'text': '3',
        'command': lambda: insert_number_in_calc_result('3'),
    },
    {
        'text': '*',
        'command': lambda: insert_number_in_calc_result('*'),
    },
    {
        'text': '0',
        'command': lambda: insert_number_in_calc_result('0'),
    },
    {
        'text': '.',
        'command': lambda: insert_number_in_calc_result('.'),
    },
    {
        'text': 'C',
        'command': lambda: insert_number_in_calc_result('C'),
    },
    {
        'text': '=',
        'command': lambda: insert_number_in_calc_result('='),
    },
    
]
calc_result_lbl = tk.Label(
    window,
    text = '0',
    width =30,
    height = 3,
)

last_op_index = -1
last_dot_index = -1

def insert_number_in_calc_result(btn_text):
    current_result = calc_result_lbl ['text']
    
    global last_op_index, last_dot_index
    if btn_text in['+', '-', '*']:
        last_op_index = len(current_result)
      
        
    print(last_op_index, last_dot_index)     
    if btn_text == 'C':
        calc_result_lbl['text'] = '0'
        last_op_index, last_dot_index = 0, 0
    elif current_result == '0':
        calc_result_lbl ['text'] = btn_text
    elif btn_text == '=':
        result = str(eval(current_result))
        calc_result_lbl['text'] = result
        last_op_index, last_dot_index = 0, 0
        if '.' in result:
            last_dot_index = result.index('.')
        
    
    elif btn_text =='.' and not(last_dot_index > last_op_index or current_result[-1] == '.'):
            calc_result_lbl['text'] += btn_text
            last_dot_index = len(current_result)
    elif btn_text in['+', '-', '*'] and current_result[-1] in ['+', '-', '*']:
        calc_result_lbl ['text'] = current_result[:-1] + btn_text
    else:
        calc_result_lbl['text'] += btn_text


calc_keys_objs =[]
for calc_key_data in calc_keys:
    btn = tk.Button(
        master = window,
        text = calc_key_data['text'],
        command = calc_key_data['command'],
        height = 3,   
        
    )
    calc_keys_objs.append(btn)

for i, calc_key_obj in enumerate(calc_keys_objs):
    calc_key_obj.grid(row = (i//4) + 1, column = i % 4, sticky = 'nsew')



calc_result_lbl.grid(row = 0, column = 0, columnspan = 4)



window.mainloop()