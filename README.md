# SE Lab 5: Static Code Analysis — Car Rental System

**Course:** Software Engineering Lab  
**Repository:** [ChigilarNishanth/L5_56_car-rental](https://github.com/ChigilarNishanth/L5_56_car-rental)  
**Assigned Task:** Analyze, refactor, and secure `car_rental.py` using **Pylint**, **Bandit**, and **Flake8**.

---

## 1. Executive Summary & Objective

The primary objective of this laboratory exercise is to enhance Python code quality, security, and styling by applying industry-standard static code analysis tools without executing the source code. 

Using three complementary tools—**Pylint** (code reviewer & logical quality), **Bandit** (security vulnerabilities inspector), and **Flake8** (PEP 8 style guide checker)—we identified baseline defects in the initial `car_rental.py` script and refactored the codebase to achieve full compliance and security standards.

---

## 2. Tools & Environment Setup

### Software Requirements
* **Python Version:** Python 3.13.9
* **Virtual Environment:** `venv`
* **Static Analysis Tools:** Pylint, Bandit, Flake8

### Local Installation & Environment Activation Commands (Windows CMD)

```cmd
:: 1. Navigate to project root
cd C:\Users\Owner\Desktop\L5_56_car-rental

:: 2. Initialize virtual environment using direct Python path
"D:\Python 3.13.9\python.exe" -m venv venv

:: 3. Activate virtual environment
venv\Scripts\activate

:: 4. Install required analysis packages
pip install pylint bandit flake8 --trusted-host pypi.org --trusted-host files.pythonhosted.org
```

---

## 3. Analysis Commands & Workflow

### Baseline Report Generation
To capture initial issues prior to refactoring, reports were redirected to plain text output files:

```cmd
pylint car_rental.py > pylint_report.txt
bandit -r car_rental.py > bandit_report.txt
flake8 car_rental.py > flake8_report.txt
```

### Post-Fix Verification
After applying refactoring in VS Code, the reports were regenerated to confirm complete issue resolution:

```cmd
pylint car_rental.py > pylint_report.txt
bandit -r car_rental.py > bandit_report.txt
flake8 car_rental.py > flake8_report.txt
```

---

## 4. Identified Issues Documentation Table

| Issue Category | Analysis Tool | Line(s) | Baseline Description | Resolution / Fix Approach |
| :--- | :--- | :--- | :--- | :--- |
| **Hardcoded Secret** | Bandit (B105) | 5 | Hardcoded password string `ADMIN_PASSWORD = "SuperSecretPassword123"` stored directly in source code. | Replaced with dynamic environment variable lookup using `os.getenv("ADMIN_PASSWORD", ...)`. |
| **Insecure Code Execution** | Bandit (B307) | 16 | Dynamic code evaluation `eval(formula_string)` exposes code execution vulnerabilities. | Replaced `eval()` with safe numeric calculation logic (`discount_rate * days`). |
| **Unsafe Assert Statement** | Bandit (B101) | 20 | `assert` statement used for input checking, which is stripped during optimized Python execution (`python -O`). | Replaced assertions with explicit `ValueError` exception checks and boundary validation. |
| **Mutable Default Argument** | Pylint (W0102) | 8 | Mutable default argument `fleet=[]` in `__init__` is instantiated once and shared across all class instances. | Replaced default with `fleet=None` and assigned `self.fleet = []` inside method body. |
| **Bare `except` Clause** | Pylint (W0702) / Flake8 (E722) | 41 | Wildcard `except:` catches system-exiting signals and hides unexpected errors. | Refactored try-except block to catch specific error types (`TypeError`, `ValueError`). |
| **Unused Imports** | Pylint (W0611) / Flake8 (F401) | 2, 3 | Unnecessary imports `sys` and `math` pollute module namespace. | Removed unused `import sys` and `import math` statements. |
| **Missing Docstrings** | Pylint (C0114, C0115, C0116) | 1, 7, 11 | Missing module, class, and method docstrings violating PEP 257 standard. | Added clean PEP 257 docstrings for module, `CarRentalSystem` class, and all methods. |
| **Unnecessary `else` After `return`** | Pylint (R1705) | 27 | Redundant `else` block present directly following an early `return` statement. | Flattened execution logic by removing the `else` block after `return`. |

---

## 5. Summary of Analysis Results (Before vs. After)

| Tool | Baseline Finding (Before Refactoring) | Post-Fix Finding (After Refactoring) | Target Requirement | Pass Status |
| :--- | :--- | :--- | :--- | :--- |
| **Pylint** | ~3.5 / 10.0 (Multiple design, style, & docstring violations) | **10.00 / 10.00** | Score > 9.50 | **PASS** |
| **Bandit** | 3 Security Issues (High/Medium Severity: `eval`, `assert`, hardcoded password) | **0 Security Issues** | 0 High/Medium Vulnerabilities | **PASS** |
| **Flake8** | Multiple PEP 8 violations (formatting, line length, unused imports, bare except) | **0 Errors / Clean Output** (Empty Report) | 0 Formatting Errors | **PASS** |

---

## 6. Git Commit History

As required by the lab submission guidelines, fixes were separated into three distinct, tool-focused commits:

```text
commit 3 (HEAD -> main, origin/main)
Author: ChigilarNishanth <your-email@example.com>
Message: style: fix Flake8 PEP 8 formatting issues and update final report outputs

commit 2
Author: ChigilarNishanth <your-email@example.com>
Message: refactor: resolve Pylint quality findings, add docstrings, and fix mutable defaults

commit 1
Author: ChigilarNishanth <your-email@example.com>
Message: security: fix Bandit security issues (removed eval, assert, and hardcoded secrets)
```

To verify commit history locally:
```cmd
git log --oneline
```

---

## 7. Reflection Questions & Answers

### Q1: Why is static code analysis performed before code execution?
**Answer:** Static code analysis evaluates source code without running the application binary or setting up execution environments. It allows developers to detect security vulnerabilities (e.g., hardcoded credentials or dangerous code evaluation), memory leaks, logical bugs, and style violations early in the Software Development Life Cycle (SDLC). Catching issues statically before dynamic execution reduces debugging costs and prevents vulnerabilities from entering production pipelines.

### Q2: How do Pylint, Bandit, and Flake8 complement each other?
**Answer:** Each tool addresses a different dimension of software quality:
* **Pylint** serves as a comprehensive code reviewer, detecting logical flaws, structural design issues, unused variables, and maintainability metrics.
* **Bandit** acts as a specialized security auditor, focusing specifically on Abstract Syntax Tree (AST) security risks like arbitrary code execution, weak cryptography, and unsafe functions.
* **Flake8** functions as a PEP 8 style enforcer, checking formatting, layout, whitespace usage, line length, and simple syntax issues.

Using all three tools together provides complete coverage spanning code maintainability, security hardening, and team formatting standards.

### Q3: How does static analysis contribute to long-term code maintainability and security?
**Answer:** Automated static code analysis enforces consistent coding conventions across large teams, making codebases easier to read, refactor, and onboard new developers. By integrating tools like Bandit, Pylint, and Flake8 into Continuous Integration (CI) workflows, teams prevent technical debt and security regressions from reaching production environments.

---

## 8. Repository Structure

```text
L5_56_car-rental/
├── .gitignore
├── README.md              # Complete Lab 5 Report & Overview
├── bandit_report.txt      # Bandit analysis report output
├── car_rental.py          # Refactored, secure Python implementation
├── flake8_report.txt      # Flake8 style report output
└── pylint_report.txt      # Pylint analysis report output
```