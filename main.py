import json
import requests
import sys

def make_dict_for_search():
    rus_names = {}
    with open("items.json", "r", encoding="utf-8") as f:
        all_item_list = json.load(f)
        # print(all_item_list[0]["LocalizedNames"])
        for i in range(len(all_item_list)):
            if all_item_list[i]["LocalizedNames"] is None:
                continue
            for item_info in all_item_list[i]["LocalizedNames"]:
                if item_info["Key"] == "RU-RU":
                    rus_names[item_info["Value"]] = all_item_list[i]["UniqueName"]
    return rus_names

def callback():
    print("hi")
# ="T1_FARM_CARROT_SEED"
def make_request_for_data(item_name):
    default_link = "https://www.albion-online-data.com/api/v1/stats/Prices/" 
    server_response = requests.get(default_link + item_name)
    return server_response.json()

def make_cities_list(func, item_name):
    data = func(item_name)
    cities_list = []
    # возможно имеет смысл получившийся словарь сохранять отдельным файлом json 
    # и потом просто проверять его на обновления, 
    # если время пришедшее с сервера больше чем то что у нас есть, 
    # тогда разбирать полученные данные, иначе выводить сообщение, 
    # что данные на серверы пока не обновлены
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
    #надо ли возвращать список городов? подумать тут
    # return cities_list and save it in json file
    with open("carrot_from_request.json", "w") as f:
        f.write(json.dumps(price_dict_by_cities, indent=4))
    return price_dict_by_cities, cities_list

if __name__ == "__main__":
    # z, x = make_cities_list(make_request_for_data, item_name="T1_FARM_CARROT_SEED")
    make_dict_for_search()