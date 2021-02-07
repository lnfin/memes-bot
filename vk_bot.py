from random import randint
from constants import TOKEN, ID_GROUP
from users_db import UsersDB
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from tiktok.checks import check_likes_privacy


class CommanderAnswer:
    def __init__(self, m):
        self.m = m

    def get_message(self):
        return self.m


class Commander:
    def get_answer(self, u_id, m_text):
        return CommanderAnswer(self.get_message(u_id, m_text))

    def get_message(self, u_id, m_text):
        return "text"


class Server:
    def __init__(self):
        self.u_db = UsersDB()
        self.vk_session = vk_api.VkApi(token=TOKEN)
        self.longpoll = VkBotLongPoll(self.vk_session, ID_GROUP)
        self.vk = self.vk_session.get_api()
        self.cm = Commander()

    def listen(self):
        for event in self.longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                user_id = event.object.message["from_id"]
                message_text = event.object.message["text"]
                if self.u_db.is_user_in_db(sn_type="vk", u_id=user_id):
                    if self.u_db.is_tiktok(sn_type="vk", u_id=user_id):
                        pass
                    else:
                        self.u_db.add_tiktok_to_user(sn_type="vk", u_id=user_id,
                                                     tt_nm=message_text)
                else:
                    self.u_db.add_user(sn_type=VK, u_id=user_id)
                    ans = self.cm.get_answer(user_id, "Начать")
                    if ans:
                        self.send_message(user_id, ans.get_message())

    def send_message(self, u_id, mes):
        self.vk.messages.send(user_id=u_id, message=mes, random_id=randint(0, 2 * 64))


VK = "vk"
if __name__ == "__main__":
    print(check_likes_privacy("abc"))
    s = Server()
    s.listen()
