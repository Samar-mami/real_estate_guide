def define_search_parameters():
    print("Entering define_search_parameters")
    param_gender = input("Enter gender: ").strip()
    print(f"Gender: {param_gender}")

    param_product = input("Enter product: ").strip()
    print(f"Product: {param_product}")

    param_price_min = input("Enter minimum price: ").strip()
    print(f"Min Price: {param_price_min}")

    param_price_max = -1
    while int(param_price_max) < int(param_price_min):
        param_price_max = input("Enter maximum price: ").strip()
    print(f"Max Price: {param_price_max}")

    param_colour = input("Enter colour(s): ").strip()
    print(f"Colour: {param_colour}")

    param_material = input("Enter material(s): ").strip()
    print(f"Material: {param_material}")

    param_size = input("Enter size(s): ").strip()
    print(f"Size: {param_size}")

    param_brand = input("Enter brand(s): ").strip()
    print(f"Brand: {param_brand}")

    search_parameters = [param_gender, param_product, param_price_min, param_price_max, param_colour, param_material,
                         param_size, param_brand]
    print("Leaving define_search_parameters")
    return search_parameters


def construct_url_from_parameters(search_parameters):
    website_url = 'https://www.zalando.fr/'
    # URL EXAMPLE
    # def scrap_zalando_from_parameters(search_parameters):
    param_gender = search_parameters[0]
    param_product = search_parameters[1]
    param_price_min = search_parameters[2]
    param_price_max = search_parameters[3]
    param_colour = search_parameters[4]
    param_material = search_parameters[5]
    param_size = search_parameters[6]
    param_brand = search_parameters[7]
    url = (
            website_url + param_gender + '/' + param_brand + '_' + param_colour + '_taille-' + param_size + '/?q=' + param_product + '&price_from=' + param_price_min + '&price_to=' + param_price_max + '&upper_material=' + param_material)
    return url

