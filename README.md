# CS330SecurityLock
CS 330 program assignment that simulates a lock security system.

# Set Up Process
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

###### Estimated runtime for breaking passcode
Assumptions:
 - Uniform Distribution of digits for RNG
 - 1 sec for each new digit tested
The unlocking passcode 807711 is a 6 digit number. Since the checking system ultimately checks the last 6 digits for this combination, it is roughly 1/1000000 chance to get the right combination or 6 digit number. If you assume the worst case the breaking runtime would be 1000000 seconds ~= 277 hours ~= 11 days.

If we assume average luck to be 50% of worst case runtime, 500000 seconds ~= 138 hours ~= 5 days.

###### Use terminal for actual test
Using python's random number generator for algorythm

Firstly close the GUI if you have it open.
In the terminal go to the CS330SecurityLock directory.
Then run the following:
```
python tester.py
```
Follow the prompts as it asks for how many tests to run and such.
The output is the average input count for all the tests simulated and a list of all the input string generated from each test seperately, although they dont fit on a terminal (maybe if you're lucky you can rng one that does).