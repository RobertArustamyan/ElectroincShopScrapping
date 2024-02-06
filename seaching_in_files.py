import json
import asyncio


async def async_load_and_return_data(file_name: str, category: str = None):
    category_for_file = search_dict_values(file_name, category)

    with open(file_name, 'r', encoding='utf-8') as file:
        all_data = json.load(file)
    if category:
        data = []
        for cat in category_for_file:
            if cat in all_data:
                data.extend(all_data[cat])
        return data
    else:
        return all_data


def search_dict_values(file_name: str, category: str = None):
    if file_name == 'Data/MobileCenterAllData.json':
        cat_dict = {
            'phone': ["PHONE-DATA"],
            'tablet': ["TABLET-DATA"],
            'computer': ["COMPUTER-DATA"],
            'tv': ["TV-DATA"],
            'other': ["WATCH-DATA", "FOTOAPPARATY-DATA", "APPLIANCES-DATA", "OTHER-PRODUCTS-DATA", "ACCESSORIES-DATA"],
        }
        return cat_dict[category]
    elif file_name == 'Data/ZigZagAllData.json':
        cat_dict = {
            'phone': ["PHONES_COMUNICATION"],
            'tablet': ["COMPUTERS_NOTEBOOKS_TABLETS"],
            'computer': ["COMPUTERS_NOTEBOOKS_TABLETS"],
            'tv': ["TV_AUDIO_VIDEO"],
            'other': ["PHONES_COMUNICATION", "HOUSEHOLD_APPLIANCES", "KITCHEN_APPLIANCES", "AIR_CONDITIONING_EQUIPMENT",
                      "COMPUTERS_NOTEBOOKS_TABLETS", "TV_AUDIO_VIDEO"],
        }
        return cat_dict[category]
    elif file_name == 'Data/RedStoreAllData.json':
        cat_dict = {
            'phone': ["PHONE-DATA"],
            'tablet': ["TABLET-DATA"],
            'computer': ["NOTEBOOK-DATA", "COMPUTER-DATA"],
            'tv': ["TV-DATA"],
            'other': ["MONITOR-DATA", "PRINTER-DATA", "SPEAKERS-DATA", "PROEKORY-DATA", "FOTOAPPARATY-DATA",
                      "KONSOLI-DATA"
                      "SDG-DATA", "ROUTER-DATA", "DRON-DATA", "VINTILYATOR-DATA", "APPLIANCES-DATA", "XNAMQI-DATA",
                      "ACCESSORIES-DATA", "OTHER-PRODUCTS-DATA"],
        }
        return cat_dict[category]
    else:
        return category


async def async_load_all_data(category):
    tasks = [
        async_load_and_return_data('Data/MobileCenterAllData.json', category=category),
        async_load_and_return_data('Data/3DPlanet.json'),
        async_load_and_return_data('Data/RedStoreAllData.json', category=category),
        async_load_and_return_data('Data/ZigZagAllData.json', category=category)
    ]

    return await asyncio.gather(*tasks)


async def find_item(data, item_name):
    res = []
    for item in data:
        if item_name.lower() in item['name'].replace(" ", "").lower():
            res.append(item)
    return res


async def getting_result(category, item_name):
    all_data = await async_load_all_data(category)
    res = []
    for data in all_data:
        res.extend(await find_item(data, item_name))
    return res


async def sorting_result(category, item_name, min_value=0, max_value=float('inf')):
    result = await getting_result(category, item_name)
    return_result = []
    for item in result:
        if item['price'] and float(item['price'].replace('.','')) < max_value and float(item['price'].replace('.','')) > min_value:
            return_result.append(item)

    return return_result

if __name__ == "__main__":
    try:
        res = asyncio.run(sorting_result('phone', 'iphone',300000,400000))
        print(res)
    except Exception as e:
        print(f"An error occurred: {e}")
