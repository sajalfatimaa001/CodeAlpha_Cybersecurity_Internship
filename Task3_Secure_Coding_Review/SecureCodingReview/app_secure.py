"""
SECURE REFERENCE VERSION for the Secure Coding Review assignment.
This is a small local demonstration, not a complete production application.
"""

import ast
import os
import subprocess
from pathlib import Path

# Load secrets from the environment; never commit real secrets to source control.
APP_PASSWORD = os.environ.get("APP_PASSWORD")
if not APP_PASSWORD:
    APP_PASSWORD = None  # Configure through the environment when authentication is needed.

# Restrict file access to this application's own "data" directory.
BASE_DIR = (Path(__file__).parent / "data").resolve()

def calculate(expression):
    """Evaluate only numeric arithmetic expressions; reject names and function calls."""
    tree = ast.parse(expression, mode="eval")
    allowed_nodes = (
        ast.Expression, ast.Constant, ast.BinOp, ast.UnaryOp,
        ast.Add, ast.Sub, ast.Mult, ast.Div, ast.FloorDiv, ast.Mod,
        ast.Pow, ast.USub, ast.UAdd,
    )
    for node in ast.walk(tree):
        if not isinstance(node, allowed_nodes):
            raise ValueError("Only basic numeric arithmetic is allowed.")
        if isinstance(node, ast.Constant) and not isinstance(node.value, (int, float)):
            raise ValueError("Only numeric values are allowed.")
    return eval(compile(tree, "<safe-expression>", "eval"), {"__builtins__": {}}, {})

def show_file(filename):
    """Read a file only from the approved data directory."""
    candidate = (BASE_DIR / filename).resolve()
    if BASE_DIR not in candidate.parents:
        raise ValueError("File must be inside the application's data directory.")
    if not candidate.is_file():
        raise FileNotFoundError("Requested file was not found.")
    return candidate.read_text(encoding="utf-8")

def main():
    print("Secure coding demonstration")
    print("1. Calculate a simple arithmetic expression")
    print("2. Read a text file from the local data folder")
    choice = input("Choose 1 or 2: ").strip()

    if choice == "1":
        expression = input("Enter arithmetic (for example 2 + 3 * 4): ")
        try:
            print("Result:", calculate(expression))
        except (SyntaxError, ValueError, TypeError, ZeroDivisionError) as error:
            print("Invalid expression:", error)
    elif choice == "2":
        filename = input("Enter a file name from the data folder: ").strip()
        try:
            print(show_file(filename))
        except (ValueError, FileNotFoundError, OSError) as error:
            print("Could not read file:", error)
    else:
        print("Unknown option.")

if __name__ == "__main__":
    main()
