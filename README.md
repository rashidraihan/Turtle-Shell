<h1 align="center">🐢 Turtle Shell</h1>
<p align="center">
  <img src="https://img.shields.io/badge/language-python-blue?logo=python&logoColor=white&style=for-the-badge" alt="Python">
</p>

---

<p align="center">
  A lightweight, Python-based shell that brings Unix-style commands and system-level control to your fingertips.
</p>

---

## 📌 Features

Turtle Shell offers a clean set of commands that mirror familiar Unix operations, built using Python's system-level capabilities like `os.fork()` and `os.execvp()`.

| Command           | Description                          | Unix Equivalent     |
|-------------------|--------------------------------------|---------------------|
| `map`             | Show current working directory        | `pwd`               |
| `inventory`       | List all files in current directory   | `ls`                |
| `today`           | Display current date                  | `date`              |
| `go <dir>`        | Change directory                      | `cd <dir>`          |
| `back`            | Move to parent directory              | `cd ..`             |
| `make <dir>`      | Create a new directory                | `mkdir <dir>`       |
| `feel <file>`     | Create or append text to a file       | `touch` + input     |
| `ink <msg>`       | Print message to console              | `echo <msg>`        |
| `sweep`           | Clear the terminal screen             | `clear` / `cls`     |
| `record`          | View command history                  | `history`           |
| `vanish <file>`   | Delete a file                         | `rm <file>`         |
| `quit`            | Exit the Turtle Shell                 | `exit`              |

> ℹ️ Any unknown command is attempted via system call using `fork()` and `execvp()`.

---

## ⚙️ Requirements

- **Python 3.6+**
- Works best on **Unix/Linux**
- On **Windows**, some system-level operations (like `fork()`) may not function as expected.

---

## 🚀 How to Run

1. **Clone the Repository**
   ```bash
   git clone https://github.com/rashidraihan/turtle-shell.git 
   cd turtle-shell

2. Run the Shell
   ```bash
   python turtle_shell.py
3. Start Using Commands
   ```ruby
   >> inventory
   >> make my_folder
   >> go my_folder
   >> feel notes.txt
   >> quit
   
 🎨 Optional: Enable Colorized Greeting
 To activate a colorful welcome message when the shell starts:
 
 1. Install the library:
    ```bash
    pip install colorama
    
2. ✅ **Uncomment the following lines** in `turtle_shell.py`:
   - **Lines 6–8**:
     ```python
     import colorama
     from colorama import Fore, Back, Style
     colorama.init(autoreset=True)
     ```
   - **Lines 165–168** (Colorized `printGreeting()`):
     ```python
     def printGreeting():
         print(Fore.CYAN + "Welcome to Turtle Shell")
         print(Fore.GREEN + "Say Cheese")
         print(Style.RESET_ALL)
     ```

3. 🛑 **Comment out the non-colorized greeting**:
   - **Lines 160–162**:
     ```python
     # def printGreeting():
     #     print("Welcome to Turtle Shell")
     #     print("Say Cheese")
     ```

Once this is done, you'll see a vibrant greeting each time Turtle Shell starts!

## ❗ Important Notes

Turtle Shell is designed as a **learning tool** to explore Python’s interaction with the operating system.

- ⚠️ Do **not** use it as a full system shell replacement.
- 🚫 Currently, it does **not** support piping (`|`) or redirection (`>`).

---

## 🤝 Contributing

Pull requests are welcome!

For major changes, please open an issue first to discuss what you'd like to propose or improve.

Let's build and learn together. 🐢

