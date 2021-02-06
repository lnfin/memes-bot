from filename import database as Db

TT_ID = ''
TG_ID = ''
VK_ID = ''


class Adapter:
    def __init__(self):
        self.db = Db()

    def add_user(self, vk_id='', tg_id='', tt_id=''):
        if tg_id:
            self.db.add_user(sn_type=TG_ID, u_id=tg_id)
            if tt_id:
                self.db.add_tiktok_to_user(sn_type=TG_ID, u_id=tg_id)
        elif vk_id:
            self.db.add_user(sn_type=VK_ID, u_id=vk_id)
            if tt_id:
                self.db.add_tiktok_to_user(sn_type=VK_ID, u_id=vk_id)

    def add_tiktok_to_user(self, sn_type=None, u_id=None):
        self.db.add_tiktok_to_user(sn_type=sn_type, u_id=u_id)

    def found_vk_friends(self, user_id, table=VK_ID):
        unions = []
        user_vk_id =
        user_tg_id =        # TODO Получение этих данных юзера
        user_vk_data =
        user_vk_data = set(user_vk_data.split(' '))

        users = # TODO Метод получения всех юзеров
        for user in users:
            other_id = user[0]
            other_vk_id = user[1]
            other_tg_id = user[2]
            other_vk_data = user[3]
            other_vk_data = set(other_vk_data.split(' '))

            union = other_vk_data & user_vk_data
            if union > 0:
                unions.append((other_id, union))

        unions.sort(key= lambda x: x[1], reverse=True)
        return unions[:5]
