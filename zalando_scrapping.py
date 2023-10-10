import requests
from bs4 import BeautifulSoup

url = 'https://zalando.fr/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/58.0.3029.110 Safari/537.3'}
cookies = {'cookie_name': 'cookie_value'}
with requests.Session() as session:
    page = session.get(url, headers=headers, cookies=cookies,verify=False)

if page.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(page.content, 'html.parser')

    # Now you can use BeautifulSoup to navigate and extract information from the HTML
    # For example, let's print the title of the page
    title = soup.title
    contents = soup.contents
    print(f'Title: {title.text}')
    print(f'Body: {contents.}')
    #TEstr code
    # You can explore the HTML structure of the page and extract other information as needed

else:
    print(f'Failed to retrieve the page. Status code: {page.status_code}')
