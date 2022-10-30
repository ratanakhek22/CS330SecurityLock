# CS330SecurityLock
CS 330 program assignment that simulates a lock security system.  
Entering the sequence 807711 unlocks the system while entering 807714 locks it.  
The executable opens a GUI for this system and a command line can be used to run tests through a terminal.

Project: CS 330 Program Assignment  
Name: Sovannratana Khek

# Set Up Process
Language: python3 (I ran it on version 3.10.6 to be specific)  
OS: bieng Windows 11  
Testing: done through terminal, output of tests are in terminal

1. clone from GitHub to some directory

for example using git bash (assuming you're in your desired folder)
```
git clone https://github.com/ratanakhek22/CS330SecurityLock.git
```
2. in that directory run the follow in a terminal
```
cd CS330SecurityLock
pip install pyinstaller
pyinstaller --onefile lock.py
```
Note: can skip cd CS330SecurityLock if you are already in the directory

# How to use
### Get executable
Through terminal (assuming you are in CS330SecurityLock directory)
```
cd dist
lock.exe
```
You can also open CS330SecurityLock/dist in a file management tool and run lock.exe manually.

### Part 1: Security Device
Type into the textbox any characters you want.
The current state of the lock system is displayed after every new input.

Note: non-int inputs are ignored, but this mechanic is not explicitly displayed.

### Part 2: Intruder Simulation tests
Note: Part 2 has no GUI elements and will be run in terminal because it is counterintuitive for your security device to have a button that breaks your system.

#### Estimated runtime for breaking passcode
Assumptions:
 - Uniform Distribution of digits for RNG
 - 1 sec for each new digit tested
The unlocking passcode 807711 is a 6 digit number. Since the checking system ultimately checks the last 6 digits for this combination, it is roughly 1/1000000 chance to get the right combination or 6 digit number. If you assume the worst case the breaking runtime would be 1000000 seconds ~= 277 hours ~= 11 days.

If we assume average luck to be 50% of worst case runtime, 500000 seconds ~= 138 hours ~= 5 days.

#### Use terminal for actual test
Using python's default random number generator for tests.

Firstly close the GUI if you have it open.
In the terminal go to the CS330SecurityLock directory.
Then run the following:
```
python tester.py
```
Follow the prompts as it asks for how many tests to run and such.
The output is the average input count for all the tests simulated.

### Memo/Summary
#### Development process
Firstly, I decided I'd use python for the assignment because it is able to create a simple GUI and it is easily executable even without making the .exe file that I had in the set up process. This left me with 2 tasks, find how to make a GUI with python (I knew it was possible just didn't learn it yet) and make a python file into an executable (assumed it was possible because python is already a script). I ended up learning how to use tkinter which is built into python for GUI creation and found a library to make a .exe (if I didn't I'd have left it to run as a script). After making a simple GUI, I started thinking about the checking algorithm. Luckily, the state machine was straight forward in that one digit/input is either correct or not. Thus I implemented the state machine using an array of every digit with some pointer that would follow the state machine diagram I attached. For the testing algorithm I used the Password class I created and its functions aongside a RNG to just run checks until the lock unlocked.

#### Findings
My estimating was way off, I underestimated randomness (probably would have helped if I remembered things from AP Stats). I originally ran a 10,000 iteration test, but my laptop fans went up to 5000+ rpm only happens on the heavy games I play. Thus I tested changed the test amount and found 70 iterations to be not as frightening (results are attached).

#### Finite Automata
The program takes in a string of digits and changes from locked to unlocked while running thus it doesn't really have an "accepted input". If we work on the assumption that an accepted ending is one where the program ends in an unlocked state, then the accepted input string x ends in 80771 (unlocks system) with any combination of digits afterword that aren't 807714 (locks system).

let the set A = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 }  
let the set B = { all x's where x an infinite sequences of A } = a set of strings made up of elements in A of any length \[0, infinity)  
let the set C = { all x's where x is in B and doesn't have '80774' in it } = a set of strings from set B that don't have the combination '80774' in them  
If y is a string accepted by the FA, then it is a language of the FA and y = a + '80771' +  b where a is some element in A and b is some element in B.
