import requests
from bs4 import BeautifulSoup

target_url = "https://taqaddusshafi.github.io/"
response = requests.get(target_url)
soup = BeautifulSoup(response.text, 'html.parser')

vulnerabilities = {
    "SQL injection": False,
    "Cross-Site Scripting (XSS)": False,
    "Cross-Site Request Forgery (CSRF)": False,
    "Remote File Inclusion": False,
    "Local File Inclusion": False
}

for vulnerability in vulnerabilities.keys():
    if vulnerability.lower() in response.text.lower():
        vulnerabilities[vulnerability] = True

print("Vulnerabilities found on", target_url + ":")
for vulnerability, found in vulnerabilities.items():
    if found:
        print(f"- {vulnerability}: Found")
    else:
        print(f"- {vulnerability}: Not Found")
