import tkinter as tk

# --- functions ---

def numInser(value):

    # inform function to use external/global variable
    global pin

    if value == 'Del':
        # remove last number from `pin`
        pin = pin[:-1]
        # remove all from `entry` and put new `pin`
        e.delete('0', 'end')
        e.insert('end', pin)

    else:
        # add number to pin
        pin += value
        # add number to `entry`
        e.insert('end', value)

    print("Current:", pin)

# --- main ---

keys = [
    ['1', '2', '3'],    
    ['4', '5', '6'],    
    ['7', '8', '9'],    
    ['Del', '9', '#'],    
]

# create global variable for pin
pin = '' # empty string

root = tk.Tk()

# place to display pin
e = tk.Entry(root)
e.grid(row=0, column=0, columnspan=3, ipady=5)

# create buttons using `keys`
for y, row in enumerate(keys, 4):
    for x, key in enumerate(row):
        # `lambda` inside `for` has to use `val=key:numInser(val)` 
        # instead of direct `numInser(key)`
        b = tk.Button(root, text=key, command=lambda val=key:numInser(val))
        b.grid(row=y, column=x, ipadx=10, ipady=10)

root.mainloop()