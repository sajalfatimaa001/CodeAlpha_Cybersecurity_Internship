"""
INTENTIONALLY INSECURE TRAINING SAMPLE — DO NOT USE IN PRODUCTION.
Run Bandit against this file for the Secure Coding Review assignment.
The unsafe patterns are included only to demonstrate code-review findings.
"""

import os
import pickle
import subprocess

# Finding 1: hard-coded credential (Bandit may report B105).
APP_PASSWORD = "Admin123"

def calculate(expression):
    # Finding 2: eval executes arbitrary Python expressions (Bandit B307).
    return eval(expression)

def show_file(filename):
    # Finding 3: shell=True with user-controlled input can enable command injection
    # (Bandit may report B602).
    subprocess.run("type " + filename, shell=True, check=False)

def load_user_data(filename):
    # Finding 4: unpickling untrusted data can execute code (Bandit B301).
    with open(filename, "rb") as file_handle:
        return pickle.load(file_handle)

def main():
    print("Training sample only. Do not enter real passwords or sensitive data.")
    print("1. Calculate a simple expression")
    print("2. Display a file (unsafe demonstration)")
    choice = input("Choose 1 or 2: ").strip()

    if choice == "1":
        expression = input("Enter an expression: ")
        try:
            print("Result:", calculate(expression))
        except Exception as error:
            print("Calculation failed:", error)
    elif choice == "2":
        filename = input("Enter a file name: ")
        show_file(filename)
    else:
        print("Unknown option.")

if __name__ == "__main__":
    main()
