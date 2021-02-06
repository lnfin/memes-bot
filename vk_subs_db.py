import sqlite3
import os

from db import DB, correct_sn


class VkSubsDB(DB):
    def __init__(self):
        super().__init__()
        self.db = sqlite3.connect(os.path.join("data", "database.db"))
        self.cur = self.db.cursor()

    @correct_sn
    def add_sub(self, sn_type=None, u_id=None, sub=None):
        self.cur.execute(
            "INSERT INTO subs({}, sub) VALUES({}, {})".format(sn_type, u_id, "\"{}\"".format(sub)))
        self.db.commit()

    @correct_sn
    def get_matches(self, sn_type=None, u_id=None):
        user_subs = [str(i[0]) for i in self.cur.execute(
            "SELECT sub FROM subs WHERE {} = {}".format(sn_type, u_id)).fetchall()]
        user_subs = "(\"{}\")".format("\", \"".join(user_subs))
        matches = self.cur.execute("SELECT * FROM subs WHERE sub IN {} AND {} != {}".format(
            user_subs, sn_type, u_id)).fetchall()
        counter = {}
        for m in matches:
            counter[m[1:3]] = counter.get(m[1:3], 0) + 1
        return counter


if __name__ == "__main__":
    db = VkSubsDB()
    db.add_sub(sn_type="vk", u_id=1, sub="c")
    db.get_matches(sn_type="vk", u_id=1)
    db.print_table("subs")
