# AKIBA PROJECTS

## AKIBA TECHNOLOGIES | WEEK 3

### Python Programming — Functions and Modular Programming

**Program:** Akiba Technologies Software Engineering & Backend Bootcamp
**Track:** Software Engineering & Backend Development
**Student:** Musab Moahmmedamin
**GitHub:** [@musabmohamin](https://github.com/musabmohamin)
**Week:** 03
**Primary Language:** Python

---

## 1. Overview

Week 3 focuses on **Python functions, code reusability, input validation, and modular programming**. The goal is to develop programs that are organized into smaller, reusable functions instead of putting all the logic in one place.

Throughout this week, I practice using parameters, return values, default arguments, lists, dictionaries, loops, and conditional statements to solve practical programming problems.

The week also includes the **Akiba Business Management Toolkit**, a menu-driven application designed to manage products, record sales, monitor inventory, and generate business reports.

## 2. Learning Objectives

By completing this week's assignments, I aim to improve my ability to:

- Design functions that perform specific tasks.
- Use parameters and return values correctly.
- Apply default arguments and reuse functions.
- Divide larger programs into smaller, manageable modules.
- Work with lists of dictionaries to organize data.
- Validate user input and handle invalid data.
- Test normal cases, boundary values, and incorrect inputs.
- Write readable, maintainable Python programs.
- Organize a multi-file Python project using imports.

## 3. Weekly Assignments

The following checklist tracks the Week 3 programming tasks.

- [ ] **Task 01 — Smart Shopping Receipt Generator:** Calculate subtotals, discounts, tax, and final purchase amounts.
- [ ] **Task 02 — Student Performance Analyzer:** Analyze student scores, grades, averages, and pass/fail results.
- [ ] **Task 03 — Advanced Number Analyzer:** Analyze prime numbers, divisors, digit sums, and reversed numbers.
- [ ] **Task 04 — Text Statistics and Word Analyzer:** Analyze words, characters, vowels, consonants, and word frequency.
- [ ] **Task 05 — Bank Transaction Processor:** Manage deposits, withdrawals, balances, and transaction history.
- [ ] **Task 06 — Inventory Stock Controller:** Manage products, prices, quantities, and low-stock alerts.
- [ ] **Task 07 — Password Policy and Strength Analyzer:** Check password requirements and report missing conditions.
- [ ] **Task 08 — Electricity Bill Calculator:** Calculate electricity charges using a tiered pricing model.
- [ ] **Task 09 — Reusable Quiz Engine:** Build a reusable quiz with answer validation, scoring, and results.
- [ ] **Task 10 — Function-Based Expense Analyzer:** Analyze expenses, category totals, and spending patterns.

## 4. Mini Project — Akiba Business Management Toolkit

### Project Description

The Akiba Business Management Toolkit is a menu-driven Python application designed to help a small business manage its products, sales, and inventory.

The application uses functions to separate responsibilities and modules to organize related operations. Product and sales information is stored using lists and dictionaries.

### Main Features

**Product Management**

- Add new products.
- View all available products.
- Search for products by name.
- Update product information.
- Validate product names, prices, and quantities.

**Sales Management**

- Record product sales.
- Validate requested quantities.
- Prevent sales that exceed available stock.
- Calculate the total cost of a sale.
- Reduce inventory after a successful sale.

**Business Reporting**

- Calculate total sales revenue.
- Calculate the value of remaining inventory.
- Display products with low stock.
- Show a summary of recorded sales.

### Application Menu

```text
===== AKIBA BUSINESS TOOLKIT =====

1. Add Product
2. View Products
3. Search Product
4. Update Product
5. Record Sale
6. View Reports
7. Exit
```

### Technical Approach

The application separates product management, sales processing, and reporting into different Python modules. Functions receive the data they need through parameters, while calculated results are returned where appropriate.

This structure helps make the application easier to understand, test, debug, and extend.

## 5. Skills Practiced

During Week 3, I focus on developing the following skills:

- **Function design:** Breaking a problem into smaller tasks.
- **Code reusability:** Using functions instead of repeating logic.
- **Input validation:** Checking user input before processing it.
- **Data structures:** Managing lists and dictionaries.
- **Modular programming:** Separating functionality into different files.
- **Error handling:** Managing invalid inputs and unexpected cases.
- **Problem-solving:** Applying programming concepts to practical scenarios.
- **Testing and debugging:** Checking program behavior and correcting errors.
- **Code organization:** Writing readable code that can be maintained and improved.

## 6. Technologies and Tools

- **Python 3** — Main programming language.
- **Visual Studio Code** — Code editor and development environment.
- **Ubuntu Linux** — Development operating system.
- **Git** — Version control.
- **GitHub** — Source-code hosting and project submission.

## 7. Project Structure

The Week 3 files are organized inside the main `AKIBA PROJECTS` repository.

```text
AKIBA PROJECTS/
│
├── akiba_week1_python/
│   └── README.md
│
├── akiba_week_02_python/
│   └── README.md
│
└── akiba_week3_python/
    ├── README.md
    ├── theory_answers.md
    │
    ├── task_01_shopping_receipt.py
    ├── task_02_student_analyzer.py
    ├── task_03_number_analyzer.py
    ├── task_04_text_analyzer.py
    ├── task_05_bank_processor.py
    ├── task_06_inventory_controller.py
    ├── task_07_password_analyzer.py
    ├── task_08_electricity_calculator.py
    ├── task_09_quiz_engine.py
    ├── task_10_expense_analyzer.py
    │
    └── akiba_business_management/
        ├── main.py
        ├── product.py
        ├── sales.py
        └── report.py
```

*Note: This structure describes the intended organization. The filenames in the repository should match the files actually created, and the README should be updated as the project develops.*

## 8. How to Run the Programs

### Requirements

Install Python 3 and a code editor such as Visual Studio Code.

Check the Python installation in the terminal:

```bash
python3 --version
```

### Run an Individual Assignment

Navigate to the Week 3 directory and run the relevant Python file:

```bash
cd "AKIBA PROJECTS/akiba_week3_python"
python3 task_01_shopping_receipt.py
```

Replace the filename with the assignment you want to execute.

### Run the Business Management Toolkit

Navigate to the mini project directory:

```bash
cd "AKIBA PROJECTS/akiba_week3_python/akiba_business_management"
python3 main.py
```

Follow the menu options displayed in the terminal.

## 9. Theory Questions

The file `theory_answers.md` contains answers to the two required theory questions:

1. **Function Design:** Why large functions are difficult to maintain and how smaller functions improve code organization, reuse, testing, and debugging.
2. **Mutable Data and Function Side Effects:** How modifying a list inside a function affects the original list, and how copying a list can avoid unwanted changes.

## 10. Learning Reflection

Week 3 helps me understand that writing a program is not only about making it work. It is also important to organize the code so that it is understandable, reusable, and easier to maintain.

By practicing functions and modular programming, I am building a stronger foundation for developing larger Python applications. The Business Management Toolkit gives me an opportunity to apply these concepts to a practical system involving inventory, sales, validation, and reporting.

My next goal is to continue improving the correctness, organization, and reliability of my programs while testing different inputs and handling edge cases.

## 11. Submission and Progress

**Repository:** [AKIBA PROJECTS](https://github.com/musabmohamin/AKIBA-PROJECTS)

**Week 3 directory:** `akiba_week3_python/`

Before submission, I will:

- [ ] Complete the ten programming assignments.
- [ ] Test normal, boundary, and invalid inputs.
- [ ] Complete the Business Management Toolkit.
- [ ] Include `theory_answers.md`.
- [ ] Verify that imports and file paths work correctly.
- [ ] Update this README to reflect the actual completed work.
- [ ] Commit and push the changes to GitHub.

---

**Akiba Technologies — Learn • Build • Grow**

*Week 3: Practicing functions, improving code organization, and building reusable Python applications.*
