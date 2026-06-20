import os

def push():
    os.system("git add .")
    os.system('git commit -m "Leo update"')
    os.system("git push")

def status():
    os.system("git status")