# This is a sample Python script.
from construct_url import define_search_parameters, construct_url_from_parameters
from data_collection_zalando_scrapping import *
from df_csv import *
from data_storage_s3 import *
import boto3


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Welcome to my shopping guide !')
    search_parameters = define_search_parameters()
    print("Search parameters:", search_parameters)
    url = construct_url_from_parameters(search_parameters)
    print("URL:", url)
    soup = scrap_website(url)
    filtered_links = find_product_links(soup)
    print(len(filtered_links))
    soups = get_products_details(filtered_links)
    prices = get_price_products(soups)
    brands = get_brand_products(soups)
    print('filtered_links: ', filtered_links)
    products = create_df_from_links(brands, prices, filtered_links)
    # filepath = r'C:\Users\Jean-francois\Desktop\shopping_guide\zalando.csv'
    bucket = 'shopping-guide-sm'
    filename = 'zalando'
    store_csv_to_s3(bucket, products, filename)
