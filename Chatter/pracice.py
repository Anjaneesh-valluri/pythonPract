import random
class Calling():
    command = ""
    def __init__(self, command):
        self.command = command
    def menu(self):
        comm = self.command.lower()
        out = ""
        tasks = Tasks()
        if comm == "display":
             tasks.displayAll()
        elif comm == "remove":
            out = (tasks.removeTask(input("Enter the name of the task you want to remove: ")))
        elif comm == "add":
            out = (tasks.addTask(input("Enter the name of the task you want to add: ")))
        elif comm == "quit":
            out = "Exiting the process ....\n"
        else:
            out = ("Sorry wrong input")

        return out
class Tasks():
    tasks = []
    def addTask(self, task):
        if task not in self.tasks:
            self.tasks.append(task)
            return "Task added successfully!"
        else:
            return "Task Already exists"
    def removeTask(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            return "Task deleted successfully!"
        else:
            return "Task is not present"
    def displayAll(self):
        if len(self.tasks)<1:
            print("Tasks are empty")
        else:
            print(self.tasks)


command = ""
callings = ["Hello", "Bonjor", "Konnichiwa" , "Namaskaram" , "Namaste"]
print(f"{random.choice(callings)} , Welcome to the tasks app ...\n ")
while command.lower() != "quit":
    command  = input("Enter a command you wish - Display all tasks, Add new task, Delete a task or quite : ")

    call = Calling(command)
    print(call.menu())
print("Thank you !")