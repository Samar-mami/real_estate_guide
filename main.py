# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from df_csv import *
import boto3

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    search_parameters = define_search_parameters()
    print("Search parameters:", search_parameters)
    url = construct_url_from_parameters(search_parameters)
    print("URL:", url)
    soup = scrap_website(url)
    filtered_links = find_product_links(soup)
    print(len(filtered_links))
    soups = get_products_details(filtered_links)
    prices = get_price_products(soups)
    print('prices: ', prices)
    print(len(prices))
    brands = get_brand_products(soups)
    print('brands: ', brands)
    print(len(brands))
    print('filtered_links: ', filtered_links)
    print(len(filtered_links))
    products = create_df_from_links(brands, prices, filtered_links)
    print(type(products))
    # filepath = r'C:\Users\Jean-francois\Desktop\shopping_guide\zalando.csv'
    store_df_to_csv(r'C:\Users\Jean-francois\Desktop\shopping_guide\zalando.csv', products)
