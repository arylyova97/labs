import datetime
import lib.base_class as bc
from lib import request_exception as exp


class Friends(bc.BaseClient):

    method = 'friends.get'

    def __init__(self):
        super(bc.BaseClient, self).__init__()
        self.friends_lst = []



    def _get_friends_lst(self, data):
        friends_with_full_bdate = []
        for item in data:
            if 'bdate' in item and len(item['bdate'].split('.')) == 3:
                date = datetime.datetime.strptime(item['bdate'], '%d.%m.%Y').date()

                today = datetime.date.today()

                delta = today - date

                item['age']  = (delta.days // 365)
                friends_with_full_bdate.append(item)
        self.friends_lst = friends_with_full_bdate
        #print(friends_with_full_bdate)
        return friends_with_full_bdate

    # Обработка ответа от VK API
    def response_handler(self, response):

        try:
            data = response.json()
            #print(data)
            data = data['response']
            #print(data)
        except:
            raise exp.RequestError('Bad request')
        else:
            return self._get_friends_lst(data)


