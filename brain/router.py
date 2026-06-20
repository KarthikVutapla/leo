import json
from tools.git_tool import git_push, git_status
from tools.readme_tool import update_readme

def execute(response):

    try:
        data = json.loads(response)
    except:
        return response

    action = data.get("action")

    if action == "git_push":
        return git_push(data.get("message", "LEO update"))

    if action == "git_status":
        return git_status()

    if action == "readme":
        return update_readme(data.get("content", ""))

    return "done"