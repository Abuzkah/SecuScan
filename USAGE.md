# SecuScan Usage Examples

## Install dependencies
pip install -r requirements.txt

## Scan for open ports
python secuscan.py example.com --ports 80 443 8080

## Check HTTP security headers
python secuscan.py example.com --url https://example.com

## Directory brute-forcing
python secuscan.py example.com --url https://example.com --dirb --wordlist wordlist.txt
