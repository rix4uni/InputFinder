import requests
from bs4 import BeautifulSoup
import concurrent.futures
import argparse
import random
import sys

def get_inputs(url):
    # Make a request to the URL
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0.2 Safari/604.4.7",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1",
        "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15",
        "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3 Edge/16.16299",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1",
        "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"
    ]
    headers = {"User-Agent": random.choice(user_agents)}
    response = requests.get(url, headers=headers)

    # Parse the HTML of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the input fields of type "text"
    text_inputs = soup.find_all('input', {'type': 'text'})

    # Find the input fields of type "email"
    email_inputs = soup.find_all('input', {'type': 'email'})

    # Find the input fields of type "password"
    password_inputs = soup.find_all('input', {'type': 'password'})

    # Find the input fields of type "textarea"
    comments_inputs = soup.find_all('textarea')

    # Find the input fields of type "search"
    search_inputs = soup.find_all('input', {'type': 'search'})

    # Create a list to store the id and name values of the input fields
    name_values = []

    for input in text_inputs:
        name_values.append((f"id={input.get('id')}", f"name={input.get('name')}"))
    for input in email_inputs:
        name_values.append((f"id={input.get('id')}", f"name={input.get('name')}"))
    for input in password_inputs:
        name_values.append((f"id={input.get('id')}", f"name={input.get('name')}"))
    for input in comments_inputs:
        name_values.append((f"id={input.get('id')}", f"name={input.get('name')}"))
    for input in search_inputs:
        name_values.append((f"id={input.get('id')}", f"name={input.get('name')}"))

    name_values.sort()
    return name_values

parser = argparse.ArgumentParser()
parser.add_argument('--threads', type=int, default=8, help='Number of threads to use')
args = parser.parse_args()

# Read the input URLs from sys.stdin
url_list = sys.stdin.read().splitlines()

with concurrent.futures.ThreadPoolExecutor(max_workers=args.threads) as executor:
    for url in url_list:
        results = executor.map(get_inputs, [url])
        name_values = [result for result in results]
        print(f"{url}: {name_values}")