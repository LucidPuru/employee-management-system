'''
========================================
- Employee Management System
- By ~ Purunjay Singh XII 12
- A Simple CLI application for managing 
  menployee records using Python & MySQL
========================================
'''

import mysql.connector as mycon
from config import *

# Database Connection

cn = mycon.connect(
    host = HOST,
    user = USER,
    password = PASSWORD,
    database = DATABASE
)
cur = cn.cursor()

# Utility Functions

def clear():
    print("\n" * 40)


def display_records(records):
    print("=" * 60)
    print(f"{'EMPNO':<8}{'EMP NAME':<20}{'DEPARTMENT':<18}{'SALARY':>10}")
    print("=" * 60)

    for row in records:
        print(f"{row[0]:<8}{row[1]:<20}{row[2]:<18}{row[3]:>10}")
    print("=" * 60)


def get_employee(empno):
    cur.execute("SELECT * FROM emp WHERE empno = %s", (empno,))
    return cur.fetchall()

# Employee Functions

def show_all():
    try:
        cur.execute("SELECT * FROM emp")
        results = cur.fetchall()

        if results:
            display_records(results)
            print(f"Total Records : {len(results)}")
        else:
            print("No employee records found.")

    except Exception as e:
        print("Error:", e)


def add_employee():
    try:
        print("\nADD NEW EMPLOYEE")
        eno = int(input("Employee Number : "))
        en = input("Employee Name   : ")
        dp = input("Department      : ")
        sl = int(input("Salary          : "))

        cur.execute(
            "INSERT INTO emp VALUES (%s,%s,%s,%s)",
            (eno, en, dp, sl)
        )
        cn.commit()
        print("\nRecord added successfully!")

    except Exception as e:
        print("Error:", e)


def search_employee():
    try:
        eno = int(input("Enter Employee Number : "))
        records = get_employee(eno)

        if records:
            display_records(records)
        else:
            print("No matching employee found.")

    except Exception as e:
        print("Error:", e)


def edit_employee():
    try:
        eno = int(input("Enter Employee Number : "))
        records = get_employee(eno)

        if not records:
            print("Employee not found.")
            return

        display_records(records)

        if input("Update record? (y/n): ").lower() == "y":
            dept = input("New Department : ")
            salary = int(input("New Salary     : "))

            cur.execute(
                "UPDATE emp SET dept=%s, salary=%s WHERE empno=%s",
                (dept, salary, eno)
            )
            cn.commit()
            print("Record updated successfully!")

    except Exception as e:
        print("Error:", e)


def delete_employee():
    try:
        eno = int(input("Enter Employee Number : "))
        records = get_employee(eno)

        if not records:
            print("Employee not found.")
            return

        display_records(records)

        if input("Delete record? (y/n): ").lower() == "y":
            cur.execute("DELETE FROM emp WHERE empno=%s", (eno,))
            cn.commit()
            print("Record deleted successfully!")

    except Exception as e:
        print("Error:", e)


def generate_salary_slip():
    try:
        eno = int(input("Enter Employee Number : "))
        cur.execute("SELECT * FROM emp WHERE empno=%s", (eno,))
        emp = cur.fetchone()

        if not emp:
            print("Employee not found.")
            return

        clear()

        basic = emp[3]
        hra = basic * 0.12
        da = basic * 0.15
        income_tax = 1000
        nps = (basic + hra) * 0.10

        gross = basic + hra + da
        deductions = income_tax + nps
        net = gross - deductions

        print("=" * 50)
        print("               SALARY SLIP")
        print("=" * 50)
        print(f"Employee No : {emp[0]}")
        print(f"Name        : {emp[1]}")
        print(f"Department  : {emp[2]}")
        print("-" * 50)
        print(f"Basic Salary : {basic:.2f}")
        print(f"HRA (12%)    : {hra:.2f}")
        print(f"DA  (15%)    : {da:.2f}")
        print("-" * 50)
        print(f"Income Tax   : {income_tax:.2f}")
        print(f"NPS          : {nps:.2f}")
        print("-" * 50)
        print(f"Gross Salary : {gross:.2f}")
        print(f"Net Salary   : {net:.2f}")
        print("=" * 50)
        input("Press Enter to continue...")

    except Exception as e:
        print("Error:", e)

# Main Menu

while True:
    print("\n" + "=" * 45)
    print("      EMPLOYEE MANAGEMENT SYSTEM")
    print("=" * 45)
    print("1. Show Employee List")
    print("2. Add New Employee")
    print("3. Search Employee")
    print("4. Edit Employee")
    print("5. Delete Employee")
    print("6. Generate Salary Slip")
    print("7. Exit")

    try:
        choice = int(input("Enter your choice : "))

        if choice == 1:
            show_all()
        elif choice == 2:
            add_employee()
        elif choice == 3:
            search_employee()
        elif choice == 4:
            edit_employee()
        elif choice == 5:
            delete_employee()
        elif choice == 6:
            generate_salary_slip()
        elif choice == 0:
            print("Exiting application...")
            cn.close()
            break
        else:
            print("Invalid choice.")

    except ValueError:
        print("Please enter a valid number.")
