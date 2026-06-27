# Employee Management System

A simple command-line Employee Management System built using **Python** and **MySQL**. This project was developed as a Class 12 Computer Science project and demonstrates basic database connectivity, CRUD (Create, Read, Update, Delete) operations, and salary slip generation using Python.

## Features

- View all employee records
- Add a new employee
- Search employees by Employee ID
- Edit employee details
- Delete employee records
- Generate a salary slip

## Requirements

- Python 3.x
- MySQL Server
- `mysql-connector-python`

Install the required Python package using:

```bash
pip install -r requirements.txt
```

## Installation

1. Clone this repository.

   ```bash
   git clone https://github.com/<your-username>/employee-management-system.git
   ```

2. Open MySQL and execute the `database.sql` file to create the required database and tables.

3. Open `empproj.py` and update the database connection details if required.

   ```python
   host="127.0.0.1"
   user="root"
   password="your_password"
   database="company"
   ```

4. Run the program.

   ```bash
   python empproj.py
   ```

## Project Structure

```
employee-management-system/
├── empproj.py
├── database.sql
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE
```

## Author

**Purunjay Singh**

Developed as a Class 12 Computer Science project.
