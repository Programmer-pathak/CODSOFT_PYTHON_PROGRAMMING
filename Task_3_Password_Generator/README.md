# 🔐 Password Generator

## 📌 Project Overview

This is a command-line **Password Generator** developed using Python as part of the **CodSoft Python Programming Internship**.

The application allows users to generate customizable passwords by selecting the desired password length and character types such as uppercase letters, lowercase letters, numbers, and symbols.

---

## 🎯 Objective

The objective of this project is to build a customizable password generator using Python while practicing functions, loops, conditional statements, input validation, string operations, and secure random character selection.

---

## ✨ Features

The application provides:

* 🔢 User-defined password length
* 🔠 Optional uppercase letters
* 🔡 Optional lowercase letters
* 🔢 Optional numbers
* 🔣 Optional symbols
* 🔐 Secure random character selection
* ✅ Character-type validation
* ⚠️ Invalid input handling
* 🔄 Multiple password generation without restarting the program

---

## ⚙️ How It Works

The program asks the user to:

1. Enter the desired password length.
2. Choose whether uppercase letters should be included.
3. Choose whether lowercase letters should be included.
4. Choose whether numbers should be included.
5. Choose whether symbols should be included.
6. Generate the password using the selected character types.

The program ensures that at least one selected character type is included in the generated password.

The final password characters are shuffled before the password is returned.

---

## 🔐 Password Generation

The project uses Python's `secrets` module for selecting password characters.

Available character sets are provided using the `string` module:

* `string.ascii_uppercase`
* `string.ascii_lowercase`
* `string.digits`
* `string.punctuation`

The `secrets` module is designed for generating cryptographically strong random values and is more appropriate for password generation than ordinary pseudo-random selection.

---

## 🧠 Python Concepts Used

This project demonstrates:

* Functions
* Parameters and Return Values
* Python Lists
* `while` Loop
* `for` Loop
* Conditional Statements
* `try-except`
* Input Validation
* String Manipulation
* `string` Module
* `secrets` Module
* `secrets.choice()`
* List Shuffling
* `"".join()`

---

## 🛠️ Technologies Used

* Python
* VS Code
* Python `string` module
* Python `secrets` module

No external Python packages are required.

---

## 📁 Project Structure

```text
Task_3_Password_Generator/
│
├── password_generator.py
└── README.md
```

---

## ▶️ How to Run

### 1. Download or clone the repository

Open the Password Generator project folder.

### 2. Check Python installation

```bash
python --version
```

### 3. Run the program

```bash
python password_generator.py
```

---

## 📌 Example

```text
--- PASSWORD GENERATOR ---

Enter password length: 12
Include uppercase letters? (yes/no): yes
Include lowercase letters? (yes/no): yes
Include numbers? (yes/no): yes
Include symbols? (yes/no): yes

Generated Password: [random password]

Generate another password? (yes/no): no

Thank you for using the Password Generator!
```

> The generated password will be different each time because characters are selected randomly.

---

## ⚠️ Input Validation

The program handles several invalid inputs.

### Invalid Password Length

If the user enters zero or a negative number:

```text
Password length must be greater than zero.
```

### Invalid Numeric Input

If the user enters text instead of a whole number:

```text
Invalid input. Please enter a valid whole number.
```

### Invalid Yes/No Input

```text
Please enter only yes or no.
```

### No Character Type Selected

```text
You must select at least one character type.
```

The program also checks whether the requested password length is large enough to include all selected character types.

---

## 🚀 Future Improvements

Possible future enhancements include:

* Password strength indicator
* Copy generated password to clipboard
* Save generated passwords securely
* Graphical User Interface (GUI)
* Custom symbol selection
* Password-generation presets

---

## 👨‍💻 Author

**Ashish Kumar**

GitHub: [Programmer-pathak](https://github.com/Programmer-pathak)

---

## 📚 Internship

**Python Programming Internship — CodSoft**

This project was developed as part of the Python Programming Internship tasks assigned by CodSoft.
