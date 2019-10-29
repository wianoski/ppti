import serial 
import tkinter as tk
from tkinter import messagebox
import time

port = '/dev/ttyUSB0'
ard = serial.Serial(port, 57600, timeout=1)

root = tk.Tk()
root.title("Enroll Finger")
frame = tk.Frame(root)
frame.pack()

def enroll():
    inputs = 1
    ard.write(str(inputs).encode())

enrollBtn = tk.Button(frame, height=5, width=20,
                    text="Start", command=enroll)
enrollBtn.pack()

large_font = ('Verdana',25)
medium_font = ('Verdana',15)

txt = tk.Entry(frame,font=large_font,width=15)
inputStr = txt
txt.pack()

#--------------------------------------------------------------------
def numInser(value):

    # inform function to use external/global variable
    global pin

    if value == 'Del':
        # remove last number from `pin`
        pin = pin[:-1]
        # remove all from `entry` and put new `pin`
        txt.delete('0', 'end')
        txt.insert('end', pin)

    else:
        # add number to pin
        pin += value
        # add number to `entry`
        txt.insert('end', value)

    print("Current:", pin)

# --- main ---

keys = [
    ['1', '2', '3'],    
    ['4', '5', '6'],    
    ['7', '8', '9'],    
    ['0', 'Del'],    
]
# create global variable for pin
pin = '' # empty string

root = tk.Tk()
e = tk.Entry(root)
frame.grid(row=0, column=0, columnspan=3, ipady=5)
# create buttons using `keys`
for y, row in enumerate(keys, 5):
    for x, key in enumerate(row):
        # `lambda` inside `for` has to use `val=key:numInser(val)` 
        # instead of direct `numInser(key)`
        b = tk.Button(root, text=key, command=lambda val=key:numInser(val), width=10, font=medium_font)
        b.grid(row=y, column=x, ipadx=10, ipady=10)
#--------------------------------------------------------------------
def clicked():
    # tk.Tk()
    messagebox.showinfo('Finger system', 'Tekan OK, Lalu letakkan jari anda')
    res = txt.get()
    ard.write(str(res).encode())
    while True:
        msg = ard.readline().decode('ascii')
        print(msg)
        break
    time.sleep(10)
    

btn = tk.Button(frame, height=3, width=20,
                text="Enrollment", command=clicked)
btn.pack()
button = tk.Button(frame,height=5, width=20,  
                   text="QUIT", 
                   fg="red",
                   command=quit)
button.pack()
root.mainloop()