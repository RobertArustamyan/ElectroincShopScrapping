import requests
from bs4 import BeautifulSoup
import os
from firebase_admin import credentials, db, initialize_app
from dotenv import load_dotenv
class ZigZagReq:
    cookies = {
        'section_data_ids': '%7B%7D',
        '_gcl_au': '1.1.382139865.1706537126',
        '_gid': 'GA1.2.231880980.1706537131',
        '_fbp': 'fb.1.1706537131127.1121472335',
        'PHPSESSID': '8ivtsomn40cjteah5hvdagepqg',
        'wp_ga4_customerGroup': 'NOT%20LOGGED%20IN',
        'form_key': 'jmbgjcWqMpxlNpVP',
        'mage-cache-storage': '%7B%7D',
        'mage-cache-storage-section-invalidation': '%7B%7D',
        'mage-cache-sessid': 'true',
        'mage-messages': '',
        'recently_viewed_product': '%7B%7D',
        'recently_viewed_product_previous': '%7B%7D',
        'recently_compared_product': '%7B%7D',
        'recently_compared_product_previous': '%7B%7D',
        'product_data_storage': '%7B%7D',
        'form_key': 'jmbgjcWqMpxlNpVP',
        'section_data_ids': '%7B%22messages%22%3A1706537628%2C%22customer%22%3A1706537628%2C%22compare-products%22%3A1706537628%2C%22last-ordered-items%22%3A1706537628%2C%22cart%22%3A1706537628%2C%22directory-data%22%3A1706537628%2C%22captcha%22%3A1706537628%2C%22instant-purchase%22%3A1706537628%2C%22loggedAsCustomer%22%3A1706537628%2C%22persistent%22%3A1706537628%2C%22review%22%3A1706537628%2C%22wishlist%22%3A1706537628%2C%22wp_ga4%22%3A1706537628%2C%22recently_viewed_product%22%3A1706537628%2C%22recently_compared_product%22%3A1706537628%2C%22product_data_storage%22%3A1706537628%2C%22paypal-billing-agreement%22%3A1706537628%7D',
        '_gat_UA-1987183-2': '1',
        'private_content_version': 'dfd989eb18e2f19f7c5884f8717e87e6',
        '_gat': '1',
        '_ga_8JGPSHQL41': 'GS1.1.1706537068.1.1.1706537784.56.0.0',
        '_gat_gtag_UA_164782692_1': '1',
        '_ga': 'GA1.1.751115414.1706537068',
        '_ga_LWC5Z1FS0R': 'GS1.1.1706537156.1.1.1706537784.0.0.0',
        '_ga_0PL6B4SSLB': 'GS1.1.1706537068.1.1.1706537787.0.0.0',
    }
    headers = {
        'authority': 'www.zigzag.am',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        # 'cookie': 'section_data_ids=%7B%7D; _gcl_au=1.1.382139865.1706537126; _gid=GA1.2.231880980.1706537131; _fbp=fb.1.1706537131127.1121472335; PHPSESSID=8ivtsomn40cjteah5hvdagepqg; wp_ga4_customerGroup=NOT%20LOGGED%20IN; form_key=jmbgjcWqMpxlNpVP; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; mage-cache-sessid=true; mage-messages=; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; form_key=jmbgjcWqMpxlNpVP; section_data_ids=%7B%22messages%22%3A1706537628%2C%22customer%22%3A1706537628%2C%22compare-products%22%3A1706537628%2C%22last-ordered-items%22%3A1706537628%2C%22cart%22%3A1706537628%2C%22directory-data%22%3A1706537628%2C%22captcha%22%3A1706537628%2C%22instant-purchase%22%3A1706537628%2C%22loggedAsCustomer%22%3A1706537628%2C%22persistent%22%3A1706537628%2C%22review%22%3A1706537628%2C%22wishlist%22%3A1706537628%2C%22wp_ga4%22%3A1706537628%2C%22recently_viewed_product%22%3A1706537628%2C%22recently_compared_product%22%3A1706537628%2C%22product_data_storage%22%3A1706537628%2C%22paypal-billing-agreement%22%3A1706537628%7D; _gat_UA-1987183-2=1; private_content_version=dfd989eb18e2f19f7c5884f8717e87e6; _gat=1; _ga_8JGPSHQL41=GS1.1.1706537068.1.1.1706537784.56.0.0; _gat_gtag_UA_164782692_1=1; _ga=GA1.1.751115414.1706537068; _ga_LWC5Z1FS0R=GS1.1.1706537156.1.1.1706537784.0.0.0; _ga_0PL6B4SSLB=GS1.1.1706537068.1.1.1706537787.0.0.0',
        'referer': 'https://www.zigzag.am/am/phones-and-communication.html?p=5&product_list_mode=list',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }
    params = {
        'product_list_mode': 'list'
    }

    def making_resopnse(self, page, url):
        self.params['p'] = str(page)
        return requests.get(url, params=self.params, cookies=self.cookies, headers=self.headers)

    def getting_data(self, page, category):
        url = f'https://www.zigzag.am/am/{category}'
        products = []
        for i in range(1, page + 1):
            response = self.making_resopnse(i, url)
            if response.status_code == 200:
                print(f"{url} - {i}")

                soup = BeautifulSoup(response.text, 'lxml')
                items = soup.find_all('div', class_='block_inner product-item-details')
                for item in items:
                    product = {}

                    item_category = item.find('div', class_='product_category')
                    if item_category:
                        product['item_category'] = item_category.text
                    else:
                        product['item_category'] = None

                    item_link_name = item.find('a', class_='product_name combo_link')
                    if item_link_name:
                        product['name'] = item_link_name.text.split('\n')[1]
                        product['link'] = item_link_name.get('href')
                    else:
                        product['name'] = None
                        product['link'] = None

                    item_price = item.find('span', class_='price')
                    if item_price:
                        product['price'] = item_price.text.split(' ')[0].replace(',', '.')
                    else:
                        product['price'] = None

                    products.append(product)

        return products

    def getting_all_data(self):
        tv_audio_video = self.getting_data(56, 'tv-audio-video.html')
        computers_notebooks_tablets = self.getting_data(85, 'computers-notebooks-tablets.html')
        phones_comunication = self.getting_data(81, 'phones-and-communication.html')
        household_appliances = self.getting_data(44, 'household-appliances.html')
        kitchen_appliances = self.getting_data(63, 'kitchen-appliances.html')
        air_conditioning_equipment = self.getting_data(21 ,'air-conditioning-equipment.html')

        return {
            "TV_AUDIO_VIDEO" : tv_audio_video,
            "COMPUTERS_NOTEBOOKS_TABLETS" : computers_notebooks_tablets,
            "PHONES_COMUNICATION" : phones_comunication,
            "HOUSEHOLD_APPLIANCES" : household_appliances,
            "KITCHEN_APPLIANCES" : kitchen_appliances,
            "AIR_CONDITIONING_EQUIPMENT" : air_conditioning_equipment
        }

