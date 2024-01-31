import requests
from bs4 import BeautifulSoup
import json


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
        'product_list_mode': 'list',
    }
    base_url = 'https://www.zigzag.am/am/phones-and-communication.html'

    # Making request for phone,accsesories, and naushniks
    def making_request_pan(self, page):
        self.params['p'] = str(page)
        return requests.get(self.base_url, params=self.params, cookies=self.cookies, headers=self.headers)

    # Getting phones accesories and naushniks
    def getting_p_a_n(self):
        products = []
        for i in range(1, 99):
            # Getting response
            print(i)
            response = self.making_request_pan(i)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'lxml')

                # All info blocks
                info_blocks = soup.find_all('div', class_='block_inner product-item-details')
                for block in info_blocks:
                    product_data = {}
                    # Product Category
                    product_category = block.find('div', class_='product_category')
                    if product_category:
                        product_data['category'] = product_category.text
                    else:
                        product_category['category'] = None
                    # Product Name and Url
                    product_name = block.find('a', class_='product_name combo_link')
                    if product_name:
                        product_data['name'] = product_name.text
                        product_data['url'] = product_name.get('href')
                    else:
                        product_data['name'] = None
                        product_data['url'] = None
                    # Products Details list
                    details_list = []
                    detail_list = block.find('ul', class_='details_list')
                    if detail_list:
                        for li in detail_list.find_all('li'):
                            details_list.append(li.text.strip())
                        product_data['details'] = details_list
                    else:
                        product_data['details'] = None
                    # Products Price
                    price = block.find('span', class_='price')
                    if price:
                        product_data['price'] = price.text
                    else:
                        product_data['price'] = None

                    products.append(product_data)

            else:
                print(f"No response from page {i}")
                products.append({f"page{i}"})
        # Writing Data in json file
        with open('zigzag_data.json', 'w', encoding='utf-8') as json_file:
            json.dump(products, json_file, ensure_ascii=False, indent=2)


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

    def getting_data(self,page_count,IT_name):
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
                    item_name = item.find('a', class_='frame-photo-title').get('title')
                    if item_name:
                        product_data['name'] = item_name
                    else:
                        product_data['name'] = None

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
        phone_data = self.getting_data(552,'smartfony')

        self.url_for_category('tablets')
        tablet_data = self.getting_data(120,'tablets')

        self.url_for_category('watches')
        watch_data = self.getting_data(72,'watches')

        self.url_for_category('notebooks')
        notebook_data = self.getting_data(240, 'notebooks')

        self.url_for_category('computers')
        computer_data = self.getting_data(108, 'computers')

        self.url_for_category('monitors')
        monitor_data = self.getting_data(48, 'monitors')

        self.url_for_category('tv')
        tv_data = self.getting_data(72,'tv')

        self.url_for_category('printery')
        printer_data = self.getting_data(36,'printery')

        self.url_for_category('Speakers')
        speakers_data = self.getting_data(168,'Speakers')

        self.url_for_category('proektory')
        proektory_data = self.getting_data(36,'proektory')

        self.url_for_category('zerkalnye-fotoapparaty')
        fotoapparaty_data = self.getting_data(60,'zerkalnye-fotoapparaty')

        self.url_for_category('igrovye-konsoli')
        konsoli_data = self.getting_data(72,'igrovye-konsoli')

        self.url_for_category('sdg')
        sdg_data = self.getting_data(0,'sdg')

        self.url_for_category('54')
        router_data = self.getting_data(24,'54')

        self.url_for_category('dronys')
        dron_data = self.getting_data(0,'dronys')

        self.url_for_category('l')
        vintilyator_data = self.getting_data(60,'l')

        self.url_for_category('Appliances')
        appliances_data = self.getting_data(324,'Appliances')

        self.url_for_category('f')
        xnamqi_data = self.getting_data(84,'f')

        self.url_for_category('accessories')
        accessories_data = self.getting_data(1644,'accessories')

        self.url_for_category('other-products')
        other_products_data = self.getting_data(96,'other-products')

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

smartphone_request = RedStoreReq()
smartphone_request.getting_all_data()
