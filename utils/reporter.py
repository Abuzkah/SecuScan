import json

def save(results, filename):
    try:
        with open(filename, 'w') as f:
            json.dump(results, f, indent=4)
    except Exception as e:
        print(f"[!] Failed to save report: {e}")
