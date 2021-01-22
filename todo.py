from os import system, name
from task import Task

def clearConsole():
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')


def stringToInt(x):
    try:
        x = int(x)
        return x
    except ValueError:
        return 'Error'
        

class Todo:

    tasks = []

    def __init__(self) -> None:
        pass


    def addTask(self):
        self.updateInterface()

        newTask = input('Add task: ')
        if(newTask != 'c'):
            Todo.tasks.append(Task(newTask))
            self.updateInterface()
        else:
            self.updateInterface()
            return


    def removeTask(self):
        self.updateInterface()

        if(len(Todo.tasks) < 1):
            print("TODO EMPTY - NOTHING TO REMOVE")
            return

        while(True):
            taskToRemove = input("Remove task: ")
            if(taskToRemove == 'c'):
                return

            taskToRemove = stringToInt(taskToRemove) - 1
            if(isinstance(taskToRemove, int) and taskToRemove < len(Todo.tasks)):
                del Todo.tasks[taskToRemove]
                self.updateInterface()
                return
            else:
                print("ERROR: TASK DOESN'T EXIST")

    
    def checkTask(self):
        self.updateInterface()

        if(len(Todo.tasks) < 1):
            print("TODO EMPTY - NO TASK TO CHECK")
            return

        while(True):
            taskToCheck = input("Check task nbr: ")
            if(taskToCheck == 'c'):
                return

            taskToCheck = stringToInt(taskToCheck)
            if(isinstance(taskToCheck, int) and taskToCheck <= len(Todo.tasks)):
                Todo.tasks[taskToCheck - 1].check()
                self.updateInterface()
                return
            else:
                self.updateInterface()
                print("ERROR: TASK DOESN'T EXIST")


    def showTodo(self):
        if(len(Todo.tasks) == 0):
            print('TODO EMPTY\n')
            return
        
        print('YOUR TODO:\n')
        for i in range(len(Todo.tasks)):
            task = f"[{i + 1}] {Todo.tasks[i].title}"
            if(Todo.tasks[i].done):
                task += ' - DONE'
            print(task)
        print('\n')

    
    def updateInterface(self):
        clearConsole()
        self.showTodo()

    
    def showCmd(self):
        self.updateInterface()
        print('COMMANDS\na: add task | r: remove task | c: check/uncheck task | q: quit program')


    def run(self):
        self.updateInterface()

        while(True):
            #print('\nCOMMANDS\na: add task | r: remove task | c: check/uncheck task | q: quit program\n')
            userImput = input('Your action? ')
            if(userImput == 'q'):
                break
            elif(userImput == 'a'):
                self.addTask()
            elif(userImput == 'r'):
                self.removeTask()
            elif(userImput == 'c'):
                self.checkTask()
            elif(userImput == 'cmd'):
                self.showCmd()
            else:
                self.updateInterface()
                print('ERROR: COMMAND INVALID')


myTodo = Todo()
myTodo.run()