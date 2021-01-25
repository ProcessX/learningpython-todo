import os
from todo import Todo
from command import Command


def stringToInt(x):
    # Convert string to int, return Error if ValueError
    try:
        x = int(x)
        return x
    except ValueError:
        return 'Error'


class Interface:
    'Base for the user interface'

    commands = []
    running = False
    todo = Todo()
    

    def __init__(self):
        Interface.commands.append(Command('cmd', self.displayCmd, 'Display command list'))
        Interface.commands.append(Command('q', self.quit, 'Quit'))

    
    def clearConsole(self):
        # Clear the console, depending on the OS
        if os.name == 'nt': 
            _ = os.system('cls') 
    
        else: 
            _ = os.system('clear')


    def runCmd(self, input):
        # Run the command if it exists, otherwise call for an error message.
        # @param input : command's shortcut
        for cmd in Interface.commands:
            if(cmd.shortcut == input):
                cmd.effect()
                return
        print('ERROR : Cmd not found')

    
    def displayCmd(self):
        # Display a list of every command available at the time.
        cmdList = ''
        for cmd in Interface.commands:
            cmdList += f'{cmd.shortcut}: {cmd.description}, '
        cmdList = cmdList.rstrip(', ')
        print(cmdList)

    
    def displayInterface(self):
        # Display every part of the interface needed at the time
        print('Display Interface')

    
    def quit(self):
        quitting = False
        while(not quitting):
            userInput = input('Are you sure you want to quit (y/n)? ')
            if(userInput == 'y'):
                Interface.running = False
                quitting = True
            elif(userInput == 'n'):
                return
            else:
                print('ERROR: cmd not found')
        return

    
    def save(self):
        # Save the todo list as a .txt file. If it doesn't exist, the function will create a new file.
        return
    

    def load(self):
        # Load the todo list from a .txt file, if it exists
        return


    def run(self):
        Interface.running = True
        while(Interface.running):
            userInput = input('Your action? ')
            self.runCmd(userInput)

            

    
todoProgram = Interface()
todoProgram.run()