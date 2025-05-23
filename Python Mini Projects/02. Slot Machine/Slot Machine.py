import random #need this for spinner results, will be used to pick a random key from the list 
import os
from time import sleep #because using wait() wasnt enough

##A simple spinner wheel

class Slot_Machine:
    def __init__(self):
        self.wheel1 = ['A', 'E', 'I', 'O', 'U', 'Y'] #The 3 list and their keys for the spinner wheel
        self.wheel2 = ['A', 'E', 'I', 'O', 'U', 'Y']
        self.wheel3 = ['A', 'E', 'I', 'O', 'U', 'Y']

    def spinwheel(self):  # SPIN THE WHEEL
        res1 = random.choice(self.wheel1)
        res2 = random.choice(self.wheel2)
        res3 = random.choice(self.wheel3)
        return (res1, res2, res3) #Passes the 3 results generated from inside through the spinwheel function, used later


    def playgame(self): #PLAY THE GAME
        print('''Welcome to the spinner wheel!!\n
Type "PLAY" to play!''')
        
        startgame = input("").strip().upper() #added this incase 'play' is typed in all lowercase
        if startgame == "PLAY":
            print("SPINNING...")
            sleep(2)
            spinresult = self.spinwheel() #naming the function from earlier and assigning it to a variable and then calling it for use
            print(spinresult[0], " | ", spinresult[1], " | ", spinresult[2]) #Prints your results (indexes from the returned results in return and prints them)
            if spinresult[0] == spinresult[1] == spinresult[2]: #checks to see if they're all the same returned result
                print("YOU WIN!!")
            else:
                print("Better luck next time!")
        else:
            print("Game not started.") ##dded 34-35 in case don't type 'play'

# USING the famous starter line (goes at bottom, this will start)
if __name__ == "__main__":
    slotmachine = Slot_Machine()
    slotmachine.playgame()
