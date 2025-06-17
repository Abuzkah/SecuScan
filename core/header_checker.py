import requests
from rich.console import Console

console = Console()

REQUIRED_HEADERS = [
    "Content-Security-Policy",
    "X-Content-Type-Options",
    "Strict-Transport-Security",
    "X-Frame-Options",
    "Referrer-Policy",
    "Permissions-Policy"
]

def check(url):
    try:
        resp = requests.get(url, timeout=5)
        headers = resp.headers
        missing = [h for h in REQUIRED_HEADERS if h not in headers]
        return missing
    except Exception as e:
        console.print(f"[red]Header check failed: {e}[/red]")
        return []
