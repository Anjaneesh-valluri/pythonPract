import random
from pathlib import Path
from googlesearch import search

for result in search("your search query", num_results=10):
    print(result)

callings = ["Sir","Sire","Master", "Boss"]
commands = ["wakeup", "start", "begin"]


def response(command):
    command = command.lower()
    words = command.split(" ")
    out = ""
    files = []
    for word in words:
        if word in commands:
            out = f"> Hello {random.choice(callings)}, Welcome back. Starting the process >>>\n What are we working on today? "
            print(out)
            searching(command)
            break
        else:
            out = "> Sorry command not found"
    print(out)
    print(files)

def searching(command):
    for result in search(command,num_results=10):
        print(result)

def printing():
    path = Path("C:/Users/SA2313/OneDrive - Hitachi Energy/Documents/LEARNINGS/django_prac/BuyIt")
    files = ""
    for file in path.glob('*.py'):
        print(file)
        files+=str(file)
    return files