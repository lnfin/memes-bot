import vk_api  # Пожалуй, можешь переписать init и вместо логина с паролем пихать сессию в self.vk (Если ты через юзера)
from database import DataBase


class VkParser:
    def __init__(self, login, password):
        self.vk = vk_api.VkApi(login, password)

        try:
            self.vk.auth(token_only=True)

        except Exception:
            self.ok = False
        else:
            self.ok = True

    def get_subscribes(self, user_id):
        """
        :return: список групп и None, если удачно иначе None и:
                                                                0, если всё ок
                                                                1, если пользователь c закрытым профилем
                                                                2, если ошибка связана с vk
                                                                3, если иная ошибка
        """
        params = {
            'user_id': str(user_id)
        }
        try:
            response = self.vk.method(method='users.getSubscriptions', values=params)
        except vk_api.exceptions.ApiError as exc:
            if exc.code == 30:
                return None, 1
            else:
                return None, 2
        except Exception:
            return None, 3
        else:
            try:
                response = response['groups']['items']
            except Exception:
                return None, 3
            else:
                return response, 0

    def get_activity(self, groups):
        param = {
            'group_ids': (', '.join(map(str, groups)))[:-2],
            'fields': 'activity'
        }
        response = self.vk.method(method='groups.getById', values=param)
        ans = set()
        for q in response:
            try:
                if q['activity'] == 'Юмор':
                    ans.add(q['id'])
            except Exception:
                pass
        return ans

    def get_humor_subscribes(self, user_id):
        """Даёт список с группами 'Юмор' и None, либо None и код ошибки (См. Выше)"""
        groups, error = self.get_subscribes(user_id)
        if not error:
            return self.get_activity(groups), None
        else:
            return None, error

    def get_user_id(self, name):
        """Переводит короткое имя в id, если пихнуть id, то тоже вернёт id"""
        if name.isdigit():
            name = 'id' + name
        params = {'screen_name': name}
        try:
            response = self.vk.method(method='utils.resolveScreenName', values=params)
            print(response)
            if response['type'] == 'user':
                return response['object_id']
        except Exception:
            return None


if __name__ == '__main__':
    db = DataBase()
    LOGIN = ''
    PASSWORD = ''
    api = VkParser(LOGIN, PASSWORD)
    a = api.get_user_id('232266268')
