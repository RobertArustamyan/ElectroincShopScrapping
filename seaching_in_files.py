import json
import asyncio

async def async_load_and_return_data(file_name: str, category: str = None):
    category_for_file = search_dict_values(file_name, category)

    with open(file_name, 'r',encoding='utf-8') as file:
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
    if file_name == 'MobileCenterAllData.json':
        cat_dict = {
            'phone': ["PHONE-DATA"],
            'tablet': ["TABLET-DATA"],
            'computer': ["COMPUTER-DATA"],
            'tv': ["TV-DATA"],
            'other': ["WATCH-DATA", "FOTOAPPARATY-DATA", "APPLIANCES-DATA", "OTHER-PRODUCTS-DATA", "ACCESSORIES-DATA"],
        }
        return cat_dict[category]
    elif file_name == 'ZigZagAllData.json':
        cat_dict = {
            'phone': ["PHONES_COMUNICATION"],
            'tablet': ["COMPUTERS_NOTEBOOKS_TABLETS"],
            'computer': ["COMPUTERS_NOTEBOOKS_TABLETS"],
            'tv': ["TV_AUDIO_VIDEO"],
            'other': ["PHONES_COMUNICATION", "HOUSEHOLD_APPLIANCES", "KITCHEN_APPLIANCES", "AIR_CONDITIONING_EQUIPMENT",
                      "COMPUTERS_NOTEBOOKS_TABLETS", "TV_AUDIO_VIDEO"],
        }
        return cat_dict[category]
    elif file_name == 'RedStoreAllData.json':
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
        async_load_and_return_data('MobileCenterAllData.json', category=category),
        async_load_and_return_data('3DPlanet.json'),
        async_load_and_return_data('RedStoreAllData.json', category=category),
        async_load_and_return_data('ZigZagAllData.json', category=category)
    ]

    return await asyncio.gather(*tasks)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(async_load_all_data('phone'))
    print(result)
