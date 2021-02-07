from filename import database as Db


class Adapter:
    def __init__(self):
        self.db = Db()

    def get_vk_friends(self, user_id, subscribes):
        matches = self.db.get_get_subscribe_match(subscribes)
        ans = []
        while True:
            user = matches.pop[0]
            if user[0] != user_id:
                ans.append(user)
            if len(ans) == 5:
                break
        return ans
