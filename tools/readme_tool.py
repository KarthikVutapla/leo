def update_readme(content):
    with open("README.md", "a") as f:
        f.write("\n" + content + "\n")
    return "README updated"