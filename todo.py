from task import Task
        

class Todo:
    'List of tasks to do'

    tasks = []
    url = ''
    separator = '###'


    def __init__(self):
        self.setFile()
        self.run()
        pass


    def setFile(self):
        Todo.url = os.getcwd()
        file = None
        if(not os.path.isfile(Todo.url + '/todo.txt')):
            file = open('todo.txt', 'x')
            file.closed
        else:
            self.setTodo()
    

    def setTodo(self):
        file = open('todo.txt', 'r')
        todo = file.readlines()
        for task in todo:
            taskInfo = task.replace('\n', '').split('###')
            print(taskInfo)
            newTask = Task(taskInfo[0])
            newTask.done = True if taskInfo[1] == 'True' else False
            Todo.tasks.append(newTask)
        file.close()


    def save(self):
        file = open('todo.txt', 'w')
        for task in Todo.tasks:
            file.write(task.title + '###' + str(task.done) + '\n')


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
            userImput = input('Your action? ')
            if(userImput == 'q'):
                self.save()
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