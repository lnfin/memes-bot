from filename import database as Db


class Adapter:
    def __init__(self):
        self.db = Db()

    def get_vk_friends(self, user_id):
        """Возвращает 5 человек с общими интересами"""
        unions = []
        user_vk_id =
        user_tg_id =        # TODO Получение этих данных юзера
        user_vk_data =      # TODO Получение интересов пользователя
        users = # TODO Метод получения всех юзеров
        for user in users:
            other_id = user[0]
            other_vk_id = user[1]
            other_tg_id = user[2]
            other_vk_data = user[3]
            other_vk_data = set(other_vk_data.split(' '))

            union = other_vk_data & user_vk_data
            if union > 0:
                unions.append(other_tg_id, union)

        unions.sort(key= lambda x: x[1], reverse=True)
        return unions[:5]
