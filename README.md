# 🔒 SecuScan – Modular Web Vulnerability Scanner

**SecuScan** is a beginner-friendly but powerful web security scanner written in Python. It helps ethical hackers, cybersecurity students, and developers perform essential vulnerability checks on web services.

---

## ✨ Features

- 🔍 **Port Scanning** – Detects open TCP ports.
- 🛡️ **HTTP Security Header Checker** – Identifies missing best-practice headers.
- 📂 **Directory Brute-forcing** – Discovers hidden directories/files using wordlists.
- 📄 **Report Generation** – Save your scan results to a JSON file.
- 🧱 Modular codebase – Easily extensible for more scans.

---

## 📁 Project Structure

```
secuscan/
├── core/
│   ├── port_scanner.py        # Handles TCP port scanning
│   ├── header_checker.py      # Checks for HTTP security headers
│   ├── dirb.py                # Brute-forces common directories
├── utils/
│   ├── reporter.py            # Saves reports to JSON
│   ├── validator.py           # Validates URLs
├── wordlists/
│   └── common.txt             # Wordlist for dirb scan
├── main.py                    # Entry point CLI app
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Installation

```bash
git clone https://github.com/yourusername/secuscan.git
cd secuscan
pip install -r requirements.txt
```

---

## ⚙️ Usage

### Port Scan
```bash
python main.py example.com --ports 80 443 22
```

### HTTP Header Check
```bash
python main.py example.com --url https://example.com
```

### Directory Brute-force (with custom wordlist)
```bash
python main.py example.com --url https://example.com --dirb --wordlist wordlists/common.txt
```

### Save Results to JSON
```bash
python main.py example.com --url https://example.com --report results.json
```

---

## ✅ Recommended Headers Checked

- Content-Security-Policy
- X-Content-Type-Options
- Strict-Transport-Security
- X-Frame-Options
- Referrer-Policy
- Permissions-Policy

---

## 📚 Example Output

| Type       | Example               |
|------------|------------------------|
| Ports      | `22, 80, 443`          |
| Headers    | `Missing: CSP, HSTS`   |
| Directories| `/admin`, `/login`     |

---

## 🧠 Notes

- Make sure the target allows scanning (don't break laws).
- Extend the tool by adding more modules under `/core`.

---

## 🧑‍💻 Author

**Your Name** – [@yourhandle](https://github.com/yourusername)

---

## 📄 License

MIT – do what you want with it, but no liability.

