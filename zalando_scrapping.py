import requests
from bs4 import BeautifulSoup
import re
import json


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


def construct_url_from_parameters():
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
    return url


def scrap_website(url):
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
    return soup


def find_product_links(soup):
    links = []
    for link in soup.find_all('a'):
        links.append(link.get('href'))
    # if param_brand != '':
    #    param_brand_ = param_brand.replace(".", "|")
    #    pattern = rf'https://www\.zalando\.fr/({param_brand_})-[^\s]+'
    # else:
    # pattern = rf'https://www\.zalando\.fr/[a-zA-Z0-9/-]+\.html\?size={param_size}'
    pattern = rf'https://www\.zalando\.fr/[a-zA-Z0-9/-]+\.html\?size=36'

    # Extract the matching links
    filtered_links = list(filter(re.compile(pattern).match, links))

    # Print the result
    filtered_links = set(filtered_links)
    return filtered_links


def get_products_details(filtered_links):
    soups = []
    for link in filtered_links:
        soups.append(scrap_website(link))
    return soups


def get_price_products(soups):
    prices = []
    for product in soups:
        # Find the meta tag with name="description" and get its content attribute
        description_meta = product.find('meta', {'name': 'description'})
        description_content = description_meta['content']
        # Extract the price from the description content
        price_start_index = description_content.find('pour') + len('pour ')
        price_end_index = description_content.find('€', price_start_index) + 1  # Find the index of '€' and include it
        price = description_content[price_start_index:price_end_index].strip()  # Strip any leading/trailing spaces
        prices.append(price)
        # Replace non-breaking space with a regular space
        prices = [s.replace('\xa0', '') for s in prices]
        return prices


def get_brand_products(soups):
    brands = []
    for product in soups:
        # Find the script tag containing the JSON-like data
        script_tag = product.find('script', class_='re-data-el-init')

        # Extract the JSON-like data from the script tag
        json_data = json.loads(script_tag.string)

        # Extract the brand name handling potential KeyError
        product_info = json_data.get("enrichedRootEntity", {})

        # Splitting the product URI using ':'
        uri_parts = product_info['id'].split(':')

        # The brand is the third element in the split URI
        brand = uri_parts[3].split('-')
        brands.append(brand[0])
    return brands
