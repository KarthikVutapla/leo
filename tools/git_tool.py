import os

def git_push(message):
    os.system("git add .")
    os.system(f'git commit -m "{message}"')
    os.system("git push")
    return "pushed to github"

def git_status():
    os.system("git status")
    return "status shown"