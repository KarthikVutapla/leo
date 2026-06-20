# LEO

LEO is a personal voice-based system designed to capture, structure, and organize everything I do on a daily basis. It converts spoken input into logs, tasks, and updates, helping me maintain a clear record of my work across coding, learning, fitness, and projects.

---

# 🟢 CATEGORY CREATION COMMANDS

## 🎙️ Create a Category
Say anything like:
- “create category”
- “make a category”
- “I want a category”
- “help me create a category”

### What happens:
LEO asks for a category name and creates a folder for it.

---

## 🎙️ Add Items to Category
After category is created, speak items one by one:
- “python”
- “cs50”
- “github”

### Stop commands:
- “that’s all”
- “stop leo”
- “shutdown”

### What happens:
Each spoken item is saved under that category.

---

# 🟡 GENERAL LOGGING

## 🎙️ Log any activity
Just speak normally:
- “I studied CS50 week 1”
- “I went to gym”
- “week 1 week 2 week 3”

### What happens:
LEO stores everything in a structured daily log file automatically.

---

# 🔵 GITHUB COMMANDS

## 🎙️ Push to GitHub
Say:
- “push this”
- “sync repo”
- “commit this”
- “save to github”

### What happens:
LEO runs:
- git add .
- git commit
- git push

---

## 🎙️ Check repository status
Say:
- “check status”
- “git status”
- “what changed”

### What happens:
LEO runs:
- git status (shows current repository state)

---

# 🔴 EXIT COMMANDS

Say:
- “bye leo”
- “shutdown”
- “stop leo”

### What happens:
LEO safely exits the program.

---

# 🧠 HOW LEO THINKS

- Understands natural speech (not strict commands)
- Detects intent (category / logging / git / exit)
- Automatically stores data locally
- Can sync with GitHub when requested

---

# ⚠️ NOTES

- Speak clearly for best recognition
- Internet required for speech-to-text
- GitHub must be authenticated before push works

## Features (upcoming)

- [ ]  Voice input to text logging 
- [ ] Daily activity tracking  
- [ ] Local storage of updates 
- [ ] Basic GitHub sync support (manual commit flow)

---

## What LEO is becoming

- Automatic task categorization (coding, fitness, learning, etc.)  
- Structured daily README generation  
- Voice-controlled GitHub operations (commit, push, repo updates)  
- Personal memory system for past activity retrieval  
- Expansion into a full personal productivity and development OS  

---

## Goal

To evolve into a lightweight personal operating system that connects voice, code, and GitHub into one continuous system for tracking and improving my work and learning over time.