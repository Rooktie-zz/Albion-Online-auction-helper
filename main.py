import json
import requests
import sys

def make_dict_for_search():
    """
        makes russian localized dict with items and their id's
    """
    rus_names = {}
    data_of_all_tems_from_api = requests.get(
        "https://raw.githubusercontent.com/broderickhyman/ao-bin-dumps/master/formatted/items.json"
        ).json()
    for i in range(len(data_of_all_tems_from_api)):
        if data_of_all_tems_from_api[i]["LocalizedNames"] is None:
            continue
        for item_info in data_of_all_tems_from_api[i]["LocalizedNames"]:
            if item_info["Key"] == "RU-RU":
                rus_names[item_info["Value"]] = data_of_all_tems_from_api[i]["UniqueName"]
    return rus_names

def make_request_for_data(item_name):
    """
        make request to server by item name 
        and return info we need to know about this element in json format
    """
    default_link = "https://www.albion-online-data.com/api/v1/stats/Prices/" 
    server_response = requests.get(default_link + item_name)
    return server_response.json()

def make_cities_list(func, item_name):
    """
        return prices of item separate by cities
        and cities list
    """
    data = func(item_name)
    cities_list = []
    price_dict_by_cities = {}
    for item in data:
        if "Cross" in item["city"]:
            continue
        if "0" in item["city"]:
            continue
        cities_list.append(item["city"])
        price_dict_by_cities[item["city"]] = {
            "sell_price_min": item["sell_price_min"],
            "sell_price_max": item["sell_price_max"],
            "buy_price_min": item["buy_price_min"],
            "buy_price_max": item["buy_price_max"],
        }
    with open("carrot_from_request.json", "w") as f:
        f.write(json.dumps(price_dict_by_cities, indent=4))
    return price_dict_by_cities, cities_list