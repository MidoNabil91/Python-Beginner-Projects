# Python Beginner Projects 🐍

A structured collection of beginner-friendly Python projects and debugging exercises created while mastering Python fundamentals, logic design, and clean coding standards.

This repository focuses on practical problem-solving, real-world supply chain scenarios, data handling, modular function design, and hands-on code reviews.

---

## 🛠️ Projects & Exercises

### 0. Debugging & Code Review Exercises

A dedicated series of debugging challenges focused on inspecting buggy code, identifying logic errors, analyzing scope behaviors, and refactoring for production-ready efficiency

* Set 1 (debugging_exercises_01.py & debugging_exercises_02.py): Practical debugging challenges covering loop counters, infinite loop prevention, `while-else` control flows, `if-elif` conditional hierarchy order, scope initialization (`NameError`), arithmetic operator precedence, and missing `return` statements (`TypeError`)
* Set 2 (debugging_exercises_03.py): 5 advanced functional challenges inspired by procurement & inventory logic—covering boundary conditions (`<=` vs `<`), pure functions vs scope modification, strict boolean evaluation (`and` vs `or`), default parameter ordering (`SyntaxError`), and defensive checks against division by zero (`ZeroDivisionError`)
* Set 3 (debugging_exercises_04.py): Practical debugging & refactoring challenges covering logical operator selection (`and` vs `or`), variable scope/naming typos (`NameError`), defensive validation against `ZeroDivisionError`, and standard return-value modular structures
* Set 4 (debugging_exercises_05.py): Intermediate debugging challenges reinforcing conditional logic, loop control, data structure manipulation, and clean function return patterns
* Set 5 (dictionaries_supply_chain_training.py): Practical dictionary exercises covering CRUD operations, nested dictionaries, data filtering, aggregation logic, inventory management, fleet tracking, supplier evaluation, and procurement-focused business scenarios
* Set 6 (debugging_Supply Chain & Procurement Practice.py): A collection of 10 practical debugging exercises focused on identifying and fixing syntax, runtime (`KeyError`, `ValueError`, `AttributeError`), and logical bugs in supply chain and procurement scripts
* Set 7 (dictionary_business_scenarios.py): Focused on business logic, RFQ evaluation, inventory management, fleet tracking, and supplier assessment using Python
* Set 8 (debugging_exercises_06_pos_and_inventory.py): 12 real-world debugging challenges focused on POS billing math, dictionary lookups, stock guards, exception handling, and JSON data initialization
* Set 9 (debugging_exercises_07.py): 10 practical business logic scenarios covering tiered discount thresholds, inventory stock updates, cart accumulation, string normalization, zero-division guards, safe dictionary `.get()` lookups, list comprehension filtering, tax precedence, mutable default argument fixes, and Kuwaiti phone validation
* Set 10 (debugging_exercises_08.py): 8 Object-Oriented Programming (OOP) debugging challenges covering `self` binding (`TypeError`), instance vs. local attribute initialization (`AttributeError`), internal sibling method calls, `__repr__` object formatting, `return` vs. `print` in methods, shared mutable class dictionary traps, encapsulation price-validation guards, and custom `to_dict()` JSON serialization

### 1. Interactive Multiplication Table Generator

(multiplication-table-python.py & multiplication_table_v2.py) — v2.0

An interactive multiplication trainer refactored from a basic loop script into a modular, dual-mode CLI application:

* **Learn Mode (`generate_table`):** Generates clean multiplication tables for any number with customizable upper limits (e.g., 1 to 10 or 1 to 12)
* **Interactive Quiz Mode (`start_quiz`):** Tests the user with randomized multiplication questions (`random.randint`), tracks the final score, and lists mistakes for review
* **Modular Architecture:** Refactored into single-responsibility functions (`get_valid_int`, `generate_table`, `start_quiz`, `main_lines`, `main`) with a `while True` menu loop
* **Defensive Input Validation:** Protects all numeric prompts against invalid text inputs using `try...except ValueError` handling

### 2. Interactive Countdown Timer

A simple countdown timer that:

* Takes a number from the user
* Counts down to zero
* Displays a completion message
* Allows the user to start another countdown
* Exits when requested

### 3. Number Guessing Game

A simple guessing game that:

* Generates a random number between 1 and 100
* Gives hints when the guess is too high or too low
* Tracks the number of attempts
* Limits the player to 10 attempts
* Allows the player to restart the game
* Displays a Game Over message when attempts run out

### 4. Simple & Continuous Calculator

