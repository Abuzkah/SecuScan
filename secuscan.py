import argparse
import socket
import requests
from rich.console import Console
from rich.table import Table

console = Console()

def scan_ports(target, ports):
    console.print(f"[bold cyan]Scanning ports on {target}...[/bold cyan]")
    open_ports = []
    for port in ports:
        try:
            with socket.create_connection((target, port), timeout=1) as s:
                open_ports.append(port)
        except Exception:
            continue
    return open_ports

def check_http_headers(url):
    console.print(f"[bold cyan]Checking HTTP security headers for {url}...[/bold cyan]")
    try:
        resp = requests.get(url, timeout=5)
        headers = resp.headers
        required = [
            "Content-Security-Policy",
            "X-Content-Type-Options",
            "Strict-Transport-Security",
            "X-Frame-Options"
        ]
        missing = [h for h in required if h not in headers]
        return missing
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        return []

def dir_bruteforce(url, wordlist_path):
    console.print(f"[bold cyan]Starting directory brute-force on {url}...[/bold cyan]")
    found = []
    try:
        with open(wordlist_path, 'r') as f:
            words = [line.strip() for line in f if line.strip()]
        for word in words:
            test_url = url.rstrip('/') + '/' + word
            try:
                resp = requests.get(test_url, timeout=3)
                if resp.status_code < 400:
                    found.append((test_url, resp.status_code))
            except Exception:
                continue
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
    return found

def main():
    parser = argparse.ArgumentParser(description="SecuScan: Basic Web Vulnerability Scanner")
    parser.add_argument("target", help="Target IP or domain (e.g., example.com)")
    parser.add_argument("--ports", nargs="*", type=int, default=[80, 443, 21, 22, 8080], help="Ports to scan")
    parser.add_argument("--url", help="Target URL for HTTP header check (e.g., https://example.com)")
    parser.add_argument("--dirb", action="store_true", help="Enable directory brute-forcing (requires --url)")
    parser.add_argument("--wordlist", default="wordlist.txt", help="Path to wordlist for dir brute-forcing")
    args = parser.parse_args()

    if args.ports:
        open_ports = scan_ports(args.target, args.ports)
        table = Table(title="Open Ports")
        table.add_column("Port", justify="right")
        for port in open_ports:
            table.add_row(str(port))
        console.print(table)

    if args.url:
        missing = check_http_headers(args.url)
        if missing:
            console.print(f"[yellow]Missing headers: {', '.join(missing)}[/yellow]")
        else:
            console.print("[green]All required headers present![/green]")

        if args.dirb:
            found = dir_bruteforce(args.url, args.wordlist)
            if found:
                table = Table(title="Discovered Paths")
                table.add_column("URL")
                table.add_column("Status Code")
                for url, code in found:
                    table.add_row(url, str(code))
                console.print(table)
            else:
                console.print("[yellow]No directories/files found from wordlist.[/yellow]")

if __name__ == "__main__":
    main()
