import lib.draw_hist as drawer
import lib.friends_class as fr
from lib import user_class as usr

if __name__ == '__main__':

    params = {'user_ids': 'ryleva97'}

    user = usr.User()
    user.set_params(params)
    user.execute()
    #print(user.uid)

    friends = fr.Friends()

    params = {'uid': user.uid,
              'fields': ('bdate')}

    friends.set_params(params=params)
    friends.execute()

    drawer.draw(friends.friends_lst)

