import os

def push(msg):
    os.system("git add .")
    os.system(f'git commit -m "{msg}"')
    os.system("git push")

def status():
    os.system("git status")