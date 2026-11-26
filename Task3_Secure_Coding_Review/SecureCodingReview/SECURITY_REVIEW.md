# Secure Coding Review — Task 3

## 1. Scope
**Language:** Python  
**Application:** A small command-line demonstration application  
**Review methods:** Manual source inspection and Bandit static analysis  
**Files reviewed:** `app_insecure.py` and the remediated reference `app_secure.py`

The insecure file is intentionally created for this training exercise. It should not be deployed or used with real credentials, files, or untrusted input.

## 2. Findings and recommendations

| ID | Issue | Risk | Recommended remediation |
|---|---|---|---|
| SCR-01 | Hard-coded password (`APP_PASSWORD`) | Secrets can be exposed through source control, backups, or shared code. | Remove credentials from source. Load secrets from a managed secret store or environment configuration; rotate any exposed secret. |
| SCR-02 | Use of `eval()` on user input | An attacker may cause unintended Python code execution. | Avoid `eval`. Parse a narrowly defined expression grammar and allow only expected AST node types. |
| SCR-03 | `subprocess.run(..., shell=True)` with input | Shell metacharacters in input may alter the command being executed. | Avoid a shell. Pass a list of arguments to `subprocess.run`, validate inputs, and use least privilege. |
| SCR-04 | `pickle.load()` on a file | Loading untrusted pickle data can execute attacker-controlled code. | Do not unpickle untrusted data. Use a data-only format such as JSON and validate its schema. |

## 3. Static analysis procedure
Install and run Bandit from the project directory:

```cmd
py -m pip install bandit
bandit -r app_insecure.py -f txt
bandit -r app_secure.py -f txt
```

Bandit commonly associates the sample patterns with checks such as B105 (hard-coded password string), B307 (`eval`), B602 (subprocess with shell), and B301 (pickle load). Exact output depends on the installed Bandit version and configuration. Run the commands and attach the actual terminal output as evidence; this document does not claim that a scan was executed on your computer.

## 4. Remediation summary
- Removed the hard-coded credential value; configuration is read from the environment.
- Replaced unrestricted expression evaluation with a restricted arithmetic-expression parser and an empty built-ins environment.
- Removed shell-based command execution from the safer example.
- Removed unsafe pickle deserialization from the safer example.
- Restricted demonstration file reads to a dedicated local data directory.

## 5. Additional secure coding best practices
1. Validate all input on the server or trusted application boundary.
2. Apply least privilege to processes, files, and accounts.
3. Keep dependencies updated and review their security advisories.
4. Do not log passwords, tokens, or other sensitive information.
5. Use parameterized database queries rather than building SQL strings.
6. Handle errors without exposing stack traces or internal secrets to users.
7. Add automated tests for validation, authorization, and error cases.
8. Require peer review before deploying security-sensitive changes.

## 6. Conclusion
The review identified four common insecure coding patterns in the intentionally vulnerable training sample. The safer reference version demonstrates practical mitigations. Before submission, execute the Bandit commands locally, save the real scan output, and include screenshots of the vulnerable scan and the rescan.

## 7. Evidence checklist
- [ ] Python version screenshot
- [ ] Bandit installation screenshot
- [ ] Bandit output for `app_insecure.py`
- [ ] Bandit output for `app_secure.py`
- [ ] Safe application execution screenshot
