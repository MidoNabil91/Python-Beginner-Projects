# Python Beginner Projects 🐍

A structured collection of beginner-friendly Python projects and debugging exercises created while mastering Python fundamentals, logic design, and clean coding standards.

This repository focuses on practical problem-solving, real-world supply chain scenarios, data handling, modular function design, and hands-on code reviews.

---

## 🛠️ Projects & Exercises

### 0. Debugging & Code Review Exercises
A dedicated series of debugging challenges focused on inspecting buggy code, identifying logic errors, analyzing scope behaviors, and refactoring for production-ready efficiency.

* **Set 1 (`debugging_exercises_01.py` & `debugging_exercises_02.py`):** 
  * Practical debugging challenges covering loop counters, infinite loop prevention, `while-else` control flows, `if-elif` conditional hierarchy order, scope initialization (`NameError`), arithmetic operator precedence, and missing `return` statements (`TypeError`).
* **Set 2 (`debugging_exercises_03.py`):** 
  * 5 advanced functional challenges inspired by procurement & inventory logic—covering boundary conditions (`<=` vs `<`), pure functions vs scope modification, strict boolean evaluation (`and` vs `or`), default parameter ordering (`SyntaxError`), and defensive checks against division by zero (`ZeroDivisionError`).
* **Set 3 (`debugging_exercises_04.py`):** 
  * Practical debugging & refactoring challenges covering logical operator selection (`and` vs `or`), variable scope/naming typos (`NameError`), defensive validation against `ZeroDivisionError`, and standard return-value modular structures.
* Set 4 (dictionaries_supply_chain_training.py):
Practical dictionary exercises covering CRUD operations, nested dictionaries, data filtering, aggregation logic, inventory management, fleet tracking, supplier evaluation, and procurement-focused business scenarios.
* Set 5 ( debugging_Supply Chain & Procurement Practice.py )
A collection of 10 practical debugging exercises focused on identifying and fixing syntax, runtime (`KeyError`, `ValueError`, `AttributeError`), and logical bugs in supply chain and procurement scripts.
* Set 6 (dictionary_business_scenarios.py)
Focused on business logic, RFQ evaluation, inventory management, fleet tracking, and supplier assessment using Python.

### 1. Interactive Countdown Timer
A simple countdown timer that:
* Takes a number from the user
* Counts down to zero
* Displays a completion message
* Allows the user to start another countdown
* Exits when requested

### 2. Interactive Multiplication Table Generator
A multiplication table generator that:
* Creates multiplication tables from 1 to 10
* Accepts multiple numbers without restarting the program
* Uses loops and user input
* Allows the user to exit by entering 0

### 3. Number Guessing Game
A simple guessing game that:
* Generates a random number between 1 and 100
* Gives hints when the guess is too high or too low
* Tracks the number of attempts
* Limits the player to 10 attempts
* Allows the player to restart the game
* Displays a Game Over message when attempts run out

### 4. Simple & Continuous Calculator
A calculator project that:
* Supports addition (`+`), subtraction (`-`), multiplication (`*`), division (`/`), modulus (`%`), and exponentiation (`**`)
* Built using Python pure functions and return statements
* Safely handles division by zero exceptions
* Allows continuous calculations using previous results
* Allows the user to start a new calculation or quit

### 5. Supplier Evaluation System 📦
A practical procurement-focused application that:
* Evaluates supplier performance using weighted scoring (Quality: 40%, Delivery: 30%, Price: 30%)
* Calculates total weighted average score dynamically
* Automatically assigns Supplier Status (*Approved*, *Conditional*, *Rejected*)
* Assesses Supplier Risk Level (*Low Risk*, *Medium Risk*, *High Risk*)
* Features modular Python functions for clean code architecture
* Formats output into a clean, professional summary report
* Implements continuous evaluation loops to evaluate multiple suppliers

### 6. Inventory Tracker Mini System 📦 (`inv_tracker_system.py`) — v1.4
A feature-rich inventory control application built with pure functions, menu-driven control flow, and supply chain logic:
* **Stock Transactions:** Supports receiving (`+In`) and issuing (`-Out`) operations with defensive input validation against invalid inputs or negative numbers.
* **Capacity Control & Reorder Alerts:** Enforces max warehouse capacity limits (`max_capacity = 500`) and issues automated Low Stock Warnings (`stock <= 5`).
* **Financial Valuation:** Calculates real-time total inventory monetary valuation formatted explicitly in KWD (`:.3f`).
* **Supply Chain KPIs:** Dynamically calculates Warehouse Occupancy Rate (`%`) and tracks cumulative Movement Metrics (`+Added` / `-Removed`).
* **Audit Trail:** Features a continuous string-based session history log to audit all transactions within an active session.

### 7. Supplier List Manager 📦 (supplier_list_manager.py)

A interactive CLI procurement tool designed to maintain and manage an active directory of approved suppliers:
CRUD Management: Fully supports adding new suppliers, viewing directory summaries, searching existing vendors, and deleting obsolete suppliers.
Duplicate Prevention: Protects the supplier directory against duplicate entries using membership checks (in operator).
Defensive Exception Handling: Prevents application crashes from invalid user choices using try...except ValueError blocks.
Formatted Output: Features dynamic index listing with range()/len(), text case normalization via .lower().strip() and presentation layer formatting with .title().
---

## 🧠 Concepts Practiced

Through these projects I practiced:
- Variables & Primitive Data Types
- Python Lists & Dynamic Sequences (append(), remove(), len(), zip(), enumerate())
- User Input Handling & String Sanitization (strip(), lower(), title())
- Print Formatting, Decimal Precision Formatting (:.3f, :.2f), & F-strings
- Modular Code Architecture with Pure Functions & return Statements
- Weighted Average & Mathematical Calculation Logic
- Dynamic KPI Calculations (Warehouse Occupancy Rate %, Valuation Reports)
- Random Module & Logic Control
- Control Flow (if / elif / else) & Logical Operators (and, or, not)
- Iteration Controls (while Loops, for Loops, break, continue)
- Defensive Programming, Stock Boundary Validation, & Duplicate Prevention
- Audit Log Trail Management using String Accumulation (+=)
- Defensive Exception Handling (try...except ValueError) & Zero-Division Risk Prevention.

---

## 🎯 Purpose of This Repository

I am currently learning Python step by step. Instead of only studying theory, I am building small projects and analyzing code bugs to strengthen my understanding of programming logic, supply chain automation, and problem-solving skills.

---

## 🚀 Future Roadmap

* 🔐 User Authentication & Login System
* 📁 File-Based Supplier Management System (CSV / JSON integration)
* 📈 Procurement Data Analysis & KPI Dashboard Tools

---

## 👨‍💻 Author

**Mohamed Nabil**  
*Procurement Professional | Python Learner*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat&logo=linkedin)](https://www.linkedin.com/in/mohamed-abdeldayem-b80174a5)
[![GitHub](https://img.shields.io/badge/GitHub-MidoNabil91-181717?style=flat&logo=github)](https://github.com/MidoNabil91)

---
*Learning Python one step at a time 🚀*