(simple_continuous_calculator.py, simple_continuous_calculator_v2.0.py, & simple_continuous_calculator_v3.0.py) — v3.0 (OOP)

A CLI calculator showcasing progressive software architecture across three iterations:

**v1.0 (Procedural):** Core arithmetic functions with continuous calculation loops and basic zero-division checks
**v2.0 (Modular & Dictionary Dispatch):** Refactored with `OPERATIONS` dictionary mapping, session calculation history (`show_history`), and defensive input validation (`get_valid_float`, `get_valid_operation`)
**v3.0 (Object-Oriented):** Encapsulates state (`self.history`, `self.operations`) and all calculation logic inside a clean, reusable `Calculator` class

### 5. Supplier Evaluation System 📦

A practical procurement-focused application that:

* Evaluates supplier performance using weighted scoring (Quality: 40%, Delivery: 30%, Price: 30%)
* Calculates total weighted average score dynamically
* Automatically assigns Supplier Status (*Approved*, *Conditional*, *Rejected*)
* Assesses Supplier Risk Level (*Low Risk*, *Medium Risk*, *High Risk*)
* Features modular Python functions for clean code architecture
* Formats output into a clean, professional summary report
* Implements continuous evaluation loops to evaluate multiple suppliers

### 6. Inventory Tracker System 📦

(`inv_tracker_system.py` v1.4, `inv_tracker_system_v2.0.py`, & `inv_tracker_system_v3.0.py`) — v3.0 (OOP)

A persistent, dictionary-driven warehouse and procurement inventory control system upgraded from a single-item session tracker (`v1.4`) to a full multi-SKU database architecture:

* **Multi-SKU Nested Dictionary Architecture (`v2.0`):** Manages unlimited materials indexed by unique `material_code`, storing item name, category, current stock, custom `max_capacity`, custom `reorder_point`, and `unit_price` (KWD).
* **JSON Data Persistence:** Automatically loads and saves all inventory records and movement logs via `inv_tracker.json` (`load_invtracker` / `save_invtracker`), preserving data across sessions with `FileNotFoundError` and `JSONDecodeError` protection.
* **Stock Movement & Capacity Enforcement:** Supports `OPENING`, `IN` (Receive), and `OUT` (Issue) transactions with strict validation against negative values, out-of-stock issues, and maximum warehouse capacity limits.
* **Automated Reorder Alert Report:** Dedicated alert engine (`reorder_report`) scans all SKUs and flags items reaching or falling below their custom `reorder_point` (`stock <= reorder_point`).
* **Financial Valuation & Occupancy KPIs:** Generates a full warehouse valuation report (`view_inventory`) calculating per-item value, occupancy rate (`%`), and total warehouse valuation in KWD (`:.3f`).
* **Timestamped Audit Trail (Bin Card):** Logs every inventory movement with `datetime` timestamps (`YYYY-MM-DD HH:MM`), transaction type, quantity, and running balance (`view_transactions`).
* **Object-Oriented Architecture (`v3.0`):** Encapsulates inventory state (`self.data`), file persistence, stock movements, and reporting methods inside a cohesive `InventoryTracker` class.

### 7. Supplier List Manager 📦

(supplier_list_manager.py) / (supplier_list_manager_v2.py) — v2.0 / (supplier_list_manager_v3.py) (v3.0)

An interactive CLI procurement tool upgraded to a dictionary-based architecture to maintain and manage an active directory of approved suppliers:

* **User Authentication Gate:** Secured with a login system (`login()`) enforcing a 3-attempt lockout limit before granting system access.
* **Dictionary-Based CRUD Management:** Stores supplier records with nested attributes (`category` and `status`), supporting adding, viewing, updating status, and deleting suppliers.
* **Partial-Match Smart Search:** Allows searching suppliers using partial keywords rather than exact full-name matches.
* **Duplicate Prevention & Validation:** Protects against duplicate entries and empty inputs with defensive exception handling (`try...except ValueError`).
* ** Full architectural refactoring into modular, single-responsibility functions (`main`, `show_menu`, `get_choice`, `add_supplier`, `view_suppliers`, `search_supplier`, `update_supplier`, `delete_supplier`) with comprehensive docstrings and `enumerate` formatting.

### 8. Vendor Evaluation Matrix 📊

(vendor_evaluation_matrix_v2.py & vendor_evaluation_matrix_v3.py) — v3.0

A modular procurement decision-support CLI application designed to evaluate and rank competing vendors using a two-stage technical and commercial scoring methodology with persistent storage:

