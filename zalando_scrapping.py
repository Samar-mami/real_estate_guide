import requests
from bs4 import BeautifulSoup
import re


def define_search_parameters():
    param_gender = input("Enter gender: ")
    param_product = input("Enter product: ")
    param_price_min = input("Enter minimum price: ")
    param_price_max = input("Enter maximum price: ")
    param_colour = input("Enter colour(s): ")
    param_material = input("Enter material(s): ")
    param_size = input("Enter size(s): ")
    param_brand = input("Enter brand(s): ")
    return param_gender, param_product, param_price_min, param_price_max, param_colour, param_material, param_size, param_brand


search_parameters = define_search_parameters()
# URL EXAMPLE
# def scrap_zalando_from_paramteres(search_parameters):
param_gender = search_parameters[0]
param_product = search_parameters[1]
param_price_min = search_parameters[2]
param_price_max = search_parameters[3]
param_colour = search_parameters[4]
param_material = search_parameters[5]
param_size = search_parameters[6]
param_brand = search_parameters[7]
website_url = 'https://www.zalando.fr/'
url = (website_url + param_gender + '/' + param_brand + '_' + param_colour + '_taille-' + param_size + '/?q=' +
       param_product + '&price_from=' + param_price_min + '&price_to=' + param_price_max + '&upper_material=' +
       param_material)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/58.0.3029.110 Safari/537.3'}
cookies = {'cookie_name': 'cookie_value'}
with requests.Session() as session:
    page = session.get(url, headers=headers, cookies=cookies, verify=False)

if page.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(page.content, 'html.parser')
    # Now you can use BeautifulSoup to navigate and extract information from the HTML
    # For example, let's print the title of the page
    title = soup.title
    print(title.string)
    # You can explore the HTML structure of the page and extract other information as needed
else:
    print(f'Failed to retrieve the page, URL invalid. Status code: {page.status_code}')
  # Manteau En Laine noir, beige, gris GANT, Tommy Hilfiger Taille 36, 38 | Manteaux | Zalando

links = []
for link in soup.find_all('a'):
    links.append(link.get('href'))


if param_brand != '':
    param_brand_ = param_brand.replace(".", "|")
    pattern = rf'https://www\.zalando\.fr/({param_brand_})-[^\s]+'
else:
    pattern = rf'https://www\.zalando\.fr/[a-zA-Z0-9/-]+\.html\?size={param_size}'

# Extract the matching links
filtered_links = list(filter(re.compile(pattern).match, links))

# Print the result
filtered_links = set(filtered_links)
for link in filtered_links:
    print(link)
