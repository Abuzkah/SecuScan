# SecuScan

SecuScan is a Python command-line tool that scans a target website or IP for common web vulnerabilities, including:
- Open ports (Nmap-lite)
- HTTP headers misconfigurations
- Outdated server software (optional)
- Directory brute-forcing (like dirb)
- Basic SQLi/XSS pattern detection (optional)

## Features
1. **Port Scanner**: Scan for open ports and display basic service info.
2. **HTTP Security Headers Check**: Check for missing security headers.
3. **Directory/File Enumeration**: Brute-force common files/dirs using a wordlist.
4. **(Optional) Outdated Software & Pattern-based Scanning**: Detect outdated server software, XSS, and SQLi patterns.

## Usage
1. Install dependencies: `pip install -r requirements.txt`
2. Run: `python secuscan.py --help`

## Requirements
- Python 3.8+
- See `requirements.txt` for dependencies

## Roadmap
- Add logging and PDF/HTML report generation
- Add advanced vulnerability checks
