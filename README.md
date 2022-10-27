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
Through terminal (assuming you are in CS330SecurityLock directory)
```
cd dist
lock.exe
```
You can also open CS330SecurityLock/dist in a file management tool and run lock.exe manually.

Type into the textbox any characters you want.
The current state of the lock system is displayed after every next input.

Note: non-int inputs are ignored, but this mechanic is not explicitly displayed.
