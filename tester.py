import random

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

def simulate_break():
    password = Password(code=[8,0,7,7,1])
    simulated_input = ''
    simulated_input_cnt = 0

    while(True):
        new_input = random.randint(0,9)
        simulated_input = simulated_input + str(new_input)
        simulated_input_cnt += 1
        password.check_digit(new_input)
        if password.get_lock_state():
            break
    
    return [simulated_input_cnt, simulated_input]

def test(iters=10):
    if iters < 1:
        iters = 1
    results = []
    total = 0
    for i in range(iters):
        x = simulate_break()
        total += x[0]
        results.append(x[1])
        
    print(results)
    print('The above is the final string of inputs for all simulated breaks done')
    print('Average inputs needed: ' + str(total/iters))

while(True):
    print('How many iterations do you want to test?')
    user_in = input()
    if user_in.isdigit():
        test(int(user_in))
        print('Again? [y/n]')
        user_in = input()
        if user_in != 'y':
            break
    else:
        print("Input a number > 0")
print('TERMINATED')