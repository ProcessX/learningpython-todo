from command import Command

class Interface:
    'Base for the user interface'

    commands = []
    running = False

    def __init__(self):
        Interface.commands.append(Command('cmd', self.displayCmd, 'Display command list'))
        Interface.commands.append(Command('q', self.quit, 'Quit'))
        self.run()


    def runCmd(self, input):
        # Run the command if it exists, otherwise call for an error message.
        # @param input : command's shortcut
        for cmd in Interface.commands:
            if(cmd.shortcut == input):
                cmd.effect()
                return
        print('ERROR : Cmd not found')

    
    def displayCmd(self):
        #Display a list of every command available at the time.
        cmdList = ''
        for cmd in Interface.commands:
            cmdList += f'{cmd.shortcut}: {cmd.description}, '
        cmdList = cmdList.rstrip(', ')
        print(cmdList)

    
    def displayInterface(self):
        #Display every part of the interface needed at the time
        print('Display Interface')

    
    def quit(self):
        Interface.running = False


    def run(self):
        Interface.running = True
        while(Interface.running):
            userInput = input('Votre action? ')
            self.runCmd(userInput)

            

    
todoProgram = Interface()