* **Two-Stage Evaluation Gate:** Screens vendors first through a mandatory Technical Pass/Fail threshold (`score >= 70` to pass), automatically disqualifying technically non-compliant bids from commercial ranking.
* **Technical Qualification Engine:** Automatically classifies vendors as *Passed* or *Rejected* based on the mandatory technical threshold (`>= 70`), simulating real RFQ technical evaluation workflows.
* **Weighted Commercial Scoring:** Calculates overall commercial performance dynamically using procurement weights (**Price: 40%**, **Quality: 35%**, **Delivery: 25%**).
* **Winner Selection Engine (`find_best_vendor`):** Iterates through qualified vendors and returns a tuple `(best_score, best_vendor)` to generate a formatted Best Vendor Award Report.
* **JSON Data Persistence (`v3.0`):** Automatically saves and loads vendor evaluation records using a local `vendors.json` file (`json.load` / `json.dump`) so data persists across sessions.
* **Defensive Input & Edge-Case Protection:** Enforces strict `0–100` score boundaries, prevents duplicate vendor entries, handles `ValueError` and `FileNotFoundError` exceptions, and safely manages empty or unqualified vendor lists.

---

## 🧠 Concepts Practiced

Through these projects, I practiced:

* Variables & Primitive Data Types.
* Python Lists & Dynamic Sequences (`append()`, `remove()`, `len()`, `zip()`, `enumerate()`)
* Python Dictionaries, Nested Dictionary Structures & CRUD Operations
* User Input Handling & String Sanitization (`strip()`, `lower()`, `title()`)
* Print Formatting, Decimal Precision Formatting (`:.3f`, `:.2f`), & F-strings
* Modular Code Architecture with Pure Functions & `return` Statements
* Weighted Average & Mathematical Calculation Logic
* Dynamic KPI Calculations (Warehouse Occupancy Rate %, Valuation Reports)
* Random Module & Logic Control
* Control Flow (`if` / `elif` / `else`) & Logical Operators (`and`, `or`, `not`)
* Iteration Controls (`while` Loops, `for` Loops, `break`, `continue`)
* Defensive Programming, Stock Boundary Validation, & Duplicate Prevention
* Audit Log Trail Management using String Accumulation (`+=`)
* Defensive Exception Handling (`try...except ValueError`) & Zero-Division Risk Prevention
* Business Rule Implementation, Technical Qualification Logic, & Weighted Vendor Evaluation Models
* Decision-Making Algorithms
* File Handling & JSON Data Persistence (`with open()`, `json.load()`, `json.dump()`, `FileNotFoundError` handling)
* Timestamped Audit Trails & Date Formatting (`datetime.now().strftime()`)
* User Input Handling, String Sanitization & ID Padding (`strip()`, `lower()`, `title()`, `zfill()`)
* Object-Oriented Programming (OOP) Fundamentals (`class`, `__init__`, `self`, instance vs. class attributes, `__repr__`, encapsulation guards, `to_dict()` JSON serialization) & Dictionary Dispatch Patterns

---

## 🎯 Purpose of This Repository

I am currently learning Python step by step. Instead of only studying theory, I am building small projects and analyzing code bugs to strengthen my understanding of programming logic, supply chain automation, and problem-solving skills.

---

### 📚 Learning Approach

This repository follows a project-based learning approach.

Each project starts with a simple version and is gradually improved through debugging, refactoring, code reviews, feature enhancements, and real-world business scenarios.

The objective is not only learning Python syntax but also developing problem-solving skills, software design thinking, and supply chain automation concepts.

---

### 🚀 Future Roadmap

* 🔐 User Authentication & Login System ✅
* 📊 Vendor Evaluation Matrix ✅
* 📁 File-Based Supplier Management System (CSV / JSON) ✅
* 🏗️ Object-Oriented Programming (OOP) ✅
* 📈 Procurement KPI Dashboard
* 🐼 Data Analysis with Pandas

---

### 📊 Repository Statistics

* 📊 8 Practical Python Projects.
* 📊 10 Debugging Exercise Sets.
* 📊 Supply Chain & Procurement-Focused Scenarios.
* 📊 Progressive Refactoring & Code Review Practice.
* 📊 Dictionary-Based, OOP & JSON-Persistent Business Applications.

---

## 👨‍💻 Author

**Mohamed Nabil**  
*Procurement Professional | Python Learner*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat&logo=linkedin)](https://www.linkedin.com/in/mohamed-abdeldayem-b80174a5)
[![GitHub](https://img.shields.io/badge/GitHub-MidoNabil91-181717?style=flat&logo=github)](https://github.com/MidoNabil91)

---

Learning Python one step at a time 🚀
