# AKIBA TECHNOLOGIES | WEEK 4

### Mutability, References, and Memory Model in Python

**Software Engineering & Backend Bootcamp**

---

## Student Information

| **Field** | **Details** |
|---|---|
| **Name** | Musab Moahmmedamin |
| **GitHub** | [@musabmohamin](https://github.com/musabmohamin) |
| **Program** | Akiba Technologies |
| **Track** | Software Engineering & Backend |
| **Week** | 04 |
| **Language** | Python |

## Overview

This repository contains my Week 4 assignment and practical mini-project completed as part of the Akiba Technologies Software Engineering & Backend Bootcamp.

The primary objective of this week is to understand how Python handles mutable and immutable objects, references, object identity, shared references, function arguments, and memory management through practical programming exercises.

## Learning Objectives

- Differentiate mutable and immutable objects in Python.
- Understand references and object identity using `is` and `==`.
- Identify shared references and side effects when modifying mutable objects.
- Understand how mutable objects behave when passed to functions.
- Explain Python memory management and garbage collection.
- Apply copying and reference concepts in a practical project.
- Organize, document, and submit Python programs using Git and GitHub.

## Weekly Assignments

| **No.** | **Assignment** | **Description** | **Status** |
|---|---|---|---|
| 01 | Mutable and Immutable Objects | Demonstrate the difference between lists and strings. | ☑ |
| 02 | References and Object Identity | Compare object identity and value equality using `is` and `==`. | ☑ |
| 03 | Shared References and Side Effects | Explore shared lists and independent copies. | ☑ |
| 04 | Function Arguments and Mutability | Examine how functions modify mutable objects. | ☑ |
| 05 | Memory Management and Garbage Collection | Understand references, `del`, and object reclamation. | ☑ |

## Mini Project

### Student Marks Manager

A Python program designed to manage student marks while demonstrating mutability, shared references, object identity, and list copying.

**Key concepts applied:**

- Creating and modifying lists.
- Assigning multiple references to the same object.
- Creating independent copies using `copy()`.
- Adding new marks without modifying the original list.
- Comparing object identity using `is`.
- Comparing values using `==`.
- Understanding the effects of modifying shared objects.

### Expected Output

```text
Original marks: [75, 80, 65, 90, 85]
Shared reference: [75, 80, 65, 90, 85]
Copied marks: [75, 80, 65, 90, 85, 95]

Original and shared reference are identical: True
Original and copied lists have equal values: False
Original and copied lists are identical: False
```

## Skills Practiced

- **Python Fundamentals:** Understanding mutable and immutable data types.
- **Object References:** Working with references, identity, and equality.
- **Problem-Solving:** Predicting program behavior and explaining results.
- **Function Design:** Understanding side effects and returning independent copies.
- **Memory Management:** Learning how Python handles object references and garbage collection.
- **Code Organization:** Writing readable, maintainable, and reusable code.
- **Version Control:** Managing source code using Git and GitHub.
- **Documentation:** Explaining concepts, program outputs, and project decisions.

## Technologies & Tools

- Python 3
- Visual Studio Code
- Git
- GitHub

## Project Structure

```text
week-4-python-task/
├── README.md
├── questions.py
└── student_marks_manager.py
```

### File Descriptions

- **`README.md`** — Contains assignment explanations, expected outputs, project reflection, and instructions for running the programs.
- **`questions.py`** — Contains the Python solutions for all five assignment questions.
- **`student_marks_manager.py`** — Contains the complete Student Marks Manager mini-project.

## Learning Reflection

Week 4 provides an opportunity to understand how Python variables refer to objects in memory and how those objects behave when modified or passed between functions.

Through these assignments, I am learning that assigning one variable to another does not necessarily create a new object. I have also learned to distinguish object identity from value equality and to use list copying when independent modifications are required.

These concepts are important for writing reliable, predictable, and maintainable Python programs. They also strengthen my understanding of programming fundamentals as I continue developing my software engineering and embedded systems skills.

## Future Development

This repository is part of my ongoing technical learning journey. As I progress through the bootcamp, I intend to strengthen my Python programming skills, explore object-oriented programming and data structures, and apply these concepts to more advanced software and embedded systems projects.

I will continue maintaining organized repositories, writing meaningful commit messages, testing my programs, and documenting my learning progress.

## How to Run the Programs

Make sure Python 3 is installed on your computer.

Open a terminal in the project directory and run:

```bash
python questions.py
python student_marks_manager.py
```

On systems where Python 3 uses a separate command, run:

```bash
python3 questions.py
python3 student_marks_manager.py
```

## GitHub Submission

**Repository Name:** `week-4-python-task`

**Program:** Akiba Technologies — Software Engineering & Backend Bootcamp

**Assignment:** Week 4 — Mutability, References, and Memory Model in Python

**Student:** Musab Moahmmedamin

**GitHub:** [github.com/musabmohamin](https://github.com/musabmohamin)

### Submission Checklist

- [ ] All five questions answered.
- [ ] `questions.py` completed and tested.
- [ ] `student_marks_manager.py` completed and tested.
- [ ] `README.md` includes explanations and project reflection.
- [ ] All required files committed and pushed to GitHub.
- [ ] Repository access verified.
- [ ] Repository URL submitted to the instructor.

---

*Learning by building, improving through practice, and documenting progress.*