import requests as req


class BaseClient:
    # URL vk api
    BASE_URL = 'https://api.vk.com/method/'
    # метод vk api
    method = None
    # GET, POST, ...
    http_method = 'GET'

    def __init__(self):
        self.params = {}

    def set_params(self, params):
        self.params = params

    # Получение GET параметров запроса
    def get_params(self):
        return self.params

    # Получение данных POST запроса
    def get_json(self):
        return None

    # Получение HTTP заголовков
    def get_headers(self):
        return None

    # Склейка url
    def generate_url(self, method):
        return '{0}{1}'.format(self.BASE_URL, method)

    # Отправка запроса к VK API
    def _get_data(self, method, http_method):

        url = self.generate_url(method)
        response = req.get(url, params=self.get_params())
        # print(response.headers)
        return self.response_handler(response)

    # Обработка ответа от VK API
    def response_handler(self, response):
        return response

    # Запуск клиента
    def execute(self):
        return self._get_data(
            self.method,
            http_method=self.http_method
        )