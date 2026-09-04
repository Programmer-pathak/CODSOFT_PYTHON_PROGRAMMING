# 📝 To-Do List Application

## 📌 Project Overview

This is a command-line **To-Do List Application** developed using Python as part of the **CodSoft Python Programming Internship**.

The application allows users to manage their daily tasks directly from the terminal using a simple menu-driven interface.

---

## 🎯 Objective

The objective of this project is to build a simple task management application using Python and practice fundamental programming concepts such as lists, loops, conditional statements, user input, exception handling, and data manipulation.

---

## ✨ Features

The application provides the following operations:

* ➕ Add a new task
* 📋 View all tasks
* ✏️ Update an existing task
* 🗑️ Delete a task
* ✅ Validate empty task input
* ⚠️ Handle invalid task numbers
* 🔢 Handle non-numeric input
* 🚪 Exit the application safely

---

## ⚙️ How It Works

When the program starts, the user is presented with the following menu:

```text
--- TO-DO LIST MENU ---

1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Exit
```

The user selects an option from `1` to `5`, and the program performs the corresponding operation.

Tasks are stored in a Python list during program execution.

---

## 🧠 Python Concepts Used

This project demonstrates the use of:

* Python Lists
* `while` Loop
* `match-case`
* Conditional Statements
* User Input
* `enumerate()`
* List `append()`
* List `pop()`
* Exception Handling using `try-except`
* Input Validation
* String Formatting using f-strings

---

## 🛠️ Technologies Used

* Python 3.10+
* VS Code

---

## 📁 Project Structure

```text
Task_1_To_Do_List/
│
├── todo_list.py
└── README.md
```

---

## ▶️ How to Run

### 1. Download or clone the repository

Open the project folder on your computer.

### 2. Make sure Python 3.10 or later is installed

Check your Python version:

```bash
python --version
```

### 3. Run the application

Open a terminal inside the project folder and execute:

```bash
python todo_list.py
```

### 4. Use the menu

Enter a number between `1` and `5` to perform the required task operation.

---

## 📌 Example

```text
--- TO-DO LIST MENU ---

1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Exit

Enter your choice (1-5): 1
Enter your task: Complete Python assignment

Task 'Complete Python assignment' added successfully!
```

---

## ⚠️ Note

Tasks are stored temporarily in memory while the program is running.

When the program is closed, the tasks are not permanently saved because this basic version does not use a file or database for persistent storage.

---

## 🚀 Future Improvements

Possible future enhancements include:

* Save tasks permanently using a text or JSON file
* Add task completion status
* Add task priority
* Add due dates
* Build a graphical user interface (GUI)
* Connect the application to a database

---

## 👨‍💻 Author

**Ashish Kumar**

GitHub: [Programmer-pathak](https://github.com/Programmer-pathak)

---

## 📚 Internship

**Python Programming Internship — CodSoft**

This project was developed as part of the Python Programming Internship tasks assigned by CodSoft.
