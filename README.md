````markdown
# 🛡️ SecuScan – Lightweight Python Web Vulnerability Scanner

SecuScan is a beginner-friendly, Python-based vulnerability scanner designed to identify common web and network security issues. It's ideal for ethical hackers, security enthusiasts, and students looking to learn practical cybersecurity scanning techniques.

---

## 🚀 Features

- ✅ **Port Scanning** (Top 15 common ports)
- ✅ **HTTP Security Header Checker**
- ✅ **Directory Bruteforcing**
- 🧪 Optional: Banner grabbing, basic SQLi/XSS detection (coming soon)

---

## 🛠️ Tech Stack

- Python 3
- `socket` – for network scans
- `requests` – for HTTP checks
- `threading` – for parallel port scanning

---

## 📸 Demo

![screenshot](screenshots/secuscan-demo.png)

---

## 📥 Installation

```bash
git clone https://github.com/yourusername/secuscan.git
cd secuscan
pip install -r requirements.txt
````

---

## 🧪 Usage

```bash
python secuscan.py
```

**Input formats:**

* For **HTTP checks**: `https://example.com`
* For **Port scanning**: `example.com` or IP `192.168.1.1`

---

## 🧠 How It Works

| Module         | Description                               |
| -------------- | ----------------------------------------- |
| Port Scanner   | Scans 15+ top ports, checks for openness  |
| Header Check   | Audits missing HTTP security headers      |
| Dir Bruteforce | Tries to discover common hidden endpoints |

---

## 🔒 Ethical Use Only

> ⚠️ **This tool is intended for legal, educational, and authorized testing purposes only.** Do **not** scan systems you don’t own or have explicit permission to audit.

---

## 🌱 TODO

* [ ] Add banner grabbing
* [ ] Export results to PDF/HTML
* [ ] Add advanced vulnerability checks (e.g., XSS, SQLi)
* [ ] Add Shodan API integration
* [ ] Build Flask web interface

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**\[ABUBAKAR NASTEH]**
🔗 [yourportfolio.com](https://yourportfolio.com)
🐦 [@yourhandle](https://twitter.com/skycrue44)
📧 [your.email@example.com](mailto:your.email@example.com)

---

## ⭐️ Support

If you find this project helpful, please ⭐ the repo to support ongoing development!

```

---
