import sqlite3
import os

from db import DB, correct_sn


class UsersDB(DB):
    @correct_sn
    def add_test_results(self, sn_type=None, u_id=None, test_r=None):
        test_r = " ".join([str(i) for i in test_r])
        self.cur.execute("""UPDATE users SET test_result = \"{}\" WHERE {} = {}""".
                         format(test_r, sn_type, u_id))
 
    @correct_sn
    def get_matches(self, sn_type=None, u_id=None):
        users_test = self.cur.execute(
            "SELECT test_result FROM users WHERE {} = {}".format(sn_type, u_id)).fetchall()[
            0][0].split()
        matches = self.cur.execute("SELECT * FROM users".format()).fetchall()
        counter = []
        for m in matches:
            if not m[-1]:
                continue
            ids = m[1:3]
            if u_id in ids:
                continue
            test = [str(n) for n in m[-1].split()]
            c = 0
            for i in range(len(users_test)):
                if users_test[i] == test[i]:
                    c += 1
            counter.append((ids, c))
        counter.sort(key=lambda x: x[1], reverse=True)
        return counter[:5]
        
    def __init__(self):
        super().__init__()
        self.db = sqlite3.connect(os.path.join("data", "database.db"))
        self.cur = self.db.cursor()

    @correct_sn
    def is_user_in_db(self, sn_type=None, u_id=None):
        r = self.cur.execute("SELECT * FROM users WHERE {} = {}".format(sn_type, u_id, )).fetchall()
        return bool(r)

    @correct_sn
    def add_user(self, sn_type=None, u_id=None):
        if not self.is_user_in_db(sn_type=sn_type, u_id=u_id):
            self.cur.execute("INSERT INTO users({}) VALUES ({})".format(sn_type, u_id))
            self.db.commit()
        self.print_table("users")

    @correct_sn
    def add_tiktok_to_user(self, sn_type=None, u_id=None, tt_nm=None):
        self.cur.execute(
            """UPDATE users SET tt_nm = \"{}\" WHERE {} = {}""".format(tt_nm, sn_type, u_id))
        self.db.commit()
        self.print_table("users")

    @correct_sn
    def is_tiktok(self, sn_type=None, u_id=None):
        return bool(self.cur.execute("""SELECT * FROM users WHERE {} = {} AND tt_nm != NULL""".
                                     format(sn_type, u_id)).fetchall())

    def check_test_matches(self, test):
        result = self.cur.execute(f"""SELECT vk_id, tg_id, test_result FROM users
                                    WHERE test result IS NOT NULL""").fetchall()
        ans = []
        for user in result:
            vk_id = user[0]
            tg_id = user[1]
            other_test = user[2]
            match = list(map(lambda x: 1 if x else 0, (other_test[i] == test[i] for i in range(10))))
            cost = sum(match)
            if cost > 0:
                ans.append(((vk_id, tg_id), cost))
        ans.sort(key=lambda x: x[1], reverse=True)
        return ans[:10]
    
    def get_subscribe_match(self, subscribes):
        """Возвращает list с 5 (tg_id, совпадений) с наибольшими совпадениями"""
        matches = {}
        for subscribe in subscribes:
            users = set()
            results = self.cur.execute(f'''SELECT tg_id FROM subs WHERE sup = {subscribe}''').fetchall()
            for result in results:
                other_id = result[0]
                if other_id not in users:
                    try:
                        matches[other_id] += 1
                    except Exception:
                        matches[other_id] = 1
        ans = []
        for user, match in matches.items():
            ans.append((user, match))

        ans.sort(key=lambda x: x[1], reverse=True)
        return ans

        
if __name__ == "__main__":
    db = UsersDB()
    db.print_table("users")
