#  проверил, нужна авторизация именно через юзера. Сообществам нельзя
import vk_api


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
        ans = []
        for q in response:
            try:
                if q['activity'] == 'Юмор':
                    ans.append(q['id'])
            except Exception:
                pass
        return ans

    def get_humor_subscribes(self, user_id):
        groups, error = self.get_subscribes(user_id)
        if not error:
            return self.get_activity(groups), 0
        else:
            return None, error


if __name__ == '__main__':
    LOGIN = ''
    PASSWORD = ''
    api = VkParser(LOGIN, PASSWORD)
    print(api.get_humor_subscribes(232266268))
