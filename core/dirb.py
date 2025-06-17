import requests

def scan(url, wordlist_path):
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
            except:
                continue
    except Exception as e:
        print(f"[!] Wordlist error: {e}")
    return found
