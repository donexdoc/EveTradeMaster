"""
EVE API helper
"""

import json
import requests


class APIHelper:
    """
    Класс обращения к API через requests
    """

    def __init__(self, debug=False):
        self.api_url = 'https://esi.evetech.net/dev/'
        self.api_headers = {
            'Content-Type': 'application/json',
        }
        self.keys = {
            'datasource': 'tranquility',
            'language': 'en-us',
        }
        self.debug_mode = debug

    def get_types(self, etag="", page=1):
        """
        Список типов на странице
        """
        add_keys = {
            'page': page,
        }
        add_headers = {
            'If-None-Match': etag,
        }
        api_path = f'universe/types/'
        return self.__request(api_path, add_keys, add_headers)

    def get_all_types(self):
        """
        Весь список типов
        """
        result = []
        first_page_result = self.get_types(page=1)

        if self.debug_mode:
            print(f'first_page_result content: {first_page_result}')

        if first_page_result:
            pages = int(first_page_result.get('headers').get('x-pages'))
            etag = first_page_result.get('headers').get('Etag')
            if self.debug_mode:
                print(f'pages: {pages}')
                print(f'etag: {etag}')

            result.extend(first_page_result.get('content'))
            if pages > 1:
                for page in range(2, pages):
                    mid_result = self.get_types(etag, page)
                    etag = mid_result.get('headers').get('Etag')
                    result.extend(mid_result.get('content'))

        return result

    def get_orders(self, region_id, type_id, etag="", order_type='all', page=1):
        """
        Получение ордеров в регионе по id на странице

        :param etag: тег предыдущего запроса
        :param order_type: тип ордера (all, buy, sell)
        :param region_id: id региона
        :param type_id: id типа предмета
        :param page: страница, если запрашивается не первая
        :return: список всех ордеров по предмету по странице
        """
        add_keys = {
            'page': page,
            'order_type': order_type,
            'type_id': type_id,
        }
        add_headers = {
            'If-None-Match': etag,
        }
        api_path = f'markets/{region_id}/orders/'

        return self.__request(api_path, add_keys, add_headers)

    def get_all_orders(self, region_id, type_id):
        """
        Получение всех ордеров в регионе по типу

        :param region_id: id региона
        :param type_id: id типа предмета
        :return: список всех ордеров по предмету в регионе
        """

        sell_orders = []
        buy_orders = []

        fpr_sell_orders = self.get_orders(
            region_id=region_id,
            order_type='sell',
            type_id=type_id
        )

        if self.debug_mode:
            print(f'get_all_orders fpr_sell_orders content: {fpr_sell_orders}')

        if fpr_sell_orders.get('headers').get('x-pages'):
            pages = int(fpr_sell_orders.get('headers').get('x-pages'))
            etag = fpr_sell_orders.get('headers').get('Etag')

            sell_orders.extend(fpr_sell_orders.get('content'))
            if pages > 1:
                for page in range(2, pages):
                    mid_result = self.get_orders(
                        page=page,
                        etag=etag,
                        order_type='sell',
                        region_id=region_id,
                        type_id=type_id
                    )
                    etag = mid_result.get('headers').get('Etag')
                    sell_orders.extend(mid_result.get('content'))

        fpr_buy_orders = self.get_orders(
            region_id=region_id,
            order_type='buy',
            type_id=type_id
        )

        if self.debug_mode:
            print(f'get_all_orders fpr_buy_orders content: {fpr_buy_orders}')

        if fpr_buy_orders.get('headers').get('x-pages'):
            pages = int(fpr_buy_orders.get('headers').get('x-pages'))
            etag = fpr_buy_orders.get('headers').get('Etag')

            buy_orders.extend(fpr_buy_orders.get('content'))
            if pages > 1:
                for page in range(2, pages):
                    mid_result = self.get_orders(
                        page=page,
                        etag=etag,
                        order_type='buy',
                        region_id=region_id,
                        type_id=type_id
                    )
                    etag = mid_result.get('headers').get('Etag')
                    buy_orders.extend(mid_result.get('content'))

        return {
            'sell': sell_orders,
            'buy': buy_orders
        }

    def type_info(self, type_id):
        """
        Информация о типе

        :param type_id: id типа
        :return:
        """
        api_path = f'universe/types/{type_id}/'

        return self.__request(api_path)

    def group_info(self, group_id):
        """
        Информация о группе

        :param group_id: id группы
        :return:
        """
        api_path = f'universe/groups/{group_id}/'

        return self.__request(api_path)

    def system_info(self, system_id):
        """
        Информация о системе

        :param system_id: id системы
        :return:
        """
        api_path = f'universe/systems/{system_id}/'

        return self.__request(api_path)

    def api_status(self):
        """
        Информация о статусе ESI API

        :return:
        """

        api_url = f'https://esi.evetech.net/status.json'

        keys = {
            'version': "dev",
        }

        session = requests.Session()
        response = session.get(api_url, params=keys)

        result = json.loads(response.content.decode('utf-8'))
        if 'error' not in result:
            return True
        else:
            return False

    def __request(self, api_path, add_keys={}, add_headers={}):
        """
        Запрос к API интерфейсу

        :param api_path: полный путь запроса
        :param add_keys: добавочные ключи
        :return: результат запроса. Если результат не имеет ответ 200, то возвращается None
        """

        keys, headers = {}, {}

        keys.update(self.keys)
        keys.update(add_keys)

        headers.update(self.api_headers)
        headers.update(add_headers)

        session = requests.Session()

        response = session.get(self.api_url + api_path, params=keys)
        # response = requests.get(self.api_url + api_path, params=keys)

        if self.debug_mode:
            print(f'getting info from {response.url} ')

        if response.status_code == 200:
            return {
                'headers': response.headers,
                'content': json.loads(response.content.decode('utf-8'))
            }
        else:
            return {
                'headers': response.headers,
                'content': response.content.decode('utf-8')
            }

    def get_min_max(self, orders, systems=[]):
        """
        Фильтр ордеров по системам и получение данных по максимальным и минимальным ценам на ордера
        :param orders: список ордеров
        :param systems: фильтр по системам, если пустрой, проверяет по всем системам региона
        :return: словарь с минимальными и максимальными ценами и количество доступных позиций
        """

        min_price = 0
        max_price = 0
        volume_min_remain = 0
        volume_max_remain = 0

        for order in orders:
            if len(systems) == 0 or order['system_id'] in systems:
                if min_price == 0:
                    min_price = order['price']
                else:
                    min_price = min(min_price, order['price'])
                    if min_price == order['price']:
                        volume_min_remain += order['volume_remain']
                    else:
                        volume_min_remain = order['volume_remain']

                if max_price == 0:
                    max_price = order['price']
                else:
                    max_price = max(max_price, order['price'])
                    if max_price == order['price']:
                        volume_max_remain += order['volume_remain']
                    else:
                        volume_max_remain = order['volume_remain']

        return {
            "min_price": min_price,
            "max_price": max_price,
            "volume_min_remain": volume_min_remain,
            "volume_max_remain": volume_max_remain,
        }

    def item_pricing_info(self, type_id, regions, systems=[]):
        """
        Получение информации о ценах на предмет по регионами
        :param type_id: id предмета
        :param regions: список регионов, для проверки
        :param systems: фильтр по системам, если пустой, проверяет по всем системам региона
        :return: словарь или массив словарей с данными по ценами по остатку товаров для минимальной цены
        """
        result = []
        for region in regions:
            orders = self.get_all_orders(region, type_id)

            min_max_sell = self.get_min_max(orders['sell'], systems)
            min_max_buy = self.get_min_max(orders['buy'], systems)

            result.append({
                "min_sell": min_max_sell['min_price'],
                "max_sell": min_max_sell['max_price'],
                "min_buy": min_max_buy['min_price'],
                "max_buy": min_max_buy['max_price'],
                "min_sell_remain": min_max_sell['volume_min_remain']
            })

        if len(result) > 1:
            return result
        else:
            return result[0]