class RedStoreReq:
    cookies = {
        'PHPSESSID': 't4bq5sjdrasldap0cj95tlte25',
        'u2id': '-4150598',
        '_ga': 'GA1.2.2063571743.1706538663',
        '_gid': 'GA1.2.658331147.1706538663',
        '_ym_uid': '1706538669857965908',
        '_ym_d': '1706538669',
        '_ym_isad': '2',
        '_ym_visorc': 'w',
        'url': 'shop%2Fcategory%2Fcategories%2Fsmartfony',
        '_gat': '1',
        '_ga_W55CRBY06M': 'GS1.2.1706543578.2.1.1706543849.0.0.0',
    }
    headers = {
        'authority': 'redstore.am',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        # 'cookie': 'PHPSESSID=t4bq5sjdrasldap0cj95tlte25; u2id=-4150598; _ga=GA1.2.2063571743.1706538663; _gid=GA1.2.658331147.1706538663; _ym_uid=1706538669857965908; _ym_d=1706538669; _ym_isad=2; _ym_visorc=w; url=shop%2Fcategory%2Fcategories%2Fsmartfony; _gat=1; _ga_W55CRBY06M=GS1.2.1706543578.2.1.1706543849.0.0.0',
        'referer': 'https://redstore.am/shop/category/categories/smartfony?per_page=552',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }
    params = {}
    requests_url = None

    def url_for_category(self, category):
        self.requests_url = f'https://redstore.am/shop/category/categories/{category}'

    # Request
    def making_request(self, page):
        self.params['per_page'] = str(page)
        return requests.get(self.requests_url, params=self.params, cookies=self.cookies, headers=self.headers)

    def getting_data(self, page_count, IT_name):
        products = []
        for i in range(0, page_count + 1, 12):
            print(f"{IT_name} PAGE {i // 12}")
            response = self.making_request(i)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'lxml')
                # All cards
                items = soup.find_all('li', class_='globalFrameProduct to-cart')
                for item in items:
                    product_data = {}
                    # name
                    item_name = item.find('a', class_='frame-photo-title')
                    if item_name:
                        product_data['name'] = item_name.get('title')
                        product_data['link'] = item_name.get('href')
                    else:
                        product_data['name'] = None
                        product_data['link'] = None

                    # price
                    item_price = item.find('span', class_='price priceCashVariant')
                    if item_price:
                        product_data['price'] = item_price.text
                    else:
                        product_data['price'] = None
                    products.append(product_data)
            else:
                print(f"No response from page {i // 12}")
                products.append({"page": i // 12, "data": None})
        return products

    def getting_all_data(self):
        self.url_for_category('smartfony')
        phone_data = self.getting_data(552, 'smartfony')

        self.url_for_category('tablets')
        tablet_data = self.getting_data(120, 'tablets')

        self.url_for_category('watches')
        watch_data = self.getting_data(72, 'watches')

        self.url_for_category('notebooks')
        notebook_data = self.getting_data(240, 'notebooks')

        self.url_for_category('computers')
        computer_data = self.getting_data(108, 'computers')

        self.url_for_category('monitors')
        monitor_data = self.getting_data(48, 'monitors')

        self.url_for_category('tv')
        tv_data = self.getting_data(72, 'tv')

        self.url_for_category('printery')
        printer_data = self.getting_data(36, 'printery')

        self.url_for_category('Speakers')
        speakers_data = self.getting_data(168, 'Speakers')

        self.url_for_category('proektory')
        proektory_data = self.getting_data(36, 'proektory')

        self.url_for_category('zerkalnye-fotoapparaty')
        fotoapparaty_data = self.getting_data(60, 'zerkalnye-fotoapparaty')

        self.url_for_category('igrovye-konsoli')
        konsoli_data = self.getting_data(72, 'igrovye-konsoli')

        self.url_for_category('sdg')
        sdg_data = self.getting_data(0, 'sdg')

        self.url_for_category('54')
        router_data = self.getting_data(24, '54')

        self.url_for_category('dronys')
        dron_data = self.getting_data(0, 'dronys')

        self.url_for_category('l')
        vintilyator_data = self.getting_data(60, 'l')

        self.url_for_category('Appliances')
        appliances_data = self.getting_data(324, 'Appliances')

        self.url_for_category('f')
        xnamqi_data = self.getting_data(84, 'f')

        self.url_for_category('accessories')
        accessories_data = self.getting_data(1644, 'accessories')

        self.url_for_category('other-products')
        other_products_data = self.getting_data(96, 'other-products')

        return {
            "PHONE-DATA": phone_data,
            "TABLET-DATA": tablet_data,
            "WATCH-DATA": watch_data,
            "NOTEBOOK-DATA": notebook_data,
            "COMPUTER-DATA": computer_data,
            "MONITOR-DATA": monitor_data,
            "TV-DATA": tv_data,
            "PRINTER-DATA": printer_data,
            "SPEAKERS-DATA": speakers_data,
            "PROEKORY-DATA": proektory_data,
            "FOTOAPPARATY-DATA": fotoapparaty_data,
            "KONSOLI-DATA": konsoli_data,
            "SDG-DATA": sdg_data,
            "ROUTER-DATA": router_data,
            "DRON-DATA": dron_data,
            "VINTILYATOR-DATA": vintilyator_data,
            "APPLIANCES-DATA": appliances_data,
            "XNAMQI-DATA": xnamqi_data,
            "ACCESSORIES-DATA": accessories_data,
            "OTHER-PRODUCTS-DATA": other_products_data,
        }


class MobileCenterReq:
    cookies = {
        'PHPSESSID': 'ge1gtdfcpesc97qbki08san446',
        '_gid': 'GA1.2.304375013.1706698525',
        'twk_idm_key': 'gqMOe4Gd7hj4mFQQz1e6a',
        '_ga_H6H0DTRSD9': 'GS1.1.1706698524.1.1.1706698627.0.0.0',
        '_ga': 'GA1.2.2012551776.1706698525',
        'TawkConnectionTime': '0',
        'twk_uuid_5f16133c7258dc118bee9cff': '%7B%22uuid%22%3A%221.WrubhMozqHDTp4cHWiFnCkmLU7uzcOQDEoeNFtEk8gEpJgyxNudlZnHZqqdGsbIKhlzL8mdyVx3s6WtyHuRqWi5ph1GiM2WN0V2pEo4Dl0K6XWzEbQQfPx05M%22%2C%22version%22%3A3%2C%22domain%22%3A%22mobilecentre.am%22%2C%22ts%22%3A1706698628408%7D',
    }

    headers = {
        'authority': 'www.mobilecentre.am',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        # 'cookie': 'PHPSESSID=ge1gtdfcpesc97qbki08san446; _gid=GA1.2.304375013.1706698525; twk_idm_key=gqMOe4Gd7hj4mFQQz1e6a; _ga_H6H0DTRSD9=GS1.1.1706698524.1.1.1706698627.0.0.0; _ga=GA1.2.2012551776.1706698525; TawkConnectionTime=0; twk_uuid_5f16133c7258dc118bee9cff=%7B%22uuid%22%3A%221.WrubhMozqHDTp4cHWiFnCkmLU7uzcOQDEoeNFtEk8gEpJgyxNudlZnHZqqdGsbIKhlzL8mdyVx3s6WtyHuRqWi5ph1GiM2WN0V2pEo4Dl0K6XWzEbQQfPx05M%22%2C%22version%22%3A3%2C%22domain%22%3A%22mobilecentre.am%22%2C%22ts%22%3A1706698628408%7D',
        'referer': 'https://www.mobilecentre.am/',
        'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    }

    def url_for_category(self, category):
        return f'https://www.mobilecentre.am/category/{category}'

    def getting_data(self, category):
        url = self.url_for_category(category)
        response = requests.get(url, cookies=self.cookies, headers=self.headers)
        if response.status_code == 200:
            products = []
            soup = BeautifulSoup(response.text, 'lxml')
            items = soup.find_all('div', class_='listitem')
            for item in items:
                product = {}

                item_name = item.find('h3')
                if item_name:
                    product['name'] = item_name.text
                else:
                    product['name'] = None

                item_link = item.find('a', class_='prod-item-img')
                if item_link:
                    product['link'] = item_link.get('href')
                else:
                    product['link'] = None

                item_price = item.find('span', class_='regular')
                if item_price:
                    product['price'] = item_price.text.split('դր')[0].replace(',','.')
                else:
                    product['price'] = None

                products.append(product)

            return products

        else:
            print(f"No response from url-{url}")
            return None

    def getting_all_data(self):
        phone_data = self.getting_data('phones/138/0/')
        tablet_data = self.getting_data('tablets/139/0/')
        watch_data = self.getting_data('watches/141/0/')
        tv_data = self.getting_data('tvs/143/0/')
        computer_data = self.getting_data('computers/144/0/')
        accessories_data = self.getting_data('accessories/146/0/')
        appliance_data = self.getting_data('household-appliances/178/0/')
        equipment_data = self.getting_data('equipments/148/0/')
        photo_camera_data = self.getting_data('photo-cameras/140/0/')

        return {
            "PHONE-DATA": phone_data,
            "TABLET-DATA": tablet_data,
            "WATCH-DATA": watch_data,
            "COMPUTER-DATA": computer_data,
            "TV-DATA": tv_data,
            "FOTOAPPARATY-DATA": photo_camera_data,
            "APPLIANCES-DATA": appliance_data,
            "ACCESSORIES-DATA": accessories_data,
            "OTHER-PRODUCTS-DATA": equipment_data,
        }

class ThreeDPlanetReq:
    cookies = {
        'qtrans_front_language': 'hy',
        '_gid': 'GA1.2.612525651.1706700913',
        '_ga_YDGZLGE0D0': 'GS1.1.1706700903.1.1.1706700929.0.0.0',
        '_ga': 'GA1.1.857811235.1706700904',
    }

    headers = {
        'authority': '3dplanet.am',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        # 'cookie': 'qtrans_front_language=hy; _gid=GA1.2.612525651.1706700913; _ga_YDGZLGE0D0=GS1.1.1706700903.1.1.1706700929.0.0.0; _ga=GA1.1.857811235.1706700904',
        'referer': 'https://3dplanet.am/',
        'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    }

    params = {
        'per_page': '36',
    }

    def url_for_page(self, page):
        return requests.get(f'https://3dplanet.am/shop/page/{page}/', params=self.params, cookies=self.cookies,
                            headers=self.headers)

    def getting_data_per_page(self, page):
        response = self.url_for_page(page)
        if response.status_code == 200:
            products = []
            soup = BeautifulSoup(response.text, 'lxml')
            items = soup.find_all('div', class_='product-information')
            for item in items:
                product = {}
                item_name = item.find('h3', class_='product-title')
                if item_name:
                    product['name'] = item_name.text
                    product['link'] = item_name.a.get('href')
                else:
                    product['name'] = None
                    product['link'] = None

                item_price = item.find('span', class_='woocommerce-Price-amount amount')
                if item_price:
                    price_parts = item_price.text.replace('\xa0', '').split('\\')
                    numeric_price = (price_parts[0][:-3])
                    numeric_price = numeric_price.replace(',', '.')
                    product['price'] = numeric_price
                else:
                    product['price'] = None
                products.append(product)
            return products
        else:
            return None

    def getting_all_data(self):
        all_product = []
        for i in range(1, 31):
            print(f"ON PAGE {i}")
            all_product.extend(self.getting_data_per_page(i))
        return all_product


def update_data(data, key):
    ref = db.reference('/')
    ref.child(key).update(data)

if __name__ == "__main__":
    zigzag = ZigZagReq()
    zigzag_data = zigzag.getting_all_data()

    redstore = RedStoreReq()
    redstore_data = redstore.getting_all_data()

    mobilecenter = MobileCenterReq()
    mobilecenter_data = mobilecenter.getting_all_data()

    threedplanet = ThreeDPlanetReq()
    threedplanet_data = threedplanet.getting_all_data()

    load_dotenv()
    cred = credentials.Certificate("electro-shops-arm-firebase-adminsdk-fznxq-e286074b55.json")
    initialize_app(cred, {
        'databaseURL': os.environ.get('DataServerLink')
    })


    update_data(zigzag_data, "zig_zag_data")
    update_data(redstore_data, "red_store_data")
    update_data(mobilecenter_data, "mobile_center_data")
    update_data(threedplanet_data, "3d_planet_data")