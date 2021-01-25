from command import Command

class Interface:
    'Base for the user interface'

    cmd = []
    running = False

    def __init__(self):
        self.cmd = {'cmd': self.displayCmd}
        self.run()


    def runCmd(self, input):
        # Run the command if it exists, otherwise call for an error message.
        # @param input : command's shortcut
        cmdFunction = self.cmd.get(input, False)
        if(cmdFunction == False):
            print('Cmd not found')
        else:
            cmdFunction()

    
    def displayCmd(self):
        #Display a list of every command available at the time.
        print(self.cmd)
        cmdList = ''
        for cmd in self.cmd.items():
            cmdList += f'{cmd[0]}: {cmd[1]}, '
        print(cmdList)

    
    def displayInterface(self):
        #Display every part of the interface needed at the time
        print('Display Interface')

    
    def quit(self):
        self.running = False


    def run(self):
        self.running = True
        while(self.running):
            userInput = input('Votre action? ')
            self.runCmd(userInput)

            

    
todoProgram = Interface()