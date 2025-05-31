# 🐍 Python Tasks Overview

---

## 📄 task1.py — Arithmetic Operations Calculator

🔢 **Functionality:**
- 🧮 Prompts the user to input **two numbers** as `float` datatypes.
- ➕ Performs **Addition**
- ➖ Performs **Subtraction**
- ✖️ Performs **Multiplication**
- ➗ Performs **Division**

🛡️ **Error Handling:**
- 🚫 Gracefully handles **Division by Zero** errors with a friendly message.

🖥️ **Output:**
- Displays results of all arithmetic operations in a clean format.

---

## 📄 task2.py — Welcome Message Generator

🔤 **Functionality:**
- ✍️ Prompts the user for **two inputs** (default type: `string`).
- 🔗 **Concatenates** the two strings.
- 🎉 Displays a **personalized Welcome Message** using the concatenated string.

📌 **Example Output:**
> `Welcome JohnDoe! Have a great day!` 🙌

---

## 📄 task3.py — Even or Odd Checker

🔢 **Functionality:**
- 🔎 Prompts the user to enter an integer.
- 🧠 Uses conditional logic to determine if the number is **even** or **odd**.
- 📣 Prints the result.

📌 **Example Output:**
> `The number 7 is odd.`

---

## 📄 task4.py — Sum of Natural Numbers (1 to 50)

🔁 **Functionality:**
- 📈 Uses a `for` loop to calculate the **sum of natural numbers from 1 to 50**.
- ➕ Continuously adds each number in the range.
- 📣 Displays the final sum.

📌 **Example Output:**
> `The sum of natural numbers from 1 to 50 is 1275.` ✅


## 📄 task5.py — Factorial Calculator

🧮 **Functionality:**
- Asks the user for a **non-negative integer**.
- Calculates its **factorial** using recursion.
- 📣 Displays the result.

📌 **Example Output:**
> `The factorial of 5 is 120.`


## 📄 task6.py — Math Function Evaluator

🧠 **Functionality:**
- Prompts the user to input a **number** (`float`).
- Uses the `math` module to perform:
  - 📐 **Square Root** (`math.sqrt`)
  - 🔢 **Natural Logarithm** (`math.log`)
  - 🌊 **Sine** (`math.sin`)

🖥️ **Output:**
- Displays the calculated:
  - ✅ Square root
  - ✅ Logarithm
  - ✅ Sine of the number



  ## 📄 task7.py — File Reader with Error Handling

📂 **Functionality:**
- 📄 Tries to **open and read** a file named `sample.txt`.
- 📌 Displays the file content **line by line**, each with its corresponding **line number**.

🛡️ **Error Handling:**
- 🚫 If the file is **not found**, it prints a user-friendly **error message** without crashing.

📌 **Example Output:**
> Reading file content:  
> Line 1: This is the first line  
> Line 2: It contains multiple lines  

📌 **If file is missing:**
> Error: The file sample.txt was not found

## 📄 task8.py — File Writer, Appender & Reader

✍️ **Functionality:**
- Prompts the user to **enter text**, which is **written to a file** named `sample2.txt`.
- Then asks for **additional text** and **appends** it to the same file.
- Finally, **reads and displays** the full content of the file **line by line**.

🖥️ **Output:**
- Prints each line from the file after writing and appending.

📌 **Example Output:**
> Enter text to write to the file: Hello  
> Enter additional text to append: World  
> Final content of output.txt:  
> Hello  
> World