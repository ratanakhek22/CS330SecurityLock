import tkinter as tk

class Password:
    code = []
    index = 0
    unlocked = False
    
    def __init__(self, code):
        # code is an array of each digit in your password
        self.code = code
        
    def check_digit(self, digit):
        if self.index == len(self.code):
            if digit == 1:
                self.unlocked = True
            elif digit == 4:
                self.unlocked = False
            self.index = 0
        elif self.code[self.index] == digit:
            self.index = self.index + 1
        else:
            self.index = 0
            
    def get_lock_state(self):
        return self.unlocked
    
def update_label():
    result_label.config(text='Lock State: ' + ('Unlocked' if password.get_lock_state() else 'Locked'), font=('Arial', 18))

root = tk.Tk()
root.geometry('350x250')
root.title('Lock Security')

password = Password(code=[8,0,7,7,1]) # 80771 is the 5 least sig digits in my ID

def callback(user_entry):
    new_digit = user_entry.get()[len(user_entry.get())-1::] # last char at the end of user_entry
    if new_digit.isdigit():
        password.check_digit(int(new_digit))
        update_label()

user_entry = tk.StringVar()
user_entry.trace('w', lambda name, index, mode, user_entry=user_entry: callback(user_entry))

title_label = tk.Label(root, text='Lock Security', font=('Arial', 18))
title_label.pack(padx=10, pady=15)

input_entry = tk.Entry(root, font=('Arial', 18), textvariable=user_entry)
input_entry.pack(padx = 10, pady=0)

result_label = tk.Label(root, text='Lock State: Locked', font=('Arial', 18))
result_label.pack(padx=10, pady=15)

root.mainloop()