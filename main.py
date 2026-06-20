from speech import listen

def save(text):
    with open("log.txt", "a") as f:
        f.write(text + "\n")

while True:
    text = listen()

    if text:
        print("Heard:", text)
        save(text)
    else:
        print("Try again")