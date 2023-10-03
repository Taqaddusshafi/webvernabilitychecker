import requests
from bs4 import BeautifulSoup

target_url = "https://example.com"
response = requests.get(target_url)
soup = BeautifulSoup(response.text, 'html.parser')

links = []
for link in soup.find_all('a'):
    links.append(link.get('href'))

vulnerabilities = ["SQL injection", "Cross-Site Scripting (XSS)", "Cross-Site Request Forgery (CSRF)", "Remote File Inclusion", "Local File Inclusion"]

for vulnerability in vulnerabilities:
    if vulnerability.lower() in response.text.lower():
        print(f"Potential {vulnerability} found on {target_url}")

for link in links:
    for vulnerability in vulnerabilities:
        if vulnerability.lower() in link.lower():
            print(f"Potential {vulnerability} found in link: {link}")
