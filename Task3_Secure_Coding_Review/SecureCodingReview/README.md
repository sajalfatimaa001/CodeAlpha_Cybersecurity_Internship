# Task 3 — Secure Coding Review

## Project overview
This project demonstrates a secure code review of a small Python application.
It contains:
- `app_insecure.py`: intentionally vulnerable training sample. **Do not deploy or use with real data.**
- `app_secure.py`: safer reference implementation showing remediation.
- `SECURITY_REVIEW.md`: findings, risk explanations, and remediation notes.

## Requirements
- Python 3.9 or newer
- Bandit (static security analyzer)

## Setup (Windows)
Open Command Prompt in this folder and run:

```cmd
py --version
py -m venv .venv
.venv\Scripts\activate
py -m pip install --upgrade pip
py -m pip install bandit
```

## Run the static analysis
Scan the intentionally vulnerable sample:

```cmd
bandit -r app_insecure.py -f txt
```

Save a report to a file:

```cmd
bandit -r app_insecure.py -f json -o bandit-report.json
```

Then scan the safer version:

```cmd
bandit -r app_secure.py -f txt
```

Bandit results can vary slightly by version and configuration. Review every finding manually;
a scanner result is an indicator, not proof that code is exploitable or safe.

## Run the safe demonstration
```cmd
py app_secure.py
```

The file-reading example expects files to be placed inside a `data` folder beside the script.
Do not put secrets or sensitive files in the demo folder.

## Suggested evidence screenshots
1. `py --version` showing the installed Python version.
2. `bandit -r app_insecure.py -f txt` showing findings.
3. `bandit -r app_secure.py -f txt` showing the rescan.
4. `py app_secure.py` showing a normal arithmetic calculation and a rejected unsafe expression.

## Important
The insecure file is deliberately unsafe and is included only for static analysis and classroom review.
Do not run it with untrusted input, do not expose it to a network, and do not use it in production.
