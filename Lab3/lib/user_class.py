import lib.base_class as bc
from lib import request_exception as exp


class User(bc.BaseClient):

    method = 'users.get'

    def __init__(self):
        super(bc.BaseClient, self).__init__()
        self.uid = None

    # Обработка ответа от VK API
    def response_handler(self, response):
        ret = None
        try:
            data = response.json()

            self.uid = data['response'][0]['uid']
            ret = data['response'][0]
        except:
            raise exp.RequestError('Bad request')
        return ret

