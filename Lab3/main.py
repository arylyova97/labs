import lib.draw_hist as smpl_hist
import lib.friends_class as fr
from lib import user_class as usr
import lib.nice_drawer as nice_hist

if __name__ == '__main__':
    params = {'user_ids': 'ryleva97'}

    user = usr.User()
    user.set_params(params)
    user.execute()


    friends = fr.Friends()

    params = {'uid': user.uid,
              'fields': ('bdate')}

    friends.set_params(params=params)
    friends.execute()

    smpl_hist.draw(friends.friends_lst)
    nice_hist.draw(friends.friends_lst)

