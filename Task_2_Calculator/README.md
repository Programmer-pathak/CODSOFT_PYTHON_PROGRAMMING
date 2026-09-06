# 🧮 Simple Calculator

## 📌 Project Overview

This is a command-line **Simple Calculator** developed using Python as part of the **CodSoft Python Programming Internship**.

The program allows users to perform basic arithmetic calculations using a simple terminal-based interface.

---

## 🎯 Objective

The objective of this project is to build a basic calculator using Python and practice fundamental programming concepts such as user input, conditional statements, `match-case`, loops, exception handling, and arithmetic operations.

---

## ✨ Features

The calculator supports:

* ➕ Addition
* ➖ Subtraction
* ✖️ Multiplication
* ➗ Division
* ⚠️ Division-by-zero handling
* 🔢 Invalid numeric input handling
* 🔄 Multiple calculations without restarting the program
* 🚪 Safe program exit

---

## ⚙️ How It Works

The program asks the user to:

1. Enter the first number.
2. Enter the second number.
3. Select an arithmetic operation.
4. View the calculated result.
5. Choose whether to perform another calculation.

Supported operations:

```text
+
-
*
/
```

The calculator continues running until the user chooses to stop.

---

## 🧠 Python Concepts Used

This project demonstrates the use of:

* Variables
* `float()` Conversion
* User Input
* Arithmetic Operators
* `while` Loop
* `match-case`
* Conditional Statements
* `try-except`
* Error Handling
* f-Strings
* String Methods

---

## 🛠️ Technologies Used

* Python 3.10+
* VS Code

---

## 📁 Project Structure

```text
Task_2_Calculator/
│
├── calculator.py
└── README.md
```

---

## ▶️ How to Run

### 1. Download or clone the repository

Open the calculator project folder on your computer.

### 2. Check Python version

Make sure Python 3.10 or later is installed:

```bash
python --version
```

### 3. Run the program

Open a terminal inside the project folder and execute:

```bash
python calculator.py
```

---

## 📌 Example

```text
--- SIMPLE CALCULATOR ---

Enter first number: 20
Enter second number: 5
Choose operation (+, -, *, /): /

Result: 20.0 / 5.0 = 4.0

Do you want another calculation? (yes/no): no

Thank you for using the calculator!
```

---

## ⚠️ Error Handling

The program handles common input errors.

If the user enters invalid numeric data:

```text
Invalid input. Please enter valid numbers only.
```

If the user attempts to divide by zero:

```text
Error: Cannot divide by zero.
```

If an unsupported operator is entered:

```text
Invalid operation. Please choose +, -, * or /.
```

---

## 🚀 Future Improvements

Possible future enhancements include:

* Add percentage calculation
* Add power and square-root operations
* Add calculation history
* Create a graphical user interface
* Add scientific calculator functions

---

## 👨‍💻 Author

**Ashish Kumar**

GitHub: [Programmer-pathak](https://github.com/Programmer-pathak)

---

## 📚 Internship

**Python Programming Internship — CodSoft**

This project was developed as part of the Python Programming Internship tasks assigned by CodSoft.
